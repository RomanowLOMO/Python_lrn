#include <iostream>
using namespace std;
#include <conio.h>

int main()
{
	const unsigned char WHITE = 219;
	const unsigned char GRAY = 176;
	unsigned char ch;

	for (int count = 0; count < 80 * 25 - 1; count++)
	{
		ch = WHITE; //предполагаем, что число простое
		for (int j = 2; j < count; j++) // делим на каждое целое, большее 2
			if (count % j == 0) // если остаток равен 0,
			{
				ch = GRAY; // то число не простое
				break; // выход из внутреннего цикла
			}
		cout << ch; // вывод символа на экран
	}
	_getch(); // задержка полученного изображени€
	return 0;
}