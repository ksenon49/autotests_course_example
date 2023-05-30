class PersonInfo:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def short_name(self):
        name = self.name.split()
        return name[1] + ' ' + name[0][0]

    def path_deps(self):
        return '--> '.join(self.department)

    def new_salary(self):
        


