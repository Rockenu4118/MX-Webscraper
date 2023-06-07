class Util:

    @staticmethod
    def time_elapsed(start_time, end_time):
        time_elapsed = end_time - start_time
        return f"{float(time_elapsed):.2f}"
    
    @staticmethod
    def time_elapsed_ms(start_time, end_time):
        time_elapsed = end_time - start_time
        return f"{float(time_elapsed):.3f}"