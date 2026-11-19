"""
NebStudio - Blender Extension Template
Main entry point.
"""

from . import operators
from . import panels


def register():
    """Register all extension modules."""
    operators.register()
    panels.register()
    print("NebStudio Template: Registered")


def unregister():
    """Unregister all extension modules."""
    panels.unregister()
    operators.unregister()
    print("NebStudio Template: Unregistered")
