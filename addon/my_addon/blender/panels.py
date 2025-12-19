import bpy

class MYADDON_PT_main_panel(bpy.types.Panel):
    """Hlavní panel addonu v Sidebar (N-panel)."""
    bl_label = "My Addon Template"
    bl_idname = "MYADDON_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        
        col.label(text="Core Logic Status:")
        # Tady by mohlo být zobrazení stavu z core.state
        col.operator("my_addon.sample_operator", text="Run Sample Action")
