import bpy
import sys
import importlib

# Seznam tříd k registraci
from . import panels
from . import operators

classes = (
    panels.MYADDON_PT_main_panel,
    operators.MYADDON_OT_sample_operator,
)

def register():
    # Registrace tříd
    for cls in classes:
        bpy.utils.register_class(cls)
    
    print("My Addon: Classes registered")

def unregister():
    # Odregistrace tříd (v opačném pořadí)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    print("My Addon: Classes unregistered")

def safe_reload():
    """
    Provede bezpečný reload addonu.
    Využívá timer, aby reload neprobíhal přímo v rámci registrace/odregistrace,
    což může v Blenderu způsobit nestabilitu.
    """
    def reload_task():
        print("My Addon: Performing safe reload...")
        # Zde by byla logika pro znovunačtení modulů
        # V praxi se často používá F3 > Reload Scripts, 
        # ale pro interní potřeby addonu může být užitečné mít toto.
        return None # Spustit pouze jednou

    bpy.app.timers.register(reload_task)
