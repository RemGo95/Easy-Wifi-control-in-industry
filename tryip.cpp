#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int tryAddress(string Address, int a, int b){
  
  for(int i = 0; i < b; i++){
    int x = system("ping -c1 -s1"+ Address + i +  "> /dev/null 2>&1");
  if (x==0){
    cout<<"success"<<endl;
    count<<"Address"+
  }else{
    cout<<"no connection"<<endl;
    
  }
  
  
}


int main(){
  tryAddress(10.40.90., 1, 254);  
  
}
