# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

numberOfShoes = int(input())
shoeSizes = input().split()
n = int(input())

# print(shoeSizes)

customerList = collections.Counter()
for i in range(numberOfShoes):
    customerList[shoeSizes[i]] += 1

# print(customerList)

totalPrice = 0
for i in range(n):
    order = input().split()
    # print(customerList[order[0]])
    if customerList[order[0]] > 0:
        customerList[order[0]] -= 1
        totalPrice += int(order[1])

# print(customerList)
print(totalPrice)