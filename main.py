print("Sevgi kalkulyatoriga xush kelibsiz!")

name1 = input("Ismingizni kiriting: ").lower()
name2 = input("Uning ismini kiriting: ").lower()

name = name1 + name2

h = name.count("h")
a = name.count("a")
q = name.count("q")
i = name.count("i")
y = name.count("y")
s = name.count("s")
e = name.count("e")
v = name.count("v")
g = name.count("g")

haqiqiy = h + a + q + i + y
sevgi = s + e + v + g + i
haqiqiy = str(haqiqiy)
sevgi = str(sevgi)
total = int(haqiqiy + sevgi)

if total >= 90:
  print(f"{total}% sizlar juda mos ekansizlar!")
elif total <= 30:
  print(f"{total}% sizlar bir birlaringizga mos emassizlar!")
elif 90 > total >= 60:
  print(f"{total}% sizlar yaxshi juftliksizlar!")
else:
  print(f"{total}% sizlarga chidasa bo'ladi!")
