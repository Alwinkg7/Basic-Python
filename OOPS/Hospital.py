#Hospital

class hospital:
    def __init__(self):
        self.hname = " "
        self.hphone = " "
        self.hmail = " "
    def setHospital(self):
        self.hname = input("Enter your hospital name: ")
    def setPhone(self):
        self.hphone = input("Enter your hospital phone number: ")
    def setMail(self):
        self.hmail = input("Enter your hospital mail address: ")
    def displayHospital(self):
        print("***** HOSPITAL *****")
        print("Name of the Hospital: ", self.hname)
        print("Contact Phno: ", self.hphone)
        print("Mail ID: ", self.hmail)
class Location(hospital):
    def __init__(self):
        self.hLocation = ""
        self.haddress = " "
        self.hstate = " "
    def setLocation(self):
        obj.setHospital()
        obj.setPhone()
        obj.setMail()
        self.haddress = input("Enter your hospital address: ")
        self.hstate = input("Enter your hospital state: ")

    def displayLocation(self):
        print("***** LOCATION *****")
        print("Address: ", self.haddress)
        print("State: ",self.hstate)

class DoctorSection(hospital):
    def __init__(self):
        self.sec_name = ""
        self.dr_name = ""
    def setSection(self):
        obj1.setLocation()
        self.sec_name = input("Enter field of Specialization: ")
        self.dr_name = input("Enter your doctor name: ")
    def displaySection(self):
        print("***** SPECIALIZATION *****")
        print("Specialization: ", self.sec_name)
        print("Consulting Doctor: Dr.",self.dr_name)

class PatientDetails(DoctorSection):
    def __init__(self):
        self.pname = ""
        self.age = ""
        self.Mobile = ""
    def setDetails(self):
        obj2.setSection()
        self.pname = input("Enter patient name: ")
        self.age = input("Enter patient age: ")
        self.Mobile = input("Enter patient mobile number: ")
    def displayDetails(self):
        print("***** DETAILS *****")
        print("Name: ", self.pname)
        print("Age: ", self.age)
        print("Mobile: ", self.Mobile)


obj = hospital()
obj1 = Location()
obj2 = DoctorSection()
obj3 = PatientDetails()

obj3.setDetails()

obj.displayHospital()
obj1.displayLocation()
obj2.displaySection()
obj3.displayDetails()