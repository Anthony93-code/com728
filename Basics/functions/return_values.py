def sum_weights(beep_weight, bop_weight):
    sum = beep_weight + bop_weight
    return sum

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = sum_weights(beep_weight, bop_weight) / 2
    return avg_weight

def run():
    print("What is the weight of Beep?")
    beep_weight = float(input())
    print("What is the weight of Bop?")
    bop_weight = float(input())
    print("What would you like to calculate (sum or average)?")
    operation = input()
    if operation == "sum".lower().strip():
        answer = sum_weights(beep_weight, bop_weight)
        print(f"The sum of Beep's and Bop's weight is {answer: .2f}")
    elif operation == "average".lower().strip():
        answer = calc_avg_weight(beep_weight, bop_weight)
        print(f"The average of Beep's and Bop's weight is {answer: .2f}")
    else:
        print("Error")

run()