class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.b !=0:
                self.b -= 1
                return True
        elif carType == 2:
            if self.m !=0:
                self.m -= 1
                return True
        elif carType == 3:
            if self.s !=0:
                self.s -= 3
                return True
        return False