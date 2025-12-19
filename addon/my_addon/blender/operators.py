import bpy

class MYADDON_OT_sample_operator(bpy.types.Operator):
    """Ukázkový operátor pro volání core logiky."""
    bl_idname = "my_addon.sample_operator"
    bl_label = "Sample Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from ..core.client import Client
        client = Client()
        success = client.connect()
        
        if success:
            self.report({'INFO'}, "Core Client connected successfully!")
        else:
            self.report({'ERROR'}, "Failed to connect Core Client")
            
        return {'FINISHED'}
