#chp 1 - Raise statement
'''while True:
    x = int(input("Enter a number: "))
    y = 200
    if y > x:
        print(y/x)
    else:
        raise Exception("x is greater than y")'''

#assert statement
# while True:
#     def negcheck(number):
#         assert (number>= 0), "Oops! the number is negative"
#         print(f"U have entered{number}")
#     num = int(input("Enter a number: "))
#     negcheck(num)

#- File handling
#lines = ["m this\n","m that\n","m those\n"]
'''fob = open("myfile.txt","w")

#print(fob.write("hello python\nhello python\n"))
#will return no. of characterc and will also insert lines into files.
#fob.writelines("this is my project")
#fob.write(lines)-- write() function always take values in string and not in lists. And also it rerturn no. of character in interpreter and not in the files.

#fob.writelines(lines)
fob.close()'''

'''with open('myfile.text',"w") as fob:
    fob.write("hey there I am using python")'''

'''with open('myfile.text',"a") as fob:
    fob.write("hey there I am using python\nhey there I am using python")'''
#with open('myfile.text',"r") as fob:
    #print(fob.read()) # this will read whole document
    #print(fob.readlines(5))# this will read the "5th line" and not the all five line form top!
    #print(fob.readline()) #this will read complete line, but if tou give number like 3, 5 then it will  read characters frm the very of the lines here 3, 5.
   # print(fob.readline(2))#  this will return what 2 characters are from the very beginning of the file, this will do same work of read() but difference is read() doesnot know where lines ends but readline() does.
    #print(fob.readlines())  this will return whole document as a list and each lines as list items that ends with \n. one list per line.
    #split() will break list into words
    #splitlines() will break list into lines.

'''with open ('myfile.txt','w+') as fpointer:
    #fpointer.write("\n this is to be subtracted!")
    r = fpointer.readline()
    print(r)
if you  do this the above one... i mean opening files in w+ mode and then not writing anything to file then it will blank the file completely....yes !'''
#----------------------------------------------------------------------------------------------
# A . with open ('myfile.text','a') as fpointer:
#     fpointer.write("\n this is to be subtracted!")
#     r = fpointer.readline()
#     print(r)

# B . with open ('myfile.text','a+') as fpointer:
#     fpointer.write("\n this is to be subtracted!")
#     r = fpointer.readline()
#     print(r)

#look if mode 'a' comes with read as it is in A, then it will be wrong because it is not in read mode but...
#...as it is in B. '+a' mode with read is ok because 'a+' is read plus append, but it wont give output in interpreter it just add lines to the file.
#------------------------------------------------------------------------------------------------

'''li = fob.readlines()
    for items in li:
        subitmes = items.split()
        print(subitmes)
    li = fob.readlines()
    for items in li:
        subitmes = items.splitlines()
        print(subitmes)'''

'''print(fob.tell())
    print(fob.seek(5,0))
    print(fob.read(6))
    print(fob.tell())
    print(fob.seek(5,0))
    print(fob.read(4))'''


#The Pickle Module
















     
    


