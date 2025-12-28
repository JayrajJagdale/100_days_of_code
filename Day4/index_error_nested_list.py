# fruits = ["Cherry","Apple","Graphes","Mango"]

# print(len(fruits))

# print(fruits[5]) # error 

# Nested List

fruits = ["Apple","Banana","Graphes","Mango","Cherry"]
vegetables = ["Tomatoes","Celery","Potatoes"]

dirty_dozens = [fruits, vegetables]
# print(dirty_dozens)

# print(dirty_dozens[0])
# print(dirty_dozens[1])

print(dirty_dozens[0][3]) # Here 0 is list0 and 3 is index in 0 list0
print(dirty_dozens[1][2]) # Here 1 is list1 and 2 is index in 1 list1
print(dirty_dozens[1][0])