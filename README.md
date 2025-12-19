<p align="center">
  <img src="icon.svg" width="128" height="128" alt="Blender Addon Template Icon">
</p>

# 🏗️ Blender Addon Template

Profesionální šablona pro vývoj Blender addonů (4.5+) s čistou architekturou a automatizovaným testováním.

## 🚀 Rychlý start

1. Klikněte na **"Use this template"** na GitHubu.
2. Přejmenujte složku `addon/my_addon` na jméno svého addonu.
3. Upravte metadata v `addon/my_addon/__init__.py` (v `bl_info`).

## 🏛️ Architektura

Šablona striktně dodržuje oddělení zájmů:
- **`core/`**: Čistá Python logika. Nesmí importovat `bpy`.
- **`blender/`**: Glue kód pro Blender (operátory, panely, registrace).
- **`deps/`**: Správa externích závislostí.
- **`tests/`**: Testy umístěné mimo distribuční balíček.

## 📦 Závislosti

Externí knihovny instalujte do složky `addon/my_addon/_deps`:
```bash
pip install requests -t addon/my_addon/_deps
```
Addon je navržen tak, aby se načetl i v případě, že závislosti chybí (např. pro zobrazení varování uživateli).

## 🧪 Testování

Podrobné informace o testování naleznete v [TESTING.md](TESTING.md).

## 🛠️ Build (Vytvoření ZIPu)

Pro vytvoření instalovatelného balíčku spusťte:
```bash
python3 tools/build_zip.py
```
Výsledek najdete v adresáři `dist/`.

## 📜 Licence
GNU GPL v3
