def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2
    
def calculate_mode(numbers):
    if len(numbers) == 0:
        return None
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    if len(mode) == len(numbers):
        return None  # No unique mode
    return mode[0] if mode else None

def calculate_range(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers) - min(numbers)

def sort_numbers(numbers):
    return sorted(numbers)

def filter_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

def filter_odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]

def find_max(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)

def find_min(numbers):
    if len(numbers) == 0:
        return None
    return min(numbers)

def calculate_sum(numbers):
    return sum(numbers)

def count_occurrences(numbers, target):
    return numbers.count(target)

def reverse_list(numbers):
    return numbers[::-1]

def is_palindrome(numbers):
    return numbers == numbers[::-1]

def square_numbers(numbers):
    return [x ** 2 for x in numbers]

def cube_numbers(numbers):
    return [x ** 3 for x in numbers]

def find_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return [x for x in numbers if is_prime(x)]

def main():
    numbers = [12, 34, 56, 23, 45, 67, 89, 10, 5, 43]

    print("Original Numbers:", numbers)
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Mode:", calculate_mode(numbers))
    print("Range:", calculate_range(numbers))
    print("Sorted Numbers:", sort_numbers(numbers))
    print("Even Numbers:", filter_even_numbers(numbers))
    print("Odd Numbers:", filter_odd_numbers(numbers))
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))
    print("Sum:", calculate_sum(numbers))
    print("Occurrences of 10:", count_occurrences(numbers, 10))
    print("Reversed List:", reverse_list(numbers))
    print("Is Palindrome:", is_palindrome(numbers))
    print("Squared Numbers:", square_numbers(numbers))
    print("Cubed Numbers:", cube_numbers(numbers))
    print("Prime Numbers:", find_primes(numbers))

if __name__ == "__main__":
    main()
