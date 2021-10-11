if __name__ == '__main__':
    list = []
    N = int(input())
    function_entry = [(input()) for _ in range (N)]
    for i in function_entry:
        command = [(i.split())]
        for j in command:
            if j[0] == 'insert':
                list.insert(int(j[1]), int(j[2]))
            elif j[0] == 'print':
                print(list)
            elif j[0] == 'remove':
                list.remove(int(j[1]))
            elif j[0] == 'append':
                list.append(int(j[1]))
            elif j[0] == 'sort':
                list.sort()
            elif j[0] == 'pop':
                list.pop(-1)
            else:
                list.reverse()