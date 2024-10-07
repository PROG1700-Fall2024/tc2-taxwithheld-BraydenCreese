# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.


"""

after looking over this again I didnt format the outout for the Dependent Deduction for the amount of people correctly. its printing as 2.0 and not 2.

"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # setting values to 0 for clean numbers
    weeklySalary_preTax     = 0 
    dependentsAmount        = 0

    # welcome / opening message
    print("Tax Withholding Calculator")

    # getting user input for their weekly salary and the amount of dependents they have. ( Logic for the loop is the same for both )
    while True: # <--- setting up a loop to catch user input error
        try: # <--- telling loop to try taking inputs till it is correct or a num
            weeklySalary_preTax = float(input("\nPlease enter the full amount of your weekly salary: ")) # <--- input for users weekly salary
            break # <--- stops the loop when it is sataifed and is givien a number
        except ValueError: # <--- if a non number is found it triggers a error in the loop and prints the error message and loops back to the input.
            print("Invlaid Input! Please enter a number value for 'full amount of your weekly salary'.")

    while True:
        try:
            dependentsAmount = int(input("How many dependents do you have?: ")) # <--- input for users amount of dependents
            break
        except ValueError:
            print("Invlaid Input! Please enter a number value for 'How many dependents do you have'.")


    # calcs
    provincialTax = weeklySalary_preTax * 0.06
    federalTax = weeklySalary_preTax * 0.25
    dependentDeduction = weeklySalary_preTax * 0.02 * dependentsAmount

    # total tax after deductions
    totalTax = provincialTax + federalTax - dependentDeduction

    totalWithheld = provincialTax + federalTax - dependentDeduction

    # total take home pay
    takeHomePay = weeklySalary_preTax - totalTax

    
    # prining out end values for users inputed starting values
    print(f"Provincial Tax Withheld:                                    $""{:.2f}".format(provincialTax))
    print(f"Federal Tax Withheld:                                       $""{:.2f}".format(federalTax))
    print(f"Dependent Deduction for {dependentsAmount} dependents:                       $""{:.2f}".format(dependentDeduction))
    print(f"Total Withheld:                                             $""{:.2f}".format(totalWithheld))
    print(f"Total Take-Home Pay:                                        $""{:.2f}".format(takeHomePay))

    # YOUR CODE ENDS HERE

main()
