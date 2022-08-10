print('Fruit Pricelist: \n1. Apple: 2 Dollars \n2. Banana: 4 Dollars \n503. Orange: 6 Dollars \n4. Grape: 7 Dollars \n5. Mango: 5 Dollars')
money = int(input('How much money do you have?: '))
items = {'apple': 2, 'banana': 4, 'orange': 6, 'grape': 7, 'mango': 5}
for item_name in items:
    print('--------------------------------------------------')
    print('You have ' + str(money) + ' dollars on your wallet')
    print('Price of one ' + item_name + ' is ' + str(items[item_name]) + ' dollars')
    
    input_count = input('How much ' + item_name + ' do you want?:')
    print('Your order is ' + input_count + ' ' + item_name)
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('Total price is ' + str(total_price) + ' dollars')
    
    if money >= total_price:
        print('You have bought ' + input_count + ' ' + item_name)
        money -= total_price
        if money == 0:
            break
            print('Your wallet is empty')
        
    else:
        print('Oops sorry... not enough money:(')
        print('You cannot buy ' + item_name + ' that much')

    print('Your money left is ' + str(money) + ' dollars')
