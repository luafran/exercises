// bitset::count
#include <iostream>
#include <string>
#include <bitset>
using namespace std;

int main ()
{
    bitset<8> myset (string("10110011"));
    bitset<16> myset2 (0x0101);

    cout << "myset has " << int(myset.count()) << " ones ";
    cout << "and " << int(myset.size()-myset.count()) << " zeros.\n";
    cout << "myset2 has " << int(myset2.count()) << " ones ";
    cout << "and " << int(myset2.size()-myset2.count()) << " zeros.\n";

    return 0;
}
