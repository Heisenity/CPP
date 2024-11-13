#include <iostream>
using namespace std;

int main() {
    int sp,cp;

    cout<<"Enter the SP\n";

    cin>>sp;

    cout<<"Enter the CP\n";

    cin>>cp;

    if(sp>cp)
    {
        cout<<"Profit.\n";

        int profit=0;

        profit=sp-cp;
        cout<<"Profit="<<profit<<endl;
    }

    else if(sp==cp)
    {
        cout<<"Neither Profit Nor Loss.";
    }

    else
    {
        cout<<"Loss.\n";
        int loss=0;

        loss=cp-sp;

        cout<<"Loss="<<loss<<endl;
    }


   

    return 0;
}
