bl_info = {
    "name" : "Shader Library",
    "author" : "AndreBastos",
    "version" : (1,0),
    "blender" : (3,0,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Shader"
} 

import bpy

class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Library'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select a Shader to be added.")
        row.operator('shader.diamond_operator')

#create a custon operator for the diamond shader        
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator'
    
    def execute(self, context):
        #creating a new shader and calling it diamond
        material_diamond = bpy.data.materials.new(name = "Diamond")
        #Enable use nodes
        material_diamond.use_nodes = True
        #remove the principled bsdf
        material_diamond.node_tree.nodes.remove(
            material_diamond.node_tree.nodes.get('Principled BSDF'))
            
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        material_output.location = (-400,0)
        
        #adding glass1 node
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #set location of node
        glass1_node.location = (-600,0)
        #setting the default color
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        #setting the default IOR value
        glass1_node.inputs[2].default_value = 1.446 
        
        #adding glass2 node
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #set location of node
        glass2_node.location = (-600,-150)
        #setting the default color
        glass2_node.inputs[0].default_value = (1, 0, 0, 1)
        #setting the default IOR value
        glass2_node.inputs[2].default_value = 1.446 
        
        #adding glass3 node
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #set location of node
        glass3_node.location = (-600,-300)
        #setting the default color
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        #setting the default IOR value
        glass3_node.inputs[2].default_value = 1.450 
        
        #create the add shader node and reference it as 'add1'
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        #set location of node
        add1_node.location = (-400,-50)
        #setting the label
        add1_node.label = "Add 1"
        #minimizes the node
        add1_node.hide = True
        #deselect the node
        add1_node.select = False
        
        #create the add shader node and reference it as 'add2'
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        #set location of node
        add2_node.location = (-100,0)
        #setting the label
        add2_node.label = "Add 2"
        #minimizes the node
        add2_node.hide = True
        #deselect the node
        add2_node.select = False
        
        #adding glass4 node
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        #set location of node
        glass4_node.location = (-150,-150)
        #setting the default color
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        #setting the default IOR value
        glass4_node.inputs[2].default_value = 1.450 
        #deselect the node
        add2_node.select = False
        
        #create the mix shader node and reference it as 'Mix1'
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        #set location of node
        mix1_node.location = (200, 0)
        #deselect the node
        mix1_node.select = False
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])        
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
        
        



def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)
    

def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    
if __name__ == "__main__":
    register()