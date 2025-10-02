
a=input("ievadi savu vecumu ")
b=input("ievadi savu vardu ")
print("Tev sauc",b, "un tev ir",a, "gadi!")



sk1=int(input("ievadi pirmo skaitli "))
sk2=int(input("ievadi otro skaitli "))
summ=sk1 + sk2
print("skaitļiem",sk1,"un",sk2,"summa ir",summ)



sk=int(input("ievadi skaitli "))
if sk % 2 == 0:
    print("Ta ir pāra skaitli")
else:
    print("ta ir nepara skaitli")

c=int(input("ievadi skaitli "))
if c>0:
    print("Pozitīvs")
elif c<0:
    print("Negatīvs")
else:
    print("Nulle")

d=int(input("ievadi vecumu "))
if d>=18:
        print("Pilngadīgs")
else:
        print("Nepilngadīgs")


e=int(input("ievadi skatili "))
if 10<=e<=20:
    print("skaitlis ir starp 10 un 20")
else:
    print("skaitlis nav starp 10 un 20")

for i in range(1, 11):
     print(i)






