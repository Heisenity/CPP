#include<iostream>

using namespace std;

int main()
{
    long int a, b;

    char c;

    cout<<"Enter the first number: \n";

    cin>>a;

    cout<<"Enter the second number: \n";

    cin>>b;

    cout<<"Enter the operation i.e '+' '-' '*' '/':\n";

    cin>>c;

    switch(c)
    {
        case '+':
            cout<<"Addition of "<<a <<" and "<<b <<" is "<<a+b<<endl;
            break;
        case '-':
            cout<<"Subtraction of "<<a<<" and "<<b<<"is"<<a-b<<endl;
            break;
        case '*':
            cout<<"Multipliction of "<<a<<" and "<<b<<" is "<<a*b<<endl;
            break;

        case '/':
            cout<<"Division of "<<a<<" and "<<b<<" is "<<(float)a/b<<endl;
            break;

        default:
            cout<<"Invalid Choice";
            break;
    }


}