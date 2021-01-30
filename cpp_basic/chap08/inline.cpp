#include <iostream>

inline double square(double x){
    return x*x;
}

int main(){
    using namespace std;
    double a, b;
    double c=13.0;

    cout << square(c++) << endl;
    cout << c << endl;
    return 0;
}