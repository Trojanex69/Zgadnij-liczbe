import random
proby = 0
liczba = 0
wybor = 0
strzal = 0
print('Witaj w grze "Zgadnij liczbę". Wybierz poziom trudności:')
print('[1]-łatwy, [2]-średni [3]-trudny')
wybor = input()
if wybor == "1":
    proby += 7
    liczba = random.randint(1, 10)
    strzal = int(input("Zatem zgadnij liczbę od 1 do 10: "))
    while proby != 0:
        if strzal == liczba:
            print("Zgadłeś! Gra wygrana")
            break
        else:
            proby -= 1
            if strzal > liczba:
                print("Pudło! Podałeś za dużą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 10: "))
            elif strzal < liczba:
                print("Pudło! Podałeś za małą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 10: "))
    if proby <= 0:
        print("Game over! Liczba była: "+str(liczba))
elif wybor == "2":
    proby += 7
    liczba = random.randint(1, 30)
    strzal = int(input("Zatem zgadnij liczbę od 1 do 30: "))
    while proby != 0:
        if strzal == liczba:
            print("Zgadłeś! Gra wygrana")
            break
        else:
            proby -= 1
            if strzal > liczba:
                print("Pudło! Podałeś za dużą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 30: "))
            elif strzal < liczba:
                print("Pudło! Podałeś za małą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 30: "))
    if proby <= 0:
        print("Game over! Liczba była: " + str(liczba))
elif wybor == "3":
    proby += 5
    liczba = random.randint(1, 100)
    strzal = int(input("Zatem zgadnij liczbę od 1 do 100: "))
    while proby != 0:
        if strzal == liczba:
            print("Zgadłeś! Gra wygrana")
            break
        else:
            proby -= 1
            if strzal > liczba:
                print("Pudło! Podałeś za dużą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 100: "))
            elif strzal < liczba:
                print("Pudło! Podałeś za małą liczbę. Pozostałcyh prób: " + str(proby))
                strzal = int(input("Zgadnij liczbę od 1 do 100: "))
    if proby <= 0:
        print("Game over! Liczba była: " + str(liczba))
else:
    print("Złe dane")

