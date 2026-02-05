# Grover’s Algorithm (Qiskit)

Still in progress...

This project implements **Grover’s quantum search algorithm** using **Qiskit**, focusing on a clear and structured implementation of the algorithm and its application to unstructured search problems. The project includes both simulation and execution on real quantum hardware, allowing for a direct comparison between ideal and noisy quantum results.

---

## Project structure

- `src/`  
  Contains the main Jupyter notebook with the full implementation, explanations, and simulations of Grover’s algorithm and utils used in the notebook.

- `figures/`  
  Contains the figures generated in the notebook (quantum circuits and visualizations), saved for inspection without re-running the code.

---

## Project goals

- Introduce and explain **Grover’s algorithm** at a conceptual and mathematical level
- Implement **Grover’s algorithm** for unstructured search
- Construct valid **oracle circuits** for different marked states
- Implement the **diffusion operator** explicitly
- Illustrate the algorithm with a simple example ($n=2$ qubits)
- Simulate the algorithm using **Qiskit Aer**
- Execute the algorithm on **real quantum hardware**
- Analyze and compare the results obtained from simulation and hardware execution

---

## Requirements

Install the required Python packages with:

```bash
pip install -r requirements.txt
