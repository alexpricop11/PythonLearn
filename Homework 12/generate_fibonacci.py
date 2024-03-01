def generate_fibonacci(terms):
    if terms == 0:
        return []
    elif terms == 1:
        return [0]

    fibonacci_sequence = [0, 1]

    for i in range(2, terms):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


while True:
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        fibonacci_result = generate_fibonacci(num_terms)
        print(f"Generated Fibonacci sequence: {fibonacci_result}")
        break
    except ValueError:
        print("Enter a number")
