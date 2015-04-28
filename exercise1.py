def DebuggingExercise1():
    list_of_int = []
    for i in range(1, 5):
        print("About to try to insert %d into the array at position %d") %(i, i)
        list_of_int.append(i)
        print("Successful")

    print("This is what is in the array: ")
    for i in range(1, 5):
        element = list_of_int[i]
        print(element)
        print(" ")


DebuggingExercise1()
