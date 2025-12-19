import shutil
import zipfile
import os
from pathlib import Path

def build_zip(addon_name="my_addon"):
    """
    Zabalí addon do ZIP souboru pro distribuci.
    Vynechává testy, .git, pyproject.toml atd.
    """
    project_root = Path(__file__).parent.parent
    dist_dir = project_root / "dist"
    addon_dir = project_root / "addon" / addon_name
    
    # Vytvoření dist adresáře
    dist_dir.mkdir(exist_ok=True)
    
    zip_path = dist_dir / f"{addon_name}.zip"
    
    print(f"Building {zip_path}...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(addon_dir):
            for file in files:
                # Cesta k souboru
                file_path = Path(root) / file
                # Relativní cesta uvnitř ZIPu (musí začínat jménem addonu)
                arcname = Path(addon_name) / file_path.relative_to(addon_dir)
                
                # Ignorovat pycache
                if "__pycache__" in str(file_path):
                    continue
                    
                zipf.write(file_path, arcname)
    
    print("Build complete!")
    return zip_path

if __name__ == "__main__":
    build_zip()
