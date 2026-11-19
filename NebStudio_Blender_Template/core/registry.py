"""Centralized registration helpers for Blender classes."""

import bpy


_REGISTERED_CLASSES = set()


def register_classes(classes):
    """Register classes safely, rolling back if registration fails."""
    registered = []

    try:
        for cls in classes:
            if cls in _REGISTERED_CLASSES:
                continue

            bpy.utils.register_class(cls)
            _REGISTERED_CLASSES.add(cls)
            registered.append(cls)

    except Exception:
        for cls in reversed(registered):
            bpy.utils.unregister_class(cls)
            _REGISTERED_CLASSES.discard(cls)
        raise


def unregister_classes(classes):
    """Unregister classes in reverse order."""
    for cls in reversed(classes):
        if cls not in _REGISTERED_CLASSES:
            continue

        bpy.utils.unregister_class(cls)
        _REGISTERED_CLASSES.discard(cls)
