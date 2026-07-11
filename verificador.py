import json
import glob
from collections import Counter

def verificar_callsign(callsign_procurado):
    arquivos = glob.glob("dados_*.json")
    if not arquivos:
        print("Nenhum arquivo encontrado!")
        return
    
    ultimo = max(arquivos)
    print(f"Analisando: {ultimo}\n")
    
    with open(ultimo, "r") as f:
        voos = json.load(f)

    contagem = 0
    for voo in voos:
        callsign = voo[1]  
        if callsign and callsign.strip():
            if callsign.strip() == callsign_procurado:
                contagem += 1
    
    print(f"Procurando por: '{callsign_procurado}'")
    print(f"Encontrado: {contagem} vezes")
    
    # Mostra informações do primeiro voo encontrado
    for voo in voos:
        callsign = voo[1] if voo[1] else ""
        if callsign.strip() == callsign_procurado:
            print(f"\n📋 Informações do voo:")
            print(f"  - Callsign: {voo[1]}")
            print(f"  - País: {voo[2]}")
            print(f"  - Altitude: {voo[7]} metros")
            print(f"  - Velocidade: {voo[9]} m/s")
            break
    
    print("\n**TOP 10 CALLSIGNS:**")
    todos_callsigns = []
    for voo in voos:
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