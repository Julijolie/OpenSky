import json
import glob #buscas e padrão de arquivos
from collections import Counter

def carregar_ultimo_arquivo():
    arquivos=glob.glob("dados_*.json") 
    if not arquivos:
        print("Nenhum arquivo encotrado. Execute o arquivo coletor.py primeiro!")
        return None
    
    ultimo=max(arquivos) 
    print(f"Carregando: {ultimo}")
    with open(ultimo, "r") as f:
        return json.load(f)
    
def rotas_congestionadas(voos):
    contagem = {}
    for voo in voos:
        id_voo = voo[1] 
    if id_voo and id_voo.strip():
        nome_voo = id_voo.strip()
        contagem[nome_voo] = contagem.get(nome_voo, 0) + 1
    ordenados = sorted(contagem.items(), key=lambda x:x[1], reverse=True)
    return ordenados