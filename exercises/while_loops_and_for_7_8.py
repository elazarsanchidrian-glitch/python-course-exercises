#number = 9
#while number != 10:
#     print("please enter a number")
#     number = int(input("enter a number"))
# print(f"done, the number was {number}")
#
#
#secret_number = 7
#user_guess = 0
#while user_guess != secret_number:
    #user_guess = int(input("please enter a number"))
#print("correct!", user_guess)
#
#
#number = 0
#while number != 10:
 #   print(number)
#    number = number + 1
#
#for x in range(10):
#    print(x)
#
#
#x = 0
#while True:
 #   print(x)
#    x=x+1
 #   if x == 10:
 #       break
#print("after the loop")
#
#
#count = 0
#max_number_of_times = 4
#while True:
 #   print(count)
#    count = count + 1
#    if count == max_number_of_times:
#        break
#print("after the loop")
#
#
#total_num_students = 10
#count = 0
#while count <= total_num_students:
#    student_name = input("Enter student name: ")

#    print(count)
 #   count += 1
#
#
#for number in range(1,11):
 #   print(number)
#
#
#for slice in range(0,28):
#    print("eating slice number:", slice)
#
#
#arrived = False

#while not arrived:
#    answer = input("Are we there yet?")
#    if answer == "yes":
#        arrived = True

#print("yay!")
#
#
#while True:
#   answer = input("are we nearly there yet? (answer yes or no) ")
#    if answer == "yes":
 #       break

#print('yay')
#
#
secret_number = 7
max_times = 4
actual_num_times = 0
while True:
    answer = int(input("guess a number between 1 and 10"))
    if answer == secret_number:
        print("you guess it" , answer)
        break
    if actual_num_times == max_times:
        print("failed - didnt guess the number")
        break