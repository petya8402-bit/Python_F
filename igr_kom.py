all_computers=[]
class Comp:
    def __init__(self, name, ID, brand, processor, videocard, RAM, SSD, weight, price, instock):
        self.ID=ID
        self.name=name
        self.brand=brand
        self.processor=processor
        self.videocard=videocard
        self.RAM=RAM
        self.SSD=SSD
        self.weight=weight
        self.price=price
        self.instock=instock
#добавление компьютера
def add_comp():
 global all_computers
 otv=input("Хотите добавить новое устройство?(да/нет)")
 while otv=="да":
  existing_ids = {c.ID for c in all_computers}
  while True:
    ID = int(input("Введите ID устройства: "))
    if ID not in existing_ids:
        break
    else:
     print("Такой ID уже есть! Введите другой.")
  name=input("Введите название устройства: ")
  brand=input("Введите бренд устройства: ")
  processor=input("Введите название процессора: ")
  videocard=input("Введите название видеокарты: ")
  RAM=int(input("Введите ОЗУ устройства: "))
  SSD=int(input("Введите объем SSD: "))
  weight=int(input("Введите вес устройства(кг): "))
  price=int(input("Введите цену: "))
  instock=int(input("Введите кол-во устройств в наличии: "))
  new_comp=Comp(ID=ID,name=name,brand=brand,processor=processor,videocard=videocard,RAM=RAM,SSD=SSD,weight=weight,price=price,instock=instock)
  all_computers.append(new_comp)
  print(f"Устройство {name} успешно добавлено")
  otv=input("Хотите добавить новое устройство?(да/нет)")   
#список компьютеров
def spis_comp():
 global all_computers
 for c in all_computers:
   print(f'ID: {c.ID}')
   print(f'Name: {c.name}')
   print(f'Brand: {c.brand}')
   print(f'Processor: {c.processor}')
   print(f'Videocard: {c.videocard}')
   print(f'RAM: {c.RAM}')
   print(f'SSD: {c.SSD}')
   print(f'Weight: {c.weight}')
   print(f'Price: {c.price}')
   print(f'In stock: {c.instock}')
   print('_____________________________________')
#поиск компьютеров по нескольким условиям одновременно
def device_search():
 global all_computers
 otv=input("Хотите найти устройство?(да/нет): ")
 if otv=='да':
   A='a'
   B='b'
   char=input(f"Введите первую характеристику({A}): id/nm(name)/pr(processor)/br(brand)/vd(videocard)/rm(ОЗУ)/ss(SSD)wg(weight)/pc(price)/is(instock)) и вторую характеристику({B}): id/nm(name)/pr(processor)/br(brand)/vd(videocard)/rm(ОЗУ)/ss(SSD)wg(weight)/pc(price)/is(instock)): ")
   A,B=map(str, char.split())
   print(f"{A},{B}")
   if A=='id':
     a=int(input("Введите id устройства: "))
   elif A=='nm':
     a=input("Введите название устройста: ")
   elif A=='pr':
     a=input("Введите название процессора: ")
   elif A=='br':
     a=input("Введите бренд устройства: ")
   elif A=='vd':
     a=input("Введите мощность видеокарты: ")
   elif A=='rm':
     a=input("Введите ОЗУ устройства: ")
   elif A=='ss':
     a=input("Введите SSD устройства: ")
   elif A=='wg':
     a=input("Введите вес устройства: ")
   elif A=='pc':
     a=input("Введите цену устройства: ")
   elif A=='is':
     a=input("Введите количество устройств в наличии: ")
   
   if B=='id':
     b=int(input("Введите id устройства: "))
   elif B=='nm':
     b=input("Введите название устройста: ")
   elif B=='pr':
     b=input("Введите название процессора: ")
   elif B=='br':
     b=input("Введите бренд устройства: ")
   elif B=='vd':
     b=input("Введите мощность видеокарты: ")
   elif B=='rm':
     b=input("Введите ОЗУ устройства: ")
   elif B=='ss':
     b=input("Введите SSD устройства: ")
   elif B=='wg':
     b=input("Введите вес устройства: ")
   elif B=='pc':
     b=input("Введите цену устройства: ")
   elif B=='is':
     b=input("Введите количество устройств в наличии: ")
   for c in all_computers:
      values = [str(c.ID),c.name,c.brand,c.processor,c.videocard,str(c.RAM),str(c.SSD),str(c.weight),str(c.price),str(c.instock)
    ]

      if str(a) in values and str(b) in values:
       print(f'Устройство найдено: {c.name}, Характеристики: {c.brand}, {c.processor}, {c.videocard}, {c.RAM}, {c.weight},{c.price}, {c.instock}')
      else:
       print("Устройство не найдено")
#удаление из списка
def removal():
   global all_computers
   a=int(input("Введите id устройства: "))
   for c in all_computers:
     values = [str(c.ID),c.name,c.brand,c.processor,c.videocard,str(c.RAM),str(c.SSD),str(c.weight),str(c.price),str(c.instock)
    ]
     if str(a) in values:
      print(f'Устройство найдено: {c.name}, Характеристики: {c.brand}, {c.processor}, {c.videocard}, {c.RAM}, {c.weight},{c.price}, {c.instock}')
     otv=input('Удалить устройство из списка?(да/нет): ')
     if otv =='да':
       all_computers.remove(c)
       print("Устройство удалено")
       return all_computers
     else:
       return all_computers
#сортировка по характеристикам
def sorted():
  global all_computers
  all_computers.sort(key=lambda c: c.price) 
  print("Сортировка по цене: ")
  for c in all_computers:                    
    print(f"ID: {c.ID}")
    print(f"Name: {c.name}")
    print(f"Brand: {c.brand}")
    print(f"Processor: {c.processor}")
    print(f"Videocard: {c.videocard}")
    print(f"RAM: {c.RAM}")
    print(f"SSD: {c.SSD}")
    print(f"Weight: {c.weight}")
    print(f"Price: {c.price}")
    print(f"In stock: {c.instock}")
    print("_________")
  all_computers.sort(key=lambda c: c.RAM+c.SSD) 
  print("Сортировка по ОЗУ+SSD: ")
  for c in all_computers:                    
    print(f"ID: {c.ID}")
    print(f"Name: {c.name}")
    print(f"Brand: {c.brand}")
    print(f"Processor: {c.processor}")
    print(f"Videocard: {c.videocard}")
    print(f"RAM: {c.RAM}")
    print(f"SSD: {c.SSD}")
    print(f"Weight: {c.weight}")
    print(f"Price: {c.price}")
    print(f"In stock: {c.instock}")
    print("_________")
#увеличение объёма ОЗУ у компьютера по ИД
def RAM():
 global all_computers
 a=int(input("Введите id устройства: "))
 for c in all_computers:
  values = [str(c.ID),c.name,c.brand,c.processor,c.videocard,str(c.RAM),str(c.SSD),str(c.weight),str(c.price),str(c.instock)
    ]
  if str(a) in values:
   print(f'Устройство найдено: {c.name}, Характеристики: {c.brand}, {c.processor}, {c.videocard}, {c.RAM}, {c.weight},{c.price}, {c.instock}')
   RAM=int(input("Введите новое значение ОЗУ: "))
   c.RAM=RAM
   print(f'Обновленные Характеристики: {c.name}, {c.brand}, {c.processor}, {c.videocard}, {c.RAM}, {c.weight},{c.price}, {c.instock}')
 return all_computers
#сделать скидку
def price():
   global all_computers
   a=int(input("Введите id устройства: "))
   for c in all_computers:
    values = [str(c.ID),c.name,c.brand,c.processor,c.videocard,str(c.RAM),str(c.SSD),str(c.weight),str(c.price),str(c.instock)
    ]
    if str(a) in values:
      c.price=c.price*0.9
      print(f"Цена устройства {c.name} успешно снижена на 10%. Новая цена: {c.price}")
   return all_computers
#самый дорогой и дешевый
def max_min_price():
 global all_computers
 all_computers.sort(key=lambda c: c.price) 
 comp1=all_computers[0]
 comp2=all_computers[-1]
 print(f"Самый дорогой компьютер: {comp2.name}. Его цена: {comp2.price} ")
 print(f"Самый дешевый компьютер: {comp1.name}. Его цена: {comp1.price} ")
 return all_computers
#вывести компьютеры с видеокартой не слабее указанной
def videocard():
  power=int(input("Введите нужную мощность видеокарты: "))
  for c in all_computers:
    values = [str(c.ID),c.name,c.brand,c.processor,c.videocard,str(c.RAM),str(c.SSD),str(c.weight),str(c.price),str(c.instock)
    ]
    if power>=c.videocard:
       print(f'Устройство найдено: {c.name}, Характеристики: {c.brand}, {c.processor}, {c.videocard}, {c.RAM}, {c.weight},{c.price}, {c.instock}')
  return all_computers

def menu():
    print("Для начала добавьте устройства")
    add_comp()
    otv=input("Открыть меню?(да/нет)")
    while otv=='да':
        print(" МЕНЮ УПРАВЛЕНИЯ СКЛАДОМ ПК")
        print("1. Показать все устройства(только после добавления)")
        print("2. Поиск по 2-ум характеристикам")
        print("3. Сортировать по цене, сумме ОЗУ + SSD")
        print("4. Добавить новый ПК")
        print("5. Удалить ПК по ID")
        print("6. Увеличить ОЗУ по ID")
        print("7. Установить 'Распродажу' (-10%)")
        print("8. Показать самый дорогой и дешевый ПК")
        choice = int(input("Выберите действие: "))
        if choice==1:
          print(spis_comp())
        elif choice==2:
         print(device_search())
        elif choice==3:
          print(sorted())
        elif choice==4:
          print(add_comp())
        elif choice==5:
          print(removal())
        elif choice==6:
          print(RAM())
        elif choice==7:
          print(price())
        elif choice==8:
          print(max_min_price())
        otv=input("Открыть меню?(да/нет)")
menu()