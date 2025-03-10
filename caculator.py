class Calculaotr:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def batch_sub(self, a_list, b_list):
        re_list = []
        for i in range(len(a_list)):
            re_list.append(self.sub(a_list[i], b_list[i])) 
        return re_list
    
    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print('b can not be 0')
        else:
            return a / b

        
# create a calculator object
c = Calculaotr()
print(c.sub(2, 1))
print(c.batch_sub([3,2,1], [2,3,4]))    