from fastapi import FastAPI
import pandas as pd

app = FastAPI(title= 'ETL con docker y FastApi',
            description= 'Extract, Transform, Load of the platforms Amazon, Disney, Hulu y Netflix', 
            version= '1.0.1')
@app.get('/')
async def init():
    return {'Hello:World'}

@app.on_event('startup')
def startup():
    global df_integral
    df_integral= pd.read_csv('/app/Datasets/df_integral.csv', encoding='utf-8')

@app.get('/get_max_duration')
async def get_max_duration(year:int, platform:str, duration:str):
    df = df_integral[df_integral['release_year'] == year]
    df = df[df['platform_id'] == platform.lower()]
    max = df[duration].max()
    title = df[df[duration]==max]['title']
    title = title.tolist()
    title= title[0]
    return {'title': title}

@app.get('/get_count_plataform')
async def get_count_plataform(plataform:str):
    plataform= plataform.lower()
    df = df_integral[df_integral['platform_id'] == plataform]
    df_movie = df[df['type']== 'movie']
    df_tv_show = df[df['type']== 'tv show']
    return{'plataform': plataform,'movie':len(df_movie),'tv_show':len(df_tv_show)}

@app.get('/get_listedin')
async def get_listedin(gender:str):
    gender = gender.lower()
    mask= df_integral['listed_in'].str.contains(gender)
    count = {'amazon':0,'disney':0, 'hulu':0, 'netflix':0}
    for i in df_integral[mask]['platform_id']:
        if i == 'amazon':
            count['amazon'] +=1
        elif i == 'disney':
            count['disney'] +=1
        elif i == 'hulu':
            count['hulu']   +=1
        elif i == 'netflix':
            count ['netflix']+=1
    maximo = max(count)
    platform, counts = max(count), max(count.values())
    return {'paltform':platform,'count':counts}

@app.get('/get_actor')
async def get_actor(platform:str, year:int):
    platform = platform.replace("'","")
    platform = platform.lower()
    actores, repeticiones = list(), list()
    Cast_list = list(df_integral[(df_integral.platform_id == platform) & (df_integral.release_year == year)].cast.fillna('sin dato'))

    for each in Cast_list:
        if not(each == 'sin dato' or each is None):
            lista = each.split(",")
            for elem in lista:
                elem = elem.strip()
                if elem in actores:
                    repeticiones[actores.index(elem)] += 1
                else:    
                    actores.append(elem)
                    repeticiones.append(1)
    if actores == []: return 'No hay datos'
    return {'platform':platform, 'count':max(repeticiones), 'cast':actores[repeticiones.index(max(repeticiones))]}