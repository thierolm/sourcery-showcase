def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def calculate_total(prices):
    return sum(prices)

def greet(name):
    return f"Hello, {name}" if name else "Hello, stranger"
