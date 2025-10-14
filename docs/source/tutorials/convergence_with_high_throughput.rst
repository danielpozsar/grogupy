.. _convergence_with_high_throughput:

Convergence with high throughput
================================

If we want to run different simulations with different convergence parameters 
in a sequential way, then we have to guess the total runtime of the job.
Because the runtime of simulations with different convergence parameters are 
hard to predic, assuming we allocate the same resources, the total runtime of a 
job like this is also very hard to predict. If we want to create array 
jobs to run them in a parallel manner we face the same issue, where we 
either waste a lot of resources or run out of time and terminate with an error. 
For this reason, grogupy only supports the creation of input files for convergence 
tests, but they have to be run manually. Furthermore there is a visualization tool 
that can help to determine the convergence of a system with respect to some 
parameter. For more information see the :ref:`API reference <api_reference>`.