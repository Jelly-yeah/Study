def level(score):
    if score < 60:
        print("Fail")
    elif score >= 60 and score < 70:
        print("bad")
    elif score >= 70 and score < 80:
        print("commonly")
    elif score >= 80 and score < 90:
        print("good")
    elif score >= 90:
        print("excellent") 

print(level(29))