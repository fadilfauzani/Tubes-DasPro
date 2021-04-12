def datatostring(data):
    s = ""
    for i in range (len(data)):
        s += str(data[i])
        if (i != len(data) - 1):
            s += ","
    return s
print(datatostring([1,23123,23]))