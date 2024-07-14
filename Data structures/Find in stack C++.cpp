#include <bits/stdc++.h>
using namespace std;

void findElement(stack<int>& St, int K)
{
  while (!St.empty()) {
    if (St.top() == K){
      cout << "Element found!" ;
      return;
    }
    St.pop();
  }
  cout << "Element not found!";
}


int main() 
{
    stack<int> St;
    
    St.push(4);
    St.push(3);
    St.push(2);
    St.push(1);
    
    int K = 3;
    
    findElement(St,K);
    return 0;
}