from school_schedule.student import Student

def test_check_attributes_correctly_set():
    # arrange
    # ???

    # act
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])

    # assert
    # assert student
    assert student.name == "Quinn"
    assert student.grade == "junior"
    assert student.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]

def test_add_class_method_adds_to_classes():
    # arrange
    new_class = "Painting"
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])

    # act
    student.add_class(new_class)

    # assert
    assert len(student.classes) == 7
    assert new_class in student.classes

def test_num_classes_returns_correct_num():
    # arrange
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])
    # act
    result = student.get_num_classes()

    # assert
    assert result == 6
