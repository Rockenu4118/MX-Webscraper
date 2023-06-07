class Player:
    def __init__(self, id, name, grad_year, position, height, weight, bat_hand, throw_hand, state, rating):
        self.id = id
        self.name = name
        self.grad_year = grad_year
        self.position = position
        self.height = height
        self.weight = weight
        self.bat_hand = bat_hand
        self.throw_hand = throw_hand
        self.state = state
        self.rating = rating

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grad Year: {self.grad_year}"