import json
import glob #encontra arquivos e pastas que seguem um padrão
from collections import Counter

def verificar_callsign(callsign_procurado):
    arquivos = glob.glob("dados/dados_*.json")
    if not arquivos:
        print("Nenhum arquivo encontrado!")
        return
    
    print(f"\nTotal de arquivos analisados: {len(arquivos)} \n")
    todos_voos_com_arquivo = []
    for arquivo in sorted(arquivos): #ordena uma lista e retorna uma nova lista ordenada, sem modificar a original.
        with open(arquivo, "r") as f:
            voos = json.load(f) #Aqui eu Converti o JSON em um dicionário
            for voo in voos:
                todos_voos_com_arquivo.append((voo, arquivo))
        voos = [voo for voos, _ in todos_voos_com_arquivo] #crio uma nova lsta só com os voos e ignorando (_) o nome do arquivo
    
    contagem = 0
    arquivos_encontrados = set() #Guardo os nomes dos arquivos sem repetir

    for voo, arquivo in todos_voos_com_arquivo:
        callsign = voo[1]  
        if callsign and callsign.strip():
            if callsign.strip() == callsign_procurado:
                contagem += 1
                arquivos_encontrados.add(arquivo)
    
    print(f"O callsign '{callsign_procurado}' foi localizado em {contagem} arquivos diferentes.")
    
    if arquivos_encontrados:
        print(f"\nArquivos onde o callsign foi encontrado:")
        for arquivo in sorted(arquivos_encontrados):
            print(f"{arquivo}")
    else:
        print(f"\nCallsign não encontrado em nenhum arquivo!")

    for voo in voos:
        callsign = voo[1] if voo[1] else ""
        if callsign.strip() == callsign_procurado:
            print(f"\n📋 Informações do voo:")
            print(f"  - Callsign: {voo[1]}")
            print(f"  - País: {voo[2]}")
            print(f"  - Altitude: {voo[7]} metros")
            print(f"  - Velocidade: {voo[9]} m/s")
            break
    
    print(f"\n**TOP 10 CALLSIGNS (de {len(arquivos)} arquivos):**")
    todos_callsigns = []
    for voo, _ in todos_voos_com_arquivo:
        if voo[1] and voo[1].strip():  # Se o callsign existe E não é vazio
            callsign_limpo = voo[1].strip()
            todos_callsigns.append(callsign_limpo)

    for callsign, count in Counter(todos_callsigns).most_common(10):
        print(f"  {callsign}: {count} vezes")

# Executa
if __name__ == "__main__":
    # Pede qual callsign verificar
    procurado = input("✈️ Digite o callsign para verificar (ex: TAM1234): ").strip().upper()
    verificar_callsign(procurado)