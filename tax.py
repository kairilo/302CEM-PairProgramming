import math
x = 0
method = ""

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# calucalate mpf for one person
def cal_mpf(income):
    mpf = income * 0.05
    if mpf >= 18000:
        mpf = 18000
    return mpf

# calculate tax for one person
def get_tax(income):
    net_income = 0

    allowance = 132000
    i = 50000

    mpf = income * 0.05
    if mpf >= 18000:
        mpf = 18000

    net_income = income - mpf - allowance          #Net Chargeable Income

    # tax in progressive rates
    if net_income >= 0:
        if net_income <= 50000:     #On the first 50000 at 2%
            p_tax = net_income * 0.02
        elif net_income >50000 and net_income <=100000:     #On the 2nd 50000 at 6%
            p_tax = i * 0.02 + (net_income - i) * 0.06
        elif net_income >100000 and net_income <= 150000:     #On the 3rd 50000 at 10%
            p_tax = i * (0.02 + 0.06) + (net_income - 2*i) * 0.1
        elif net_income >150000 and net_income <= 200000:     #On the 4th 50000 at 14%
            p_tax = i * (0.02 + 0.06 + 0.1) + (net_income - 3*i) * 0.14
        elif net_income >200000:     #remainder at 17%
            p_tax = i * (0.02 + 0.06 + 0.1 + 0.14) + (net_income - 4*i) * 0.17
    else:
        p_tax = 0

    # tax in standard rate
    s_tax = (income - mpf) * 0.15

    # determine which method should be used
    global method
    if s_tax >= p_tax:
        tax = p_tax
        method = "charged at progressive rates"
    else:
        tax = s_tax
        method = "charged at standard rates"

    if tax < 0:
        tax = 0

    tax = round_down(tax)
    return tax



# Calculate tax under joint assessment
def joint_tax(income1, income2):
    net_income = 0
    allowance = 264000
    i = 50000
    t_income = income1 + income2


    mpf1 = income1 * 0.05
    mpf2 = income2 * 0.05
    if mpf1 >= 18000:
        mpf1 = 18000
    if mpf2 >= 18000:
        mpf2 = 18000
    mpf = mpf1 + mpf2

    net_income = t_income - mpf - allowance     #Net Chargeable Income

    # tax in progressive rates
    if net_income <= 50000:     #On the first 50000 at 2%
        p_tax = net_income * 0.02
    elif net_income >50000 and net_income <=100000:     #On the 2nd 50000 at 6%
        p_tax = i * 0.02 + (net_income - i) * 0.06
    elif net_income >100000 and net_income <= 150000:     #On the 3rd 50000 at 10%
        p_tax = i * (0.02 + 0.06) + (net_income - 2*i) * 0.1
    elif net_income >150000 and net_income <= 200000:     #On the 4th 50000 at 14%
        p_tax = i * (0.02 + 0.06 + 0.1) + (net_income - 3*i) * 0.14
    elif net_income >200000:     #remainder at 17%
        p_tax = i * (0.02 + 0.06 + 0.1 + 0.14) + (net_income - 4*i) * 0.17

    # tax in standard rate
    s_tax = (t_income - mpf) * 0.15

    # determine which method should be used
    global method
    if s_tax >= p_tax:
        tax = p_tax
        method = "Charged at progressive rates"
    else:
        tax = s_tax
        method = "Charged at standard rates"

    if tax < 0:
        tax = 0

    tax = round_down(tax)
    return tax



print("---------------------------------------------------------")
print("Tax Calculator")
print("---------------------------------------------------------")

while x == 0:

# Questions to select whether use want to calculate tax for one person or also for husband/wife (i.e. single/married)
    question = input("Enter 1 for single, enter 2 for married: ")
    try:
        if question == '1':     #single
            income = int(input("Enter your income: "))
            tax = get_tax(income)
            mpf = cal_mpf(income)
            allowance = 132000.0
            net = income - mpf - allowance
            if net <= 0:     # no tax
                net = 0
                print("---------------------------------------------------------")
                print("Your income:           $", income)
                print("Net Chargeable Income: $", net)
                print("NO NEED PAY")
                print("---------------------------------------------------------")
            else:     #normal case tax
                print("---------------------------------------------------------")
                print("Your income:           $", income)
                print("Less mpf:              $", mpf)
                print("Less Basic Allowance:  $", allowance)
                print("Net Chargeable Income: $", net)
                print("==========================================================")
                print("Tax payable by you:    $", tax)
                print(method)
                print("==========================================================")

            # create a loop
            ans = input("wanna continue? y / n\n")
            if ans == "y":
                pass
            elif ans == "n":
                x+=1
            else:
                input("Input error! The programme will now exit! \n")
                x+=1

        elif question == '2':     #married
            income1 = int(input("Enter your income: "))
            income2 = int(input("Enter spouse's income: "))
            t_income = int(income1 + income2)
            tax1 = get_tax(income1)
            tax2 = get_tax(income2)
            j_tax = joint_tax(income1, income2)
            mpf1 = cal_mpf(income1)
            mpf2 = cal_mpf(income2)
            t_mpf = mpf1 + mpf2
            allowance1 = 132000.0
            allowance2 = 264000.0
            net1 = income1 - mpf1 - allowance1
            net2 = income2 - mpf2 - allowance1
            if net1 <= 0:     #'you' do not need to pay tax
                net1 = 0
            if net2 <= 0:     #'your spouse' does not need to pay tax
                net2 = 0
            t_net = net1 + net2     #both do not need to pay tax
                 #set tax to 0 if it is negative
            if tax1 <= 0:
                tax1 = 0
            if tax2 <= 0:
                tax2 = 0
            if j_tax<= 0:
                j_tax = 0
            # Under seperate taxation
            print("----------------------------------------------------------")
            print("UNDER SEPERATE TAXATION")
            print("----------------------------------------------------------")
            print("Your income:            $", income1)
            print("Less mpf:               $", mpf1)
            print("Less Basic Allowance:   $", allowance1)
            print("Net Chargeable Income:  $", net1)
            print("----------------------------------------------------------")
            print("Tax payable by you:     $", tax1)
            print("----------------------------------------------------------")
            print("Your spouse's income:   $", income2)
            print("Less mpf:               $", mpf2) 
            print("Less Basic Allowance:   $", allowance1)
            print("Net Chargeable Income:  $", net2)
            print("----------------------------------------------------------")
            print("Tax payable by spouse:  $", tax2)
            print("==========================================================")
            print("Total tax payable by you and your spouse =  $", tax1 + tax2)
            print("==========================================================")
            # Under join taxation
            print("----------------------------------------------------------")
            print("UNDER JOINT ASSESSMENT")
            print("----------------------------------------------------------")
            if net1 <= 0 and net2 <= 0:
                print("Total income:           $", t_income)
                print("Net Chargeable Income:  $", t_net)
                print("==========================================================")
                print("NO NEED PAY TAX")
                print("==========================================================")
            elif net2 <= 0:
                print("Total income:           $", t_income)
                print("Net Chargeable Income:  $", t_net)
                print("Your spouse does not need to pay tax")
                print("==========================================================")
                print("Total tax payable by you and your spouse:  $", tax1)
                print("==========================================================")
            elif net1 <= 0:
                print("Total income:           $", t_income)
                print("Net Chargeable Income:  $", t_net)
                print("You do not need to pay tax")
                print("==========================================================")
                print("Total tax payable by you and your spouse:  $", tax2)
                print("==========================================================")
            else:     #normal case
                print("Total income:           $", t_income)
                print("Less mpf:               $", t_mpf)
                print("Less Basic Allowance:   $", allowance2)
                print("Net Chargeable Income:  $", t_net)
                print("==========================================================")
                print("Total tax payable by you and your spouse:  $", j_tax)
                print("==========================================================")

            # Determine which method is better (seperate/joint)
            # and determine the tax rate method
            if (tax1 + tax2 > j_tax):
                print("As a result, use joint assessment is better:)")
                print("----------------------------------------------------------")
                print(method)
                print("----------------------------------------------------------")
            elif (tax1 + tax2 < j_tax):
                print("As a result, use seperate assessment is better:)")
                print("----------------------------------------------------------")
                print(method)
                print("----------------------------------------------------------")

            # create a loop
            ans = input("wanna continue? y / n\n")
            if ans == "y":
                pass
            elif ans == "n":
                x+=1
            else:
                input("Input error! The programme will now exit! \n")
                x+=1

        elif question == 'test':   #Testing

            #Here is a list for comparing test cases with the expected results with the following format:

            #[
            #Your income,
            #Spouse's income,
            #Expected tax payable by you,
            #Expected tax payable by your spouse,
            #Expected tax payable under joint accessment,
            #Description
            #]

            testdict = {'test1':[400000,600000,24500,58500,101000,"Normal Case"],
            'test2':[100000,10000,0,0,0,'Low income with no tax payable'],
            'test3':[2500000,3000000,372300,447300,819600,'High income with tax calculated in standard rate (both)'],
            'test4':[2500000,600000,372300,58500,458000,'High income with tax calculated in standard rate (only one person at standard rate)'],
            'test5':[10,20,0,0,0,'Extreme case (low)'],
            'test6':[444444444,666666666,66663966,99997299,166661266,'Extreme case (high)'],
            'test7':[10,444444444,0,66663966,66663968,'Extreme case'],
            'test8':[10,400000,0,24500,5801,'One extreme data'],
            'test9':[300000,600000,9420,58500,84510,'One Mpf not higher than the limit (i.e. 18000)'],
            'test10':[300000,200000,9420,1480,17870,'Both Mpf not greater than limit (i.e. 18000)']}

            print("=============================Start Testing=============================")
            print("Data set for testing: \n")
            for key in testdict:
                print(key,': ',testdict.get(key))
            print("-----------------------------------------------------------------------")
            print("If the tax payable separately by you and your spouse, and the tax payable under joint accessment are matched with the expected result, return true. Else, return false.")
            print("-----------------------------------------------------------------------")
            for value in testdict.values():
                print('''
                        ''',value[5],'''
                        ''')
                print("Tax payable by you: ",get_tax(value[0]))
                print("Tax payable by your spouse: ",get_tax(value[1]))
                print("Tax payable under joint assessment:", joint_tax(value[0],value[1]))
                if get_tax(value[0]) == value[2] and get_tax(value[1]) == value[3] and joint_tax(value[0],value[1]) == value[4]:
                    print("True")
                    print("-----------------------------------------------------------------------")
                else:
                    print("False")
                    print("-----------------------------------------------------------------------")
            print("=============================End Testing=============================")
            # create a loop
            ans = input("wanna continue? y / n\n")
            if ans == "y":
                pass
            elif ans == "n":
                x+=1
            else:
                input("Input error! The programme will now exit! \n")
                x+=1

        else:
            print("Input error! Please try again! \n")


    except:
        pass

if __name__ == '__main__':
    pass
