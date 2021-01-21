class Train:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bookATicket(self):
        print(f"Ticket/s for {self.name} is/are booked.")

    def getStatus(self, no_of_seats):
        self.no_of_seats = no_of_seats
        print(f"Status for {self.name}'s tickets at {self.no_of_seats} seat/seats is confirmed.")

    def getFare(self):
        print(f"{self.name} has paid the amount for the ticket.")

aditya = Train("Aditya", 18)
aditya.bookATicket()
aditya.getStatus(4)
aditya.getFare()
