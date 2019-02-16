# EXERCISE PAGE 51
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sara", ["InfSys", "Accounting", "Economics", "Comlaw"]),
    ("Zuki", ["Sociology", "Economica", "Law", "Stats", "Music"])
           ]

# Print All Students with a count of their courses.

for name, subject in students:
    print(name, "takes", len(subject), "courses")
