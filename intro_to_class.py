import random

class ApplePack:
    number_of_apples = 0
    total_weight = 0
    def __init__(self,weight):
        self.weight = weight
        ApplePack.number_of_apples += 1
        ApplePack.total_weight += weight

while ApplePack.total_weight < 300 and ApplePack.number_of_apples <= 1000:
    apple = ApplePack(random.uniform(0.2, 0.5))

print(ApplePack.total_weight,"kg is the total weight")
print(ApplePack.number_of_apples, "is the amount of apples")