import qutip as qt
import numpy as np

phase = 1.21701
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 043 Entangled Density Matrix (core: 'fights meth you really gotta do that now you have to use star bucks you don't have a choice'):")
print(rho)
