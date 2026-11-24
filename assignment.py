# You can remove 'pass' if you written code in the function
# Each node is a list: [Data, Pointer]. A pointer of -1 means "points to nothing".

LinkedList = []
FirstNode = -1
FirstEmpty = 0

def Initialise():
    global LinkedList, FirstNode, FirstEmpty
    for i in range (10):
        LinkedList.append([-1,i+1])
    LinkedList[9][1]=-1
    FirstNode=-1
    FirstEmpty=0

def OutputNodes():
    global LinkedList, FirstNode
    CurrentPionter=FirstNode
    while CurrentPionter !=-1:
        print(LinkedList[CurrentPionter][0], end="\n")

        CurrentPionter = LinkedList[CurrentPionter][1]
    print()




def InsertFront(Data):
    global LinkedList, FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return False
    NewNode = FirstEmpty
    FirstEmpty = LinkedList[NewNode][1]
    LinkedList[NewNode][0] = Data
    LinkedList[NewNode][1] = FirstNode
    FirstNode = NewNode
    return True

def InsertEnd(Data):
    global LinkedList, FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return False
    NewNode = FirstEmpty
    FirstEmpty = LinkedList[NewNode][1]
    LinkedList[NewNode][0] = Data
    LinkedList[NewNode][1] = -1
    if FirstNode == -1:
        FirstNode = NewNode
    else:
        CurrentPointer = FirstNode
        while LinkedList[CurrentPointer][1] != -1:
            CurrentPointer = LinkedList[CurrentPointer][1]
        LinkedList[CurrentPointer][1] = NewNode
    return True

# Exercise 2
def InsertInOrder(Item):

    global LinkedList, FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return False
    CurrentPionter = FirstNode
    if LinkedList[FirstNode][0]>Item:
        InsertFront(Item)
        return True

    while CurrentPionter != -1:
        if LinkedList[CurrentPionter][0]>Item:
            Save=FirstEmpty
            FirstEmpty = LinkedList[Save][1]
            LinkedList[Save][0]=Item
            LinkedList[Save][1]=CurrentPionter
            LinkedList[PreviousPionter][1]=Save
            return True
        else:
            PreviousPionter = CurrentPionter
            CurrentPionter = LinkedList[CurrentPionter][1]
    InsertEnd(Item)
    return True




# Exercise 3
def Delete(Item):
    global LinkedList, FirstNode, FirstEmpty
    PreviousPointer = -1
    CurrentPointer = FirstNode
    while CurrentPointer != -1 and LinkedList[CurrentPointer][0] != Item:
        PreviousPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer][1]
    if CurrentPointer == -1:
        return False
    if PreviousPointer == -1:
        FirstNode = LinkedList[CurrentPointer][1]
    else:
        LinkedList[PreviousPointer][1] = LinkedList[CurrentPointer][1]
    LinkedList[CurrentPointer][0] = -1
    LinkedList[CurrentPointer][1] = FirstEmpty
    FirstEmpty = CurrentPointer
    return True



# Exercise 4
def LoadFromFile(FileName):
    try:
        count=0
        Initialise()
        File = open("Data.txt", "r")
        Line = File.readline().strip()
        while Line != "" and FirstEmpty!=-1:
            InsertInOrder(Line)
            count+=1
            Line = File.readline().strip()
        File.close()
        return count
    except IOError:
        print("File not found")



# Exercise 5
def Reverse():
    global LinkedList, FirstNode
    CurrentPionter = FirstNode
    copylist=[]
    for i in range(10):
        copylist.append([LinkedList[i][0], LinkedList[i][1]])


    while CurrentPionter != -1:
        if copylist[CurrentPionter][1]==-1:
            LinkedList[CurrentPionter][1] = PreviousPionter
            FirstNode=CurrentPionter
        else:
            if copylist[CurrentPionter][1]==0:
                LinkedList[CurrentPionter][1] = -1
            else:
                LinkedList[CurrentPionter][1] = PreviousPionter
        PreviousPionter = CurrentPionter

        CurrentPionter = copylist[CurrentPionter][1]


