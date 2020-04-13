"""
Read the problem statement carefully.

* Hint no.1 advises on how to get user input, get_inputs() implements this

    Observe the float() conversions.

* Hint no.2 advises on how to initialize variables
    
    Observe the careful names chosen for initialization of the variables.
    Also observe, that not all initialization is to the input values.

    current_savings and months are 0, as they should be.
    r is 0.04 or 4% as defined in the problem.

    monthly_portion_saved and portion_down_payment are derived values.
    These are the values that go into the core calculation area.

* Core calculation area

    The condition is satisfied when our MIT graduate has enough saved for a down payment.

    So, we have:
    while current_savings < portion_down_payment:

    While we increment our months, we also increment on our current_savings.

    Incrementing current_savings by the right ammount, we have:
    current_savings = current_savings + monthly_portion_saved + monthly_current_savings_return

    monthly_current_savings_return is obtained from calculate_monthly_current_savings_return().

This implentation passes the two test cases provided in the problem statement.

"""


def main():
    months = 0
    annual_salary, portion_saved, total_cost = get_inputs()

    r = 0.04
    current_savings = 0

    monthly_portion_saved = portion_saved * annual_salary / 12
    portion_down_payment = 0.25 * total_cost

    while current_savings < portion_down_payment:
        months += 1
        monthly_current_savings_return = calculate_monthly_current_savings_return(current_savings, r)
        current_savings = current_savings + monthly_portion_saved + monthly_current_savings_return

    display_output(months)


def get_inputs():
    """Get input from user and return float equivalent values"""

    annual_salary = input('Enter your annual salary: ')
    portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
    total_cost = input('Enter the cost of your dream home: ')

    return float(annual_salary), float(portion_saved), float(total_cost)


def display_output(value):
    """Add value to output string and print to user"""

    output = 'Number of months: {}'.format(str(value))
    print(output)


def calculate_monthly_current_savings_return(value, percentage):
    """Calculate returns based on current value and going percentage"""

    return value * percentage / 12


if __name__ == "__main__":
    main()
