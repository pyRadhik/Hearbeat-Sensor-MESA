import math

class Filter:
    def __init__(self):
        self.prevVal = 0.0

    def filter(self, value, time):
        self.prevVal = value
        return value

class SimpleFilter(Filter):
    def __init__(self, innerRadius):
        super().__init__()
        self.iRadius = innerRadius

    def filter(self, value, time):
        if math.fabs(value - self.prevVal) <= self.iRadius:
            value = self.prevVal
        return super().filter(value, time)

class RadialFilter(SimpleFilter):
    def __init__(self, innerRadius, outerRadius, descentSpeed, smoothness):
        super().__init__(innerRadius)
        self.oRadius = outerRadius
        self.descentSpeed = descentSpeed
        self.smoothness = smoothness

    def filter(self, value, time):
        distance = self.prevVal - value

        #Cleaned up the math
        if math.fabs(distance) > self.iRadius and math.fabs(distance) <= self.oRadius:
            value = self.prevVal + (1 - self.descentSpeed) * self.oRadius * time * (math.atan(distance * smoothness) * 2/math.pi)
        
        return super().filter(value, time)
