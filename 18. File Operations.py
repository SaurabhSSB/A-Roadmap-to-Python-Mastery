with open("ABC.txt","a") as a:
    a.write("\nFinally able to do operation on file. Thanks Python!")

a= open("ABC.txt","r")





r= a.read()
print(r)
a.close()
# r mode- Read Default
# w mode- Write
# a mode- Append
# x mode- Create
# t mode- Text Default
# b mode- Binary Jpg, Image, Pdf, exe

f= open("ABC.txt","r")
while True:
    line= f.readline()
    if not line:
        break
    print(line)

x= open("ABCD.txt","w")
y= ['one\n','two\n','three\n']
x.writelines(y)
x.close()