import os
import shutil
from pathlib import Path

def organize_files(directory_path):
    # caminho convertido para um objeto path 
    p = Path(directory_path)
    
    # iteracao dos itens no diretorio especifico
    for file_path in p.iterdir():
        # ignora diretórios
        if file_path.is_dir():
            continue

        # pega a extensão do arquivo (ex: ".jpg") e remove o ponto inicial para usar como nome da pasta
        extension = file_path.suffix.lower().strip('.')
        
        # se nao tiver extensao coloca em pasta "Sem_Extensao"
        if not extension:
            folder_name = "Sem_Extensao"
        else:
            # mapear extensoes para nomes de pastas comuns 
            if extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                folder_name = 'Imagens'
            elif extension in ['mp4', 'mkv', 'avi', 'mov']:
                folder_name = 'Videos'
            elif extension in ['pdf', 'doc', 'docx', 'txt', 'xlsx']:
                folder_name = 'Documentos'
            elif extension in ['mp3', 'wav', 'ogg']:
                folder_name = 'Audio'
            else:
                folder_name = f"{extension.upper()}_Files" # Pasta padrão baseada na extensão

        # caminho para a nova pasta de destino
        destination_folder = p / folder_name
        
        # cria pasta se ela não existir (exist_ok=True evita erros se já existir)
        destination_folder.mkdir(exist_ok=True)
        
        # move arquivo para a pasta de destino
        try:
            shutil.move(str(file_path), str(destination_folder / file_path.name))
            print(f"Movido: {file_path.name} -> {folder_name}")
        except shutil.Error as e:
            print(f"Erro ao mover {file_path.name}: {e}")

# diretorio (altere para o seu caminho)
# exemplo: r"C:\Users\SeuUsuario\Downloads"
# linux/macOS: "/home/seu_usuario/Downloads"

#'r' trata a string como raw string
directory_to_organize = r"C:\Caminho\Para\Sua\Pasta" 

# chama funcao 
organize_files(directory_to_organize)
print("\nOrganização concluída!")
