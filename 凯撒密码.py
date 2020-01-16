# -*- coding: utf-8 -*-
def encrypt(_str, offset):
    Bigs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_str = "".join(     [ Bigs[  (ord( i ) - 65 + offset  ) % 26  ] for i in _str  ]    )
    return new_str
def decrypt(_str, offset):
    Bigs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_str = "".join(     [ Bigs[  (ord( i ) - 65 - offset ) % 26  ] for i in _str   ]    )
    return new_str

if __name__ == "__main__":
    # print(decrypt("GDJ", 5))
    print(encrypt("ATTAK", 2))
