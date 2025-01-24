#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# URL stranice koja sadrži audio fajl
page_url = 'https://bihamk.ba/spi/stanje-na-cesti-u-bih'

# Slanje GET zahtjeva za preuzimanje HTML sadržaja stranice
response = requests.get(page_url)

# Provjera uspješnog statusa (status kod 200)
if response.status_code == 200:
    # Parsiranje HTML sadržaja
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tražimo <audio> tag sa klasom 'mt-3'
    audio_tag = soup.find('audio', class_='mt-3')
    
    if audio_tag:
        # Potražite <source> tag unutar <audio> taga
        source_tag = audio_tag.find('source')
        if source_tag and 'src' in source_tag.attrs:
            audio_url = source_tag['src']
            #print(f"Audio fajl se nalazi na: {audio_url}")
            
            # Sada skidamo audio fajl sa preuzetog URL-a
            filename = "bihamk_audio.mp3" 
            response = requests.get(audio_url, stream=True)
            response.raise_for_status()

            with open(filename, "wb") as audio_file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        audio_file.write(chunk)

