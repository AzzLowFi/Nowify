"""
NebStudio Blender Extension Template.
"""

from . import operators
from . import panels


def register():
    """Register all extension modules."""
    operators.register()
    panels.register()
    print("NebStudio Template: Registered")


def unregister():
    """Unregister all extension modules in reverse order."""
    panels.unregister()
    operators.unregister()
    print("NebStudio Template: Unregistered")
