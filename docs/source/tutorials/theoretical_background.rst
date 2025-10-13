.. _theoretical_background:

Theoretical background
======================


.. math::

    \mathcal{H}=\frac{1}{2}\sum_{i\neq j}J_{ij}^{H}\boldsymbol{e}_{i}\cdot\boldsymbol{e}_{j}+\frac{1}{2}\sum_{i\neq j}\boldsymbol{e}_{i}\hat{J}_{ij}^{S}\boldsymbol{e}_{j}+\frac{1}{2}\sum_{i\neq j}\boldsymbol{D}_{ij}\cdot\left(\boldsymbol{e}_{i}\times\boldsymbol{e}_{j}\right)+\sum_{i}\boldsymbol{e}_{i}\hat{K}_{i}\boldsymbol{e}_{i}

.. math::

    \boldsymbol{A}_i
    =
    \begin{pmatrix}
        A_i^{xx} & A_i^{xy} & A_i^{xz} \\
        A_i^{xy} & A_i^{yy} & A_i^{yz} \\
        A_i^{xz} & A_i^{yz} & A_i^{zz} \\
    \end{pmatrix}

Full matrix can be decomposed into three primary parts

*   Isotropic exchange

    .. math::
        J_{ij}^{isotropic}
        =
        \text{Tr}(\boldsymbol{J}_{ij})
* Symmetric traceless anisotropy

    .. math::
        \boldsymbol{J}_{ij}^{aniso, symm}
        =
        \dfrac{\boldsymbol{J}_{ij} + \boldsymbol{J}_{ij}^T}{2}
        -
        \dfrac{\text{Tr}(\boldsymbol{J}_{ij})}{3}
        \begin{pmatrix}
            S_i^{xx} & S_i^{xy} & S_i^{xz} \\
            S_i^{xy} & S_i^{yy} & S_i^{yz} \\
            S_i^{xz} & S_i^{yz} & S_i^{zz} \\
        \end{pmatrix}
* Antisymmetric part

    .. math::
        \boldsymbol{J}_{ij}^{dmi}
        =
        \dfrac{\boldsymbol{J}_{ij} - \boldsymbol{J}_{ij}^T}{2}
        =
        \begin{pmatrix}
            0         & D^z_{ij}  & -D^y_{ij} \\
            -D^z_{ij} & 0         & D^x_{ij} \\
            D^y_{ij}  & -D^x_{ij} & 0 
        \end{pmatrix}

Antysymmetric part can be written in a form of the Dzyaloshinskii-Moriya interaction (DMI) as

.. math::

    \mathcal{H}^{dmi}
    =
    \dfrac{1}{2}
    \sum_{i\ne j}
    \boldsymbol{e}_{i}
    \cdot
    \boldsymbol{J}^{dmi}_{ij}
    \cdot
    \boldsymbol{e}_{j}
    =
    \dfrac{1}{2}
    \sum_{i\ne j}
    \boldsymbol{D}_{ij}
    \cdot
    (
    \boldsymbol{e}_{i}
    \times
    \boldsymbol{e}_{j})

where :math:`\boldsymbol{D}_{ij} = (D^x_{ij}, D^y_{ij}, D^z_{ij})`.
