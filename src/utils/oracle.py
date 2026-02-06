from qiskit import QuantumCircuit
from qiskit.circuit.library import MCMTGate, ZGate

def grover_oracle(target_states: list[str]):
    """
    Build a Grover oracle that flips the phase of one or more marked basis states.

    The oracle implements the unitary:
        U_f |x> = (-1)^{f(x)} |x>,
    where f(x) = 1 if x is a marked state and f(x) = 0 otherwise.

    This implementation marks arbitrary bitstrings by:
      1) Applying X gates on qubits where the target bitstring has a '0',
         so that the target pattern is mapped to |11...1>.
      2) Applying a MCZ gate, which adds a phase of -1 to |11...1>.
      3) Undoing the initial X gates to restore the original computational basis.
    """
    # Ensure the input is a list
    if isinstance(target_states, str):
        target_states = [target_states]

    n = len(target_states[0])
    qc = QuantumCircuit(n)

    # Multi-controlled Z gate acting on |11...1>
    phase_flip = MCMTGate(ZGate(), n - 1, 1)

    for state in target_states:
        # Reverse string to match Qiskit's qubit ordering
        state_reversed = state[::-1]

        # Identify qubits that should be |0> in the target state
        zero_positions = [i for i, bit in enumerate(state_reversed) if bit == "0"]

        # Map the target state to |11...1>
        if zero_positions:
            qc.x(zero_positions)

        # Apply the phase flip
        qc.compose(phase_flip, inplace=True)

        # Restore the original basis
        if zero_positions:
            qc.x(zero_positions)

    return qc
