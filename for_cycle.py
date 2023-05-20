# Part one

stock = [
    {'name': 'iPhone 14', 'stock': 24, 'price': 100000, 'discount': 25},
    {'name': 'Samsung S22', 'stock': 10, 'price': 80000, 'discount': 10},
    {'name': '', 'stock': 38, 'price': 10000, 'discount': 10},
]


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


for phone in stock:
    phone['price_final'] = discounted(
        phone['price'], phone['discount'], phone_name=phone['name']
        )

print(stock)

# Part two

classes = [
    {'name': '3A', 'scores': [4, 3, 5, 2, 4]},
    {'name': '3Б', 'scores': [2, 5, 4, 3, 5]},
    {'name': '3В', 'scores': [3, 3, 4, 5, 4]},
]


def count_class_avg_score(student_scores):
    scores_sum = 0
    for score in student_scores:
        scores_sum += score
    return scores_sum / len(student_scores)


school_score_avg = 0
for one_class in classes:
    class_avg = count_class_avg_score(one_class['scores'])
    print(f'Средняя оценка класса {one_class["name"]}: {class_avg}')
    school_score_avg += class_avg

print(f'Средняя оценка по школе: {round(school_score_avg / len(classes), 1)}')
