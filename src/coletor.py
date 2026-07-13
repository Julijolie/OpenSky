import requests
import json
import os
from datetime import datetime

# [lamin, lamax, lomin, lomax]
BRASIL = [-33.75, 5.27, -73.98, -34.79]

def pegar_voos():
    url = "https://opensky-network.org/api/states/all" #voos em tempo real"""
    params = {
        "lamin": BRASIL[0],
        "lamax": BRASIL[1],
        "lomin":BRASIL[2],
        "lomax": BRASIL[3]
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        if resposta.status_code == 200: #funciona!
            dados=resposta.json()
            voos=dados.get("states", [])
            print(f"{len(voos)} voos encontrados")
            return voos
        else:
            print( "Erro {resposta.status_code}")
            return[]
    except Exception as e: #erro de conexão, incluso timout>10
        print(f"Falha: {e}")
        return []

def salvar_dados(voos):
    nome=f"dados/dados_{datetime.now().strftime('%Y%m%d_%H%M')}.json" #salvando diretamente na pasta dados!
    with open(nome, "w") as f: #with fecha automaticamente quando sair do bloco
        json.dump(voos, f, indent=2) #Aqui escrevo os dados de voos em formato JSON no arquivo f, com indentação de 2 espaços
        print(f"salvo: {nome}")
        return nome
    
if __name__ == "__main__":
    print("Buscando voos...")
    voos=pegar_voos()
    if voos:
        salvar_dados(voos)