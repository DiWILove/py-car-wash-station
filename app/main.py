from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_income: float = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                one_car_income: float = (car.comfort_class *
                                         (self.clean_power - car.clean_mark) *
                                         self.average_rating /
                                         self.distance_from_city_center)
                car.clean_mark = self.clean_power
                total_income += one_car_income
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> float:
        return self.calculate_washing_price(car)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        one_car_income: float = (car.comfort_class *
                                 (self.clean_power - car.clean_mark) *
                                 self.average_rating /
                                 self.distance_from_city_center)
        return round(one_car_income, 1)

    def rate_service(self, rate: float) -> float:
        total_rate: float = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (total_rate + rate) / self.count_of_ratings
        return round(self.average_rating, 1)
