import csv 

class Doctor:
    csv_file = "static/data/doctor.csv"
    
    @classmethod
    def get_doctor_name(cls, doctor_id):
        with open(cls.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['doctor_id'] == str(doctor_id):
                    return row['name']
        return None

    @classmethod
    def get_all_doctors(cls):
        doctors = []
        with open(cls.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                doctors.append(row)
        return doctors
