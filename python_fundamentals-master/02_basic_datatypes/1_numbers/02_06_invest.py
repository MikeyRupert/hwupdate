'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.
1,000,000∗(1+0.05) ^ 5 −$1,000,000 =$276,281.60
​	
'''
class Moneys():

    def __init__(self,amount,rate,years):
        self.amount = amount
        self.rate = rate
        self.years = years
    
    def future(self):
        return float((self.amount*(1+self.rate)**self.rate*self.years)-self.amount)
    
    def __str__(self):
        return f'you will make {self.future()} in {self.years} with {self.rate} rate.'
        
m = Moneys(1000000,0.05,3)
print(m.__str__())