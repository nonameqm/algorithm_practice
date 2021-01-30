#include <iostream>

int main(){
    using namespace std;
    int rats=101;

    //참조는 만들때 반드시 초기화를 해야하고 일단 어떤 특정 변수에 연결되면 그것을 고수해야한다.
    //참조는 대입문이 아니라 초기화 선언에 의해서만 설정 가능함
    int& rodents=rats; // int * const pr=&rats;
    int* rats_point=&rats;

    cout << " rats = " << rats;
    cout <<", rodents = " << rodents; 
    cout <<", rats_point= " << *rats_point << endl;
    rodents++;
    cout << " rats = " << rats;
    cout <<", rodents = " << rodents;
    cout <<", rats_point= " << *rats_point << endl;

    cout << "rat address " << &rats << endl;
    std::cout <<"rodents address "<< &rodents << std::endl;    
    std::cout <<"rats_point address "<< rats_point << std::endl;    


    return 0;
}