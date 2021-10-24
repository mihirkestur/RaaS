
f2=open("./Veges.txt","r")
f1=open("./Vegetables.txt","w")
for line in f2:
   f1.write(line.replace("\n","")+",")

f2.close()
f1.close()