"""Physical constants
"""

from math import sqrt as _sqrt, pi
# noinspection PyUnresolvedReferences
from scipy.constants import c as clight
from scipy.constants import physical_constants as _cst
from scipy.constants import e as qe

#: Electron mass [eV]
e_mass = 1.0e+06 * _cst['electron mass energy equivalent in MeV'][0]  # eV
#: Proton mass [eV]
p_mass = 1.0e+06 * _cst['proton mass energy equivalent in MeV'][0]    # eV
#: Electron radius [m]
e_radius = _cst['classical electron radius'][0]    # m

_hbar_c = _cst['reduced Planck constant times c in MeV fm'][0]

#: :math:`C_\gamma` [m/eV^3]
Cgamma = 4.0 * pi * e_radius / 3.0 / pow(e_mass, 3)                 # m/eV^3
#: :math:`C_q` [m]
Cq = 55 / 32 / _sqrt(3) * _hbar_c / e_mass * 1.0e-9                  # m


__all__ = ["clight", "qe", "e_mass", "p_mass", "e_radius", "Cgamma", "Cq"]
