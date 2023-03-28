import functionsAmb2

price = float(input("Product price: "))
paymentChoice = int(input("Payment method \n1 - à vista cash or check - 10%  \n2- à vista credit card - 15%\n3- duas vezes - 10% juros\n"))
price = functionsAmb2.calcPayment(price, paymentChoice)

print("Total paid for the product: ", price)