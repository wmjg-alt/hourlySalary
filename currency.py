from time import perf_counter
hr2sal = {}
sal2hr = {}

class Hourly():
    def __init__(self,r,h=None):
        self.rate = r
        self.hours = h if h else 40
    def __str__(self):
        return str(self.rate) + "/hr" 

    def pay(self):
        return self.rate * self.hours

    def salary(self):
        if self.rate in hr2sal:
            return hr2sal[self.rate]
        s = self.pay() * 52
        hr2sal[self.rate] = s
        return s

class Salary():
    def __init__(self,p,h=None):
        self.pay = p
        self.hours = h if h else 40

    def __str__(self):
        return str(self.pay) +"/yr"

    def hourly(self):
        if self.pay in sal2hr:
            return sal2hr[self.pay]
        s = self.pay / (52 * self.hours)
        sal2hr[self.pay] = s
        return s

if __name__ == "__main__":
    x = Salary(66000)
    t0 = perf_counter()
    for i in range(50):
        tmp = Hourly((i))
        print(tmp,"",  x.pay - tmp.salary(),"",round(x.hourly() -tmp.rate,2), sep='\t', end='\r')
    print('                                                  ')
    print(perf_counter() - t0,)
    t2 = perf_counter()
    for i in range(50):
        tmp = Hourly((i))
        print(tmp,"",  x.pay - tmp.salary(),"",round(x.hourly() -tmp.rate,2), sep='\t', end='\r')
    print('                                                  ')
    print(perf_counter() -t2,"\t\t\t\t\t ")
    print(len(sal2hr),len(hr2sal))
    print(sal2hr)

