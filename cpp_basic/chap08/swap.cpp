#include <iostream>

void swapr(int &a, int &b);
void swapp(int *p, int *q);
void swapv(int a, int b);

int main()
{
    using namespace std;
    int wallet1 = 3000;
    int wallet2 = 5000;

    std::cout << "wallet 1 : " << wallet1 << std::endl;
    std::cout << "wallet 2 : " << wallet2 << std::endl;

    cout << "swap by reference" << endl;
    swapr(wallet1, wallet2);
    std::cout << "wallet 1 : " << wallet1 << std::endl;
    std::cout << "wallet 2 : " << wallet2 << std::endl;

    cout << "swap by pointer" << endl;
    swapp(&wallet1, &wallet2);
    std::cout << "wallet 1 : " << wallet1 << std::endl;
    std::cout << "wallet 2 : " << wallet2 << std::endl;

    cout << "swap by value" << endl;
    swapv(wallet1, wallet2);
    std::cout << "wallet 1 : " << wallet1 << std::endl;
    std::cout << "wallet 2 : " << wallet2 << std::endl;

}

void swapr(int &a, int &b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void swapp(int *p, int *q)
{
    int temp;
    temp = *p;
    *p = *q;
    *q = temp;
}

void swapv(int a, int b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}