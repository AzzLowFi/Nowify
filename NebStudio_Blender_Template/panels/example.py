import bpy


class NEBSTUDIO_PT_example(bpy.types.Panel):
    """Example panel for NebStudio extensions."""

    bl_label = "NebStudio"
    bl_idname = "NEBSTUDIO_PT_example"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "NebStudio"

    def draw(self, context):
        layout = self.layout
        if layout is None:
            return

        layout.label(text="Welcome to NebStudio!")
        layout.operator("nebstudio.example", icon="PLAY")


def register():
    bpy.utils.register_class(NEBSTUDIO_PT_example)


def unregister():
    bpy.utils.unregister_class(NEBSTUDIO_PT_example)
