from character_builder import ConcreteCharacterBuilder, CharacterDirector
import sys

def main():
    builder = ConcreteCharacterBuilder()
    director = CharacterDirector(builder)

    while True:
        print("\nRPG Character Builder")
        print("1. Create a Custom Character")
        print("2. Create a Pre-existing Character")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            character = create_custom_character(builder)
            character.describe()
            save_character(character)

        elif choice == "2":
            print("1. Create a Warrior")
            print("2. Create a Mage")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                director.create_warrior()
                character = builder.get_result()
                character.describe()
                save_character(character)

            elif choice == "2":
                director.create_mage()
                character = builder.get_result()
                character.describe()
                save_character(character)

            elif choice == "3":
                print("Exit RPG Character Builder.")
                sys.exit()
        
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exit RPG Character Builder.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

def create_custom_character(builder):
    builder.set_race(input("Enter character race: "))
    builder.set_class(input("Enter character class: "))

    while True:
        skill = input("Add a skill (or press Enter to finish): ")
        if not skill:
            break
        builder.add_skill(skill)

    while True:
        weapon = input("Add a weapon (or press Enter to finish): ")
        if not weapon:
            break
        builder.add_weapon(weapon)

    armor = input("Enter armor type: ")
    builder.set_armor(armor)

    return builder.get_result()

def save_character(character):
    save = input("Do you want to save this character? (yes/no): ").lower()
    if save == "yes":
        filename = input("Enter filename (e.g., warrior.json): ")
        character.save_to_file(filename)
    elif save == "no":
        print("Exit RPG Character Builder.")
        sys.exit()
    else:
        print("Invalid input. Returning to the main menu.")

if __name__ == "__main__":
    main()