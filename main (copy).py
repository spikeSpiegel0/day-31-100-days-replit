red = "\033[31m"
blue = "\033[34m"
white = "\033[37m"
green = "\033[32m"
purple = "\033[35m"
yellow = "\033[33m"
reset = "\033[0m"

title = f"{white}WELCOME TO{reset}"
name = f"{blue}ARMBOOK{reset}"
text = title + name
centered_text = text.center(110)  # 80 is the width of the terminal
print(centered_text)



