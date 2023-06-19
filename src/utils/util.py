
def time_elapsed(start_time, end_time):
    time_elapsed = end_time - start_time
    mins = int(time_elapsed / 60)
    secs = time_elapsed % 60
    return f"{mins}min {secs:.2f}sec"
    
def time_elapsed_ms(start_time, end_time):
    time_elapsed = end_time - start_time
    return f"{float(time_elapsed):.3f}sec"
    
def convert_height(height):
    feet = height.split("-")[0]
    inches = height.split("-")[1]

    return (int(feet) * 12) + int(inches)