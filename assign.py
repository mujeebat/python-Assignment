customer=input("enter your name: ")
print()
customerNumber= str(0)

while len(customerNumber) !=11 :
    customerNumber= str(input("Enter your phone number:"))
    if len(customerNumber) !=11 :
        print("your phone number must be of 11 digits")
    if customerNumber[0]!='0':
        print("your phone number must start with 0")
        
    while customerNumber[0]!= '0':
        customerNumber =  str(input("Enter your phone number:"))
    if customerNumber[0]!= '0':
            print("your phone number must start from 0")

    print()
    
    Email= input("Enter your email account:")
    while("@email.com" or "@yahoo.com" or "@gmail.com") not in Email:
        Email = input("your email address must have @email.com or @gmail.com or @yahoo.com\n")
        
    print('_'*40)
    print()
    
    stocks = {"milk":400,"flakes":500,"oats":400,"apple":120,"egg":1200,"milo":350,"soap":745}
    print("select what you want to buy from the items below \n", tuple(stocks))
    print()
    
    
    
    itemName1 = (input("The name of item you want to buy"))
    itemQuantity1 = eval(input("quantity"))
    print()
    price1 = (stocks[itemName1])
    goodsPrice1 = itemQuantity1 * price1
    print("stock price: ", price1)
    print("The total price of goods : ",goodsPrice1)
    
    itemName2 = (input("The name of item you want to buy"))
    itemQuantity2 = eval(input("quantity"))
    print()
    price2 = (stocks[itemName2])
    goodsPrice2 = itemQuantity2 * price2
    print("stock price: ", price2)
    print("The total price of goods : ",goodsPrice2)
    
    itemName3 = (input("The name of item you want to buy"))
    itemQuantity3 = eval(input("quantity"))
    print()
    price3 = (stocks[itemName3])
    goodsPrice3 = itemQuantity3 * price3
    print("stock price: ", price3)
    print("The total price of goods : ",goodsPrice3)
    
    itemName4 = (input("The name of item you want to buy"))
    itemQuantity4 = eval(input("quantity"))
    print()
    price4 = (stocks[itemName4])
    goodsPrice4 = itemQuantity4 * price4
    print("stock price: ", price4)
    print("The total price of goods : ",goodsPrice4)
    
    itemName5 = (input("The name of item you want to buy"))
    itemQuantity5 = eval(input("quantity"))
    print()
    price5 = (stocks[itemName5])
    goodsPrice5 = itemQuantity5 * price5
    print("stock price: ", price5)
    print("The total price of goods : ",goodsPrice5)
    
    itemName6 = (input("The name of item you want to buy"))
    itemQuantity6 = eval(input("quantity"))
    print()
    price6 = (stocks[itemName6])
    goodsPrice6 = itemQuantity6 * price6
    print("stock price: ", price6)
    print("The total price of goods : ",goodsPrice6)
    
    
    itemName7 = (input("The name of item you want to buy"))
    itemQuantity7 = eval(input("quantity"))
    print()
    price7 = (stocks[itemName7])
    goodsPrice7 = itemQuantity7 * price7
    print("stock price: ", price7)
    print("The total price of goods : ",goodsPrice7)
    
    print("total price",goodsPrice1+goodsPrice2+goodsPrice3+goodsPrice4+goodsPrice5+goodsPrice6+goodsPrice7)
    