#include<iostream>

using namespace std;

int main()
{
    int num1=80;

    int num2=90; 

    cout<<sizeof(num1)<<endl;

    char flag;

    num1<=num2 ? flag='T' : flag='F';

    cout<<flag<<endl;

    cout<<(&num1)<<endl;

    return 0;
}