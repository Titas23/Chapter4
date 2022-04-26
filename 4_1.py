# def pay (wage, hours) :
#     amount = 0 
#     if hours <= 40: 
#         amount = wage * hours
#     else: 
#         amount = (wage * 40) + (1.5) * wage *(hours -40)
#     return amount

# hourly_wage = eval(input("Enter the hourly wage: "))
# hours_worked = eval(input("Enter the hours worked: "))

# result= pay(hourly_wage, hours_worked)

# print("Earnings: ${0:,.2f}".format(result))

# def is_vowel_word(word): 
#     word = word.upper()
#     vowels = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowels: 
#         if vowel not in word: 
#             return False
#     return True

# word = input("Enter a word: ")
# if is_vowel_word(word):
#     print(word, "contains every vowel.")
# else: 
#     print(word, "does not contain every vowel")

def main ():
    x = 2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")

def trivial():
    x = 3
    print(str(x) + ": function trivial")

main()

