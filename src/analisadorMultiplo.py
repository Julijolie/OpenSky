import json
import glob 
from collections import Counter
from datetime import datetime

def analisar_todos_arquivos():
    arquivos = glob.glob("dados/dados_*.json")
    if not arquivos:
        print("Nenhum arquivo encontrado! Execute a coleta primeiro.")
        return
    
    print("="*60)
    print("ANÁLISE COMPLETA DE TRÁFEGO AÉREO")
    print(f"Arquivos encontrados: {len(arquivos)}\n")
    print("="*60)
    
    todos_callsigns = []
    total_voos = 0
    
    for arquivo in sorted(arquivos):
        try:
            with open(arquivo, "r") as f:
                voos = json.load(f)
                total_voos += len(voos)
                
                for voo in voos:
                    if voo[1] and voo[1].strip():
                        todos_callsigns.append(voo[1].strip())
                
                print(f"{arquivo}: {len(voos)} voos")
        except Exception as e:
            print(f"❌ Erro ao ler {arquivo}: {e}")
    
    # 3. Estatísticas básicas
    print("\n" + "-"*60)
    print("📊 ESTATÍSTICAS GERAIS")
    print("-"*60)
    print(f"Total de registros de voo: {total_voos}")
    print(f"Callsigns únicos: {len(set(todos_callsigns))}")
    print(f"Média de voos por coleta: {total_voos / len(arquivos):.1f}")
    
    print("\n" + "-"*60)
    print("🏆 TOP 15 ROTAS MAIS CONGESTIONADAS")
    print("-"*60)
    
    contagem = Counter(todos_callsigns)
    
    if not contagem:
        print("❌ Nenhum callsign encontrado!")
        return
    
    for i, (callsign, count) in enumerate(contagem.most_common(15), 1):
        # Cria barra visual
        barra = "█" * min(count, 20)
        print(f"{i:2}. {callsign:15} | {count:4} ocorrências {barra}")
    
    #Salvar relatório
    relatorio = {
        "data_analise": datetime.now().isoformat(),
        "total_arquivos": len(arquivos),
        "total_voos": total_voos,
        "callsigns_unicos": len(set(todos_callsigns)),
        "top_rotas": contagem.most_common(20),
        "media_voos": total_voos / len(arquivos)
    }
    
    with open("relatorio_analise.json", "w") as f:
        json.dump(relatorio, f, indent=2) #escreve dados JSON em um arquivo
    
    print("\n💾 Relatório salvo em: relatorio_analise.json")
    print("="*60)

if __name__ == "__main__":
    analisar_todos_arquivos()
