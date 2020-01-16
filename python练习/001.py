class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# ============================
    def get_name(self):
        return str(self.name)

# -----------------------------
    def get_age(self):
        return int(self.age)

# -----------------------------
    def get_course(self):
        return str(sorted(self.score)[::-1][0])


# +++++++++++++++++++++++++++++
zm = Student("张明", 20, [69, 88, 100])
print("{}\n{}\n{}\n".format(zm.get_name(), zm.get_age(), zm.get_course()))
