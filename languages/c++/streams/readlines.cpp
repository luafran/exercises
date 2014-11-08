// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int readLines1(std::string& fileName)
{
    string line;
    ifstream myfile (fileName.c_str());
    if (myfile.is_open())
    {
        while (getline (myfile, line))
        {
            cout << line << endl;
        }
        
        myfile.close();
    }
    else cout << "Unable to open file"; 

    return 0;
}

int readLines2(std::string& fileName)
{
    char line[256];
    ifstream myfile (fileName.c_str());
    if (myfile.is_open())
    {
        while (myfile.getline (line, 256))
        {
            cout << line << endl;
        }
        
        myfile.close();
    }
    else cout << "Unable to open file"; 

    return 0;
}

int main ()
{
    std::string fileName("example.txt");
    readLines1(fileName);
    readLines2(fileName);

    return 0;
}
