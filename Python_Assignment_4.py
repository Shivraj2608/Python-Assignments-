#Tax Calculation based on income and age of individual

age = int(input("Enter your age: "))

# Age validation
if age < 18 or age > 100:
    print("Invalid age")

else:
    income = float(input("Enter your income: "))

    # Income validation
    if income < 0:
        print("Invalid income")

    else:
        # Tax calculation
        if age <= 60:
            if income <= 250000:
                tax = 0

            elif income > 250000 and income <= 500000:
                tax = income * 0.10

            elif income > 500000 and income <= 1000000:
                tax = income * 0.20

            else:
                tax = income * 0.30

        elif age <= 80:
            if income <= 300000:
                tax = 0

            elif income > 300000 and income <= 500000:
                tax = income * 0.10

            elif income > 500000 and income <= 1000000:
                tax = income * 0.20

            else:
                tax = income * 0.30

        else:
            if income <= 500000:
                tax = 0

            elif income > 500000 and income <= 1000000:
                tax = income * 0.20

            else:
                tax = income * 0.30

        print(f"The Tax amount is: {tax:.2f}")
