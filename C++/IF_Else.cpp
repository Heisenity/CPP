#include<iostream>

using namespace std;

int main()
{
    int score;

    cout<<"Enter the score: \n";

    if(!(cin>>score))
    {
        cout<<"Only Interger Allowed."<<endl;
    }

    else if(score<0)
    {
        cout<<"Not a valid score";

    }

    else if(score>80 && score<=100)
    {
        cout<<"Well Done";

    }
    else if(score>=50 && score<=80)
    {
        cout<<"Can Improve";
    }

    else if(score>=100)
    {
        cout<<"Enter a value less than or equal to 100.";
    }

    else
    {
        cout<<"Poor Performance.";

    }

    return 0;

}
