# A simulation of fluid dynamics with turbulence and vorticity

## To Run the program follow the below steps

Creating the python Environment for program to run

                create conda -n fluid python=3.7 -y
                
Activate the new environment
  
                conda activate fluid
                
install required modules

                pip install -r requirements.txt
                
After installing the requirement.txt file start VS Code 

                code .
                
fairly check all files are there well inplace. then run the command for creating Input files and Getting Output gif file for the visualisation

                python create_input.py
                
This will create around 450 to 500 files in the Input folder, Once all iteration completed, then run ouput file

                python create_output.py
                
It will take around 4 to 5 minutes to create the gif file as an output for visualisation which will be created in the Input folder                


- *SetUBoundary* function sets the boundary condition for a 2D space with five arguments as "space", "left", "right", "top", and "bottom".
  
  - The "space" argument represents the 2D space for which the boundary conditions are being set.
  
  - The "left", "right", "top", and "bottom" arguments represent the boundary conditions on the left, right, top, and bottom sides of the 
    space, respectively. Each boundary condition is represented as an object with two attributes: "type" and "value".
  
  - The "type" attribute can be either "D" or "N", representing Dirichlet or Neumann boundary conditions, respectively.

- A class called *Space* that is used to create a computational grid for simulating fluid flow. The CreateMesh method creates the grid by taking in 
  the number of row points and column points as input and initializes arrays to store the velocity components (u and v) and pressure (p) at every 
  point on the grid.
  
  - The SetTimeStep function computes the time step dt based on the Courant-Friedrichs-Lewy (CFL) criterion. The CFL criterion is a stability 
    condition for numerical methods that solves partial differential equations and ensures that the time step is small enough to prevent numerical 
    errors from dominating the solution.

- The *SetDeltas* method calculates and sets the grid spacing dx and dy based on the size of the grid and the number of points.

- The *SetInitialU, SetInitialV, and SetInitialP* methods are used to set the initial values of u, v, and p, respectively, based on user input.

- The *SetSourceTerm* method sets the source term variables S_x and S_y that can be used to add a source term to the fluid flow simulation.

- The *SetTimeStep* function computes the time step dt based on the Courant-Friedrichs-Lewy (CFL) criterion. The CFL criterion is a stability 
  ondition for numerical methods that solves partial differential equations and ensures that the time step is small enough to prevent numerical 
  errors from dominating the solution. 

- *GetStarredVelocities* function calculates the intermediate velocity field in a 2D space. It takes two arguments: "space" and "fluid".
  
  - The "space" argument represents the 2D space in which the fluid is flowing. It is an object with attributes like "u" and "v", which represent 
    the x- and y-velocities of the fluid at each point in the space.
  
  - The "fluid" argument represents the properties of the fluid, such as its density ("rho") and viscosity ("mu").
  
  - The function first saves some object attributes of the space object, then it calculate the intermediate velocities "u_star" and "v_star" from the 
    "space" object as well as the time step "dt" and fluid properties density "rho" and viscosity "mu".
  
  - To calculate the intermediate x-velocity ("u_star"), the function first calculates the first and second derivatives of the x-velocity with respect 
    to x and y, respectively. It then calculates the average value of the y-velocity at the four neighboring points around each x-velocity point 
    ("v_face") and vice-versa for intermediate y-velocity ("v_star") around ("u_face").
  
  - Using these values, the function updates the "u_star" values for each point in the space using a combination of the previous velocity values, 
    the advection terms (which represent the transport of fluid with the velocity field), the diffusion terms (which represent the spreading of 
    fluid due to viscosity), and any external forces acting on the fluid in the x-direction ("S_x") and vice-versa for intermediate y-velocity ("v_star") 
    and any external forces acting on the fluid in the y-direction ("S_y").

- *SolvePressurePoisson* function solves the Pressure Poisson equation in the Navier-Stokes equation for incompressible fluids using the finite 
  difference method. the function calculates the pressure gradient terms (ustar1_x and vstar1_y) using central differences for velocity components. 
  It then updates the pressure values using the finite difference method with a second-order central difference scheme.

- *SolveMomentumEquation* function solves the momentum equation for a fluid using the finite difference method. The function first extracts the necessary 
  variables from the space and fluid objects, and calculates the pressure gradient in the x and y directions. Then it updates the velocity arrays u and v.

- *MakeInputDirectory* function that creates an input directory in the current working directory if it does not already exist. 
  
  - If the wipe argument is set to True, the function clears any files in the directory by removing all files one by one. 
  
  - If wipe is set to False, then nothing happens to the existing files in the directory.
  
  - The function first saves the current working directory to cwdir. It then joins cwdir with "Input" to get the path to the new directory 
    it wants to create. If the directory does not already exist, *os.makedirs()* creates the new directory. If the directory already exists, 
    then the if wipe statement checks if wipe is true, and if it is, the function changes the current working directory to dir_path and uses 
    *os.listdir()* to get a list of all the files in the directory. It then loops through the files and removes them one by one using *os.remove(file)*.
    
- The  function *WriteToFile* is used to write the current values of pressure, velocity (u and v components) at each iteration into a text file.
  - If the current iteration number is divisible by the interval value, it creates a text file in a subdirectory named "Input" within the current 
    working directory. 
    
  - The filename is set as "PUV" followed by the iteration number and ".txt". It then writes the values of space.p_c[i,j], space.u_c[i,j], and 
    space.v_c[i,j] for each grid point (i,j) into the file using the write() method of the file object.
  
- The function *read_datafile* reads data from a text file in a specific format. 
  - It takes an iteration argument and constructs a filename by formatting it into a string. It then loads the data from the file located at 
    the ecified path and reshapes the data into separate 2D arrays for pressure, horizontal velocity, and vertical velocity. Finally, it returns 
    these arrays.
    
- The function *animate* generates an animation of a fluid simulation using the data files generated from the simulation using matplotlib library and specialy 
  its animation class to crate the gif file as per requirement.


