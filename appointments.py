import csv


class Appointment:
    csv_file = "static/data/appointments.csv"
    
    def __init__(self,appointment_id, user_id, doctor_id, doctor_name, date, time, phone_number):
        self.appointment_id = appointment_id
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.phone_number = phone_number
    
    def save(self):
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.appointment_id, self.user_id, self.doctor_id, self.doctor_name, self.date, self.time, self.phone_number])

    @classmethod
    def get_user_appointments(cls, user_id):
        appointments = []
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['user_id'] == str(user_id):  
                    appointments.append(row)
        return appointments
    
    @staticmethod
    def delete(appointment_id, user_id):
        appointments = []
        with open( "static/data/appointments.csv", mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["appointment_id"] != appointment_id or row['user_id'] != user_id:
                    appointments.append(row)

        with open("static/data/appointments.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["appointment_id", 'user_id', 'doctor_id', "doctor_name", 'date', 'time', "phone_number"])
            writer.writeheader()
            writer.writerows(appointments)
        return appointments    

    @staticmethod
    def edit(appointment_id, user_id, new_date, new_time):
        appointments = []
        with open("static/data/appointments.csv", mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['appointment_id'] == appointment_id and row['user_id'] == user_id:
                    row['date'] = new_date
                    row['time'] = new_time
                appointments.append(row)

        with open("static/data/appointments.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["appointment_id", 'user_id', 'doctor_id', "doctor_name", 'date', 'time', "phone_number"])
            writer.writeheader()
            writer.writerows(appointments)

    @staticmethod
    def get_by_id(appointment_id, user_id):
        with open('appointments.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if int(row["appointment_id"]) == appointment_id and int(row['user_id']) == user_id:
                    return row
        return None        
