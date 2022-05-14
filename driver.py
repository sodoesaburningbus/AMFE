### This is the driver for the Boundary Layer Atmospheric Model (BLAM)
### Here is where the namelist is read, parameterizatins set,
### and the model integrated.
### Integration is accomplished by the 4th order Runge-Kutta method.
### Christopher E. Phillips

### Import required supporting modules
import f90nml
import netCDF4
import numpy

### Read in the namelist

### Set parameterizations
#if ms_option == 1:
#    ms_scheme = microphysics.scheme1
#elif ms_option == 2:
#    ms_scheme = microphysics.scheme2


### Call grid initialization

### Write out initial conditions

### Perform first integration step

### Perform second step

### Enter main integration loop

    # Update variables

    # Check for write out time
    # Include stability parameter (base on maximum 3D wind)
