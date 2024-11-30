# Input 5-bit transmitted data
data = input("Enter 5-bit data that was transmitted: ")

# Store data bits in an array
array = [None] * 5
for i in range(0, 5):
    array[i] = int(data[i])

# Function to check if a sum is even or odd
def iseven(sum):
    if sum % 2 == 0:
        return 0  # Even
    else:
        return 1  # Odd

# Compute parity check sums based on Hamming Code rules
sum1 = array[4] + array[2] + array[0]  # Parity for P1
sum2 = array[3] + array[2] + array[0]  # Parity for P2
sum3 = array[1] + array[0]             # Parity for P4

# Find error position in binary form
e1 = iseven(sum1)  # P1
e2 = iseven(sum2)  # P2
e3 = iseven(sum3)  # P4

errorbinary = f"{e3}{e2}{e1}"
errordecimal = int(errorbinary, 2)

# Output error position and corrected data
print("Array:", array)
print("Error Position (Binary):", errorbinary)
print("Error Position (Decimal):", errordecimal)

# Correct the error if detected
if errordecimal != 0:  # If error position is not zero (no error)
    index_to_fix = 5 - errordecimal  # Convert position to index (0-based)
    array[index_to_fix] = 1 - array[index_to_fix]  # Flip the bit

print("Corrected Data:", array)