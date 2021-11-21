mystring = "hello"
myfloat = float(10)
myint = 20
intnum3 = 3
intnum2 = 2
newstring = '''\
"Isn\'t" 
they said'''
slistring1 = "garbage end of text"
slistring2 = "start of text garbage"

divres = myint / intnum2
fldivres = myint // intnum3
remdivres = myint % intnum3
calcres = divres + (remdivres - fldivres) * 2

print(divres)
print(fldivres)
print(remdivres)
print(calcres)
print(newstring)
print(slistring2[0:-7] + slistring1[8:])
print(slistring2[0:-8],slistring1[8:])
