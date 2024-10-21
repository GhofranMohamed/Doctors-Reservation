import csv
import os



class Appointment:
    csv_file = os.path.join(os.path.dirname(__file__), "static/data/appointments.csv")
    
    def __init__(self,appointment_id, user_id, doctor_id, doctor_name, date, slot, phone_number):
        self.appointment_id = appointment_id
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.date = date
        self.slot = slot
        self.phone_number = phone_number

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.csv_file):
            with open(cls.csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["appointment_id", "user_id", "doctor_id", "doctor_name", "date", "slot", "phone_number"])    
    
    def save(self):
        with open(self.csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.appointment_id, self.user_id, self.doctor_id, self.doctor_name, self.date, self.slot, self.phone_number])

    @classmethod
    def get_user_appointments(cls, user_id):
        appointments = []
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["user_id"] == str(user_id):  
                    appointments.append(row)
            if len(appointments) == 0:
                return -1   
            return appointments
    @classmethod
    def get_doctor_appointments(cls, doctor_id):
        appointments = []
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["doctor_id"] == str(doctor_id):  
                    appointments.append(row)
            if len(appointments) == 0:
                return -1   
            return appointments    
    
    @classmethod
    def delete(cls,appointment_id, user_id):
        appointments = []
        with open( cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["appointment_id"] != appointment_id or row["user_id"] != user_id:
                    appointments.append(row)

        with open("static/data/appointments.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["appointment_id", "user_id", "doctor_id", "doctor_name", "date", "slot", "phone_number"])
            writer.writeheader()
            writer.writerows(appointments)
        return appointments    

    @classmethod
    def edit(cls,appointment_id, user_id, new_date, new_slot):
        appointments = []
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["appointment_id"] == appointment_id and row["user_id"] == user_id:
                    row["date"] = new_date
                    row["slot"] = new_slot
                appointments.append(row)

        with open("static/data/appointments.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["appointment_id", "user_id", "doctor_id", "doctor_name", "date", "slot", "phone_number"])
            writer.writeheader()
            writer.writerows(appointments)

          
