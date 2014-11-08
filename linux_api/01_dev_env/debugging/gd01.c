
void func03(void)
{
    int loc3 = 33;
}

int func02(int x, int y)
{
    int loc2 = 22;
    int res2;

    res2 = x / y;
    
    return res2;
}

int func01(int a, int b)
{
    int loc1 = 11;
    int res1;

    res1 = func02(a, b);
    
    return res1;
}    

int main(int argc, char *argv[])
{
    int res;

    res = func01(5, 0);

    func03();

    return res;
}

