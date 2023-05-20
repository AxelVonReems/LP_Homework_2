def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Скидка не может быть больше 100%')
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)


new_price = discounted(100000, 10, phone_name='iPhone 14')
print(new_price)

new_price = discounted(80000, 20, phone_name='Samsung S22')
print(new_price)

new_price = discounted(10000, 20)
print(new_price)
