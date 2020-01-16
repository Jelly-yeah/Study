class DictClass(object):
    def __init__(self, _dict):
        self._dict = _dict

# =============================
    def del_dict(self, key):
        del self._dict[key]
        return self._dict

# -----------------------------
    def get_dict(self, key):
        return self._dict[key]

# -----------------------------
    def get_key(self):
        return list(self._dict.keys())

# -----------------------------
    def update_dict(self, d):
        d.update(self._dict)
        return self._dict


# +++++++++++++++++++++++++++++
a = DictClass({'a': 1, 'b': 2, 'c': 3})
print(a.get_key())
