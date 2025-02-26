import os
import sys
from unidecode import unidecode
import re

# ARGUMENT 1 : Chemin du dossier à traiter
path = sys.argv[1]
nbr_files = len(os.listdir(path))
nbr_files_treated = 0
files_treated = set(os.listdir(path))

def clean_name_files(path):
    global nbr_files_treated 
    for file in os.listdir(path):
        new_name = clean_filename(file)
        if new_name:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, new_name)
            if old_path != new_path: 
                os.rename(old_path, new_path)
                files_treated.add(new_name)
                nbr_files_treated += 1
                print(f"{nbr_files_treated} fichiers traités sur {nbr_files}")          

def clean_filename(name):
    base = os.path.splitext(name)[0]
    ext = os.path.splitext(name)[1]
    
    base = unidecode(base)
    
    base = base.replace(' ', '_').replace('-', '_').replace('.', '_')
    base = base.replace(',', '_').replace(';', '_').replace('(', '_').replace(')', '_')
    base = base.replace('&', '_').replace('%', '_').replace('$', '_').replace('@', '_')
    base = base.replace('!', '_').replace('?', '_').replace('#', '_').replace('=', '_')
    base = base.replace('[', '_').replace(']', '_').replace('{', '_').replace('}', '_')
    base = base.replace('^', '_').replace('~', '_')
    base = base.lower()
    
    base = re.sub(r'_+', '_', base).strip('_')
    base = re.sub(r'_\d+$', '', base)
    
    counter = 1
    new_name = f"{base}{ext}"
    while new_name in files_treated:
        new_name = f"{base}_{counter}{ext}"
        counter += 1
    
    print(new_name)
    return new_name

if(type(path) == str):
    clean_name_files(path)
