#include <iostream>
using namespace std;
#include <conio.h>

int main()
{
	int x = 10, y = 10;
	char dir = 'a';
	while (dir != '\r')
	{
		cout << "\nYour coord: " << x << ", " << y;
		cout << "\nEnter path (n,s,e,w): ";
		dir = _getche();
		switch (dir) 
		{
			case 'n':y--; break;
			case 's':y++; break;
			case 'e':x++; break;
			case 'w':x--; break;
			case '\r':cout << "Exit..\n"; break;
			default: cout << "Again\n";
		}
	}
	return 0;
}