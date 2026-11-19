import bpy


class NEBSTUDIO_OT_example(bpy.types.Operator):
    """Example operator for NebStudio extensions."""

    bl_idname = "nebstudio.example"
    bl_label = "NebStudio Example"
    bl_description = "Run a test action"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.report({"INFO"}, "NebStudio is working!")
        return {"FINISHED"}


def register():
    bpy.utils.register_class(NEBSTUDIO_OT_example)


def unregister():
    bpy.utils.unregister_class(NEBSTUDIO_OT_example)
