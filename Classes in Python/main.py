#Part One
class Stadium:
    """class to discribe statiums"""

    def __init__(self, name, city_state, capacity):
        """Initializer of the stadium class"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity
        

    def describe_stadium(self):
        """describes the stadium"""
        print("The " + self.name + " is located in " + self.city_state + " and holds " + self.capacity + " fans.")
    
    def sport_played(self, sport):
        """Describes the sports played in statium"""
        self.sport = sport
        print("The following sport is mainly played in this stadium: " + self.sport)

    def seats_available(self, seats):
        """Describes the seats available"""
        self.seats = seats
        print("There are " + self.seats + " seats still available for tonight's game.")

stadium1 = Stadium("Mercedes Benz Arena", "Atlanta, GA", "70,000")
stadium1.describe_stadium()
stadium1.sport_played("Football")
stadium1.seats_available("15,000")