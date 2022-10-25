'''
    Reference:
        https://docs.blender.org
'''

import bpy

import time
from math import sin, cos, pi


def delete_all():
    if (len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)


def create_mesh(name, vertices=[], edges=[], faces=[]):
    new_mesh = bpy.data.meshes.new("%s_mesh" % (name))
    new_mesh.from_pydata(vertices, edges, faces)
    new_mesh.update()
    return new_mesh


def prepare(x, y, z):

    def template(x, y, z, radius=1, angle=0):

        def rad(angle):
            return angle * pi / 180

        return [
            (x + radius * cos(rad(angle)), y + radius * sin(rad(angle)), z),
            (x + radius * cos(rad(angle)) / 2, y + radius * sin(rad(angle)) / 2, z),
            (x + radius * cos(rad(angle + 45)) / 2, y + radius * sin(rad(angle + 45)) / 2, z),
            (x + radius * cos(rad(angle + 45)), y + radius * sin(rad(angle + 45)), z),
            (x + radius * cos(rad(angle + 90)), y + radius * sin(rad(angle + 90)), z),
            (x + radius * cos(rad(angle + 135)), y + radius * sin(rad(angle + 135)), z),
            (x + radius * cos(rad(angle + 180)), y + radius * sin(rad(angle + 180)), z),
            (x + radius * cos(rad(angle + 225)), y + radius * sin(rad(angle + 225)), z),
            (x + radius * cos(rad(angle + 270)), y + radius * sin(rad(angle + 270)), z),
            (x + radius * cos(rad(angle + 315)), y + radius * sin(rad(angle + 315)), z),
            (x + radius * cos(rad(angle + 0)), y + radius * sin(rad(angle + 0)), z)
        ]   # 11 vertices


    depth = 8
    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.8, depth=depth,
        location=(x, y, z+depth/2), scale=(1, 1, 1))
    bpy.context.object.name = "drill"

    vertices = template(x=x, y=y, z=depth, radius=1.5, angle=0)
    vertices += template(x=x, y=y, z=depth+1, radius=1.5, angle=0)
    z = depth + 2
    for i in range(0, 250):
        vertices += template(x=x, y=y, z=z+i*0.05, radius=1.5, angle=i*10)
        z += 0.1

    faces = [tuple([i for i in range(0,11)])]
    faces += [(i, i+1, i+12, i+11) for i in range(0, len(vertices) - 11)]
    vertices += [(x, y, z + 20)]
    faces += [(i, i+1, len(vertices) - 1) for i in range(len(vertices) - 12, len(vertices) - 2)]

    new_mesh = create_mesh(name="spiral", vertices=vertices, faces=faces)
    new_object = bpy.data.objects.new("spiral", new_mesh)
    view_layer = bpy.context.view_layer
    view_layer.active_layer_collection.collection.objects.link(new_object)

    drill = bpy.data.objects['drill']
    spiral = bpy.data.objects['spiral']

    modifier = spiral.modifiers.new("Subsurf", 'SUBSURF')
    modifier.levels = 2

    bpy.context.view_layer.objects.active = spiral
    bpy.ops.object.modifier_apply(modifier='Subsurf')

    bpy.context.view_layer.objects.active = drill
    drill.select_set(True)
    spiral.select_set(True)
    bpy.ops.object.join()


# Drill Bit
time_start = time.time()
delete_all()
prepare(0, 0, 0)
print("Finished: %.4f sec" % (time.time() - time_start))