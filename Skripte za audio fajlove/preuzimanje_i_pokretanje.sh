#! /usr/bin/env bash

python3 bihamk_audio.py

ffmpeg -i -n bihamk_audio.mp3 -acodec pcm_s16le -ac 1 -ar 16000 test.wav

cp -n test.wav /home/pjproject-2.11/
