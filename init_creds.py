from qiskit_ibm_runtime import QiskitRuntimeService
import dotenv
import os
 
dotenv.load_dotenv()
api_key = os.getenv("API_KEY")

QiskitRuntimeService.save_account(
token=api_key, # In a .env file, add your IBMQ API_KEY
)