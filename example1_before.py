def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

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