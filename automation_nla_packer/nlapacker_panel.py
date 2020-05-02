import bpy

class nlapacker_PT_panel(bpy.types.Panel):
    bl_idname = "nla_packer_panel"
    bl_label = "Simple NLA Packer"
    bl_category = "Automation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('automation.nlapacker', text="Pack Actions as NLA Tracks")