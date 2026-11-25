#Qu 1
   
# # Number input lenge
# num = float(input("Enter a number: "))

# # Square calculate karenge
# square = num * num

# print("Square is:", square)


#Qu 2

# a = input("Enter first value (a): ")
# b = input("Enter second value (b): ")

# # Third variable (temp) use karke swap karenge
# temp = a
# a = b
# b = temp

# print(f"After swapping: a = {a}, b = {b}")



# Qu 3

# base = float(input("Enter base: "))
# height = float(input("Enter height: "))

# # Area ka formula apply karenge
# area = 0.5 * base * height

# print("Area of Triangle is:", area)


#Qu 4

# km = float(input("Enter distance in KM: "))

# # KM ko MM me convert karenge
# mm = km * 1000000

# print("Distance in MM:", mm)


#Qu 5

# n1 = float(input("Enter 1st number: "))
# n2 = float(input("Enter 2nd number: "))
# n3 = float(input("Enter 3rd number: "))

# # Average nikalenge
# avg = (n1 + n2 + n3) / 3

# print("Average is:", avg)


#QU 6

# celsius = float(input("Enter temperature in Celsius: "))

# # Fahrenheit formula apply karenge
# fahrenheit = (9/5) * celsius + 32

# print("Temperature in Fahrenheit:", fahrenheit)


#QU 7 

# char = input("Enter a character: ")

# # ord() function ASCII value deta hai
# ascii_value = ord(char)

# print(f"ASCII value of '{char}' is:", ascii_value)


#Qu 8 

# basic = float(input("Enter Basic Salary: "))

# # Given values calculate karenge
# ta = 0.10 * basic
# pf = 0.078 * basic
# da = 500

# # Formulas as per question
# gs = basic + da + ta
# ns = gs - pf

# print("Gross Salary:", gs)
# print("Net Salary:", ns)


#Qu 9

# num = int(input("Enter a 3-digit number: "))

# # Modulus (%) aur Floor Division (//) ka use karenge
# d1 = num % 10      # Last digit alag karega
# num = num // 10    # Last digit ko remove karega

# d2 = num % 10      # Middle digit alag karega
# d3 = num // 10     # First digit bachegi

# # Logic to reverse and sum
# reverse_num = (d1 * 100) + (d2 * 10) + d3
# digit_sum = d1 + d2 + d3

# print("Reverse is:", reverse_num)
# print("Sum of digits:", digit_sum)


#QU 10

# s1 = float(input("Subject 1 marks: "))
# s2 = float(input("Subject 2 marks: "))
# s3 = float(input("Subject 3 marks: "))
# s4 = float(input("Subject 4 marks: "))
# s5 = float(input("Subject 5 marks: "))

# # Total aur Percentage calculation
# total = s1 + s2 + s3 + s4 + s5
# percentage = (total / 500) * 100

# print("Total Marks:", total)
# print("Percentage:", percentage, "%")

#QU 11  (A)

# num = float(input("Enter a number: "))

# # if-elif-else structure use karenge
# if num > 0:
#     print("The number is Positive")
# elif num < 0:
#     print("The number is Negative")
# else:
#     print("The number is Zero")


# (B)


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Remainder check karne ke liye modulus (%) use karenge
# if num1 % num2 == 0:
#     print(f"{num1} is divisible by {num2}")
# else:
#     print(f"{num1} is NOT divisible by {num2}")


#qu 12  (A)

# num = int(input("Enter a 3-digit number: "))

# # Q9 ke tarah digits alag karenge
# original_num = num
# d1 = num % 10
# num = num // 10
# d2 = num % 10
# d3 = num // 10

# reverse_num = (d1 * 100) + (d2 * 10) + d3

# # Check karenge original number aur reverse same hain ya nahi
# if original_num == reverse_num:
#     print(f"{original_num} is a Palindrome number")
# else:
#     print(f"{original_num} is NOT a Palindrome number")

# (B)


# num = int(input("Enter a 3-digit number: "))

# original_num = num
# d1 = num % 10
# num = num // 10
# d2 = num % 10
# d3 = num // 10

# # Har digit ka cube karke sum karenge
# armstrong_sum = (d1**3) + (d2**3) + (d3**3)

# if original_num == armstrong_sum:
#     print(f"{original_num} is an Armstrong number")
# else:
#     print(f"{original_num} is NOT an Armstrong number")

#QU 13

# num = int(input("Enter a 3-digit number: "))

# # Digits ko separate karenge
# d1 = num % 10
# num = num // 10
# d2 = num % 10
# d3 = num // 10

# # max() function se sabse bada digit find karenge
# greatest = max(d1, d2, d3)

# print("The greatest digit is:", greatest)


# (B)

# year = int(int(input("Enter a year: ")))

# # Leap year ki conditions check karenge
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is NOT a Leap Year")


#Qu 14

# char = input("Enter a character: ").lower() # Lowercase me convert kiya simplify karne ke liye

# # Check karenge agar character alphabetic hai
# if char.isalpha() and len(char) == 1:
#     if char in ['a', 'e', 'i', 'o', 'u']:
#         print(f"'{char}' is a Vowel")
#     else:
#         print(f"'{char}' is a Consonant")
# else:
#     print("Please enter a valid single alphabet.")


# # (B)

# char = input("Enter a character: ")

# # isupper() aur islower() methods ka use karenge
# if char.isupper():
#     print(f"'{char}' is in Uppercase")
# elif char.islower():
#     print(f"'{char}' is in Lowercase")
# else:
#     print(f"'{char}' is not an alphabet letter")


 #QU 15

# last_month = float(input("Enter last month unit: "))
# current_month = float(input("Enter current month unit: "))

# # Net consumed units nikalenge
# units = current_month - last_month
# bill = 0

# # Slab wise calculation karenge
# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)
# elif units <= 300:
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 4)
# # else:
# #     bill = (100 * 2) + (100 * 3) + (100 * 4) + ((units - 300) * 5)

# # print(f"Total consumed units: {units}")
# # print(f"Total Electricity Bill Amount: Rs. {bill}")


# # (B)

# # s1 = float(input("Enter Subject 1 marks: "))
# # s2 = float(input("Enter Subject 2 marks: "))
# # s3 = float(input("Enter Subject 3 marks: "))

# # avg = (s1 + s2 + s3) / 3

# # # Dono conditions fulfill honi chahiye
# # if (s1 > 75 and s2 > 75 and s3 > 75) and avg > 80:
# #     print("Result: PASS")
# # else:
# #     print("Result: FAIL")



# #QU 16

# # num = int(input("Enter a number: "))
# # factorial = 1

# # if num < 0:
# #     print("Factorial does not exist for negative numbers")
# # elif num == 0:
# #     print("Factorial of 0 is 1")
# # else:
# #     # loop chala kar multiply karenge
# #     for i in range(1, num + 1):
# #         factorial = factorial * i
# #     print(f"Factorial of {num} is {factorial}")


# # #(B)

# # num = int(input("Enter a number for its table: "))

# # # 1 se 10 tak loop chalega
# # for i in range(1, 11):
# #     print(f"{num} x {i} = {num * i}")


# #Qu 17

# # n = 25
# # a, b = 0, 1
# # count = 0

# # print("Fibonacci series upto first 25 elements:")
# # while count < n:
# #     print(a, end=" ")
# #     # Value update karne ka logic
# #     nth = a + b
# #     a = b
# #     b = nth
# #     count += 1
# # print() # New line ke liye


# # (B)

# # limit = int(input("Enter the maximum value limit: "))
# # a, b = 0, 1

# # print(f"Fibonacci series upto limit {limit}:")
# # while a <= limit:
# #     print(a, end=" ")
# #     nth = a + b
# #     a = b
# #     b = nth
# # print()


# #QU 18

# num = int(input("Enter any number: "))
# temp = num
# num_str = str(num)
# n = len(num_str) # Number of digits count karega
# armstrong_sum = 0

# while temp > 0:
#     digit = temp % 10
#     armstrong_sum += digit ** n # Digit ki power n karenge
#     temp //= 10

# if num == armstrong_sum:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is NOT an Armstrong number")

#  #(B)

# num = int(input("Enter any number: "))
# temp = num
# reverse_num = 0

# while temp > 0:
#     digit = temp % 10
#     reverse_num = (reverse_num * 10) + digit
#     temp //= 10

# # if num == reverse_num:
# #     print(f"{num} is a Palindrome number")
# # else:
# #     print(f"{num} is NOT a Palindrome number")


# #QU 19

# num = int(input("Enter a number: "))
# divisor_sum = 0

# for i in range(1, num):
#     if num % i == 0:
#         divisor_sum += i

# if divisor_sum == num:
#     print(f"{num} is a Perfect Number")
# else:
#     print(f"{num} is NOT a Perfect Number")


# (B)

# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))

# # # Dono me se maximum number se start karenge
# # max_num = max(a, b)

# # while True:
# #     if max_num % a == 0 and max_num % b == 0:
# #         lcm = max_num
# #         break
# #     max_num += 1

# # print(f"LCM of {a} and {b} is:", lcm)


# #QU 20

# # lower = int(input("Enter lower limit: "))
# # upper = int(input("Enter upper limit: "))

# # print(f"Prime numbers between {lower} and {upper} are:")
# # for num in range(lower, upper + 1):
# #     if num > 1:
# #         for i in range(2, int(num**0.5) + 1):
# #             if (num % i) == 0:
# #                 break
# #         else:
# #             print(num, end=" ")
# # print()



# # (B)

# # lower = int(input("Enter lower limit: "))
# # upper = int(input("Enter upper limit: "))

# # print(f"Perfect numbers between {lower} and {upper} are:")
# # for num in range(lower, upper + 1):
# #     divisor_sum = 0
# #     for i in range(1, num):
# #         if num % i == 0:
# #             divisor_sum += i
# #     if divisor_sum == num:
# #         print(num, end=" ")
# # print()


# #QU 21

# # Function to calculate factorial
# def get_factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# # Main function with argument and return value
# def is_strong(num):
#     temp = num
#     total_sum = 0
#     while temp > 0:
#         digit = temp % 10
#         total_sum += get_factorial(digit)
#         temp //= 10
#     return total_sum == num

# # User Input
# number = int(input("Enter a number: "))
# if is_strong(number):
#     print(f"{number} is a Strong Number")
# else:
#     print(f"{number} is NOT a Strong Number")



# (B)

# def is_palindrome(num):
#     temp = num
#     reverse_num = 0
#     while temp > 0:
#         digit = temp % 10
#         reverse_num = (reverse_num * 10) + digit
#         temp //= 10
#     return num == reverse_num

# # User Input
# number = int(input("Enter a number: "))
# if is_palindrome(number):
#     print(f"{number} is a Palindrome Number")
# else:
#     print(f"{number} is NOT a Palindrome Number")


# #QU 22

# def check_prime(num):
#     if num <= 1:
#         print(f"{num} is NOT a Prime Number")
#         return
    
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
            
#     if is_prime:
#         print(f"{num} is a Prime Number")
#     else:
#         print(f"{num} is NOT a Prime Number")

# # User Input
# number = int(input("Enter a number: "))
# check_prime(number)  # Function direct print karega, return nahi karega


# (B)

# def is_perfect(num):
#     divisor_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisor_sum += i
#     return divisor_sum == num

# # User Input
# number = int(input("Enter a number: "))
# if is_perfect(number):
#     print(f"{number} is a Perfect Number")
# # else:
# #     print(f"{number} is NOT a Perfect Number")


# #QU 23

# # 10 elements ki list user se lenge
# my_list = []
# print("Enter 10 elements for the list:")
# for i in range(10):
#     element = int(input(f"Element {i+1}: "))
#     my_list.append(element)

# print("Original List:", my_list)

# # Bubble Sort Algorithm
# n = len(my_list)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if my_list[j] > my_list[j+1]:
#             # Elements swap karenge
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# print("Sorted List (Ascending):", my_list)


# # QU 24

# # 8 elements ki list user se lenge
# my_list = []
# print("Enter 8 elements for the list:")
# for i in range(8):
#     element = int(input(f"Element {i+1}: "))
#     my_list.append(element)

# search_item = int(input("Enter the element you want to search: "))

# # Linear Search logic
# found = False
# for i in range(len(my_list)):
#     if my_list[i] == search_item:
#         print(f"Element found at index position: {i}")
#         found = True
#         break

# if not found:
#     print("Element is NOT present in the list.")



# #Qu 25

# # Elements input lene ke liye loop
# my_list = []
# n = int(input("How many elements do you want to add to the list? "))

# print(f"Enter {n} elements:")
# for i in range(n):
#     element = int(input(f"Element {i+1}: "))
#     my_list.append(element)

# print("Original List:", my_list)

# # Logic to reverse the list without built-in function
# reversed_list = []
# for i in range(len(my_list) - 1, -1, -1):
#     reversed_list.append(my_list[i])

# print("Reversed List:", reversed_list)






