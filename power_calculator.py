base=int(input("Enter the base: "))
power=int(input("Enter the power: "))
current_answer=1
for i in range(power):
    current_answer=current_answer*base
print(current_answer)