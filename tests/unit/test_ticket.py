import unittest
from zoo_ticketing import Ticket, AdultTicket, ConcessionTicket  # Adjust import to match your project structure

class TestTicket(unittest.TestCase):

    def test_adult_ticket_cost(self):
        """Test that the cost of an adult ticket is 20"""
        adult_ticket = AdultTicket()
        self.assertEqual(adult_ticket.cost, 20)

    def test_concession_ticket_cost(self):
        """Test that the cost of a concession ticket is 10"""
        concession_ticket = ConcessionTicket()
        self.assertEqual(concession_ticket.cost, 10)

    def test_ticket_cost_is_set_correctly(self):
        """Test that the cost of a general ticket can be set"""
        ticket = Ticket(15)
        self.assertEqual(ticket.cost, 15)

if __name__ == '__main__':
    unittest.main()
