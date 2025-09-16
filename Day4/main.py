age = int(input("Enter your age:"))
# Check validity of age
if age > 0:
    vip = input("Do you have a VIP pass? (yes or no)").lower()
    discount = 20
    # checking for the price
    if age < 12 or age > 65 :
        base_price = 10
        if vip == 'yes':
            discount_amount = base_price * discount / 100
            vip_price = base_price - discount_amount
            print(f"The base price is ${base_price} amount to get off is ${discount_amount}, you have to pay ${vip_price}")
        else:
            print(f"You have to pay the base price ${base_price}.")

    else:
        base_price = 15
        if vip == 'yes':        
            discount_amount = base_price * discount / 100
            vip_price = base_price - discount_amount
            print(f"The base price is ${base_price} amount to get off is ${discount_amount}, you have to pay ${vip_price}")
        else:
            vip_price = base_price
            print(f"You have to pay the base price ${base_price}.")
else:
    print("Invaid age!")            
