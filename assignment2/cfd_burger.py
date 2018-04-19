import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot, cm
from matplotlib.colors import Normalize
import numpy 

def equation_of_motion(u, v, nu, dy, dx, dt): 
    # generate the next state as a function of the old state 
    un = u.copy() 
    vn = v.copy() 
    u[1:-1, 1:-1] = (un[1:-1, 1:-1] - dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) - dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) + nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1
, 1:-1] + un[1:-1, 0:-2]) + nu * dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] - dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) - dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) + nu * dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1
, 1:-1] + vn[1:-1, 0:-2]) + nu * dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1]))
    
    return (u,v) 
    
def boundary(u, v, nozzle_u, nozzle_v, nx, ny, t_step): 
    u[0, :] = 0 
    u[-1, :] = 0 
    u[:, 0] = 0 
    u[:, -1] = 0 
    v[0, :] = 0 
    v[-1, :] = 0 
    v[:, 0] = 0 
    v[:, -1] = 0 
    # special nozzle BC 
    u[ny//2-2:ny//2+2, 0] = nozzle_u[t_step] 
    v[ny//2-2:ny//2+2, 0] = nozzle_v[t_step] 
    print ny//2-2
    print ny//2+2
    return (u, v) 
    
def evolve(u, v, nozzle_u, nozzle_v, nx, ny, nu, dx, dy, dt, steps): 
  
    for i in range(steps): 

        (u, v) = equation_of_motion(u, v, nu, dy, dx, dt) 
        (u, v) = boundary(u, v, nozzle_u, nozzle_v, nx, ny, i) 
        
        if i%50 == 0:
          ax = pyplot.figure() 
          norm = Normalize() 
          magnitude = numpy.sqrt(u[::2]**2 +  v[::2]**2) 
          pyplot.quiver(u[::2], v[::2], norm(magnitude), scale=60, cmap=pyplot.cm.jet) 
          ax.savefig('frame'+str(i).zfill(5)+'.png',dpi=300) 
          ax.clear()
        
    return (u, v) 
    
    

