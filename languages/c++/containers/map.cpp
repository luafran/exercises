#include <iostream>
#include <map>
using namespace std;

int main ()
{
    map<char,int> mymap;
    map<char,int>::iterator it;

    it = mymap.find('b');
    if (it == mymap.end())
        cout << "Map is empty\n";

    // insert some values:
    mymap['a']=10;
    mymap['b']=20;
    mymap['c']=30;
    mymap['d']=40;
    mymap['e']=50;
    mymap['f']=60;

    it = mymap.find('b');
    mymap.erase (it);                   // erasing by iterator

    mymap.erase ('c');                  // erasing by key

    it = mymap.find ('e');
    mymap.erase ( it, mymap.end() );    // erasing by range

    // show content:
    for ( it = mymap.begin() ; it != mymap.end(); it++ )
        cout << (*it).first << " => " << (*it).second << endl;

    return 0;
}
