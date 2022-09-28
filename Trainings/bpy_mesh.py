import bpy
from math import sin, cos, pi

def create_mesh(name, vertices=[], edges=[], faces=[]):
    new_mesh = bpy.data.meshes.new("%s_mesh" % (name))
    new_mesh.from_pydata(vertices, edges, faces)
    new_mesh.update()
    return new_mesh

def prepare(name, x, y, z, segments, angle, radius, width, step):
    vertices=[]
    for i in range(segments + 1):
        rad =  i * angle * pi / 180
        vertices+=[(x + width / 2, y, z), (x - width / 2, y, z)]
        y += radius * cos(rad) + i * step
        z += radius * sin(rad)
    faces=[(i, i+1, i+3, i+2) for i in range(0, len(vertices) - 3, 2)]

    new_mesh = create_mesh(name=name, vertices=vertices, faces=faces)
    new_object = bpy.data.objects.new(name, new_mesh)
    view_layer = bpy.context.view_layer
    view_layer.active_layer_collection.collection.objects.link(new_object)

# Test
prepare("obj_1",  0, 0, 0, 10, 36,  1, 1,    0)
prepare("obj_2",  2, 0, 0, 10, 36,  1, 1,  0.2)
prepare("obj_3",  4, 0, 0, 10, 36,  1, 1, -0.2)
prepare("obj_4",  6, 0, 0, 10, 36, -1, 1,  0.1)
prepare("obj_5",  8, 0, 0, 18, 20,  1, 1,  0.1)
prepare("obj_6", 10, 0, 0, 36, 10,  1, 1, 0.01)
prepare("obj_7", 12, 0, 0, 72, 20,  1, 1, 0.01)
prepare("obj_8", 14, 0, 0, 72, 15,  1, 1, 0.01)
