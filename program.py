def SwapFileData():
    fileName1=input("Enter the First file name: ")
    f1=open(fileName1,"r")
    data_a=f1.read()
    fileName2=input("Enter the Second file name: ")
    f2=open(fileName2,"r")
    data_b=f2.read()
    f1.close()
    f2.close()
    f1=open(fileName1,"w")
    f2=open(fileName2,"w")
    f1.write(data_b)
    f2.write(data_a)
    f1.close()
    f2.close()

SwapFileData()