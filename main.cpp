#include <iostream>
using namespace std;
#include <conio.h>

int main()
{
	char dir = 'a';
	int x = 10, y = 10;
	cout << "Press Enter to exit..\n";

	while (dir != '\r')
	{
		cout << "\n Your coord: " << x << ", " << y;
		cout << "\n Enter new path (n,s,e,w): ";
		dir = _getche();
		if (dir == 'n')
			y--;
		else if (dir == 's')
			y++;
		else if (dir == 'e')
			x++;
		else if (dir == 'w')
			x--;
	}
	return 0;
}


