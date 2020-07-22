# house-hunting

Problem Set 1, Question A of MIT 6.0001: Introduction to Computer Science and Programming in Python (Fall 2016)

## Solution

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
    Incrementing current_savings by the right amount, we have:
    current_savings = current_savings + monthly_portion_saved + monthly_current_savings_return
    monthly_current_savings_return is obtained from calculate_monthly_current_savings_return().

This implementation passes the two test cases provided in the problem statement.
