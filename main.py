#Get Student Score by Name
#Database
names = ["JBSong", "Jeffery", "Joe" ,"Jane", "DJ_Mic", "Alien","Buzz", "Paul"]
math_scores =[70, 80, 65 ,83, 62, 12,45, 10]
english_scores =[71, 81, 66 ,84, 63, 13, 46, 11]
art_scores =[72, 82, 67 ,85, 64, 14,47, 12]

print("Print All Student's Name...")

#get array size function
student_size = len(names)
print("Strudent Size :"+str(student_size))

print("Choice:"+ str(names))
print("first letter needs to be capital")
user_name = input("enter your name:")

succeed = False

for i in range(student_size): # i = 0 ~ student_size-1
  if(user_name==names[i]):
    print(names[i]+"         math "+str(math_scores[i])
          + "   English "+str(english_scores[i])
          + "   art " +str(art_scores[i]))
    succeed = True

if(succeed == False):
  print("there is no name called  "+(user_name))
  
print("math,art,english.")
subject_name=input("What subject do you want to see?:")
if subject_name=="math":
  #math score check
  math_standard = int(input("enter math standard score:"))
  for i in range(student_size):
    if math_standard <= math_scores[i]:
      print(names[i]+"  "+str(math_scores [i]))
elif subject_name=="art":
  art_standard = int(input("enter art standard score:"))
  for i in range(student_size):
    if art_standard <= art_scores[i]:
      print(names[i]+"  "+str(art_scores [i]))
elif subject_name=="english":
  english_standard = int(input("enter english standard score:"))
  for i in range(student_size):
    if english_standard <= english_scores[i]:
      print(names[i]+"  "+str(english_scores [i]))
else:
  print("That is not a subject here.")
  