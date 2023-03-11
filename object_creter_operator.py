import bpy
 #here we create the bars with sttings for our operator
class PropertyGroup(bpy.types.PropertyGroup):
    
    count_X: bpy.props.IntProperty(default=2, min=1, max=10)
    count_Y: bpy.props.IntProperty(default=2, min=1, max=10)
    count_Z: bpy.props.IntProperty(default=2, min=1, max=10)
    types_of_objects: bpy.props.EnumProperty(items=[
    ("Torus", "Torus mesh", ""),
    ("Cube", "Cube mesh",""),
    ("uv_Sphere", "uv_Sphere mesh", ""),
    ("ico_Sphere", "ico_Sphere mesh", ""),
    ("Cone", "Cone mesh", ""),
    ("Cylinder", "Cylinder mesh", ""),
    ("Grid", "Grid mesh", ""),
    ("Monkey", "Monkey mesh", "")
    ])
    rotation: bpy.props.FloatVectorProperty(default=(0.0, 0.0, 0.0))
    location: bpy.props.FloatVectorProperty(default=(0.0, 0.0, 0.0))
    scale: bpy.props.FloatVectorProperty(default=(1.0, 1.0, 1.0))
    show_axis: bpy.props.BoolProperty(default=False)
    show_texture_space: bpy.props.BoolProperty(default=False)
    show_in_wire: bpy.props.BoolProperty(default=False)
    create_mode: bpy.props.BoolProperty(default=False)
    set_default_location: bpy.props.BoolProperty(default=False)

#here is our operator 
class CreaterOperator(bpy.types.Operator):
     #requiwerd params for bpy Operator Type
    bl_label = "matrix_object_creater"
    bl_idname = "mesh.new_operator"
    
    #required function for bpy Operator Type
    def execute(self, context):
        
        scene = context.scene
        tool = scene.my_tool_creater
        
        if tool.show_in_wire == True:
            context.object.display_type = "WIRE"
        else:
            context.object.display_type = "TEXTURED"
        
        if tool.show_texture_space == True:
            context.object.show_texture_space = True
        else:
            context.object.show_texture_space = False
        
        if tool.show_axis == True:
            context.object.show_axis = True
        else:
            context.object.show_axis = False
        
        # set the location and roration for active object
        context.object.location[0] = tool.location[0]
        context.object.location[1] = tool.location[1]
        context.object.location[2] = tool.location[2]
        context.object.rotation_euler[0] = tool.rotation[0]
        context.object.rotation_euler[1] = tool.rotation[1]
        context.object.rotation_euler[2] = tool.rotation[2]
        
        """if context.object != "Torus" and tool.types_of_objects != "Torus":
            context.object.scale = tool.scale[0]
            context.object.scale = tool.scale[1]
            context.object.scale = tool.scale[2]"""
        
        if tool.create_mode:
            
            for idx in range(tool.count_Z):
                
                for indexes in range(tool.count_X * tool.count_Y * 6):
                    
                    x_core = indexes % tool.count_X
                    y_core = indexes // tool.count_Y
                    
                    if tool.types_of_objects == "ico_Sphere":
                        bpy.ops.mesh.primitive_ico_sphere_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                        
                    elif tool.types_of_objects == "Torus":
                        bpy.ops.mesh.primitive_torus_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                        
                    elif tool.types_of_objects == "Cylinder":
                        bpy.ops.mesh.primitive_cylinder_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                        
                    elif tool.types_of_objects == "Cone":
                        bpy.ops.mesh.primitive_cone_add(roration=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                    
                    elif tool.types_of_objects == "uv_Sphere":
                        bpy.ops.mesh.primitive_uv_sphere_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                    
                    elif tool.types_of_objects == "Grid":
                        bpy.ops.mesh.primitive_grid_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))
                    
                    elif tool.types_of_objects == "Mokey":
                        bpy.ops.mesh.primitive_monkey_add(rotation=tool.rotation, location=(x_core, y_core, idx), scale=(tool.scale[0], tool.scale[1], tool.scale[2]))            
                    
                    if tool.set_default_location == True:
                        context.object.location = (0.0, 0.0, 0.0)        
        return {"FINISHED"}
    
class Panel_For_Operator(bpy.types.Panel):
    bl_label = "Creater Tab"
    bl_idname = "ops.mypanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_categori = "MYTools"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.my_tool_creater
        
        layout.prop(tool, "location")
        layout.prop(tool, "rotation")
        layout.prop(tool, "scale")
        layout.prop(tool, "types_of_objects")
        layout.prop(tool, "show_axis")
        layout.prop(tool, "show_texture_space")
        layout.prop(tool, "count_X")
        layout.prop(tool, "count_Y")
        layout.prop(tool, "count_Z")
        layout.prop(tool, "show_in_wire")
        layout.prop(tool, "create_mode")
        layout.prop(tool, "set_default_location")
        
        row = layout.row()
        row.operator("mesh.new_operator")
        

cls_names = [PropertyGroup, CreaterOperator, Panel_For_Operator]

def register():
    for cls in cls_names:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool_creater = bpy.props.PointerProperty(type=PropertyGroup)

def unregister():
    for cls in cls_names:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool_creater


if __name__ == "__main__":
    register()    
    
    