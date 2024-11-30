array = [0] * 7  # Initialize all positions to 0
data = input("Enter 4-bit data to send: ")

if len(data) != 4:
    print("Error: Please enter exactly 4 bits of data.")
else:
    array[0] = int(data[0])  
    array[1] = int(data[1])  
    array[2] = int(data[2])
    array[4] = int(data[3])

    def iseven(sum):
        return 0 if sum % 2 == 0 else 1

    sum1 = array[0] + array[2] + array[4]
    sum2 = array[1] + array[2] + array[4]
    sum3 = array[0] + array[1] + array[2]

    p1 = iseven(sum1)
    p2 = iseven(sum2)
    p3 = iseven(sum3)

    array[6] = p1
    array[5] = p2
    array[3] = p3

    result = ''.join(map(str, array))
    print("Encoded 7-bit Hamming code:", result)
