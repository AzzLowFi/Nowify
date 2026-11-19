"""Centralized registration helpers for Blender classes."""

import bpy


def _get_registered_class(cls):
    """Find a registered Blender class by its Python name."""
    try:
        return getattr(bpy.types, cls.__name__)
    except AttributeError:
        return None


def register_classes(classes):
    """Register classes safely, replacing stale registrations if necessary."""
    registered = []

    try:
        for cls in classes:
            existing = _get_registered_class(cls)

            if existing is cls:
                continue

            if existing is not None:
                bpy.utils.unregister_class(existing)

            bpy.utils.register_class(cls)
            registered.append(cls)

    except Exception:
        for cls in reversed(registered):
            existing = _get_registered_class(cls)

            if existing is not None:
                bpy.utils.unregister_class(existing)

        raise


def unregister_classes(classes):
    """Unregister classes in reverse order."""
    for cls in reversed(classes):
        existing = _get_registered_class(cls)

        if existing is not None:
            bpy.utils.unregister_class(existing)
