#include <iostream>
#include <fstream>

int main(int argc, char *argv[])
{

    std::string crashFile(argv[1]);

    std::ifstream file(crashFile.c_str());

    //if (file.is_open())
    if (file)
    {
        std::cout << "File is open\n";
    }
    else
    {
        std::cout << "File is NOT open\n";
    }
}

