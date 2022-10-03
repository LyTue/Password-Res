# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that I made up.")

# height = float(input("Height : "))
# weight = int(input("Weight : "))
#
# if height > 3:
#     raise ValueError("Human Height shoild not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# challenge

# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'likes': 13, 'comments': 2, 'shares': 1},
    {'likes': 33, 'comments': 8},
    {'comments': 4, 'Shares': 2},
    {'comments': 1, 'Shares': 1},
    {'likes': 19, 'comment': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        pass

print(total_likes)
