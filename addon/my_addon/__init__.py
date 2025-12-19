bl_info = {
    "name": "My Addon Template",
    "author": "Jiří Lebduška",
    "version": (0, 1, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > My Addon",
    "description": "Template pro Blender addon s čistou architekturou",
    "warning": "",
    "doc_url": "",
    "category": "Generic",
}

import sys
import importlib

# Seznam modulů, které mají být reloadovány při F3 > Reload Scripts
# Pořadí je důležité
modules_to_reload = [
    "deps.deps",
    "core.client",
    "core.state",
    "blender.registration",
]

def reload_addon_modules():
    """Zajistí reload všech modulů addonu."""
    prefix = __package__ + "."
    for module_name in modules_to_reload:
        full_name = prefix + module_name
        if full_name in sys.modules:
            importlib.reload(sys.modules[full_name])

def register():
    # Inicializace závislostí
    from .deps import deps
    deps.add_deps_to_path()

    # Registrace Blender komponent
    from .blender import registration
    registration.register()

def unregister():
    # Odregistrace Blender komponent
    from .blender import registration
    registration.unregister()

if __name__ == "__main__":
    register()
