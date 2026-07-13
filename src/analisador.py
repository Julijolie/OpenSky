import json
import glob #buscas e padrão de arquivos
from collections import Counter

def carregar_ultimo_arquivo():
    arquivos=glob.glob("dados/dados_*.json") 
    if not arquivos:
        print("Nenhum arquivo encotrado. Execute o arquivo coletor.py primeiro!")
        return None
    
    ultimo=max(arquivos) 
    print(f"Carregando: {ultimo}")
    with open(ultimo, "r") as f: #com with eu não preciso dar f.close() para fechar o arquivo após seu carregamento.
        return json.load(f)
    
def rotas_congestionadas(voos):
    contagem = {}
    for voo in voos:
        id_voo = voo[1] 
        if id_voo and id_voo.strip():
            nome_voo = id_voo.strip()
            if nome_voo in contagem:
                contagem[nome_voo] += 1
            else:
                contagem[nome_voo] = 1
    ordenados = sorted(contagem.items(), key=lambda x:x[1], reverse=True)
    return ordenados

# EXECUTA ;)
if __name__ == "__main__":
    print("Analisando rotas congestionadas...")
    
    # Carrega os dados
    voos = carregar_ultimo_arquivo()
    
    if voos:
        # Analisa as rotas
        resultado = rotas_congestionadas(voos)
        
        # Mostra na tela
        print("\n" + "="*50)
        print("ROTAS MAIS CONGESTIONADAS")
        print("="*50)
        
        for i, (voo, count) in enumerate(resultado[:10], 1):
            print(f"{i:2}. {voo:15} | {count:3} ocorrências")
        
        print(f"\nTotal de voos únicos: {len(resultado)}")
