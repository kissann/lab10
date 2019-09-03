#Задача 1
#Реалізуйте текстову гру битви героя із драконом. Герой має ім'я, яке вводиться з клавіатури. Кількість здоров'я задається програмно.
# Рівень атаки (числове значення) задається програмно. Рівень захисту (числове значення) задається програмно.
#Аналогічні параметри має дракон, ім'я дракону задається автоматично.
import t1
import math
name=input("Введите имя героя")
heroes={}
dragon={}
battle={}
heroes['name']=name
heroes['healf'] = int(t1.healf())
dragon['healf'] = int(t1.healf())
heroes['attac']=t1.attack(10)
dragon['attac'] = t1.attack(10)
dragon['protect'] = t1.protection(10)
heroes['protect'] = t1.protection(10)
round=min(dragon['healf'],heroes['healf'])
dragon['name']='Drogo'
round=1
print("Жизнь героя "+str(heroes['healf']))
flag=True
while flag:
    if (dragon['healf']>0) or (heroes['healf']>0):
        print("Раунд"+str(round)+"\n")
        battle['her_a']=t1.attack(heroes['attac'])
        battle['drag_a'] = t1.attack(dragon['attac'])
        battle['her_pr'] = t1.attack(heroes['protect'])
        battle['drag_pr'] = t1.attack(dragon['protect'])
        act_h=input("Ваши действия герой? (Attac, Prot)")
        act_d=t1.drag_act()
        if(act_h=='Attac' and act_d=='Attac'):
            print("Дракон тоже атакует")
            dragon['healf']=dragon['healf'] -battle['her_a']/2
            heroes['healf'] = heroes['healf'] - battle['drag_a'] / 2
        if(act_h=='Prot' and act_d=='Prot'):
            print("Дракон тоже выбрал стратегию защиты")
        if (act_h == 'Attac' and act_d == 'Prot'):
            print("Дракон решил защитится")
            if battle['her_a']>battle['drag_pr']:
                yron=battle['her_a']-battle['drag_pr']
            if battle['her_a']<battle['drag_pr']:
                yron=0
            dragon['healf'] =dragon['healf']-yron
        if (act_h == 'Prot' and act_d == 'Attac'):
            print("Дракон атакует")
            if battle['drag_a'] > battle['her_pr']:
                yron = battle['her_a'] - battle['drag_pr']
            if battle['drag_a'] < battle['her_pr']:
                yron = 0
            heroes['healf'] = heroes['healf'] - yron
        if (dragon['healf']<=0):
            print("Игра закончена Дракон сдох")
            flag=False
        if (heroes['healf']<=0):
            print("Игра закончена Герой сдох")
            flag=False
        round=round+1
    print(heroes)
    print(dragon)
