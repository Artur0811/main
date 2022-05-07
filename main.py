class Season:
    def __init__(self, mes):
        self.mes = mes
    def __str__(self):
        a = ''
        if 3 <= self.mes <= 5:
            a = "spring"
        elif 6 <= self.mes <= 8:
            a= "summer"
        elif 9 <= self.mes <= 11:
            a = "autumn"
        else:
            a = 'winter'
        return "Month {}, {}, {}".format(self.mes, self.__class__.__name__,a)

class Autumn(Season):
    def __init__(self, mes, dic):
        self.dic = dic
        self.dic[mes] = ""
        self.mes = mes

    def __getitem__(self, item):
        return self.dic[item]
    def __setitem__(self, key, value):
        self.dic[key]=value
    def __delattr__(self, item):
        del self.dic[item]

    def get_dict(self):
        return self.dic
    def __len__(self):
        return len(self.dic)
    def __call__(self, *args, **kwargs):
        if args == 1:
            return "Sep"
        elif args == 2:
            return "Oct"
        else:
            return "Nov"
sn = Season(5)
print(sn)
dic = {10: "cold wind", 9: "red sheet"}
at = Autumn(11, dic)
print(at)
at[11] = "rain"
temp = at.get_dict()
for k in temp:
    print(temp[k])
print(len(temp), at(3))