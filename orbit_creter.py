import bpy
import site
site.addsitedir(r"C:\\Users\\эльдо\\OneDrive\\Рабочий стол\\new_venv\\venv\\Lib\\site-packages")
import random as rd
import numpy as np

class BieserProperty(bpy.types.PropertyGroup):
    
    bl_scale: bpy.props.FloatVectorProperty(default=(1.0, 1.0, 1.0))
    bl_link_object: bpy.props.BoolProperty(default=False)
    random_mode: bpy.props.BoolProperty(default=False)
    

class Operator(bpy.types.Operator):
    
    bl_idname = "ops.orbit_creater"
    bl_label = "Orbit Creater"
    
    def execute(self, context):
        
        scene = context.scene
        tool = scene.new_object
        
        bpy.ops.curve.primitive_bezier_circle_add(location=(0.0, 0.0, 0.0))
        bpy.ops.mesh.primitive_ico_sphere_add(location=(0.0, 0.0, 0.0))
        ico_spheres = [x for x in context.scene.objects if x.type == "MESH"]
        biezer_circle = [x for x in context.scene.objects if x.type == "CURVE"]
        
        if tool.random_mode == True:
            for element in range(len(ico_spheres)):
                
                biezer_circle[element].rotation_euler =(rd.randint(-360, 360),
                rd.randint(-360, 360),rd.randint(-360, 360))
                
                biezer_circle[element].location = (rd.randint(-7, 7),
                rd.randint(-7, 7),rd.randint(-7, 7))
                ico_spheres[element].show_texture_space = True
                ico_spheres[element].show_axis = True
                biezer_scale = rd.randint(45, 120)
                biezer_circle[element].scale = (biezer_scale, biezer_scale, biezer_scale)
                ico_sphere_scale = rd.randint(1, 5)
                ico_spheres[element].scale = (ico_sphere_scale, ico_sphere_scale, ico_sphere_scale)
                
                if tool.bl_link_object == True:
                    bpy.ops.object.constraint_add(type="FOLLOW_PATH")
                    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner="OBJECT")
                    ico_spheres[element].constraints["Follow Path"].target = biezer_circle[element]
                else:
                    pass  
        return {"FINISHED"}

class Panel(bpy.types.Panel):
    
    bl_idname = "mesh.panel"
    bl_label = "Orbit Maneger"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        tool = scene.new_object
        
        layout.prop(tool, "bl_scale")
        layout.prop(tool, "bl_link_object")
        layout.prop(tool, "random_mode")
        
        row = layout.row()
        row.operator("ops.orbit_creater")
        
        
        
        
        


cls_list = [BieserProperty, Operator, Panel]

def register():
    for cls in cls_list:
        bpy.utils.register_class(cls)
        bpy.types.Scene.new_object = bpy.props.PointerProperty(type=BieserProperty)
        
def unregister():
    for cls in cls_list:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.new_object

register()
    
        
    