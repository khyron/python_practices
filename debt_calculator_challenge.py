n = int(input("number of people: "))
print(n)
names=[]
amount=[]
i = 0
while i < n :
    in_names = input("name:")
    names.append(in_names)    
    in_amount = int(input("spend amount: ")) 
    amount.append(in_amount)
    i += 1 

mean_spend = (sum(amount)/n)
total = (sum(amount))
print("mean spend: " , mean_spend)
print("Total spend: ", total)
j = 0
for j in range(len(names)):
    to_pay = amount[j] - mean_spend 
    if to_pay > 0:
        print(names[j], "must receive", round(to_pay,2))
    elif to_pay < 0:
        print(names[j], "must pay", round(-to_pay,2))
    else:
        print(names[j], "Nothing to do")
 
