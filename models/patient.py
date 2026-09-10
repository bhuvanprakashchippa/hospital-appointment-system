class Patient:
    def __init__(self, patient_id, name, age, phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        return (
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Phone: {self.phone}"
        )