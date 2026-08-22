items = ["A", "B", "C"]
n = len(items)
total_subsets = 2 ** n

print("BINARY SUBSET BUILDER")
print("Items:", items)
print("Number of items:", n)
print("Total subsets:", total_subsets)

print("\nPART 1: Power Set")
print("For", n, "items, we can create", total_subsets, "subsets.")

print("\nPART 2: Binary Mask Table")
mask = 0
while mask < total_subsets:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print("Mask", mask, "-> [C][B][A] =", bit2, bit1, bit0)
    mask += 1

print("\nPART 3: Bit Probe")
sample_mask = 5
print("Sample Mask:", sample_mask, "Binary:", bin(sample_mask))
j = 0
while j < n:
    probe = 1 << j
    if sample_mask & probe:
        print("Bit", j, "is set, so item", items[j], "is selected.")
    else:
        print("Bit", j, "is not set, so item", items[j], "is not selected.")
    j += 1

print("\nPART 4: All Subsets")
mask = 0
while mask < total_subsets:
    subset = []
    j = 0
    while j < n:
        probe = 1 << j
        if mask & probe:
            subset.append(items[j])
        j += 1
    print("Mask", mask, "->", subset)
    mask += 1

def bit_difference(a, b):
    difference_count = 0
    while a > 0 or b > 0:
        if (a & 1) != (b & 1):
            difference_count += 1
        a >>= 1
        b >>= 1
    return difference_count

print("\nPART 5: Bit Difference")
print("Difference between 12 and 15:", bit_difference(12, 15))
print("12 =", bin(12), "15 =", bin(15))
print("Difference between 21 and 24:", bit_difference(21, 24))
print("21 =", bin(21), "24 =", bin(24))
print("Difference between 8 and 8:", bit_difference(8, 8))
print("8 =", bin(8), "8 =", bin(8))

print("\nSUMMARY")
print("Power Set: All possible subsets of a set.")
print("Binary Mask: A number that selects items using bits.")
print("Bit Probe: Uses 1 << j to check a specific bit.")
print("Two Loops: One loop for masks, one loop for items.")
print("Bit Difference: Counts different bit positions.")
