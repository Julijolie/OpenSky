import requests
import json
from datetime import datetime

# [lamin, lamax, lomin, lomax]
BRASIL = [-33.75, 5.27, -73.98, -34.79]

def pegar_voos():
    url = "https://opensky-network.org/api/states/all" """voos em tempo real"""
    params = {
        "lamin": BRASIL[0],
        "lamax": BRASIL[1],
        "lomin":BRASIL[2],
        "lomax": BRASIL[3]
    }

    try:
        resposta = resquests.get(url, params=params, timeout=10)
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
