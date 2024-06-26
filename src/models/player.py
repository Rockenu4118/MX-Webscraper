import csv

class Player:
    def __init__(self, id, name, grad_year, position, height, weight, bat_hand, throw_hand, state, rating):
        self.id         = id
        self.name       = name
        self.grad_year  = grad_year
        self.position   = position
        self.height     = height
        self.weight     = weight
        self.bat_hand   = bat_hand
        self.throw_hand = throw_hand
        self.state      = state
        self.rating     = rating

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grad Year: {self.grad_year}"
    
    def log(self):
        with open('./logs/players.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.id,
                self.name,
                self.grad_year,
                self.position,
                self.height,
                self.weight,
                self.bat_hand,
                self.throw_hand,
                self.state,
                self.rating
            ])

    def log_id(self):
        with open('./logs/player_ids.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id])