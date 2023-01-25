def Tax_calcutor (income):

    if income <= 250000:
        return 0
    elif 250000<income <=500000:

        return (income-250000)*0.05

    elif 500000<income <=750000:

        return ((income-500000)*0.1)+12500
    
    elif 750000<income <=1000000:

        return ((income-750000)*0.15)+37500
    elif 1000000<income <=1250000:

        return ((income-1000000)*0.2)+(75000)
    elif 1250000<income <=1500000:

       return ((income-1250000)*0.25)+(125000)
    elif income >=1500000:

        return ((income-1500000)*0.3)+(187500)


if __name__ =="__main__":

    total_income = float(input("please enter your income"))
    exemputed_income = float(input("please enter exemputed amount"))
    income = total_income-exemputed_income
    tax = Tax_calcutor(income)
    print(tax)
    
    

