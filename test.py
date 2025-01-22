from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create a simple quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Get the simulator backend
simulator = Aer.get_backend('qasm_simulator')

# Transpile the circuit for the simulator
transpiled_qc = transpile(qc, simulator)

# Execute the job directly on the simulator
job = simulator.run(transpiled_qc, shots=1024)

# Get the result
result = job.result()

# Output the results
print(result.get_counts())
