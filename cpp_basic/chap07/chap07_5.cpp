#include <iostream>
double gildong(int);
double moonsoo(int);

// second parameter is a pointer of function that takes int as a parmeter and double as a return value
void estimate(int lines, double (*pf) (int));

int main(){
    using namespace std;
    int code;

    cout << "input the number of lines needed : ";
    cin >> code;
    cout << "gildong" << endl;
    estimate(code, gildong);
    cout << "moonsoo" << endl;
    estimate(code, moonsoo);
}


double gildong(int lns){
    return 0.05*lns;
}

double moonsoo(int lns){
    return 0.03*lns + 0.004*lns*lns;
}

void estimate(int lines, double (*pf) (int)){
    using namespace std;
    cout << lines << " lines to writes ";
    cout << " takes " << (*pf) (lines) <<" sec\n";
}
