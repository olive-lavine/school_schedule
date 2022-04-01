class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes
        # self.classes = classes[:]

    def add_class(self, subject):
        self.classes.append(subject)

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        return (f"{self.name} is a {self.grade} and " 
            f"is enrolled in {self.get_num_classes()} classes")