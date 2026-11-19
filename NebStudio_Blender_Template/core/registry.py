"""Centralized registration helpers for Blender classes."""

import bpy


def register_classes(classes):
    """Register classes safely, rolling back if registration fails."""
    registered = []

    try:
        for cls in classes:
            if bpy.utils.is_registered_class(cls):
                continue

            bpy.utils.register_class(cls)
            registered.append(cls)

    except Exception:
        for cls in reversed(registered):
            bpy.utils.unregister_class(cls)
        raise


def unregister_classes(classes):
    """Unregister classes in reverse order when currently registered."""
    for cls in reversed(classes):
        if bpy.utils.is_registered_class(cls):
            bpy.utils.unregister_class(cls)
