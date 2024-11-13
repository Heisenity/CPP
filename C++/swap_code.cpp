#include<iostream>
using namespace std;

int main()
{
    int a,b;

    cout<<"Enter the number of a:\n ";
    cin>>a;
    cout<<"Enter the number of b:\n ";
    cin>>b;

    int c;
    c=a;
    a=b;
    b=c;
    cout<<"After Swapping\n";
    cout<<"a:"<<a <<"\nb:"<<b <<endl;

    return 0;
}