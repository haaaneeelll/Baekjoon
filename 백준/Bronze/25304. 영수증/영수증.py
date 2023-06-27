total_amount = int(input())
num_items = int(input())
calculated_amount = 0

for _ in range(num_items):
    price, quantity = map(int, input().split())
    calculated_amount += price * quantity

if calculated_amount == total_amount:
    print("Yes")
else:
    print("No")