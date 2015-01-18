def altChar():
    num = int(raw_input())
    for i in range(0,num):
        list = []
        string = raw_input("input")
        for char in string:
            list.append(char)
        j = 0
        k = 1

        while (j < len(list)-1):
            while (k < len(list)):
                if (list[j] == list[k]):
                    list[k] = 0
                    k = k + 1

                else:
                    j = j + 1
                    k = k + 1
    
    print list.count(0)




if __name__ == '__main__':
    altChar()


