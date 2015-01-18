def solution():
    num = int(raw_input("input1"))
    countList = []
    for i in range(0,num):
        list = []
        count = 0
        divided = raw_input("input")
        for j in range(0,len(divided)):
            list.append(divided[j])
        divide = int(divided)
        for k in list:
            if ((int(k) != 0)):
                if (divide % int(k) == 0):
                    count = count + 1
        countList.append(count)
    for i in countList:
        print i

if __name__ == '__main__':
    solution()
