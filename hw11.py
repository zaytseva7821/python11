# Задача 1. Постройте график функции f(x)=5x^2+10x−30
# По графику определите, при каких значения x значение функции отрицательно.

 

def quadratic_plot(a, b, c):
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.subplots()
    x0 = -b/(2*a)
    x = np.linspace(x0-5, x0+5, 100)
    y = a*(x**2)+b*x+c
    plt.plot(x, y)
    y1 = 0 * x
    x1 = np.linspace( x0-5, x0+5, 100)
    plt.plot(x1, y1)
    plt.show() 
    discr= b**2-4*a*c
    if discr > 0:
        import math
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        list_x = sorted([round(x1,2), round(x2,2)])
        print(list_x)
        print(f"x1 = {x1} \nx2 = {x2}")
        if a > 0:
            print(f"Значения функции отрицательны при значениях x от {list_x[0]} до {list_x[1]}")
        else:
            print(f"Значения функции отрицательны при значениях x от -∞ до {list_x[0]} и от {list_x[1]} до +∞")
    elif discr == 0:
        x = -b / (2 * a)
        if a > 0:
            print(f"нет отрицательных значений функций")
        else:
            print(f"Значения функции отрицательны при значениях x от -∞ до {x} и от {x} до +∞")
    else:
        if a > 0:
            print(f"Значения функции всегда положительны")
        else:
            print(f"Значения функции отрицательны при значениях x от -∞ до +∞")

quadratic_plot(5, 10, -30)



# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и 
# список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
def check_apartments(quantity,affordable_price):
    import random
    import numpy as np
    import matplotlib.pyplot as plt

    square_list = [random.randint(100, 300) for i in range(quantity)]
    price_list = [random.randint(3000000, 20000000) for i in range(quantity)]
    price_per_meter = [round(price_list[i]/square_list[i],2) for i in range(len(square_list))]
    print("Площадь,\nкв.м;   цена, руб;  цена за кв.м")
    for i in range(len(square_list)):
        print(f"{square_list[i]}    {price_list[i]}   {price_per_meter[i]}")
    apartment_list = dict()
    affordable_apartment = []
    for i in range(len(price_per_meter)):
        if price_per_meter[i]<affordable_price:
            apartment_list[square_list[i]] = price_list[i]
            affordable_apartment.append(price_per_meter[i])
        else:
            affordable_apartment.append(0)
    list_x = list(range(1,16))
    x1 = list_x
    y1 = price_per_meter
    x2 = list_x
    y2 = affordable_apartment

    fig, ax = plt.subplots()
    ax.bar(x1, y1,linewidth=0.5, width=0.98)
    ax.bar(x2, y2, linewidth=0.5, width=0.98)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    plt.xticks(list_x)
    ax.grid(True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2) 
    rects = ax.patches
    for rect, label in zip(rects, price_per_meter):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom")

    plt.show()
    print(sorted(apartment_list.items()))

# check_apartments(15, 50000)