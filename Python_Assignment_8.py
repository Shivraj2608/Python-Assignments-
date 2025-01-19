#News Report Generation for Japan Tsunami

def generate_tsunami_report():
  """Generates a Tsunami report based on user input.

  Args:
    None

  Returns:
    str: The generated Tsunami report or "Invalid input" if any count is negative.
  """

  try:
    dead_count = int(input("Dead Count: "))
    injured_count = int(input("Injured Count: "))
    safe_count = int(input("Safe Count: "))
2000
    if dead_count < 0 or injured_count < 0 or safe_count < 0:
      return "Invalid input"

    report = """
TSUNAMI REPORT OF JAPAN

The number of people
Dead:{}
Injured:{}
Safe:{}

Please help the people who are suffering!!!
""".format(dead_count, injured_count, safe_count)

    return report

  except ValueError:
    return "Invalid input"

if __name__ == "__main__":
  report = generate_tsunami_report()
  print(report)