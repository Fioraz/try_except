height = float(input("Enter height: "))
weight = int(input("Enter weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 metres.")

bmi = weight / height ** 2
print(bmi)
