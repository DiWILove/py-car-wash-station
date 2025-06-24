class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        print(comfort_class, clean_mark, brand)


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        one_car_income = 0
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                one_car_income = (car.comfort_class * (self.clean_power - car.clean_mark)
                                  * self.average_rating / self.distance_from_city_center)
                car.clean_mark = self.clean_power
            total_income += one_car_income
        return round(total_income, 1)

    def calculate_washing_price(self, car) -> None:
        one_car_income = (car.comfort_class * (self.clean_power - car.clean_mark)
                          * self.average_rating / self.distance_from_city_center)
        return round(one_car_income, 1)

    def wash_single_car(self, car):
        return self.calculate_washing_price(car)

    def rate_service(self, rate: float) -> float:
        total_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (total_rate + rate) / (self.count_of_ratings)
        return round(self.average_rating, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])
wash_station.rate_service(5)

###calculate_washing_price - method, that calculates cost for a single car
# wash, cost is calculated as: car's comfort class * difference between
# wash station's clean power and car's clean mark * car wash station
# rating / car wash station distance to the center of the city,
# returns number rounded to 1 decimal;
