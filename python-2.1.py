# Create an Empty Inventory
# 1. Question: Create an empty dictionary named inventory that will store product
# names as keys and their quantities as values.

inventory = {}
print("Initial Inventory:", inventory)


# 2. Add a Product
# Question: Add a product (e.g., "apple") with a quantity (e.g., 10 to the inventory
# dictionary. Print the updated inventory.

inventory["apple"] = 10
print("Added apples:",inventory)
# list with dictionary [{"product": "banana", "quantity": 5}, {"product": "apple", "quantity": 5}]


# 3. Update a Product Quantity
# Question: Now add another product (e.g., "banana" with quantity 5, then update
# the quantity of "apple" by adding 5 more. Print the inventory after updates.

inventory["banana"] = 5
inventory["apple"] += 5
print("Added banana & 5 more apples:",inventory)

# 4. Remove a Product
# Question: Remove "banana" from the inventory (simulate running out of stock)
# and print the inventory.

del inventory["banana"]
print("removing banana", inventory)

# 5. Display the Inventory Summary
# Question: Use a loop to iterate over the inventory and print a summary message
# for each product (e.g., "We have 15 apples in stock.").
inventory["guitar"]= 15
inventory["basketball"]= 10

for key, value in inventory.items():
    print(f"We have {value} {key} in stock.")


# Unpacking Tuples
my_tuple = ('apple', 15)
k, v = my_tuple
# k should return apple
# v should return 15 
k , v,  = my_tuple

# inventory.items()
# Out[45]: dict_items([('apple', 15), ('banana', 5), ('guitar', 15), ('basketball', 10)])
# inventory.keys()
# Out[46]: dict_keys(['apple', 'banana', 'guitar', 'basketball'])
# inventory.values()
# Out[47]: dict_values([15, 5, 15, 10])
inventory.items()
