# File not found
try:
    file = open("non_existing_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["non_existing_key"])
except FileNotFoundError:
    file = open("non_existing_file.txt", "w")
    file.write("Write something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
