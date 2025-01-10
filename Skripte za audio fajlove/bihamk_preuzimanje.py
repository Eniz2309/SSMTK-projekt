import requests


url = "https://bihamk.ba/assets/files/page/1736519958-stanje-na-cestamamp3mp3-pages.mp3"

filename = "bihamk_audio.mp3"

response = requests.get(url, stream=True)
response.raise_for_status()

with open(filename, "wb") as audio_file:
	for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # Provjera da nije prazan blok
                audio_file.write(chunk)