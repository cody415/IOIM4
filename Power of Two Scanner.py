print("================================")
print("POWER OF TWO SCANNER")
print("================================")

n = 16
print("\nPART 1: The n & (n-1) Trick")
print("n       =", n, "->", bin(n))
print("n - 1   =", n - 1, "->", bin(n - 1))
print("n&(n-1) =", n & (n - 1), "->", bin(n & (n - 1)))
print("This trick removes the rightmost set bit.")

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0

print("\nPART 2: Power of 2 Check")
numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]
for num in numbers:
    print(num, "->", bin(num), "->", is_power_of_2(num))

def is_power_of_4(num):
    if not is_power_of_2(num):
        return False
    position = 0
    while num > 1:
        num >>= 1
        position += 1
    return position % 2 == 0

print("\nPART 3: Power of 4 Check")
for num in numbers:
    print(num, "->", is_power_of_4(num))

def is_power_of_8(num):
    if not is_power_of_2(num):
        return False
    position = 0
    while num > 1:
        num >>= 1
        position += 1
    return position % 3 == 0

print("\nPART 4: Power of 8 Check")
for num in numbers:
    print(num, "->", is_power_of_8(num))

def binary_power(base, exponent):
    answer = 1
    while exponent > 0:
        if exponent & 1:
            answer *= base
        base *= base
        exponent >>= 1
    return answer

print("\nPART 5: Binary Exponentiation")
print("2^5 =", binary_power(2, 5))
print("3^4 =", binary_power(3, 4))
print("5^3 =", binary_power(5, 3))

print("\n================================")
print("POWER SCANNER SUMMARY")
print("================================")
print("Power of 2: only one bit is set.")
print("Power of 4: set-bit position is even.")
print("Power of 8: set-bit position is divisible by 3.")
print("Binary exponentiation calculates powers quickly.")
print("================================")
