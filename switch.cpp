#include <iostream>
using namespace std;

int main()
{
	int speed;
	cout << "Enter 33, 45 or 78:";
	cin >> speed;
	switch (speed)
	{
		case 33:
			cout << "longplay";
			break;
		case 45:
			cout << "single";
			break;
		case 78:
			cout << "old format";
			break;
	}
	return 0;
}

//��� ��������, ������������� � ���������� case, ������ ��������� � ����� ����������, ������� � ������� ��������� switch.