import csv 

class Doctor:
    csv_file = "static/data/doctor.csv"
    
    @classmethod
    def get_all_doctors(cls):
        doctors = []
        with open(cls.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                doctors.append(row)
        return doctors
    
    @classmethod
    def get_doctor_by_id(cls, doctor_id):
        with open(cls.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['doctor_id']) == int(doctor_id):
                    available_dates = row['available_dates'].split(',')
                    available_slots = row['available_slots'].split(',')
                    return {
                        'doctor_id': row['doctor_id'],
                        'name': row['name'],
                        'available_dates': available_dates,
                        'available_slots': available_slots
                    }
        return None
    
    @classmethod
    def search(cls, text):
        doctors = []
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["name"].lower().find(str(text).lower()) != -1 or row["specialization"].lower().find(str(text).lower()) != -1 :
                    doctors.append(row)
            if len(doctors) == 0:
                return -1   
            return doctors        
                   
