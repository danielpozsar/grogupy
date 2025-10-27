.. _theoretical_background:

Theoretical background
======================

grogupy is based on the *Relativistic magnetic 
interactions from non-orthogonal basis sets* 
paper (see the bibliography) and uses the same 
convention for the generalized classical 
Heisenberg model

.. math::

    H({\boldsymbol{e}_{i}})=
    \frac{1}{2}
    \sum_{i\neq j} \boldsymbol{e}_{i} J_{ij} \boldsymbol{e}_{j} + 
    \sum_{i} \boldsymbol{e}_{i} K_{i} \boldsymbol{e}_{i}, 

where :math:`\boldsymbol{e}_{i} = 1 / (\hbar S_i) \boldsymbol{S}_{i}` 
is a unit vector from the angular momentum vector and :math:`J_{ij}`, 
and :math:`K_{i}` are the exchange and on-site anisotropy tensor 
respectively. Importantly they are renormalized to the unit vector 
:math:`\boldsymbol{e}_{i}`. Internally they are stored as a 
``np.array``, even if it is an 'isotropic-only' calculation, but
then the expected matrix elements are zero.

grogupy uses the following defnition for the on-site anisotropy 
tensor

.. math::

    K_i
    =
    \begin{pmatrix}
        K_i^{xx} - K_i^{zz} & K_i^{xy} & K_i^{xz} \\
        K_i^{yx} & K_i^{yy} - K_i^{zz} & K_i^{yz} \\
        K_i^{zx} & K_i^{zy} & 0 \\
    \end{pmatrix}, 

which have five independent elements. The isotropic exchange tensor can be split into a 
symmetric and antisymmetric part

.. math::
    J = J^s + J^a
    =
    \begin{pmatrix}
    J^{xx} & J^{xy} & J^{xz} \\
    J^{yx} & J^{yy} & J^{yz} \\
    J^{zx} & J^{zy} & J^{zz} \\
    \end{pmatrix}
    +
    \begin{pmatrix}
    0 & D^{z} & -D^{y} \\
    -D^{z} & 0 & D^{x} \\
    D^{y} & -D^{x} & 0 \\
    \end{pmatrix},
    
where the site inidices have been omitted for clarity. It 
is also possible to define the isotropic exchange 
:math:`J^{iso} = \text{Tr} J^s/3` and the symmetric 
exchange :math:`J^S = J^s - J^{iso} I_3`, where :math:`I_3` 
is the identity matrix. With these new defnitions we can 
expand the above classical Hamiltonian to the following 
form

.. math::

    H({\boldsymbol{e}_{i}})
    =
    \frac{1}{2}
    \sum_{i\ne j}
    J^{iso}
    \boldsymbol{e}_{i}
    \cdot
    \boldsymbol{e}_{j}
    +
    \frac{1}{2}
    \sum_{i\ne j}
    \boldsymbol{e}_{i}
    J_{ij}^{S}
    \boldsymbol{e}_{j}
    

    +
    \frac{1}{2}
    \sum_{i\ne j}
    \boldsymbol{D}_{ij}
    \cdot
    (\boldsymbol{e}_{i} \times \boldsymbol{e}_{j})
    +
    \frac{1}{2}
    \sum_{i}
    \boldsymbol{e}_{i}
    K_i
    \boldsymbol{e}_{i}.


Furthermore grogupy returns the energy variations upon 
infinitesimal rotations based on the 
Liechtenstein-Katsnelson-Antropov-Gubanov torque formalism. 
The most general Hamiltonian implemented in grogupy is the 
above example, but in principle any classical Hamiltonian 
can be fitted based on these energies. For examples see 
the bibliography.