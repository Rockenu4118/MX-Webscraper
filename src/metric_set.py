class MetricSet:
    def __init__(self, player_id, exit_velo, of_velo, if_velo, sixty, fb_velo):
        self.player_id = player_id
        self.exit_velo = exit_velo
        self.of_velo = of_velo
        self.if_velo = if_velo
        self.sixty = sixty
        self.fb_velo = fb_velo

    def __str__(self):
        return f"Metric set of player #{self.player_id}"