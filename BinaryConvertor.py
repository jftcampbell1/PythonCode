#Binary Covertor
bNumber = input("Please enter a binary number: ")

while len(bNumber) != 8:
    bNumber = input("Please enter a binary number, this number must be 8 bits long: ")

b1 = bNumber[0]
b2 = bNumber[1]
b3 = bNumber[2]
b4 = bNumber[3]
b5 = bNumber[4]
b6 = bNumber[5]
b7 = bNumber[6]
b8 = bNumber[7]

b1 = int(b1)
b2 = int(b2)
b3 = int(b3)
b4 = int(b4)
b5 = int(b5)
b6 = int(b6)
b7 = int(b7)
b8 = int(b8)

dNumber = b1*128 + b2*64 + b3*32 + b4*16 + b5*8 + b6*4 + b7*2 + b8*1

print("That equals " + str(dNumber) + " in denary")
