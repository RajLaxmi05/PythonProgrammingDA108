while True:
    mass = input("Enter the mass: ")
    if mass == "q":
       print("Exit")
       break
    c = 300
    E = float(mass)*c*c
    print("The energy is: ",E, 'Joules')
