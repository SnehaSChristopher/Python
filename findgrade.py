english=int(input("Mark of English:"))
hindi=int(input("Mark of Hindi:"))
maths=int(input("Mark of maths:"))
socialscience=int(input("Mark of social science:"))
biology=int(input("Mark of biology:"))
physics=int(input("Mark of physics:"))
total=english+hindi+maths+socialscience+biology+physics
print ("Total mark is ",total)
avg=total/6
if avg>=97 and avg<=100:
 print("Grade : A+")
elif avg>=93 and avg <=96:
  print("Grade : A")
elif avg>=90 and avg <=92:
   print("Grade : A-")
elif avg>=87 and avg <=89:
   print("Grade : B+")
elif avg>=87 and avg <=89:
   print("Grade : B+")
elif avg>=87 and avg <=89:
   print("Grade : B+")
elif avg>=83 and avg <=86:
   print("Grade : B")
elif avg>=80 and avg <=82:
   print("Grade : B-")
elif avg>=77 and avg <=79:
   print("Grade : C+")
elif avg>=77 and avg <=79:
   print("Grade : C+")
elif avg>=73 and avg <=76:
   print("Grade : C")
else:
    print("poor performance")


   