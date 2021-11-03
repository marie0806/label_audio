import os
import playsound
import json


AUDIO_FOLDER = "../MP3_Files"

def get_audio_paths(audio_folder):
    audio_paths=[]
    for root, dir, files in os.walk(audio_folder):
        for file in files:
            if file.endswith(".mp3"):
                audio_paths.append(os.path.join(root, file))
    return audio_paths



if os.path.isfile('files.json'):
    with open('files.json', 'r') as file:
        data = json.load(file)
else:
    data = {}

def check_audio(audio_path):
    choice = None
    while choice not in ("n", "c"):
        mp3 = playsound.playsound(audio_full_path)
        choice = input("Enter n or c: ")
        if choice == 'n':
            print("The audio is noisy")
        elif choice == 'c':
            print("The audio is clean")
        else:
            print("Wrong input provided, please hear the audio one more time and select from options {c, n}")
    file = audio_full_path.split("/")[-1]
    data[file] = choice


for audio_full_path in get_audio_paths(AUDIO_FOLDER):
    file = audio_full_path.split("/")[-1]
    if file in data:
        continue
    check_audio(audio_full_path)
    choice = None
    while choice not in ("y", "n"):
        choice = input("Continue: y or n: ")
        if choice in ('y', 'n'):
            continue
        else:
            print("Invalid choice, please select from options {y, n}")
    if choice == 'n':
        break

with open('files.json', 'w') as f:
    json.dump(data, f)


