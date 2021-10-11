if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_list = []
    
    for i in list(arr):
        if i not in unique_list:
            unique_list.append(i)
            
    unique_list.sort()
    
    print(unique_list[-2])