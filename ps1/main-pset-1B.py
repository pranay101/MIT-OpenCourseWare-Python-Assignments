
def expect(what_is_given, what_to_expect):
    return what_is_given == what_to_expect

# first problem set


def problem_set_1(annual_salary_test, portion_saved_test, total_cost_test,semi_annual_raise):
    # total cost of the house you are willing to buy
    total_cost = float(total_cost_test)

    # entering annual salary. what else you do expect
    annual_salary = float(annual_salary_test)

    # down payment for your house
    portion_down_payment = 0.25*total_cost

    # portion of monthly salary saved
    portion_saved = float(portion_saved_test)

    # Savings to pay the downpayment
    current_saving = 0

    # investment return rate
    r = 0.04

    # Numberof months it would take to save fro downpayment
    No_of_months = 0

    # Monthly salary not very legit way to comment lol
    monthly_salary = annual_salary/12

    # loop to find the number of months
    while current_saving <= portion_down_payment:

        # increment in savings in 2 ways investment and salary
        current_saving += current_saving * r/12
        current_saving += monthly_salary * portion_saved
        No_of_months += 1
        if No_of_months % 6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise

    return No_of_months


def test_case():
    annual_salary_test = 120000
    portion_saved_test = 0.05
    total_cost_test = 500000
    Number_of_months = 142
    semi_annual_raise = 0.03
    expect = problem_set_1(annual_salary_test,portion_saved_test,total_cost_test,semi_annual_raise)==Number_of_months
    if expect:
        print("\033[1;32;32m Test case 1 passed !!")
        annual_salary_test = 80000
        portion_saved_test = 0.1
        total_cost_test = 800000
        Number_of_months = 159
        semi_annual_raise = 0.03
        expect = problem_set_1(annual_salary_test, portion_saved_test, total_cost_test,semi_annual_raise) == Number_of_months
        if expect:
            print("\033[1;32;32m Test case 2 passed !!")
            annual_salary_test = 75000
            portion_saved_test = 0.05
            total_cost_test = 1500000
            Number_of_months = 261
            semi_annual_raise = .05
            expect = problem_set_1(annual_salary_test, portion_saved_test, total_cost_test,semi_annual_raise) == Number_of_months
            if expect:
                print("\033[1;32;32m Test case 3 Passed !!")
                print("\033[1;32;32m Program running fine")
            else:
                print("\033[1;31;31m Test case 3 Failed !!")
        else:
            print("\033[1;31;31m Test case 2 Failed !!")
    else:
        print("\033[1;31;31m Test case 1 Failed !!")

# main function offcourse


def main():
    test_case()


# just trying to be a bit professional
if __name__ == '__main__':
    main()
