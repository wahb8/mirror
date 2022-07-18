stream = "000 001 111 000 001 111 000 001 010 011 100 101 1101 0000"

def Convert(string): #to convert string to list to use
  list1=[]
  list1[:0] = string
  return list1


def a(x):
    a = Convert(x)

    #something to make sure everything is compressed right
    w = a[::-1]
    e = False
    f = False
    for i in w:
        if i == "0" and e == False and f == False:
            a += "1"
            e = True
        elif i == "1" and f == False and e == False:
            a += "0"
            f = True
    
    #some veriables to set up the compression algorithm
    c = 0
    d = 0
    b = ""

    v = False
    n = False
    #the compression
    for i in a:
        if i == "0" and v == False:
            c += 1
        elif i == "1" and v == False:
            b += "x" + str(c) + "0"
            c = 0
            n = False
            v = True
            
        elif i == "1" and v == True:
            d += 1
        elif i == "0" and v == True:
            b += "x" + str(d + 1) + "1"
            c += 1
            d = 0
            n = False
            v = False
    print(b)

a(stream)
    
    
    
    
