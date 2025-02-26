import os
import sys
from unidecode import unidecode

path = sys.argv[1]

def clean_name_files(path):
    for file in os.listdir(path):
        new_name = clean_filename(file)
        if new_name:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, new_name)
            if old_path != new_path: 
                print(f"Renaming {old_path} to {new_path}")
                os.rename(old_path, new_path)

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
    
    new_name = base + ext
    
    print(new_name)
    return new_name

if(type(path) == str):
    clean_name_files(path)
