def divide_numbers(a, b):
    result = a / b
    return result

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

def process_scores(score_list):
    average = calculate_average(score_list)
    print(f"Average score: {average}")
    return average

# This will cause an error
scores = []
process_scores(scores)