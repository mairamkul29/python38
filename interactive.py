pets = []

name = input("What is your name? :")
age = input(f"Hello there {name}! How old are you? :")
pet = input("Do you have any pets? ")

if pet in ['y', 'Y', 'yes', 'yep', 'for sure', 'totally']:
    pet_name = input("What is his/her name:")
    pets.append(pet_name)
    print(f"{name} has a pet")
else:
    print(f"{name} doesn't have a pet😆")

