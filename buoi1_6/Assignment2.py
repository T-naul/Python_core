
#1
test_score1=int(input("Enter the first test score: "))
test_score2=int(input("Enter the second test score: "))
test_score3=int(input("Enter the third test score: "))

average_score=(test_score1+test_score2+test_score3)/3
print("The average of score is ",round(average_score,2))
if average_score>=95:
    print("Congratulate, your score is great!")

#2
hours_worked=int(input("Enter the number of hours worked: "))
pay_rate=int(input("Enter the hourly pay rate: "))

if hours_worked>40:
    gross_pay=40*pay_rate+(hours_worked-40)*1.5*pay_rate
else:
    gross_pay=hours_worked*pay_rate

print("The gross pay is ",round(gross_pay,2))

#3
salary=int(input("Enter your salary: "))
years_on_job=int(input("Enter years on job: "))
if salary>=30000:
    if years_on_job>=2:
        print("You qualify for the loan")
    else:
        print("You must have been on your current job for at least two years to qualify")
else:
    print("You must ear at least $30,000 per year to qualify")

#4
for i in range(5):
    print("Hello world")

#5
check='y'
while(check=='y'):
    sales=int(input("Enter the amount of sales: "))
    comm_rate=int(input("Enter the commision rate: "))
    commision=sales*comm_rate
    print("The commision is ",round(commision,2))
    check=input("Press y to continue: ")

