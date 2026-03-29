import random

class Pet:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
        self.hunger = random.randint(1, 10)
        self.happiness = random.randint(1, 10)
        self.health = random.randint(1, 10)
        min_satiety = 1
    max_satiety = 10
    min_mood = 1
    max_mood = 10
    min_health = 1
    max_health = 10
    all_pets = []
    dead_pets=[]

    def feed(self):
        self.hanger+=2
        if self.hunger < 1:
            self.hunger = 1
        print(f"{self.name} поел. Голод: {self.hunger}")

    def play(self):
      max_health = 10
      min_health = 1
      max_mood = 10
      min_mood = 1

      print("Во что хотите сыграть с питомцем?:")
      print("1. Выучить новую команду")
      print("2. Догонялки")
      print("3. Апорт")
      print("4. Перетягивание")
      print("5. Погулять с другими питомцами")

      otv = int(input("Введите номер игры: "))

      if otv == 1:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец выучил новую команду и стал умнее!")
            fun_amount = random.randint(1, max_mood - self.happiness)
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
            self.health += 1
            print('Здоровье +1')
        elif event == 2:
            print("Питомец сильно устал и не хочет больше играть")
            fun_amount = random.randint(1, max(1, max_mood - self.happiness))
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
            self.health -= 1
            print('Здоровье -1')
            if self.health < min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        else:  # event == 3
            print("Питомец запутался в командах и расстроился")
            self.happiness -= 1
            print("Счастье -1")
            if self.happiness < min_mood:
                self.happiness = min_mood

      elif otv == 2:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец упал и ударился")
            hel = random.randint(1, 2)
            self.health -= hel
            self.happiness -= 1
            print("Счастье -1")
            print(f"Здоровье -{hel}")
            if self.health < min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        elif event == 2:
            print("Питомец догнал вас и очень обрадовался!")
            fun_amount = random.randint(1, max_mood - self.happiness)
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
            if self.health < max_health:
                self.health += 1
                print('Здоровье +1')
        else:  # event == 3
            print("Питомец пробежал большое расстояние и стал сильнее")
            fun_amount = random.randint(1, max_mood - self.happiness)
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
            if self.health < max_health:
                hel = random.randint(1, 2)
                self.health += hel
                print(f'Здоровье +{hel}')

      elif otv == 3:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец ловко поймал предмет и принёс его!")
            fun_amount = random.randint(2, 3)
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
        elif event == 2:
            print("Питомец потерял предмет и расстроился")
            self.happiness -= 2
            print("Счастье -2")
            if self.happiness < min_mood:
                self.happiness = min_mood
        else:  # event == 3
            print("Питомец перепутал команды и принёс не тот предмет")
            self.happiness += 1
            print("Счастье +1")

      elif otv == 4:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец победил в перетягивании!")
            fun_amount = random.randint(1, 2)
            self.happiness += fun_amount
            self.health += 1
            print(f"Счастье +{fun_amount}, Здоровье +1")
        elif event == 2:
            print("Питомец устал от борьбы")
            self.health -= 1
            self.happiness -= 1
            print("Здоровье -1, Счастье -1")
            if self.health < min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        else:  # event == 3
            print("Игра закончилась вничью — все довольны!")
            self.happiness += 1
            print("Счастье +1")

      elif otv == 5:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец подружился с другими животными!")
            fun_amount = random.randint(2, 3)
            self.happiness += fun_amount
            print(f"Счастье +{fun_amount}")
        elif event == 2:
            print("Питомец испугался большой собаки")
            self.happiness -= 2
            print("Счастье -2")
            if self.happiness < min_mood:
                self.happiness = min_mood
        else:  # event == 3
            print("Прогулка прошла спокойно, питомец отдохнул")
            self.health += 1
            print("Здоровье +1")

  
    def check_status(self):
        print(f"\n--- {self.name} ---")
        print(f"Тип: {self.type}")
        print(f"Возраст: {self.age}")
        print(f"Голод: {self.hunger}/10 ")
        print(f"Счастье: {self.happiness}/10")
        print(f"Здоровье: {self.health}/10")

class Shelter:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"Питомец {pet.name} добавлен в приют {self.name}")

    def show_pets(self):
        print(f"\nПитомцы приюта '{self.name}':")
        if not self.pets:
            print("В приюте пока нет питомцев.")
        else:
            for pet in self.pets:
                print(f"- {pet.name} ({pet.type}), возраст: {pet.age}")

    def find_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

class Volunteer:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, shelter, pet_name):
        pet = shelter.find_pet(pet_name)
        if pet:
            pet.feed()
        else:
            print("Питомец не найден!")

    def play_with_pet(self, shelter, pet_name):
        pet = shelter.find_pet(pet_name)
        if pet:
            pet.play()
        else:
            print("Питомец не найден!")

    def check_pet_status(self, shelter, pet_name):
        pet = shelter.find_pet(pet_name)
        if pet:
            pet.check_status()
        else:
            print("Питомец не найден!")

def main():
   
    shelter_name = input("Введите название приюта для животных: ")
    shelter = Shelter(shelter_name)

   
    volunteers = []

    print(f"\nПриют '{shelter_name}' создан! Теперь добавьте первого волонтёра.")


    first_volunteer_name = input("Введите имя первого волонтёра: ")
    volunteers.append(Volunteer(first_volunteer_name))
    print(f"Волонтёр {first_volunteer_name} добавлен!\n")

    while True:
        print(f"\n=== ПРИЮТ '{shelter.name}' ===")
        print("1. Добавить питомца")
        print("2. Показать всех питомцев")
        print("3. Добавить волонтёра")
        print("4. Показать всех волонтёров")
        print("5. Покормить питомца")
        print("6. Поиграть с питомцем")
        print("7. Проверить статус питомца")
        print("8. Выход")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            name = input("Имя питомца: ")
            type = input("Тип питомца: ")
            age = int(input("Возраст: "))
            new_pet = Pet(name, type, age)
            shelter.add_pet(new_pet)

        elif choice == "2":
            shelter.show_pets()

        elif choice == "3":
            volunteer_name = input("Имя нового волонтёра: ")
            volunteers.append(Volunteer(volunteer_name))
            print(f"Волонтёр {volunteer_name} добавлен!")

        elif choice == "4":
            print("\nСписок волонтёров:")
            counter = 1
            for volunteer in volunteers:
                print(f"{counter}. {volunteer.name}")
                counter += 1

        elif choice == "5":

            print("\nВыберите волонтёра:")
            counter = 1
            for volunteer in volunteers:
                print(f"{counter}. {volunteer.name}")
                counter += 1
            vol_num = int(input("Номер волонтёра: ")) - 1
          
            if 0 <= vol_num < len(volunteers):
                selected_volunteer = volunteers[vol_num]
                pet_name = input("Имя питомца: ")
                selected_volunteer.feed_pet(shelter, pet_name)
            else:
                print("Неверный номер волонтёра!")


        elif choice == "6":
            
            print("\nВыберите волонтёра:")
            counter = 1
            for volunteer in volunteers:
                print(f"{counter}. {volunteer.name}")
                counter += 1
            vol_num = int(input("Номер волонтёра: ")) - 1

            if 0 <= vol_num < len(volunteers):
                selected_volunteer = volunteers[vol_num]
                pet_name = input("Имя питомца: ")
                selected_volunteer.play_with_pet(shelter, pet_name)
            else:
                print("Неверный номер волонтёра!")


        elif choice == "7":
     
            print("\nВыберите волонтёра:")
            counter = 1
            for volunteer in volunteers:
                print(f"{counter}. {volunteer.name}")
                counter += 1
            vol_num = int(input("Номер волонтёра: ")) - 1
       
            if 0 <= vol_num < len(volunteers):
                selected_volunteer = volunteers[vol_num]
                pet_name = input("Имя питомца: ")
                selected_volunteer.check_pet_status(shelter, pet_name)
            else:
                print("Неверный номер волонтёра!")

        elif choice == "8":
            print("До свидания!")
            break

if __name__ == "__main__":
    main()
