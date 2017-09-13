class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for count in range(0, self.cap):
            beds.append({
                "id": count,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"

    # def all(self):
    #     for element in self.patients:
    #         print "ID: {}  Name: {}  Allergies: {}  Bed: {}".format(element.id,element.name,element.allergies,element.bed)


class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed = None
        Patient.PATIENT_COUNT +=1

    # def __str__(self):
        # return "ID: {}  Name: {}  Allergies: {}  Bed: {}".format(self.id,self.name,self.allergies,self.bed)


DB = Hospital("test", 2)
DB.admit("Mike")
DB.admit("Rhett")
DB.admit("Henry")
