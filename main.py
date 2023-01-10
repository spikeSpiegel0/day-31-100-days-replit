red = "\033[31m"
blue = "\033[34m"
white = "\033[37m"
green = "\033[32m"
purple = "\033[35m"
yellow = "\033[33m"
reset = "\033[0m"

title = f"{red}={white}={blue}= {yellow}Music App{reset} {blue}={white}={red}={reset}"
centered_text = title.center(90)
print(centered_text)

play = f"▶️🔥 Eminem"
print(f"{play: >5}")
song = f"Slim shady"
print(f"{yellow}{song: >14}{reset}")
print()
print()
prev = f"PREV"
next = f"NEXT"
pause = f"PAUSE"
print(f"{prev}")
print(f"{green}{next: >10}")
print(f"{purple}{pause: >17}")
print()
print()
print()
print()
title2 = f"{white}WELCOME TO{reset}"
name = f"{blue}--    ARMBOOK    --{reset}"
print(f"{title2: ^60}")
print(f"{name: ^60}")

text3 = f"{yellow}Definetely not a rip off of"
text4 = "a certain other social"
text5 = f"networking site.{reset}"
print(f"{text3: >97}")
print(f"{text4: >92}")
print(f"{text5: >95}")
print()
text6 = (f"{red}Honest.{reset}")
print(f"{text6: ^70}")
print()
text7 = (f"Username:")
print(f"{text7: ^60}")
text8 = (f"Password:")
print(f"{text8: ^60}")