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
    annual_salary = input('Enter your annual salary: ')
    portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
    total_cost = input('Enter the cost of your dream home: ')

    return float(annual_salary), float(portion_saved), float(total_cost)


def display_output(value):
    output = 'Number of months: {}'.format(str(value))
    print(output)


def calculate_monthly_current_savings_return(value, percentage):
    return value * percentage / 12


if __name__ == "__main__":
    main()
