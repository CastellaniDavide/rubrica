"""Rubrica
"""
import json
from os import path
import json

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2021-12-17"

class rubrica:
	def __init__ (self, debug=False):
		"""Where it all begins
		"""
		self.debug = debug
		self.source_path = path.dirname(path.abspath(__file__))
		if self.debug: print("Source path:", self.source_path)

		self.get_contacts()
		self.print()

	def get_contacts(self):
		"""Get contacts
		"""
		self.contacts = json.load(open(path.join(self.source_path, "..", "src", "contacts.json"), "r"))
		if self.debug: print("Data loaded: " + str(self.contacts))

	def print(self):
		"""Print contacts
		"""
		for contact in self.contacts["contacts"]:
			print("id: " + str(contact["id"]))
			print("name: " + contact["name"])
			print("surname: " + contact["surname"])
			print("phone numbers:")
			for phone in contact["phone numbers"]:
				print(f"\tnumber: {phone['number']}")
				print(f"\ttype: {phone['type']}")
				print()
			print("emails:")
			for email in contact["emails"]:
				print(f"\taddress: {email['address']}")
				print(f"\ttype: {email['type']}")
				print()
			print()
		
		if self.debug: print("Data printed")
		
if __name__ == "__main__":
	rubrica(debug=True)
