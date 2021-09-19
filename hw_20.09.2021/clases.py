class Clients:
    def __init__(self,phone, name) -> None:
        self.phone = phone
        self.name = name

class Cars:
    def __init__(self,model, number) -> None:
        self.model = model
        self.number = number

class Drivers:
    def __init__(self,name, car, rating) -> None:
        self.name = name
        self.car = car
        self.rating = rating


class Track:
    def __init__(self,where,where_t) -> None:
        self.where = where
        self.where_t = where_t

class Order:
    def __init__(self,data,track,client,driver,cost) -> None:
        self.data = data
        self.track = track
        self.client = client
        self.driver = driver
        self.cost = cost


