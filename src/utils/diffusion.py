from qiskit import QuantumCircuit
from sympy import re

def diffusion_nq(n_qubits: int):
    """
    Grover diffusion operator for an arbitrary number of qubits.
    Implements: H^n X^n (multi-controlled Z) X^n H^n
    """
    qc = QuantumCircuit(n_qubits)
    qubits  =list(range(n_qubits))

    # H^n
    qc.h(qubits)
    # X^n
    qc.x(qubits)

    # Multi-controlled Z on |11...1|
    # Convert MCX to MCZ via H on target
    target = qubits[-1]
    controls = qubits[:-1]
    qc.h(target)
    qc.mcx(controls, target)   # multi-controlled X
    qc.h(target)

    # X^n
    qc.x(qubits)
    # H^n
    qc.h(qubits)

    return qc
