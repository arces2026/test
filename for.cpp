#include <iostream>
#include <stdlib.h>
#include <iomanip>
using namespace std;
int main ()
{
	system ("color 0b");
	int unnome[9],dim,cont;
	unnome[0]==2;
	unnome[1]==3;
	unnome[2]==4;
	unnome[3]==5;
	unnome[4]==6;
	unnome[5]==7;
	unnome[6]==8;
	unnome[7]==9;
	unnome[8]==10;
	cout<<unnome[3];
	for(dim=0;dim<9;dim++)
	{
		cout<<"posizione unnome"<<dim<<"  :  ";                //Fase di caricamento dell vettore
		cin>>unnome[dim]; 
	}
	for (dim=0;dim<9;dim++)
	{
		cout<<endl;
		cout<<"posizione unnome 0"<<dim<<" :  "<<unnome[dim]<<endl;  //fase din visualizzazione del vettore
	}
		cout<<endl<<"numeri maggiori di cinque :"<<cont<<endl;
	for(dim=0;dim<9;dim++)
	{
		if(unnome[dim]>5)
		{
			cout<<endl;
			cont++;
			cout<<endl<<unnome[dim]<<endl;
			cout<<setw(4)<<unnome[dim];                             //Visualizzazione di un numero maggiore di 5
		}
	}
	cout<<cont;
	cout<<endl;
	system ("pause");
	return 0;
}
