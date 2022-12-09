
# PI_DATA_ENGINEER
<img src=".\_src\etl.gif" height="500"><br>

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como csv o json. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

<FONT SIZE=5>Las consultas a realizar son:</font>

* Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

* Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

* Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

* Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

# PASOS DEL PROYECTO
1. Revision de las consignas y los datasets para la ingesta y normalización de datos ubicados en la carpeta Datasets en el `README.md`, `amazon_prime_titles.csv`, `disney_plus_titles.csv`, `hulu_titles.csv`, `netflix_titles.json`.

2. La limpieza y normalizacion se realizo a traves de python, se encuentra en el archivo `ETL.ipynb`

3. Se exporto un nueva base de dato, ubicado en la carpeta Datasets titulado `df_integral.csv` y alli se hizo la relacion del conjunto de datos y se crearon las tabla necesaria para realizar consultas.

4. Creacion un archivo Dockerfile, Docker-compuse.yml, requirements.txt y main.py para que se pueda crear el entorno de Docker compuse.

5. Creacion de la API en un entorno Docker a traves de Docker-compuse.

6. Ejecutar consultas solicitadas.

7. Este es el link con el video demostrativo 

8. **PLUS**: realizar un deployment en Mogenius (Pendiente por Ejecutar)



# HABILIDADES TECNICAS

1. Analisis de datos ingestados
    
2. Transformacion correcta de los archivos

3. Ingesta de los datos transformados a una base de datos
4. Propuestas para resolver tratamientos sobre los datos
    


# ¿Cómo correr la FastApi utilizando el docker compuse?
1. Tenemos que clonar el repositorio: Encima de la lista de archivos, haga clic en <img src=".\_src\Flecha_descarga.png" height="15"> Código
<br>


<img src=".\_src\git_clone.png" height="400">
<br>


2. Abra la Terminal, cambia el directorio de trabajo actual a la ubicación en donde quieres clonar el directorio y Escriba git clone y pegue la dirección URL que ha copiado antes.

    ```shell
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `PI01_DATA_ENGINEERING`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

3. Posicionar en el directorio de acabamos de crear
    ```shell
    $ cd PI01_DATA_ENGINEERING  
    ```


4. Ahora si podemos correr nuestro `Docker-compuse`, recuerda que para ello debes tener 'Docker previamente instalando y activo' 

   ```shell
    $ docker-compose up --build
    ```
 
5. Cuando termine de correr las 6 info el programa esta lista para usarse

<img src=".\_src\terminal.png" height="400">


* <strong>Nota: Recuerda redirigirte al siguiente host `http://0.0.0.0:8000/docs` </strong>

<img src=".\_src\Docker-compuse.png" height="400">


* No olvides salir del programa cuando termines, dentro de la terminal presiona `Ctrl + c `, te saldra el sieguiente mensaje.
    ```shell
    Stopping proyecto_etl_fast_api3_1   ... done
    ```
