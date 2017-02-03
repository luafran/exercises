#include <iostream>
#include <fstream>
using namespace std;

int main ()
{

    ofstream outfile;

    outfile.open("test.txt");

    // >> i/o operations here <<
    outfile << "Test" << endl;
    outfile.flush();
    outfile.close();
    return 0;
}

