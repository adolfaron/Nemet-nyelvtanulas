# lista_generator.py

import os
import json
import re

# Modulok mappa útvonala
sajat_ut = os.path.dirname(__file__)
mappa = os.path.join(sajat_ut, "modulok/modulfajajlok")

# Regex a <title> kiolvasásához
title_regex = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)

# Lista a kimeneti JSON-hoz
modulok = []

# Több kódolás kipróbálása
def beolvas_tartalom(fajl_utvonal):
    for encoding in ("utf-8", "utf-8-sig", "cp1250", "latin-1"):
        try:
            with open(fajl_utvonal, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("Nem sikerült értelmezni a fájlt semmilyen ismert kódolással.")

for fajlnev in os.listdir(mappa):
    fajl_utvonal = os.path.join(mappa, fajlnev)

    if os.path.isfile(fajl_utvonal) and fajlnev.endswith((".html", ".htm")):
        # Fájl tartalom beolvasása többféle kódolással
        tartalom = beolvas_tartalom(fajl_utvonal)

        # Title mező keresése
        talalat = title_regex.search(tartalom)
        cim = talalat.group(1).strip() if talalat else fajlnev

        modulok.append({
            "fajl": f"/modulok/modulfajajlok/{fajlnev}".replace("\\", "/"),
            "cim": cim
        })

# JSON mentés UTF-8 kódolással
with open(os.path.join(sajat_ut, 'modulok/modulok.json'), 'w', encoding="utf-8") as f:
    json.dump(modulok, f, indent=4, ensure_ascii=False)

print(f"{len(modulok)} fájl feldolgozva, mentve a modulok.json fájlba.")
