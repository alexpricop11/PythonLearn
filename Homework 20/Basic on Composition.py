class Pet:
    def __init__(self, name, animal_type, favorite_food):
        self.name = name
        self.animal_type = animal_type.lower()  # Ensure valid type names
        self.favorite_food = favorite_food

    def __str__(self):
        return f"{self.animal_type.title()} called {self.name} that loves {self.favorite_food}"


class HumanWithPet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pets = []

    def adopt_new_pet(self, name, animal_type, favorite_food):
        new_pet = Pet(name, animal_type, favorite_food)
        self.pets.append(new_pet)
        print(f"{self.name} successfully adopted {new_pet}!")

    def give_away_pet(self, pet_name):
        pet_removed = False
        for pet in self.pets:
            if pet.name == pet_name:
                self.pets.remove(pet)
                pet_removed = True
                print(f"{self.name} gave away {pet_name} to a loving home.")
                break

        if not pet_removed:
            print(f"{self.name} doesn't have a pet named {pet_name} to give away.")

    def __str__(self):
        if not self.pets:
            return f"{self.name}, age {self.age} with no pets"
        elif len(self.pets) == 1:
            return f"{self.name}, age {self.age} with a pet: {self.pets[0]}"
        else:
            pet_info = ", ".join(str(pet) for pet in self.pets)
            return f"{self.name}, age {self.age} with {len(self.pets)} pets: {pet_info}"


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    human_with_pets = HumanWithPet(name, age)

    print(f"Welcome, {human_with_pets}!")

    while True:
        action = input("What do you want to do? (adopt/give away/quit): ")
        if action.lower() == 'adopt':
            pet_name = input("Enter pet's name: ")
            animal_type = input("Enter pet's type (dog/cat/bird): ")
            favorite_food = input("Enter pet's favorite food: ")
            human_with_pets.adopt_new_pet(pet_name, animal_type, favorite_food)
        elif action.lower() == 'give away':
            pet_name = input("Enter pet's name to give away: ")
            human_with_pets.give_away_pet(pet_name)
        elif action.lower() == 'quit':
            break
        else:
            print("Invalid action. Please try again.")

    print(f"Thank you for playing, {human_with_pets}!")
