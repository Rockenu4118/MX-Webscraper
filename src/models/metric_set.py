import csv

class MetricSet:
    def __init__(self, player_id, exit_velo, of_velo, if_velo, sixty, pop, fb_velo):
        self.player_id = player_id
        self.exit_velo = exit_velo
        self.of_velo   = of_velo
        self.if_velo   = if_velo
        self.sixty     = sixty
        self.pop       = pop
        self.fb_velo   = fb_velo

    def __str__(self):
        return f"Metric set of player #{self.player_id}"
    
    def log(self):
        with open('./logs/metric_sets.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.player_id,
                self.exit_velo,
                self.of_velo,
                self.if_velo,
                self.sixty,
                self.pop,
                self.fb_velo,
            ])