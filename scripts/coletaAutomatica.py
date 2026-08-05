import sys
import os
import time
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src')) # add a pasta src ao caminho
from coletor import pegar_voos, salvar_dados

def coleta_automatica(intervalo_minutos=60): #Coleta dados automaticamente no intervalor de 60 minutos
    print("COLETA AUTOMÁTICA INICIADA")
    print(f"Intervalo: {intervalo_minutos} minutos")
    print("Pressione Ctrl+C para interromper\n")
    
    contador = 0
    try:
        while True:
            contador += 1
            print(f"\nColeta #{contador} - {datetime.now().strftime('%H:%M:%S')}")
            print("-"*40)
            
            voos = pegar_voos()
            if voos:
                salvar_dados(voos)
                print(f"✅ {len(voos)} voos salvos!")
            else:
                print("⚠️ Nenhum voo encontrado")
            
            print(f"⏳ Próxima coleta em {intervalo_minutos} minutos...")
            time.sleep(intervalo_minutos * 60)
            
    except KeyboardInterrupt:
        print(f"\n\n❌ Coleta interrompida!")
        print(f"Total de coletas: {contador}")

if __name__ == "__main__":
    # Para teste rápido: 5 minutos
    coleta_automatica(intervalo_minutos=5)