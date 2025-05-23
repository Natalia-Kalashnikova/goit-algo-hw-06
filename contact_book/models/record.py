"""This module defines the Record class for managing contact data."""

from models.fields import Name, Phone

class Record:
    """ Represents a contact record with a name and a list of phone numbers"""
    def __init__(self, name):
        self.name = Name(name) # Store contact name as a Name object
        self.phones = []       # List of Phone objects

    def add_phone(self, phone_number):
        """Add a new phone number to the record"""
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """Remove a phone number from the record by value"""
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        """Replace an existing phone number with a new one"""
        phone = self.find_phone(old_number)
        if not phone:
            raise ValueError("Old phone number not found.")
        self.phones.remove(phone)
        self.phones.append(Phone(new_number))

    def find_phone(self, phone_number):
        """Find and return a Phone object by value"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        """String representation of the record"""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
