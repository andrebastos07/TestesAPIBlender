import bpy, bmesh
import random

grama = bpy.data.materials["Grama"]
pedra = bpy.data.materials["Pedra"]

bpy.context.object.active_material_index = 0
bpy.context.object.active_material = grama

bpy.context.object.active_material_index = 1
bpy.context.object.active_material = pedra

bpy.ops.object.editmode_toggle()

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data

# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

for cara in bm.faces:
    r = random.randint(0,1)
    if r == 1:
        cara.select = True
    else:
        cara.select = False
        
bpy.ops.object.material_slot_assign()



bpy.ops.object.editmode_toggle()