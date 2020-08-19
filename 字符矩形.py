def draw_char_rectangle(length, width, char, fill):
    if fill == 1:
        for i in range(length):
            for j in range(width):
                print(char, end='')
            print("")
    elif fill == 0:
        for i in range(0, length):
            if i == 0 or i == length - 1:
                for j in range(width):
                    print(char, end='')
                print('')
            elif i != 0 or i != length - 1:
                for j in range(0, width):
                    if j == 0 or j == width - 1:
                        print(char, end='')
                    else:
                        print(" ", end='')
                print("")


l = int(input("length(|):"))
w = int(input("width(--):"))
while 1:
    char = input("Char: ")
    if len(char) == 1:
        break
    else:
        continue
while 1:
    fill = int(input("Fill? (Yes -> 1; No -> 0) :: "))
    if fill == 1 or fill == 0:
        break
    else:
        continue
draw_char_rectangle(l, w, char, fill)
