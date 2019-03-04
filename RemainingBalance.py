#RemainingBalance
def rem_balance(balance, annualInterestRate, monthlyPaymentRate):
	'''
	in:
		balance-float that stands for the outstanding balance on the credit card
		annualInterestRate- float between 0-1, annual interest rate as a decimal
		monthlyPaymentRate-float between 0-1, minimum monthly payment rate as a decimal
	out:
		a float with two decimal digits stands for the remaining balance after 12 month
	'''
	mon_interest_rate = annualInterestRate/12
	for mon in range(12):
		min_mon_payment = monthlyPaymentRate * balance
		mon_unpayed_balance = balance - min_mon_payment
		balance = mon_unpayed_balance + mon_interest_rate * mon_unpayed_balance
	return round(balance,2)

print("Remaining balance: "+str(rem_balance(balance, annualInterestRate, monthlyPaymentRate)))