f = None
try:
    f = open("X:\\vv\\a.txt", "r", encoding='utf-8')
    f.read()
except FileNotFoundError as e:
    print('FileNotFound!')
finally:
    if f:
        f.close()