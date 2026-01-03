## Bell's Inequality

A simple proof that quantum physics violates Bell's inequality. Based off Mike & Ike p115-116.

I use uv on Ubuntu:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python main.py
```

This will simulate the circuit by default. Add False as an argument to main in main.py to run on IBM's hardware.

If you have not used IBMQ services on your machine before, add your API key from the IBMQ dashboard in a .env file like the example included.

Then, in the virtual environment, run:

```bash
python init_creds.py
```