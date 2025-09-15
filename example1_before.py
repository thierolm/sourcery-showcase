def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def greet(name):
    if name:
        return "Hello, " + name
    else:
        return "Hello, stranger"