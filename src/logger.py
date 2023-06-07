import csv

class Logger:
    
    @staticmethod
    def log_id(id):
        with open('./logs/player_ids.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id])

    @staticmethod
    def log_player(player):
        with open('./logs/players.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                player.id,
                player.name,
                player.grad_year,
                player.position,
                player.height,
                player.weight,
                player.bat_hand,
                player.throw_hand,
                player.state,
                player.rating
            ])

    @staticmethod
    def log_metric_set(metric_set):
        with open('./logs/metric_sets.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                metric_set.player_id,
                metric_set.exit_velo,
                metric_set.of_velo,
                metric_set.if_velo,
                metric_set.sixty,
                metric_set.fb_velo,
            ])

    @staticmethod
    def log_write_performance(time):
        with open('./logs/write_performance.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time])