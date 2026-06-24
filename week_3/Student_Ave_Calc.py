choice = "y"

# Loop to allow another student's marks to be entered until the user chooses to stop
while choice.lower() == "y":

    # Ask the user to enter three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))
    
    # Calculate the average of the three quiz marks
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print(f"The average mark is: {average:.2f}")
    
    # Determine whether the student passes or fails based on a 50-point threshold
    if average >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")
        
    # Ask the user if they want to enter marks for another student
    choice = input("Continue? Select Y/N: ")

print("Program Ended")
