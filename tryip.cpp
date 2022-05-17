#include <iostream>
#include <string>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

std::string addresses[10];
char file2[256];

int tryAddress(string Address, int a, int b){
  
  for(int i = a; i < b; i++){
    ActualAddress=Address;
    ActualAddress += std::to_string(i);
    int x = system("ping -c1 -s1"+ ActualAddress + "> /dev/null 2>&1");
    if (x==0){
      cout<<"success"<<endl;
      cout<<"ActualAddress"<<endl;
    }else{
      cout<<"no connection"<<endl;
    
    }
  
  
}


int main(){
  
  tryAddress(10.40.90., 1, 254);  
  
}
