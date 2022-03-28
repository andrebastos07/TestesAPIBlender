def AplicarCores():
    #Aplicando Cores // Arrumar
    mat_green = bpy.data.materials.new("green")
    mat_green.diffuse_color = (0, 0.8, 0)

    mat_gray = bpy.data.materials.new("gray")
    mat_gray.diffuse_color = (0.8, 0.8, 0.8)

    hexa_mesh.materials.append(mat_green)
    hexa_mesh.materials.append(mat_gray)

    count = 0
    for f in bm.faces:
        if count in [1,3]:
            f.material_index = 1
        count += 1
        
    bm.to_mesh(mesh)

def CoordMesh():
    bpy.ops.object.editmode_toggle()

    # Get the active mesh
    obj = bpy.context.edit_object
    me = obj.data

    # Get a BMesh representation
    bm = bmesh.from_edit_mesh(me)

    for cara in bm.faces:
        print('Faces: {}', format(cara.index))
        for vertice in cara.verts:
            print('Vertice: {}', format(vertice.index),vertice.co)


    bpy.ops.object.editmode_toggle()