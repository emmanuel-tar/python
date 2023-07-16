"""
Louis wants to open a Pizza  shop and needs to write a 
program for accepting orders.

Tip ----
Always Visualize First ,Then Start Coding.
"""

#--------------------------------
#Variable Declaration
#--------------------------------

#---------------------------------
customer:str = "BeBe"
pizza_base:str = 'Thin'
pizza_size:int = 12
topping: str = 'Olives'
extra_cheese:bool = True
price:float = 8.99
amt_paid:float = float(input('Enter Amount:  '))
if amt_paid == price:
    print('Thank you')
else:
    change:float = amt_paid - price
    #-----------------------------------------------------
    print(f'Received Order from{customer}')
    print(f'invoice No: 100123\n Pizza Base: {pizza_base}\n Size: {pizza_size} Inches\n Topping:{topping} ')
print(f' Amount Received: {amt_paid} and price is {price}, change is : {change}')

