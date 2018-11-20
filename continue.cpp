#include <iostream>
using namespace std;

int main()
{
	long dividend, divisor;
	char ch;
	do 
	{
		cout << "Enter dividend: "; cin >> dividend;
		cout << "Enter divisor: "; cin >> divisor;
		if (divisor == 0)
		{
			cout << "Error!\n";
			continue;
		}
		cout << "Chastnoe ravno " << dividend / divisor;
		cout << ", ostatok " << dividend % divisor;
		cout << "\nAgain?(y/n); ";
		cin >> ch;
	} 
	while (ch != 'n');
	return 0;
}