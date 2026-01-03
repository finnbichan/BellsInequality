
from bell import repeat_experiments
from quantum import quantum

simulate = False #TBC

def main(simulate=True):
    print("Let's start with the classical Bell inequality. We are expecting a result less than or equal to 2.")
    classical_result = repeat_experiments()
    print("Classical Bell inequality result (maximum of 5000):", classical_result)
    if classical_result <= 2:
        print("This is as expected.")
    else:
        print("New physics discovered!")
        return 1
    print("\nNow, let's move on to the quantum Bell inequality. We are expecting a result greater than 2.")
    quantum_result = quantum(simulate)
    print("Quantum Bell inequality result:", quantum_result)
    if quantum_result > 2:
        print("This is as expected.")
    else:
        print("It's possible we got very unlucky. But more likely, there's an error in the code.")
        return 1
    print("We have successfully shown that nature is either non-local or non-realistic!") 

if __name__ == "__main__":
    main(simulate)