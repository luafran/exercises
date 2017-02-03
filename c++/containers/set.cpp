#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

void printElements(const string& s)
{
    cout << s << endl;
}

int main()
{
    char input[][20] = {"hello", "zzzz", "goodbye", "abacca", "country"};

    int inputSize = (sizeof(input) / sizeof(input[0]));

    cout << "size = " << inputSize << endl;

    set<string> myset;
    set<string> myset2(input, input+inputSize);
    set<string>::iterator it;

    for (int i = 0; i < inputSize; i++)
    {
        cout << input[i] << endl;
        myset.insert(input[i]);
    }

    cout << endl;
    cout << "set1:" << endl;
    for (it = myset.begin(); it != myset.end(); ++it)
    {
        cout << *it << endl;
    }

    cout << endl;
    cout << "set2:" << endl;
    for_each(myset2.begin(), myset2.end(), printElements);

    cout << endl;
    it = myset.find("goodbye");
    if (it != myset.end())
    {
        cout << "goodbye found in set1" << endl;
    }
    else
    {
        cout << "goodbye not found in set1" << endl;
    }
    
    it = myset.find("aaaa");
    if (it != myset.end())
    {
        cout << "aaaa found in set1" << endl;
    }
    else
    {
        cout << "aaaa not found in set1" << endl;
    }

    return 0;
}
