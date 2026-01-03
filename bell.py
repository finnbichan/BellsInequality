from helpers import measure, choose
from statistics import mean

#the classical Bell inequality

def alice():
    measurables = ('Q', 'R')
    #In the textbook, it is specified that the measurables are chosen randomly.
    measured = choose(measurables)
    result = measure()
    return(measured, result)

def bob():
    measurables = ('S', 'T')
    measured = choose(measurables)
    result = measure()
    return(measured, result)

def experiment():
    for _ in range(100):
        a_measurable, a_result = alice()
        b_measurable, b_result = bob()
        yield (a_measurable, a_result, b_measurable, b_result)

def aggregate_results():
    counts = {
        'QS': [],
        'RS': [],
        'RT': [],
        'QT': []
    }
    results_gen = experiment()
    for a_measurable, a_result, b_measurable, b_result in results_gen:
        key = a_measurable + b_measurable
        counts[key].append(a_result * b_result)
    expectations = {
        'QS': mean(counts['QS']),
        'RS': mean(counts['RS']),
        'RT': mean(counts['RT']),
        'QT': mean(counts['QT'])
    }
    bell_value = expectations['QS'] + expectations['RS'] + expectations['RT'] - expectations['QT']
    return bell_value

def repeat_experiments():
    bell_values = []
    print("Repeating experiment 5000 times...")
    for _ in range(5000):
        bell_value = aggregate_results()
        bell_values.append(bell_value)
    print("Selecting maximum Bell value from experiments...")
    return max(bell_values)
