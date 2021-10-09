if __name__ == '__main__':
    
    # The included code stub will read an integer, , from STDIN.
    # Without using any string methods, try to print the following:
    # 123....n

    print(*(range(1,int(input())+1)), sep='')