def palabra():
    nombre=raw_input("NOMBRE: ")
    apellido=raw_input("APELLIDO: ")
    print("Buenos dias, "+nombre +" "+ apellido)
    print("Tu lindo nombre empiezapor la letra "+nombre[0])
    print("Voy a deletrear tu nombre")
    for cont in range (0,21):
        print(nombre[cont])
   
    
palabra()
