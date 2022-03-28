bl_info = {
    "name" : "Object Adder",
    "author" : "AndreBastos",
    "version" : (1,0),
    "blender" : (3,0,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh"
}    

import bpy

class UIPanel(bpy.types.Panel):
    bl_label = "UI Panel"
    bl_idname = "PT_UIPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add object", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE')
      
      
      
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    bl_parent_id = 'PT_UIPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "Select an option to scale your object", icon = 'FONT_DATA')      
        row = layout.row()
        row.operator("transform.resize")      
        row = layout.row()
        layout_scale_y = 1.2
        
        col = layout.column()
        col.prop(obj, "scale")
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    bl_parent_id = 'PT_UIPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Select a Special Option", icon = 'COLOR_BLUE')
        row = layout.row()
        row.operator("object.shade_smooth", icon = 'MOD_SMOOTH', text="Set Smooth Shading")    
        row.operator("object.subdivision_set")
      
        
def register():
    bpy.utils.register_class(UIPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    

def unregister():
    bpy.utils.unregister_class(UIPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    
if __name__ == "__main__":
    register()