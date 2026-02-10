class sports_equipment:
    def __init__(self,id,title,type,material,weight,size,price,condition,instock):
        self.id=id
        self.title=title
        self.type=type
        self.material=material
        self.weight=weight
        self.size=size
        self.price=price
        self.condition=condition
        self.instock=instock
all_inventory=[]
def add_inventory(all_inventory):
    otv=input("Хотите добавить инвентарь?(да/нет): ")
    while otv=='да':
         existing_ids = {c.id for c in all_inventory}
         while True:
          id = int(input("Введите ID устройства: "))
          if id not in existing_ids:
           break
          else:
           print("Такой ID уже есть! Введите другой.")
         title=input("Введите название инвентаря: ")
         type=input("Введите вид спорта: ")
         material=input("Введите материал инвентаря: ")
         weight=int(input("Введите вес инвентаря(кг): "))
         size=int(input("Введите длину инвентаря(см): "))
         price=int(input("Введите цену инвентаря: "))
         condition=input("Введите состояние инвентаря(новый/не указано/старый): ")
         instock=int(input("Введите кол-во штук в наличии: "))
         new_inventory=sports_equipment(id=id,title=title,type=type,material=material,weight=weight,size=size,price=price,condition=condition,instock=instock)
         all_inventory.append(new_inventory)
         print(f"Устройство {title} успешно добавлено")
         otv=input("Хотите добавить инвентарь?(да/нет): ")
    
#поиск по характеристикам
def search_for_inventory(all_inventory):
   a=input("Введите вид спорта: ")
   b=int(input("Введите минимальный вес: "))
   v=int(input("Введите максимальный вес: "))
   for c in all_inventory:
    values=[c.type, c.weight]
    if a in values and b<=c.weight and v>=c.weight:
       print(f'Инвентарь найден. Характеристики: {c.id}, {c.title}, {c.type}, {c.material}, {c.weight}, {c.size}, {c.price}, {c.condition}, {c.instock}')
    else:
     print("Устройство не найдено")
#сортировка
def sort_i(all_inventory):
   all_inventory.sort(key=lambda c: c.instock, reverse=True)
   print("Сортировка по кол-ву на складе(по убыванию): ")
   for c in all_inventory: 
    print(f"Название: {c.title}")
    print(f"Вид спорта: {c.type}")
    print(f"Материал: {c.material}")
    print(f"Вес: {c.weight}")
    print(f"Размер: {c.size}")
    print(f"Состояние: {c.condition}")
    print(f"В наличии: {c.instock}")
    print("___________________________________")
def sort_i2(all_inventory):
    all_inventory.sort(key=lambda c: c.price)
    print("Сортировка по цене: ")
    for c in all_inventory: 
     print(f"Название: {c.title}")
     print(f"Вид спорта: {c.type}")
     print(f"Материал: {c.material}")
     print(f"Вес: {c.weight}")
     print(f"Размер: {c.size}")
     print(f"Состояние: {c.condition}")
     print(f"В наличии: {c.instock}")
     print("___________________________________")
#вывод новых
def show_new(all_inventory):
   for c in all_inventory:
      if c.condition=='новый':
         print(f"Новый инвентарь: {c.title}")
#изменить кол-во на складе
def change_the_quantity(all_inventory):
   a=int(input("введите id инвенторя: "))
   for c in all_inventory:
    values=[c.id]
    if a in values:
       otv=int(input(f"Инвентарь '{c.title}' найден. Введите новое кол-во на складе: "))
       c.instock=otv
       print(f"Кол-во инвентаря {c.title} изменено. Новое кол-во: {c.instock}")
#общ стоимость
def find_out_the_price(all_inventory):
 num=0
 for c in all_inventory:
   num=num=c.price
 print(f"общая стоимость инвентаря: {num}")
#пометить на починку
def mark_inventory(all_inventory):
   for c in all_inventory:
     if c.condition!='новый':
       c.condition='требует ремонта'
       print(f"Инвентарь {c.title} помечен, как 'требует ремонта'")
#больший вес
def find_max(all_inventory):
  spis=[]
  for c in all_inventory:
    spis.append(c.weight)
  maxweight=max(spis)
  print(f"Самый тяжелый инвентарь: {c.title}. Вес: {maxweight}")

#в наличии
def delete_inventory(all_inventory):
  for c in all_inventory:
    if c.instock==0:
      all_inventory.remove(c)
      print(f"Инвентарь '{c.title}' удален")
    else:
      print("Нет отсутствующего инвентаря")


def menu():
  print("Для начала добавьте инвентарь")
  add_inventory(all_inventory)
  ot=input("Открыть меню?(да/нет)")
  while ot=='да':
     print("________________________________________________________")
     print("МЕНЮ УПРАВЛЕНИЯ")
     print('1.Добавить новый инвентарь')
     print('2.Поиск инвентаря по характеристикам')
     print('3.Сортировка инвентаря')
     print('4.Вывод "нового" инвентаря')
     print('5.Изменить кол-во инвентаря на складе')
     print('6.Рассчитать общую стоимость инвентаря')
     print('7.Пометить не новый инвентарь, как "требует ремонта"')
     print('8.Найти самый тяжелый инвентарь')
     print('9.Удалить отсутствующий инвентарь из списка')
     print("________________________________________________________")
     otv=int(input("Выберите действие: "))
     if otv==1:
      add_inventory(all_inventory)
     elif otv==2:
      search_for_inventory(all_inventory)
     elif otv==3:
      sort_i(all_inventory)
      sort_i2(all_inventory)
     elif otv==4:
      show_new(all_inventory)
     elif otv==5:
      change_the_quantity(all_inventory)
     elif otv==6:
      find_out_the_price(all_inventory)
     elif otv==7:
      mark_inventory(all_inventory)
     elif otv==8:
      find_max(all_inventory)
     elif otv==9:
      delete_inventory(all_inventory)
     ot=input("Открыть меню?(да/нет)")

menu()