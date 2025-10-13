Introduction
============
grogupy is a package that contains a variety of modules to calculate and 
visualize magnetic interaction parameters. It supports multiple 
spin-models, both isotropic and ones with spin-orbit coupling. It can also 
be used to set up more complex convergence and high throughput calculations.

1. grogupy can efficiently calculate the magnetic interaction parameters of a 
large number of atoms or magnetic entities. The most resource consuming part of 
the simulation is the Green's function calculation, but the number of matrix 
inversions does not depend on the number of pairs in the system, so the increase 
in the number of pairs is very cheap computationally.

2. It is capable to visualize the examined system including the calculated 
magnetic parameters, like the isotropic, symmetric and antisymmetric exchange 
or the Dzyaloshinskii-Moriya vectors.

3. You can create automatic convergence test for high throughput calculations.

Package
-------

You can run grogupy in a jupyter notebook, where it is easier to set up complex 
systems, with non-trivial magnetic entities or visualize the pairs that you created.
You can also use the command line scripts, which are more suitable for HPC 
environments, where you can use GPU or MPI acceleration.

Go to the :ref:`installation <quickstart-guide>` page to install grogupy.

Command line usage
------------------

grogupy contains  :ref:`command line scripts <command_line_usage>` to run 
simulations and to create automatic summaries of the output files. Currently 
there is no way to run automatic convergence tests, because the total runtime 
and required resources are hardware dependent and hard to estimate. Instead 
there are functions to generate batches of input files and functions in the 
``viz`` module that helps the user determine the convergence from multiple runs.
