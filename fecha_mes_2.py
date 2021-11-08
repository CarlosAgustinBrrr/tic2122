def fecha_mes():
    fecha=raw_input("Introduce la fecha (dd/mm/aa): ")
    nombres_meses="Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre"
    me_elegido=
    print("Numer mes"+str(mes_elegido))
    numero_comas=0
    cont=0
    while(cont<=mes_elegido-1):
        if(nombre_meses[cont]==','):
            numero_comas=numero_comas+1
        cont=cont+1
    print(cont)
   
fecha_mes()
