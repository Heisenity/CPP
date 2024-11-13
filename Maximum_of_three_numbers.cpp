#include <iostream>
using namespace std;

int main() {
    int a,b,c;

    cout<<"Enter the first number\n";

    cin>>a;

    cout<<"Enter the second number\n";

    cin>>b;

    cout<<"Enter the third number\n";

    cin>>c;


    if(a>b && a>c)
    {
        cout<<"First Number is Max. The Number Is: "<<a<<endl;

    }
    else if(b>a & b>c)
    {
        cout<<"Second Number is Max. The Number Is: "<<b<<endl;
    }
    else
    {
        cout<<"Third Number is Max. The Number Is: "<<c<<endl;
    }
    

    
}
