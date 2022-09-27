'''
    Reference:
        https://docs.blender.org/api/current/index.html
'''

import bpy
import time

# Control runtime
time_start = time.time()

# Test
objects = list(bpy.data.objects)
selected_objects = list(bpy.context.selected_objects)
active_object = bpy.context.active_object

for item in objects:
    sel = ": selected" if item in selected_objects else ""
    act = ": active" if item == active_object else ""
    xyz = [(i.co[0], i.co[1], i.co[2]) for i in item.data.vertices] if item.type == 'MESH' else ""
    print(item.name, sel, act)
    print(xyz)  
    
# Runtime
print("Finished: %.4f sec" % (time.time() - time_start))
