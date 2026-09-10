class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        return (
            f"Doctor ID: {self.doctor_id}, "
            f"Name: Dr. {self.name}, "
            f"Specialization: {self.specialization}"
        )