from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

def generate_quantum_key():
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)

    # Apply Hadamard gate to create a superposition state
    qc.h(0)

    # Measure the qubit and store the result in the classical bit
    qc.measure(0, 0)

    # Get the simulator backend
    simulator = Aer.get_backend('qasm_simulator')

    # Transpile the circuit for the simulator
    transpiled_qc = transpile(qc, simulator)

    # Execute the quantum circuit directly on the simulator
    job = simulator.run(transpiled_qc, shots=1024)

    # Get the results from the simulation
    result = job.result()

    # Get the counts of the results (how many times each outcome was measured)
    counts = result.get_counts()

    # Return the generated key (this will be a bit string based on the measurement outcomes)
    return counts

# Example usage
if __name__ == "__main__":
    key = generate_quantum_key()
    print(f"Generated quantum key: {key}")
