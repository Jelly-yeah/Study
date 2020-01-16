class ListInfo(object):
    def __init__(self, lst):
        self.lst = lst

# =============================
    def add_value(self, value):
        self.lst.append(value)
        return self.lst

# -----------------------------
    def get_value(self, num):
        return self.lst[num - 1]

# -----------------------------
    def update_list(self, _list):
        return self.lst + _list

# -----------------------------
    def del_value(self):
        """last = self.lst[len(self.lst) - 1]
        self.lst.pop()
        return last"""
        return self.list.pop()


# +++++++++++++++++++++++++++++
a = ListInfo([44, 222, 111, 333, 454, 'sss', '333'])
print(a.add_value("abc"))
