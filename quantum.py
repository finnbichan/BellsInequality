import math
import qiskit
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.transpiler import generate_preset_pass_manager
from dotenv import load_dotenv
import os

def create_and_run_circuit(alice, bob, simulate):
    print("Creating Bell state |ψ->")
    qc = qiskit.QuantumCircuit(2, 2)
    #create Bell state 1/sqrt(2) (|01> - |10>)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(0)

    #Q = Z basis, R = X basis
    if alice == 'R':
        qc.h(0)

    #S = (-Z - X)/sqrt(2) basis, T = (Z - X)/sqrt(2) basis
    if bob == 'S':
        qc.ry(3*math.pi/4, 1)
    elif bob == 'T':
        qc.ry(math.pi/4, 1)
    
    qc.measure(0, 0)
    qc.measure(1, 1)

    print(f"Created circuit for {alice}{bob}:")
    print(qc)
    return run_circuit(qc, simulate)

def run_circuit(qc, simulate):
    if simulate:
        return simulate_circuit(qc)
    else:
        return run_on_ibm_quantum(qc)

def simulate_circuit(qc):
    print("Running circuit...")
    backend = Aer.get_backend('aer_simulator')
    compiled = qiskit.transpile(qc, backend)
    job = backend.run(compiled, shots=1024)
    return job.result().get_counts(qc)

def run_on_ibm_quantum(qc):
    service = QiskitRuntimeService()
    backend = service.least_busy(
    operational=True, simulator=False
    )
    print(f"Running on backend: {backend.name}")
    pm = generate_preset_pass_manager(backend=backend)
    isa_circuit = pm.run(qc)
    sampler = Sampler(backend)
    sampler.options.default_shots = 1024
    job = sampler.run([isa_circuit])
    result = job.result()[0].data.c.get_counts()
    print(result)
    return result

def quantum(simulate):
    pairs = [('Q', 'S'), ('Q', 'T'), ('R', 'S'), ('R', 'T')]
    averages = {}
    for pair in pairs:
        counts = create_and_run_circuit(pair[0], pair[1], simulate)
        mapped_counts = {1: counts['11'] + counts['00'], -1: counts['10'] + counts['01']}
        avg = (mapped_counts[1] + mapped_counts[-1]*-1) / 1024
        print(f"Counts for {pair[0]}{pair[1]}: {counts}, Average: {avg}")
        averages[f"{pair[0]}{pair[1]}"] = avg
    sum = averages['QS'] + averages['RT'] + averages['RS'] - averages['QT']
    print("<QS> + <RT> + <RS> - <QT>:", sum)
    return sum



