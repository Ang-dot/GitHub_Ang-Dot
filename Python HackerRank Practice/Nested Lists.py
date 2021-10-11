nested_list = []
mark_list = []

if __name__ == '__main__':

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
    
    for i in nested_list:
        if i[1] not in mark_list:
            mark_list.append(i[1])
    
    for i in sorted(nested_list):
        if i[1] == sorted(mark_list)[1]:
            print(i[0])