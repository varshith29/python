def subj(x):
   for i in l:
         d[i[0]]=i[x]
   updated = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
   counter = 1
   for i in updated:
      print("rank", counter, "=", i[0])
      counter += 1

n=int(input('number of students :'))
l=[]
for i in range (0,n):
   l.append([])
   x=input("name:")
   l[i].append(x)
   a=input('roll no :')
   l[i].append(a)
   b=int(input('maths marks :'))
   l[i].append(b)
   c=int(input('physics marks :'))
   l[i].append(c)
   d=int(input('chemistry marks :'))
   l[i].append(d)
f=open('file1.txt','w')
for i in range(0,n):
   f.write("student-")
   f.write(str(i+1))
   f.write('\n')
   for j in l[i]:
    f.write(str(j))
    f.write('\n')
print('1.show details of all students in alphabetical order')
print('2.Give ranks to students (Based on total marks)')
print('3.Average marks of students in each subject')
print('4.rank of student based on the subject')
print('5.students who scored above average(total) marks')
print('6.students who scored 10% above/below average (total marks) marks')
print('7.students who scored above average scores in maths but below average in physics')
print('8.Number of students who scored above average in all the 3 subjects ')
menu=int(input('choose the function to be  performed :'))

if menu==1:
   l.sort()
   print('students list in alphabetical order :')
   for i in l:
      print(i[0])
elif menu==2:
   d={}
   for i in l:
      d[i[0]]=i[2]+i[3]+i[4]
      updated=sorted(d.items(),key=lambda kv:kv[1], reverse=True)
   counter=1
   for i in updated:
      print("rank",counter,"=",i[0])
      counter+=1
elif menu==3:
   math,phy,chem=0,0,0
   for i in l:
      math+=i[2]
      phy+=i[3]
      chem+=i[4]
   print("maths average =",math/len(l))
   print("physics average =",phy/len(l))
   print("chemistry average =",chem/len(l))
elif menu==4:
   sub=input("give a subject :")
   d={}
   if sub=='maths':
      subj(2)
   elif sub=='physics':
      subj(3)
   elif sub=='chemistry':
      subj(4)
elif menu==5:
   d={}
   sum=0
   for i in l:
      d[i[0]]=i[2]+i[3]+i[4]
      sum+=d[i[0]]
   avg=sum/(len(l))
   print("students who scored more than total average marks :")
   for i in d.items():
      if i[1]>avg:
       print(i[0])
elif menu==6:
   d={}
   sum = 0
   for i in l:
      d[i[0]] = i[2] + i[3] + i[4]
      sum += d[i[0]]
   avg = sum / (len(l))
   print("students who scored 10% above/below total average marks :")
   for i in d.items():
      if (i[1] == (1.1)*avg or i[1]==(0.9)*avg):
         print(i[0])
elif menu==7:
   math, phy = 0, 0
   print("students who scored above average in maths an below average in physics :")
   for i in l:
      math += i[2]
      phy += i[3]
   for i in l:
      if(i[2]>math/(len(l)) and i[3] < phy/(len(l))) :
         print(i[0])
elif menu==8:
   math, phy, chem = 0, 0, 0
   print("students who scored above average in all 3 subjects :")
   for i in l:
      math += i[2]
      phy += i[3]
      chem += i[4]
   for i in l:
      if(i[2] > math/len(l) and i[3] > phy/len(l) and i[4] > chem/len(l)) :
         print(i[0])
else :
   print("invalid input")

