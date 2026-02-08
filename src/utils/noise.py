from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError

def create_noise_model(
    error_1q_rate: float = 0,
    error_2q_rate: float = 0,
    readout_error_rate: float = 0,
    one_qubit_gates: list = ("h", "x"),
    two_qubit_gates: list = ("cx", "mcx")
    ):
    """AerSimulator noise model with depolarizing errors and readout errors."""
    # Create a noise model
    noise_model = NoiseModel()

    # Depolarizing errors
    error_1q = depolarizing_error(error_1q_rate, 1)  # 0.1% error for 1-qubit gates
    error_2q = depolarizing_error(error_2q_rate, 2)   # 1% error for 2-qubit gates

    noise_model.add_all_qubit_quantum_error(error_1q, one_qubit_gates)
    noise_model.add_all_qubit_quantum_error(error_2q, two_qubit_gates)

    # Readout error
    readout_error = ReadoutError([[1-readout_error_rate, readout_error_rate],  # |0> is measured incorrectly as |1> with probability 0.03
                                [readout_error_rate, 1-readout_error_rate]]) # |1> is measured incorrectly as |0> with probability 0.03
    noise_model.add_all_qubit_readout_error(readout_error)

    return noise_model