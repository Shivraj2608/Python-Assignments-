#D Imaan song composition using prime numbers


def find_prime(start, end):
  """
  Finds prime numbers within a given range.

  Args:
    start: The starting number of the range (inclusive).3
    end: The ending number of the range (inclusive).

  Returns:
    A list of prime numbers within the given range.
    "Invalid range" if start or end is negative or start > end.
    "There is no prime numbers in this range" if no primes are found.
  """

  if start < 0 or end < 0:
    return "Invalid range"
  if start > end:
    return "Invalid range"
  if start == end:
    return "There is no prime numbers in this range"

  prime_numbers = []
  for num in range(start, end + 1):
    if num > 1:
      for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
          break
      else:
        prime_numbers.append(num)

  if not prime_numbers:
    return "There is no prime numbers in this range"

  return prime_numbers

# Get input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Find prime numbers and display the result
result = find_prime(start, end)
print(result)