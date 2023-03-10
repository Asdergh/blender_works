import bpy
import site
site.addsitedir(r"C:\\Users\\эльдо\\OneDrive\\Рабочий стол\\new_venv\\venv\\Lib\\site-packages")
import numpy as np

def create_some_plane(rot_angle=None, phi=None, theta=None) -> None:
    
    x_core = np.cos(phi) 
    y_core = np.sin(theta) 
    z_core = np.zeros(100)
    
    for (X, Y, Z) in zip(x_core, y_core, z_core):
        z_core += 0.1
        bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(X, Y, Z))

phi = np.linspace(np.pi, -np.pi, 100)
theta = np.linspace(np.pi, -np.pi, 100)
create_some_plane(phi=phi, theta=theta)

