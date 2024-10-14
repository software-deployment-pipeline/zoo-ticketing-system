class Ticket:
    def __init__(self, cost):
        self.cost = cost

        
class AdultTicket(Ticket):
    def __init__(self):
        super().__init__(20)
    

class ConcessionTicket(Ticket):
    def __init__(self):
        super().__init__(10)
    
    
class ZooTicketing():
    def __init__(self):
        self.tickets = []

    def __get_adult_count(self):        
        return sum(1 for ticket in self.tickets if isinstance(ticket, AdultTicket))

    def __get_concession_count(self):
        return sum(1 for ticket in self.tickets if isinstance(ticket, ConcessionTicket))

    def get_total_cost(self):
        return sum(ticket.cost for ticket in self.tickets)

    def add_tickets(self, ticket_type, count):
        for _ in range(count):
            self.tickets.append(ticket_type)
    
    def print_ticket_summary(self):
        adult_count = self.__get_adult_count()
        con_count = self.__get_concession_count()
        total_cost = self.get_total_cost()
        total_tickets = adult_count + con_count
        
        print(f"{'Ticket Type':<20}{'Quantity':<10}{'Price per Ticket':<20}{'Total Price':<15}")
        print("="*65)
        print(f"{'Adult Tickets':<20}{adult_count:<10}{'$20':<20}{f'${adult_count * 20}':<15}")
        print(f"{'Concession Tickets':<20}{con_count:<10}{'$10':<20}{f'${con_count * 10}':<15}")
        print("="*65)
        print(f"{'Total Tickets':<20}{total_tickets:<10}{'':<20}{f'${total_cost}':<15}")
        print()


def main():
    zoo_ticketing = ZooTicketing()
    buy_more = True
    print("Hello my homie testing test server2 welcome to Swinburne Zoo. Please select ticket.")
    print()

    while buy_more:
        option_ticket = input("Ticket option (adult/concession): ")
        if option_ticket == "adult".lower():
            ticket_type = AdultTicket()
        elif option_ticket == "concession".lower():
            ticket_type = ConcessionTicket()
        else:
            print("Invalid option, please enter the appropriate value.")
            continue

        
        while True:
            try:
                option_quantity = int(input("Quantity (max 10): "))
                if 1 <= option_quantity <= 10:
                    break 
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print()
        
        print("SUMMARY")
        zoo_ticketing.add_tickets(ticket_type, option_quantity)

        zoo_ticketing.print_ticket_summary()

        buy_more_input = input("Add more tickets? (yes or no): ").lower()
        print()
        if buy_more_input == "no":
            buy_more = False

    print(f"Total Cost: ${zoo_ticketing.get_total_cost()}\n")


main()