pan = input()
def pan():
      if ord(pan)==97 or ord(pan)==65  or ord(pan)==69 or ord(pan)==101 or ord(pan)==73 or ord(pan)==105 or ord(pan)==79 or ord(pan)==111 or ord(pan)==85 or ord(pan)==117:
            return "元音"
      if ord(pan)==97 or ord(pan)==101 or ord(pan)==105 or ord(pan)==111 or ord(pan)==117:
            return"小写"
      else:
            return"大写"
      if ord(pan)!=97 or ord(pan)!=65  or ord(pan)!=69 or ord(pan)!=101 or ord(pan)!=73 or ord(pan)!=105 or ord(pan)!=79 or ord(pan)!=111 or ord(pan)!=85 or ord(pan)!=117:
            return "辅音"
