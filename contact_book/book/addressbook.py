"""This module defines the AddressBook class for managing contact records."""

from collections import UserDict

class AddressBook(UserDict):
    """Stores and manages contact records (Record instances)"""
    def add_record(self, record):
        """Add a new contact record to the address book."""
        self.data[record.name.value] = record

    def find(self, name):
        """Find and return a record by name"""
        return self.data.get(name)

    def delete(self, name):
        """Delete a record by name"""
        if name in self.data:
            del self.data[name]

    def __str__(self):
        """String representation of the entire address book"""
        if not self.data:
            return "AddressBook is empty."
        return "\n".join(str(record) for record in self.data.values())
