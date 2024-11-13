#include<iostream>

using namespace std;

int main()
{
    int num1;

    num1=5;

     
    cout<<(num1<<1)<<endl; // a>>b= a*2^b;

    cout<<(num1>>1)<<endl; // a<<b= a/2^b;

    int num2=6;

    cout<<(num1|num2)<<endl;
    cout<<(num1&num2)<<endl;
    
}