def calculate_discount(cost):
    if cost > 400000:
        return cost*0.8
    elif cost >=200000:
        return cost*0.9
    else:
        return cost
cost= float(input('enter the cost'))

print(calculate_discount(cost))
