from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    return {'Hello':'Word'}

@app.get('/api/restaurtantes/')
def get_restaurantes(restaurtante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    reponse = requests.get(url)

    if reponse.status_code == 200:
        dados_json = reponse.json()
        if restaurtante is None:
            return {'Dados': dados_json}
         
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurtante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurtante,'Cardapio':dados_restaurante}
    else:
        return {'Erro':f'{reponse.status_code} - {reponse.text}'}