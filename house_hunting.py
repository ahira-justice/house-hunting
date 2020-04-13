def main():
    pass


def get_inputs():
    annual_salary = input('Enter your annual salary: ')
    portion_saved = input('Enter the percent of your salary to save as a decimal: ')
    total_cost = input('Enter the cost of your dream home: ')

    return float(annual_salary), float(portion_saved), float(total_cost)


def display_output(value):
    output = 'Number of months: {}'.format(str(value))
    print(output)


if __name__ == "__main__":
    main()
