class Node:
    def __init__(self, card):
        self.card = card
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_card(self, card):
        """Adds a card to the top of the pile (linked list)."""
        new_node = Node(card)
        new_node.next = self.head
        self.head = new_node

    def remove_card(self):
        """Removes a card from the top of the pile and returns it."""
        if not self.head:
            return None
        removed_card = self.head.card
        self.head = self.head.next
        return removed_card

    def peek(self):
        """Returns the top card without removing it."""
        return self.head.card if self.head else None
