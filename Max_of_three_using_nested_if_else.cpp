#include<iostream>
using namespace std;

int main()
{
    int a,b,c;


    cout<<"Enter the first number:\n";

    cin>>a;

    cout<<"Enter the second number:\n";

    cin>>b;

    cout<<"Enter the third number:\n";

    cin>>c;

    if(a>b)
    {
        if(a>c)
        {
            cout<<"a is the Max number, the number is:"<<a<<endl;
        }
        else
        {
            cout<<"c is the Max number, the number is:"<<c<<endl;
        }
    }

    if(b>a)
    {
        if(b>c)
        {
            cout<<"b is the Max number, the number is:"<<b<<endl;
        }
    
        else
        {
            cout<<"c is the Max number, the number is:"<<c<<endl;

        }
    }

    if(a==b)
    {
        if(a==c)
        {
            cout<<"Three numbers are same.";
        }
    

    else{
        cout<<"Not Executed";
    }
    }



}