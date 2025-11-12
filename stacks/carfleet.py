class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed
    
    def __abs__(self):
        return self.position


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [Car(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=abs, reverse=True)

        current = 0
        counter = 0

        for car in cars:
            time = (target - car.position) / car.speed
            if time > current:
                current = time
                counter += 1
        
        return counter
        