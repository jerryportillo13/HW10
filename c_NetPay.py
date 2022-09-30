import a_EmployeeClass as e
import b_PayrollDeductionsClass as d


employee1 = e.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

deduction1 = d.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
deduction2 = d.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
deduction3 = d.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
deduction4 = d.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
deduction5 = d.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

print("*** Employee Pay ***")
print("Name:", employee1.get_name())
print("ID Number:", employee1.get_ID())
print("Department:", employee1.get_dept())
print("Gross Pay: $", float(employee1.get_salary()), sep='')
print("Net Pay: $", employee1.get_salary()-deduction2.getAmount()-deduction4.getAmount()-deduction5.getAmount(), sep='')

