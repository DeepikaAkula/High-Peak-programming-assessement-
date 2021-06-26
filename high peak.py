#HIGH PEAK SOFTWARE ASSIGNMENT
file1=open(r"C:\Users\HP\OneDrive\Desktop\input.txt","r")#open a file for input in read mode
lines=file1.readlines()#read that file line by line
goodies=[]#initialize a goodies list
num_of_emps=int(lines[0][-2])#assigning number of employes 
for i in range(4,len(lines)):
    l=lines[i].split(":")#read the input after the ':'
    goodies.append([l[0],int(l[1])])#assigned number of goodies from file to list
goodies=sorted(goodies,key=lambda x:x[1])#sort the list
min_diff=float('inf')#max value is assigned to min_diff
for i in range(0,len(goodies)-num_of_emps+1):
    diff=goodies[i+num_of_emps-1][1]-goodies[i][1]#caluculate the minimum difference
    if diff<min_diff:
        min_index=i
        min_diff=diff
file1.close()#closing the input file
file2=open(r"C:\Users\HP\OneDrive\Desktop\output.txt","w")#open a file for output in write mode
file2.write("The goodies selected for distribution are:\n")
file2.write("\n")
for i in range(min_index,min_index+num_of_emps):
    file2.write(goodies[i][0]+":"+str(goodies[i][1])+"\n")#writing the output in ouput file
file2.write("\n")
file2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(min_diff))
file2.close() #closing output file

