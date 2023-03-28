def calcPayment(price, paymentChoice):
    if paymentChoice == 1:
        finalPrice = price - (price * 0.10)
    elif paymentChoice == 2:
        finalPrice = price - (price * 0.15)
    else:
        finalPrice = price + (price * 0.10)

    return finalPrice