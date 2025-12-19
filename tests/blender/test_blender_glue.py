import pytest

try:
    import bpy
    BLENDER_AVAILABLE = True
except ImportError:
    BLENDER_AVAILABLE = False

@pytest.mark.skipif(not BLENDER_AVAILABLE, reason="Blender (bpy) not available")
def test_blender_registration():
    """Ověří, že třídy addonu jsou registrované v Blenderu."""
    # V headless testu spouštěném přes tools/run_blender_tests.py
    # bude bpy dostupné.
    
    # Příklad kontroly, zda je přítomen náš operátor
    assert hasattr(bpy.ops.my_addon, "sample_operator")

@pytest.mark.skipif(not BLENDER_AVAILABLE, reason="Blender (bpy) not available")
def test_blender_ui_panel():
    """Ověří existenci UI panelu."""
    from my_addon.blender.panels import MYADDON_PT_main_panel
    assert MYADDON_PT_main_panel.bl_idname == "MYADDON_PT_main_panel"
