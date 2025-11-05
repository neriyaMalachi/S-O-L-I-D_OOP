from I_interface_segregation.bad.classes.Machine import Machine


class Printer(Machine):
    def print_doc(self):
        print("Printing...")
    def scan_doc(self):
        print("Can't scan!")  # מיותר
    def fax_doc(self):
        print("Can't fax!")   # מיותר