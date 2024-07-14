'''
if __name__ == '__main__':

    arr = [1 ,2 ,3 ,4 ];
    N = len(arr);

    for i in range(N):
        print(arr[i], end=' ');
'''


def print_stack(St):
    while St:
        print(St.pop(), end=' ')


St = []
St.append(4)
St.append(3)
St.append(2)
St.append(1)
print_stack(St)

