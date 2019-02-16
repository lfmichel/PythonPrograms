#count how many students are taking ComSci

students = [
	("john", ["compsci", "physics"]),
	("vusi", ["maths", "compsci", "stats"]),
	("jess", ["compsci", "accounting", "economics", "management"]),
	("sarah", ["infsys", "accounting", "economics", "commlaw"]),
	("zuki", ["sociology", "economics", "law", "stats", "music"])]

for name, subjects in students:
	print(name, "takes", len(subjects), "courses")

counter = 0
for name, subjects in students:
    for s in subjects:
        if s == "compsci":
                counter += 1

print("The number of students taking CompSci is", counter)

cont = 0; i = 0
for name, subjects in students:
    if "compsci" in subjects:
        cont += 1
    if "john" in name:
        i += 1       

print("The number of students taking CompSci is", cont)
print(i)
