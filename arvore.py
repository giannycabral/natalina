import time
import random

def gerar_natal_dev():
    print("\n🚀 Iniciando protocolo natalino...\n")
    time.sleep(1)
    
    # Cores (códigos ANSI)
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    RESET = '\033[0m'
    
    altura = 12
    
    # Estrela no topo
    print(" " * (altura + 1) + f"{AMARELO}★{RESET}")

    # Corpo da árvore
    for i in range(altura):
        espacos = " " * (altura - i)
        camada = ""
        for j in range(2 * i + 1):
            # 15% de chance de ser uma bola de natal, senão é folha
            if random.random() < 0.15:
                camada += f"{VERMELHO}o{RESET}"
            else:
                camada += f"{VERDE}*{RESET}"
        
        print(f"{espacos}{camada}")
        time.sleep(0.1) # Efeito de "construção"

    # Tronco
    tronco_largura = 3
    tronco_altura = 2
    espaco_tronco = " " * (altura - 1)
    for _ in range(tronco_altura):
        print(f"{espaco_tronco}{AMARELO}|||{RESET}")

    # Mensagem final
    mensagem = f"""
    {VERDE}{'='*36}
       FELIZ NATAL, DEV! 
    {'='*36}{RESET}
    """
    print(mensagem)
    print("Desejo para o seu novo ciclo:")
    print(f"{AMARELO}while{RESET} alive:")
    print(f"    eat()")      #comer
    print(f"    sleep()")    #dormir
    print(f"    code()")     #programar
    print(f"    be_happy()")  #ser feliz


#Executar apemas se for o arquivo principal 
if __name__ == "__main__":
    gerar_natal_dev()