#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string>
using namespace std;

int readLines(const std::string& fileName1, const std::string& fileName2)
{
    string line1;
    string line2;
    ifstream file1 (fileName1.c_str());
    ifstream file2 (fileName2.c_str());
    if (file1.is_open() && file2.is_open())
    {
        cout << setw(20) << left << "File1" << "File2" << endl;
        bool done;
        done = file1.eof() && file2.eof();
        while (!done)
        {
            getline (file1, line1);
            getline (file2, line2);
            line1.erase(std::remove(line1.begin(), line1.end(), '\n'), line1.end());   
            line2.erase(std::remove(line2.begin(), line2.end(), '\n'), line2.end());   
            cout << setw(20) << left << (file1.eof() ? "" : line1) << (file2.eof() ? "" : line2) << endl;
            done = file1.eof() && file2.eof();
        }
        
        file1.close();
        file2.close();
    }
    else
    {
        cout << "Unable to open some file"; 
    }

    return 0;
}

int main ()
{
    std::string fileName1("example1.txt");
    std::string fileName2("example2.txt");
    readLines(fileName1, fileName2);

    return 0;
}

