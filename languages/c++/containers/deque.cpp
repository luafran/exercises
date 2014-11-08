// deque::pop_front
#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

void myfunction (int i)
{
    cout << " " << i << endl;
}

int main ()
{
    deque<int> mydeque;
    int sum (0);
    mydeque.push_back (100);
    mydeque.push_back (200);
    mydeque.push_back (300);

    for_each (mydeque.begin(), mydeque.end(), myfunction);

    cout << "mydeque[" << 1 << "] is " << mydeque[1] << "\n";

    cout << "Popping out the elements in mydeque:";
    while (!mydeque.empty())
    {
        cout << " " << mydeque.front();
        mydeque.pop_front();
    }

    cout << "\nFinal size of mydeque is " << int(mydeque.size()) << endl;

    return 0;
}
