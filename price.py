def format_price(price):
    price = str(int(price))
    return "Цена: " + price + " руб."

a = format_price(56.24)
print(a)