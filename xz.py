
import numpy as np

# 1. Base states and Error Setup
logical_0 = np.array([1, 0])
gauge_plus = np.array([1, 1]) / np.sqrt(2)
I = np.array([[1, 0], [0, 1]])
Z = np.array([[1, 0], [0, -1]])

# 2. Encoded state & Z Error Strike
encoded_state = np.kron(logical_0, gauge_plus)
damaged_state = np.dot(np.kron(I, Z), encoded_state)

# 3. Partial Trace (Extracting the Logical Qubit)
# Convert state vector to density matrix: rho = |psi><psi|
rho = np.outer(damaged_state, damaged_state.conj())

# Trace out the gauge qubit (folding the 4x4 into a 2x2 logical matrix)
logical_rho = np.trace(rho.reshape([2, 2, 2, 2]), axis1=1, axis2=3)

print("XZ Labs Final Logical Density Matrix:")
print(np.round(logical_rho, 3))
