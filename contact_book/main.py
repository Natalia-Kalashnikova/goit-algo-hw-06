"""This script demonstrates usage of the AddressBook and Record classes to manage contact data."""

from models.record import Record
from book.addressbook import AddressBook

# Create a new address book
book = AddressBook()

# Create a record for John and add multiple phone numbers
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Create and add a record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all records in the address book
print("All contacts:\n", book)

# Find and update a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Print updated record for John
print("\nAfter editing John's phone:")
print(john)

# Find a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"\nFound phone in John's record: {found_phone}")

# Delete Jane's record from the address book
book.delete("Jane")

# Print address book after deletion
print("\nAfter deleting Jane:")
print(book)
