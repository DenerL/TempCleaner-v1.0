import os 
import shutil 
import time
import schedule 
from datetime import datetime

def limpar_pastas():
    pastas = [ os.path.join(os.environ.get('SYSTEMROOT', 'C:\\Windows'),'Prefetch'),
               os.path.join(os.environ.get('LocalAppData', 'C:\\ProgramData'),r'Google\Chrome\user Data\Default\Cache'),
               os.path.join(os.environ.get('LOCALAPPDATA', 'C:\\Windows'),'Temp'),
               os.path.join(os.environ.get('APPDATA')),
               os.path.join(os.environ.get('SYSTEMROOT', 'C:\\Windows'),'Temp'),
               os.path.join(os.environ.get('SystemDrive', 'C:\\'),r'\$recycle.bin')]
    total_itens_removidos = 0 # Contador para o total de itens removidos

    for caminho in pastas:# Itera sobre as pastas a serem limpas
            if os.path.exists(caminho):# Verifica se a pasta existe
             for item in os.listdir(caminho):# Lista os itens no caminho especificado
                caminho_item = os.path.join(caminho, item)# Cria o caminho completo do item
                try:# Tenta remover o item, seja ele um arquivo ou um diretório
                    if os.path.isfile(caminho_item):# Se for um arquivo, remove-o
                        os.unlink(caminho_item)# Remove o arquivo
                        total_itens_removidos += 1 # Incrementa o contador de itens removidos
                    elif os.path.isdir(caminho_item):# Se for um diretório, remove-o recursivamente
                        shutil.rmtree (caminho_item)# Remove o diretório e todo o seu conteúdo
                        total_itens_removidos += 1 # Incrementa o contador de itens removidos
                except PermissionError:
                    print(f"Sem permissão para remover {caminho}. Tente executar o programa como administrador.")
                except Exception as e:                    
                    print(f"Erro ao remover {caminho}: {e}")
                msg = f"Limpeza concluída:{total_itens_removidos} Total de itens removidos ." # Mensagem de log com o total de itens removidos
    salvar_log(msg)
    return total_itens_removidos
    

def salvar_log(mensagem):
    data_hora = datetime.now().strftime('%d/%m/%Y/%H:%M:%S') # Obtém a data e hora atual formatada como string
    with open('log_limpeza.txt', 'a') as f: # Abre o arquivo de log em modo de anexação (append)
        f.write(f"[{data_hora}] {mensagem}\n") # Escreve a mensagem de log com a data e hora no arquivo
   
schedule.every().day.at("10:00").do(limpar_pastas)

print("Script de limpeza automática iniciado. A limpeza ocorrerá diariamente às 10:00.")

while True:
    schedule.run_pending()  
    time.sleep(1)
                    
        