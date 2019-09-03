import random
def healf():
    return random.randint(1, 10)
def attack(n):
    return random.randint(1, n)
def protection(n):
    return random.randint(1, n)
def drag_act():
    foo = ['Attac','Prot']
    return random.choice(foo)