fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception


def make_pie():
    index = int(input("Enter index: "))
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie()
