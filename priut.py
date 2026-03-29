import random

class Pet:
    min_satiety = 1
    max_satiety = 10
    min_mood = 1
    max_mood = 10
    min_health = 1
    max_health = 10
    all_pets = []
    dead_pets=[]
    def __init__(self, name, type, age, satiety, mood, health):
        self.name = name
        self.type = type
        self.age = age
        self.satiety = satiety
        self.mood = mood
        self.health = health

    def add_pet(self):
        name = input("Введите имя питомца: ")
        type = input("Введите тип питомца: ")
        age = int(input("Введите возраст питомца: "))

        satiety = random.randint(self.min_satiety + 1, self.max_satiety - 1)
        mood = random.randint(self.min_mood + 1, self.max_mood - 1)
        health = random.randint(self.min_health + 1, self.max_health - 1)

        new_pet = Pet(name, type, age, satiety, mood, health)
        Pet.all_pets.append(new_pet)

        print(f"Питомец {name} успешно добавлен!")
        return new_pet

#def get_health_bar(self):
    #full_hearts = self.health
   # empty_hearts = self.max_health - self.health

    #full = '❤️'   # красное сердце (Unicode эмодзи)
    #empty = '🤍'  # белое сердце (Unicode эмодзи)

    #bar = full * full_hearts + empty * empty_hearts
    #return f"[{bar}] {self.health}/{self.max_health} HP"

    #def get_satiety_bar(self):
       # food = '🍖'
      #  empty_plate = '🍽️'
      #  food_count = self.satiety
      #  plate_count = self.max_satiety - self.satiety
     #   bar = food * food_count + empty_plate * plate_count
     #   return f"Сытость: [{bar}] {self.satiety}/{self.max_satiety}"


     #def get_mood_bar(self):
    #happy = '😀'  # весёлый смайлик (с ртом)
    #sad = '😶'   # нейтральный смайлик (без рта)
  #  happy_count = self.mood
   # sad_count = self.max_mood - self.mood
  #  bar = happy * happy_count + sad * sad_count
   # return f"Настроение: [{bar}] {self.mood}/{self.max_mood}"


    def feed(self):
   
     food_amount = None
     while food_amount is None:
        try:
            food_amount_input = input("Сколько еды дать питомцу?: ")
            food_amount = int(food_amount_input)
            if food_amount <= 0:
                print("Количество еды должно быть положительным числом. Попробуйте снова.")
                food_amount = None
        except ValueError:
            print("Пожалуйста, введите целое число.")
            food_amount = None

     if self.satiety + food_amount > self.max_satiety:
        print(f"О нет! {self.name} переел и... умер. 😔")
        if self in Pet.all_pets:
            Pet.all_pets.remove(self)
            Pet.dead_pets.append(self)
     else:
        self.satiety += food_amount
        print(f"{self.name} поел. Сытость: {self.satiety}")


    def play(self):
     global max_health, min_health, max_mood, min_mood
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
            fun_amount = random.randint(1, max_mood - self.mood)
            self.mood += fun_amount
            print(f"Счастье +{fun_amount}")
            self.health += 1
            print('Здоровье +1')
        elif event == 2:
            print("Питомец сильно устал и не хочет больше играть")
            fun_amount = random.randint(1, max(1, max_mood - self.mood))
            self.mood += fun_amount
            print(f"Счастье +{fun_amount}")
            self.health -= 1
            print('Здоровье -1')
            if self.health < self.min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        else:  # event == 3
            print("Питомец запутался в командах и расстроился")
            self.mood -= 1
            print("Счастье -1")
            if self.mood < self.min_mood:
                self.mood = self.min_mood

     elif otv == 2:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец упал и ударился")
            hel = random.randint(1, 2)
            self.health -= hel
            self.mood -= 1
            print("Счастье -1")
            print(f"Здоровье -{hel}")
            if self.health < min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        elif event == 2:
            print("Питомец догнал вас и очень обрадовался!")
            fun_amount = random.randint(1, max_mood - self.mood)
            self.mood += fun_amount
            print(f"Счастье +{fun_amount}")
            if self.health < max_health:
                self.health += 1
                print('Здоровье +1')
        else:  # event == 3
            print("Питомец пробежал большое расстояние и стал сильнее")
            fun_amount = random.randint(1, max_mood - self.mood)
            self.mood += fun_amount
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
            self.mood += fun_amount
            print(f"Счастье +{fun_amount}")
        elif event == 2:
            print("Питомец потерял предмет и расстроился")
            self.mood -= 2
            print("Счастье -2")
            if self.mood < min_mood:
                self.mood = min_mood
        else:  # event == 3
            print("Питомец перепутал команды и принёс не тот предмет")
            self.mood += 1
            print("Счастье +1")

     elif otv == 4:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец победил в перетягивании!")
            fun_amount = random.randint(1, 2)
            self.mood += fun_amount
            self.health += 1
            print(f"Счастье +{fun_amount}, Здоровье +1")
        elif event == 2:
            print("Питомец устал от борьбы")
            self.health -= 1
            self.mood -= 1
            print("Здоровье -1, Счастье -1")
            if self.health < min_health:
                print(f"О нет! {self.name} ... умер. 😔")
                if self in Pet.all_pets:
                    Pet.all_pets.remove(self)
                    Pet.dead_pets.append(self)
        else:  # event == 3
            print("Игра закончилась вничью — все довольны!")
            self.mood += 1
            print("Счастье +1")

     elif otv == 5:
        event = random.randint(1, 3)
        if event == 1:
            print("Питомец подружился с другими животными!")
            fun_amount = random.randint(2, 3)
            self.mood += fun_amount
            print(f"Счастье +{fun_amount}")
        elif event == 2:
            print("Питомец испугался большой собаки")
            self.mood -= 2
            print("Счастье -2")
            if self.mood < min_mood:
                self.mood = min_mood
        else:  # event == 3
            print("Прогулка прошла спокойно, питомец отдохнул")
            self.health += 1
            print("Здоровье +1")
     else:
        print("Неверный номер игры. Выберите число от 1 до 5.")


def get_status(all_pets):
    print("Живые питомцы:")
    number = 1
    for pet in all_pets:
        print(f"{number}. {pet.name}")
        number += 1
    num = int(input("Введите номер питомца: ")) - 1
    pet = all_pets[num]
    print(f"--- {pet.name} ---")
    print(f"Тип: {pet.type}")
    print(f"Возраст: {pet.age}")
    print(f"Здоровье: {pet.health}/{pet.max_health}")
    print(f"Счастье: {pet.mood}/{pet.max_mood}")


def show_all_pets():
    if not Pet.all_pets:
        print("В приюте пока нет животных.")
        return
    print("--- Животные в приюте ---")
    for pet in Pet.all_pets:
        status = pet.get_status()
        print(f"{pet.name} ({pet.type}) — {status}")

def is_happy(self):
       
        if self.health < 70:
            print("Питомец несчастлив: здоровье ниже нормы.")
            return False
        if self.mood < 60:
            print("Питомец несчастлив: настроение ниже нормы.")
            return False
        if self.hunger > 40:
            print("Питомец несчастлив: голод выше нормы.")
            return False
        if self.energy < 50:
            print("Питомец несчастлив: энергия ниже нормы.")
            return False
        print("Питомец счастлив!")
        return True