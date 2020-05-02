import bpy

class nlapacker_OP_operator(bpy.types.Operator):
    bl_idname = "automation.nlapacker"
    bl_label = "Pack Actions as NLA Tracks"
    bl_description = "Packs Actions in file as NLA tracks for selected object"

    def execute(self, context):
        active_object = context.active_object
        if active_object.type == 'ARMATURE':
            if not active_object.animation_data:
                active_object.animation_data_create()
            
            for track in active_object.animation_data.nla_tracks:
                active_object.animation_data.nla_tracks.remove(track)
            
            for anim in bpy.data.actions:
                active_object.animation_data.nla_tracks.new()
                index = len(active_object.animation_data.nla_tracks) - 1
                active_object.animation_data.nla_tracks[index].name = anim.name
                active_object.animation_data.nla_tracks[index].strips.new(anim.name, 0, anim)
                active_object.animation_data.nla_tracks[index].lock = True            
            
        return {'FINISHED'}
