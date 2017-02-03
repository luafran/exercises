#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <list>
#include <algorithm>
#include <vector>
#include <cstddef>
#include <cstdlib>

using namespace std;

struct split
{
    enum empties_t { empties_ok, no_empties };
};

template <typename Container>
Container& split(
    Container&                            result,
    const typename Container::value_type& s,
    const typename Container::value_type& delimiters,
    split::empties_t                      empties = split::empties_ok )
{
    result.clear();
    size_t current;
    size_t next = -1;
    do
    {
        if (empties == split::no_empties)
        {
            next = s.find_first_not_of( delimiters, next + 1 );
            if (next == Container::value_type::npos) break;
                next -= 1;
        }
        current = next + 1;
        next = s.find_first_of( delimiters, current );
        result.push_back( s.substr( current, next - current ) );
    }
    while (next != Container::value_type::npos);
    
    return result;
}

void print( vector <string> & v )
{
    //for (size_t n = 0; n < v.size(); n++)
    //    cout << "\"" << v[ n ] << "\"\n";
    if (v.size() > 3)
    {
        cout << "user = " << v[0] << ", uid = " << v[2];
        cout << endl;
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cout << "usage prog filename" << endl;
        exit(1);
    }

    map<string, list<string> > users;

    ifstream file(argv[1]);

    //string s = "One, two,, four , five,";
    string s;
    while (std::getline (file, s))
    {
        vector <string> fields;
        
        cout << "\"" << s << "\"\n";
        
        split( fields, s, ":" );
        if (fields.size() != 3)
            continue;

        cout << fields.size() << " fields.\n";
        cout << "user = " << fields[0] << ", uid = " << fields[2];
        cout << endl;
        
        //split( fields, s, ",", split::no_empties );
        //print( fields );
        //cout << fields.size() << " fields.\n";

        users[fields[2]].push_back(fields[0]);
    }

    map<string, list<string> >::const_iterator it;
    list<string>::const_iterator it2;
    for (it = users.begin(); it != users.end(); ++it)
    {
        if (it->second.size() > 1)
        {
            cout << "uid " << it->first << " has duplicated users: ";
            for (it2 = it->second.begin(); it2 != it->second.end(); ++it2)
                cout << *it2 << " ";
            cout << endl;
        }
    }

    return 0;
}
