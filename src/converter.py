class Converter:

    @staticmethod
    def height(height):
        feet = height.split("-")[0]
        inches = height.split("-")[1]

        return (int(feet) * 12) + int(inches)