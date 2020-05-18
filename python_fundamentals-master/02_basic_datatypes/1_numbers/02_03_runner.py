'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
class Runner():

    def __init__(self,dis,time):
        self.dis = dis
        self.time = time

    def __float__(self):
        km = self.dis*1.6
        hr = self.time/60
        return format(float(km)/hr,'1.3f')
        
        
g = Runner(10,30.5)
print(f'The average speed is {g.__float__()} kilometers per hour.')