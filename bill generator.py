product={}     #to store product and price
total=0        #to store total payment 

while True:
    prod=input("Enter product name or quit(q):  ")
    if prod.lower()=="q":   #quit 
        break
        print()
    else:      #add item ,price,quantity into bill
        price=int(input(f"Enter price of {prod}: "))
        quantity=int(input(f"Enter quantity of {prod}: "))
        total_price=quantity*price
        product[prod]=total_price

print("------YOUR RECEPT-------")   #show bill
print()
for key, value in product.items():
    print(f"{key}",":",f"{value}")
    total+=value
print(f"Your total is : {total}")
print()
print("-------THANK YOU--------")   