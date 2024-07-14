#include <bits/stdc++.h>
using namespace std;

void printQueue(queue<int>& Q)
{
    while (!Q.empty()){
        cout << Q.front() << ' ';
        Q.pop();
    }   
}

int main()
{
    queue<int> Q;
    Q.push(1);
    Q.push(2);
    Q.push(3);
    Q.push(4);
    printQueue(Q);
    return 0;
}