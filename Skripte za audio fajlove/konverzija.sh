#!/bin/sh

python3 skripta_za_preuzimanje.py

/var/lib/snapd/snap/bin/ffmpeg -i bihamk_audio.mp3 -acodec pcm_s16le -ac 1 -ar 16000 test.wav
