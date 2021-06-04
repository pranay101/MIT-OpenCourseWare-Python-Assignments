def test_case():
    

def problem_set_1():
    #total cost of the house you are willing to buy
    total_cost = input(float("Enter the total cost of the house: "))
    #entering annual salary. what else you do expect
    annual_salary = input(float("Enter Your anual salary: "))
    # down payment for your house 
    portion_down_payment = 0.25*total_cost
    #saving after givin the down payment which is further invest to gain return
    current_saving = total_cost - portion_down_payment
    # investment return rate
    r = 0.04
    #additional money gained apart from monthly income
    investment_return = (current_saving*r/12)-r
    #portion of monthly salary saved 
    portion_saved = 0.1
    #amount left after all this expences
    savings = portion_saved*annual_salary/12 + investment_return
    
    
#main function offcourse
def main():
    problem_set_1()
    

    

if __name__ == '__main__':
    main()