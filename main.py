

from fastapi import FastAPI
import pandas as pd

from fastapi.responses import RedirectResponse # esta libreria funciona para la url.

app=FastAPI()

@app.get("/", include_in_schema=False)  # esta funcion genera que la url ya venga con /doc*/ haciendo que se abra directo el API. 
async def redirect_to_docs():
    return RedirectResponse("/docs")

# Cargar los datos desde los archivos CSV y Parquet
genre_data = pd.read_csv('genre.csv')
items_data = pd.read_parquet('items1.parquet')
reviews_data = pd.read_csv('reviews.csv')
steam_data = pd.read_csv('steam.csv')

# Se definen los endpoints de la API:

 
@app.get("/¡Hola, bienvenido!") # Funcion que saluda a los ingresantes 
def index():
        return {"message": "¡HOLA, Bienvenido!"}

@app.get('/desarrollador/ {item_id: str}')  # Cantidad de items y porcentajede contenido Free por año según empresa desarrolladora.
def desarrollador (item_id: str):
    if item_id in items_data:
        return items_data[item_id]
    
    else:
        return "desarrollador NO encontrado", 404
    

@app.get('/userdata/ {user_id: str}') # Debe devolver cantidad de dinero gastado por el usuario, el porcentajede recomendación en base a reviews.recommend y cantidad de items.
def userdata (user_id :str):
    if user_id in reviews_data:
        return reviews_data[user_id]
    else: 
        return 'user NO encontrado', 404

@app.get('/UserForGenre/ {genero: str}') 
def UserForGenre( genero: str ):
     return

@app.get('/best_developer_year/ {año: int}') 
def best_developer_year( año: int ):
     return
     
@app.get('/desarrollador_reviews_analysis/ {desarrolladora: str}') 
def desarrollador_reviews_analysis( desarrolladora: str ):
     return

# Modelo de aprendizaje automatico: 


@app.get('/ recomendacion_juego/ {id de producto}') 
def recomendacion_juego( ):
     return 

@app.get('/recomendacion_usuario/ {id de usuario}') 
def recomendacion_usuario( ) :
     return






