#include <iostream>
using namespace std;

void findElement(int arr[], int N, int K)
{
  for (int i = 0; i < N; i++){
    if (arr[i] == K){
      cout << "Element found!";
      return;
    }
  }
  cout << "Element Not found!";
}

int main()
{
  int arr[] = {1, 2, 3, 4};
  int K = 3;
  int N = sizeof(arr) / sizeof(arr[0]);
  findElement(arr, N, K);
  return 0;
}