#include<stdio.h>

int main(){
	char letras[10];
	int cont;
		
	//for cont in range (1,10);
	//cont++ equivale a cont=cont+1
	/*while(cont<=10){
	...
	cont++*/
	//Leo datos del teclado
	for(cont=0;cont<10;cont++){
		//num=input("dame un numero: ")//	
		printf("Introduce la letra %d: ",cont);
		scanf("%c",&letras[cont]);
	}
	//Escribo datos en la pantalla
	print("\nHAS ESCRITO LA PALABRA: ");
	for(cont=0;cont<10;cont++){
		printf("%c",letras[cont]);
		
	}
	
	
	
	return(0);
			
}	
