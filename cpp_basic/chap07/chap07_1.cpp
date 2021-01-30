#include <iostream>

char* buildstr(char c, int n); //function prototype

int main(){
    using namespace std;
    int times;
    char ch;

    cin >> ch;
    cin >> times;

    char *ps=buildstr(ch, times);

    cout << ps << endl;
    delete [] ps; // 메모리 해제

    ps=buildstr('+', 20);
    cout << ps << "-DONE-" << ps << endl;
    delete[] ps;

    return 0;
}

char* buildstr(char c, int n){
    char* pstr=new char[n+1];
    pstr[n]='\0'; //문자열 종결
    while(n-- > 0){
        pstr[n]=c;
    }
    return pstr;
}