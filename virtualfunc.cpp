#include <bits/stdc++.h>
using namespace std;

class mybase{
public:
    void show()
    {
    cout<<"Base class show func"<<endl;
    }
    virtual void print()
    {
        cout<<"Base class print func"<<endl;
    }

    };

    class myderived: public mybase{

    void show()
    {
        cout<<"Derived class show func"<<endl;
    }
    void print()
    {
        cout<<"Derived class print func"<<endl;
    }

    };
int main()
{
    mybase *ptr;
    myderived obj;

    ptr=&obj;

    ptr->show();  //base class show function called
    ptr->print(); //derived class print function called

return 0;
}
