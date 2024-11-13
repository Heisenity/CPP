#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter the number: \n";
    cin>>n;

    int sum=0;

    // int sum=0;
    // int i=1;

    // while(i<=n)
    // {
    //     sum+=i;
    //     i++;
    // }
    // cout<<"sum = "<<sum<<endl;
    for(int i=1;i<=n;i++)
    {

        sum=sum+i;
        //cout<<"Sum= "<<sum<<endl;
    }

    cout<<"-----------------------------------"<<endl;

    cout<<"Sum= "<<sum<<endl;



}