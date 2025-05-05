# es 1) 
# usando poke api salvare gli sprite (immagini) 
# normal front e normal back 
# in una cartella chiamata come il nome del pokemon

import os
import requests

nome_pokemon = input("Inserire nome pokemon: ")
response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
# Crea all'utente il nome della cartella
folder_name=f"{nome_pokemon}"
# Percorso base dove creare la cartella (modifica se necessario)
base_path = os.path.expanduser("Foto Pokemon")
# Creazione del percorso completo
destination_folder = os.path.join(base_path, folder_name)
# Creazione della cartella se non esiste
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Cartella '{destination_folder}' creata con successo!")
else:
    print(f"La cartella '{destination_folder}' esiste già.")

if response.ok:
    contenuto_risposta = response.json()
    lista_sprite=[]
    lista_sprite.append(contenuto_risposta["sprites"]["front_default"])
    lista_sprite.append(contenuto_risposta["sprites"]["back_default"])
    for i, url in enumerate(lista_sprite):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Controlla se la richiesta ha avuto successo
            # Estrai l'estensione dell'immagine dall'URL
            ext = os.path.splitext(url)[-1].lower()
            filename = f"immagine_{i+1}{ext}"
            file_path = os.path.join(destination_folder, filename)
            # Salva l'immagine
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Immagine salvata: {file_path}")
    
        except requests.exceptions.RequestException as e:
            print(f"Errore nel download {url}: {e}")

print("Download completato!")

    
