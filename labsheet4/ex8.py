#ex8

annual_sal = float(input("Enter annual salary:"))
dep = int(input("Enter number of dependents:"))

if dep == 1:
    personal_allowance=110000
elif dep == 2:
    personal_allowance=190000
elif dep == 3:
    personal_allowance=275000
elif dep >= 4:
    personal_allowance=355000

tax_income = annual_sal - personal_allowance

