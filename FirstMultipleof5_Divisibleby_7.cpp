#include<iostream>
using namespace std;

int main()
{
    int n;
    int a;

    cout<<"Enter the number:\n";
    cin>>a;

    cout<<"How many multiples you want?"<<endl;
    cin>>n;
    cout<<endl;



    for(int i=1;i<=n;i++)
    {
        int prod=a*i;
        cout<<prod<<endl;

        if(prod%7==0)
        {
            cout<<prod<<" is divisible by 7\n"<<endl;
        }
        
            else
            {
                cout<<prod<<" is not Divisible by 7\n"<<endl;
            }
        }
    }
