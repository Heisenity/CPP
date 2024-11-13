#include<iostream>
using namespace std;

int main()
{
    cout<<"Enter your character\n";

    char c;
    cin>>c;

    if(cin.peek()!='\n' || cin.fail() || !isalpha(c))
    {
        cout<<"Invalid,Enter a valid and single character.";
    }

    else{

    switch (c)
    {
    case 'a':
        cout<<"Its a Vowel";
        break;
    case 'e':
        cout<<"Its a Vowel";
        break;
    
    case 'i':
        cout<<"Its a Vowel";
        break;
    case 'o':
        cout<<"Its a Vowel";
        break;

    case 'u':
        cout<<"Its a Vowel";
        break;
    
    default:
        cout<<"Its A Consonant";
        break;
    }
    }

}