#Password Protection

def get_password():
  """Calculates the password for the file based on the plot numbers.5




  The password is calculated as the average of the sum of even plot numbers 
  and the sum of odd plot numbers.

  Returns:5
      float: The calculated password with 2 decimal places.
      str: "Invalid Input" if the input is invalid.
  """

  try:
    n = int(input("Enter the total no of plots: "))

    if n <= 0 or n > 20:
      return "Invalid Input"

    plot_numbers = []
    for _ in range(n):
      num = int(input())
      if num <= 0:
        return "Invalid Input"
      plot_numbers.append(num)

    even_plots = [num for num in plot_numbers if num % 2 == 0]
    odd_plots = [num for num in plot_numbers if num % 2 != 0]

    sum_even = sum(even_plots)
    sum_odd = sum(odd_plots)

    if sum_even == 0 or sum_odd == 0:
      return "Invalid Input"

    password = (sum_even + sum_odd) / 2
    return f"The password for the file is: {password:.2f}"

  except ValueError:
    return "Invalid Input"

if __name__ == "__main__":
  password = get_password()
  print(password)