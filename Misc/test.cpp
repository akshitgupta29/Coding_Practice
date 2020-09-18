#include<iostream>
using namespace std;
class myclass{
  public:
  myclass(){
    cout<<"hello"<<"\n";
    }
  };
  class car:public myclass{
    public:
    string model;
  };
  int main()
  {
    myclass myobj;
    car myobj1;
    myobj1.model="800";
    cout<<myobj1.model;
    return 0;
  }
