
#user input the numbers of loops
n = int(input("Pls input number: "))

l0 = []
l1 = []
total = []
for i in range(n):
    n1 = input("Pls input coordinates: ")
    t = n1.split(" ")
    l0.append(int(t[0]))
    l1.append(int(t[1]))


for a, b in zip(l0, l1):
    if a > 0 and b > 0:
      
        # print("Первая четверть")
        total.append("Первая четверть")
    elif a < 0 and b > 0: 
        # print("Вторая четверть")
        total.append("Вторая четверть")
    elif a < 0 and b < 0: 
        # print("Третья четверть")
        total.append("Третья четверть")
    elif a > 0 and b < 0: 
        # print("Четвертая четверть")
        total.append("Четвертая четверть")

u = "".join(total)

q1 = u.count("Первая четверть")
q2 = u.count("Вторая четверть")
q3 = u.count("Третья четверть")
q4 = u.count("Четвертая четверть")

print(f"Первая четверть: {q1}")
print(f"Вторая четверть: {q2}")
print(f"Третья четверть: {q3}")
print(f"Четвертая четверть: {q4}")


