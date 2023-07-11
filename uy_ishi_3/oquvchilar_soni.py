def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        num_students = int(input("Enter the number of students: "))
        correct_names = []

        for i in range(num_students):
            full_name = input("Enter the full name of student {}: ".format(i+1))
            if full_name[0].isupper():
                correct_names.append(full_name)

        return func(*args, correct_names, **kwargs)

    return wrapper


@capitalize_decorator
def output_correct_names(*args, **kwargs):
    print("The correct names with the first letter capitalized are:")
    for name in args:
        print(name)
    for key, value in kwargs.items():
        print(key, value)


output_correct_names()
