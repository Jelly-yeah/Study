def level(score):
    if score >= 90 and score <= 100:
        return "Excellent!"
    elif score < 90 and score >= 80:
        return "Good"
    elif score < 90 and score >= 70:
        return "Medium"
    elif score < 70 and score >= 60:
        return "Pass"
    elif score < 60 and score >= 0:
        return "Fill"
    elif score < 0 or score >100:
        return "EEROR -- # Out of Range #"
    else:
        return "EEROR -- # Plese Input The Number #"

if __name__ == "__main__":
    while 1:
        ipt = input("Please input your score:")
        level(ipt)