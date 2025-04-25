#!/usr/bin/env python3
import os
import json

# adjust if your files live elsewhere
MP3_DIR = 'mp3s'
BASE_URL = 'https://jambojeef.github.io/mp3s'

def main():
    files = sorted(f for f in os.listdir(MP3_DIR) if f.lower().endswith('.mp3'))
    urls  = [f"{BASE_URL}/{f}" for f in files]
    with open('manifest.json', 'w') as out:
        json.dump(urls, out, indent=2)
    print(f"Generated manifest.json with {len(urls)} entries.")

if __name__=='__main__':
    main()
