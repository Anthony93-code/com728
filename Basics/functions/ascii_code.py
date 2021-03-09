print("Program Started!")
print("Please enter a standard character:")
std_chr = input()

if len(std_chr) == 1:
    value = ord(std_chr)
    print(f"The ASCII code for {std_chr} is {value}.")
else:
    print("Input Error!")

print("Program Ended!")
