import sys
import os
import importlib
from pathlib import Path

def get_deps_path():
    """Vrátí cestu k adresáři se závislostmi."""
    return Path(__file__).parent.parent / "_deps"

def add_deps_to_path():
    """Přidá adresář _deps do sys.path, pokud existuje."""
    deps_path = str(get_deps_path())
    if deps_path not in sys.path and os.path.exists(deps_path):
        sys.path.insert(0, deps_path)
        return True
    return False

def import_dependency(module_name):
    """
    Bezpečně se pokusí importovat modul.
    Vrací modul nebo None, pokud modul není nalezen.
    """
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None

def check_dependencies(required_modules):
    """
    Zkontroluje, zda jsou dostupné všechny požadované moduly.
    Vrací seznam chybějících modulů.
    """
    missing = []
    for module in required_modules:
        if import_dependency(module) is None:
            missing.append(module)
    return missing
