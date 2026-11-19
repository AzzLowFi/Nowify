import bpy

from ..core import registry


class NEBSTUDIO_OT_example(bpy.types.Operator):
    """Example operator for NebStudio extensions."""

    bl_idname = "nebstudio.example"
    bl_label = "NebStudio Example"
    bl_description = "Run a test action"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.report({"INFO"}, "NebStudio is working!")
        return {"FINISHED"}


CLASSES = (
    NEBSTUDIO_OT_example,
)


def register():
    registry.register_classes(CLASSES)


def unregister():
    registry.unregister_classes(CLASSES)
