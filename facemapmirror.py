import bpy


bl_info = {
        "name": "Facemap Mirror",
        "description": "UV map mirroring based on face maps",
        "author": "Austin",
        "location": "UV Image Editor > Tools > 'TexTools' > Mirror Tools",
        "version": (1, 0),
        "blender": (3, 1, 2),
        "support": "COMMUNITY",
        "category": "UV",
        "tracker_url": "https://github.com/depdas2/Facemap-Mirror"
        }


class FlipIslands(bpy.types.Operator):
    bl_idname = "aus.flipisland"
    bl_label = "Flip Selected"
    bl_description = "This will flip the selected islands"
    bl_options = {"REGISTER"}

    def execute(self, context):
        bpy.ops.transform.resize(value=(-1, 1, 1))
        bpy.ops.transform.resize(value=(-1, -1, -1))

        return {"FINISHED"}

class ShowAll(bpy.types.Operator):
    bl_idname = "aus.showalluvs"
    bl_label = "Show all UVs"
    bl_description = "This will show all of the UVs"
    bl_options = {"REGISTER"}

    def execute(self, context):
        bpy.data.scenes["Scene"].tool_settings.use_uv_select_sync = True
        bpy.ops.mesh.select_all(action='DESELECT')
        return {"FINISHED"}


class ShowMap(bpy.types.Operator):
    bl_idname = "aus.showmirror"
    bl_label = "Show Mirror"
    bl_description = "Shows the mirrored mesh"

    def execute(self, context):
        max = len(bpy.context.object.face_maps)
        counter = 0
        bpy.ops.uv.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='DESELECT')
        
        while counter < max:
            bpy.context.object.face_maps.active_index = counter 
            bpy.ops.object.face_map_select()
            counter += 1
        
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.data.scenes["Scene"].tool_settings.use_uv_select_sync = False

        return {"FINISHED"}


class splitUVPX(bpy.types.Operator):
    bl_idname = "aus.facemapsplitp"
    bl_label = "UV Splitting"
    bl_description = "This will split your UV map based on face maps"
    bl_options = {"REGISTER"}

    def execute(self, context):
        max = len(bpy.context.object.face_maps)
        counter = 0
        bpy.ops.uv.select_all(action='DESELECT')
        
        while counter < max:
            bpy.context.object.face_maps.active_index = counter 
            bpy.ops.object.face_map_select()
            counter += 1   

        bpy.data.scenes["Scene"].tool_settings.use_uv_select_sync = True
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.transform.translate(value=(1, 0, 0))

        return {"FINISHED"}


class splitUVNX(bpy.types.Operator):
    bl_idname = "aus.facemapsplitn"
    bl_label = "UV Splitting"
    bl_description = "This will split your UV map based on face maps"
    bl_options = {"REGISTER"}

    def execute(self, context):
        max = len(bpy.context.object.face_maps)
        counter = 0
        bpy.ops.uv.select_all(action='DESELECT')
        
        while counter < max:
            bpy.context.object.face_maps.active_index = counter 
            bpy.ops.object.face_map_select()
            counter += 1   

        bpy.data.scenes["Scene"].tool_settings.use_uv_select_sync = True
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.transform.translate(value=(-1, 0, 0))
        
        return {"FINISHED"}


class AusPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Mirror Tools"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "TexTools"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Split UVs")
        row = layout.row(align=True)
        col = layout.column()
        row.operator("aus.facemapsplitn", text="-")
        row.operator("aus.facemapsplitp", text="+")
        col.operator("aus.flipisland")
        col.operator("aus.showmirror", text="Show Mirror")
        col.operator("aus.showalluvs")



classes = [splitUVPX, splitUVNX, ShowMap, ShowAll, AusPanel, FlipIslands]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
