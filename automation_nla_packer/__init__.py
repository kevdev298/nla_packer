bl_info = {
    "name" : "NLAPacker",
    "author" : "_kev_dev",
    "description" : "Simple packer of Animations to NLA tracks for animation export to the Godot Engine",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "category" : "Automation"
}

import bpy
from . nlapacker_op import nlapacker_OP_operator
from . nlapacker_panel import nlapacker_PT_panel

classes = (nlapacker_OP_operator, nlapacker_PT_panel)

register, unregister = bpy.utils.register_classes_factory(classes)
