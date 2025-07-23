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

for fajlnev in os.listdir(mappa):
    fajl_utvonal = os.path.join(mappa, fajlnev)

    if os.path.isfile(fajl_utvonal) and fajlnev.endswith((".html", ".htm")):
        # Fájl tartalom beolvasása
        with open(fajl_utvonal, "r") as f:
            tartalom = f.read()

        # Title mező keresése
        talalat = title_regex.search(tartalom)
        cim = talalat.group(1).strip() if talalat else fajlnev

        modulok.append({
            "fajl": f"/modulok/modulfajajlok/{fajlnev}".replace("\\", "/"),
            "cim": cim
        })


# JSON mentés
with open(os.path.join(sajat_ut, 'modulok/modulok.json'), 'w') as f:
    json.dump(modulok, f, indent=4, ensure_ascii=False)

print(f"{len(modulok)} fájl feldolgozva, mentve a modulok.json fájlba.")
