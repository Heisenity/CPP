#include<iostream>
using namespace std;

int main()
{
    int n;
    int sum=0;
    cout<<"Enter the number\n";
    cin>>n;
    cout<<endl;

    for(int i=1;i<=n;i++)
    {
        if(i%3==0)
        {
            continue;
        }

        cout<<i<<endl;
       
    }
    
}