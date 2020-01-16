import random
def sum(List_numbers):
    s = 0
    for i in List_numbers:
        s += i
    return s


class RedEnvelope:
    def __init__(self, AllMoney, PersonNum):
        self.AllMoney = AllMoney * 100
        self.PersonNum = PersonNum
        MoneyList = []
        # random.randint(1, self.AllMoney - (PersonNum-1)
        for i in range(0, self.PersonNum):
            if self.PersonNum == 1:
                MoneyList.append(self.AllMoney)
            else:
 

                min = 1
                max = (self.AllMoney - sum(MoneyList)) - (self.PersonNum - len(MoneyList) - 1) - random.randint(self.PersonNum+3,self.PersonNum-3)
                money = random.randint(min, max)
                    
            MoneyList.append(money)
        
        self.monylist = MoneyList
        
    def GrabRedEnvelope(self):
        pass


a = input()

b = input()

Instantiation_Red_Envelope = RedEnvelope(int(a), int(b))
print(Instantiation_Red_Envelope.monylist)