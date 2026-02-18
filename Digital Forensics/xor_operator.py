# Python program to show
# bitwise operators

a = 10
b = 4

print("a = ",a," b1010") #1010 --> 0101 --> 1010 + 1 + 1011 = 11
print("b = ",b,"  b0100")

# Print bitwise AND operation
print("a & b =", a & b)

# Print bitwise OR operation
print("a | b =", a | b)

# Print bitwise NOT operation
print("~a =", ~a)

# print bitwise XOR operation
print("a ^ b =", a ^ b)

'''
bk   c     k
00 = 0 xor 0 = 0
01 = 1 xor 1 = 0
10 = 1 xor 0 = 1
11 = 0 xor 1 = 1
'''

