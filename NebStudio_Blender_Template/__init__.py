"""
NebStudio - Blender Extension Template
Main entry point.
"""

from . import operators
from . import panels


def register():
    """Register all extension modules safely."""
    operators.register()

    try:
        panels.register()
    except Exception:
        operators.unregister()
        raise

    print("NebStudio Template: Registered")


def unregister():
    """Unregister all extension modules."""
    try:
        panels.unregister()
    finally:
        operators.unregister()

    print("NebStudio Template: Unregistered")
