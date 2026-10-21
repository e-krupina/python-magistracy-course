def print_menu(prices):
    print("Товары в продаже:")
    for name in prices:
        print(f"  {name} — {prices[name]} руб.")


def ask_quantity(product):
    quantity = input(
        f"Количество «{product}» — целое положительное число (например, 2): "
    )
    return int(quantity)


def item_cost(price, quantity):
    cost = price * quantity
    return cost


def print_receipt(cart):
    print("\n--- Чек ---")
    costs = []
    for index in range(len(cart)):
        product, quantity, cost = cart[index]
        print(f"{index + 1}. {product} × {quantity} = {cost} руб.")
        costs.append(cost)
    receipt_total = sum(costs)
    print(f"Сумма: {receipt_total} руб.")
    return receipt_total


def apply_discount(total, card=False):
    discount_percent = 0
    if card:
        discount_percent = 10
    elif total >= 1000:
        discount_percent = 5

    discount_value = total * discount_percent // 100
    final_total = total - discount_value
    return discount_value, final_total


product_prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350,
}

cashier_name = input("Имя кассира (например, Мария): ")
print(f"Здравствуйте, {cashier_name}! Касса открыта")
print_menu(product_prices)

purchases = []
product_name = input(
    '\nТовар: хлеб, молоко, сыр, яблоки или кофе (для завершения — "оплата"): '
).strip().lower()
while product_name != "оплата":
    if product_name in product_prices:
        product_quantity = ask_quantity(product_name)
        position_cost = item_cost(product_prices[product_name], product_quantity)
        purchases.append((product_name, product_quantity, position_cost))
        print(f"Добавлено: {product_name} × {product_quantity} = {position_cost} руб.")
    else:
        print(f"Товара «{product_name}» нет в продаже")

    product_name = input(
        '\nТовар: хлеб, молоко, сыр, яблоки или кофе (для завершения — "оплата"): '
    ).strip().lower()

card_answer = input("\nКарта магазина — введите только «да» или «нет»: ").strip().lower()
receipt_total = print_receipt(purchases)
discount_value, final_total = apply_discount(receipt_total, card=card_answer == "да")

unique_products = set()
for product, quantity, cost in purchases:
    unique_products.add(product)

print(f"Скидка: {discount_value} руб.")
print(f"К оплате: {final_total} руб.")
print(f"Разных товаров в чеке: {len(unique_products)}")
print(f"\nСпасибо за работу, {cashier_name}!")
