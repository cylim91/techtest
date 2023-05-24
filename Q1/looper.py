def looper(input_num):
    for i in range(1, input_num+1):
        str_to_print = ""
        if i % 3 == 0:
            str_to_print += "fizz"
        if i % 5 == 0:
            str_to_print += "buzz"

        if str_to_print:
            print(str_to_print)
        else:
            print(i)

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input, only integer will be accepted.")
    else:
        looper(int(user_input))
