import csv
import os

class User:
    csv_file = os.path.join(os.path.dirname(__file__), "static/data/user.csv")

    def __init__(self, user_id, first_name,last_name , email, password, phone_number, date_of_birth,  gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.gender = gender

#__________________functions_______________#  

    def save(self):
        self.initialize_csv()
        with open(self.csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.user_id, self.first_name, self.last_name, self.email, self.password, self.phone_number, self.date_of_birth, self.gender])  


    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.csv_file):
            with open(cls.csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["user_id", "first_name", "last_name", "email", "password", "phone_number", "date_of_birth", "gender"])

    def signup(self):
        with open(self.csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.user_id,
                              self.first_name,
                                self.last_name,
                                  self.email,
                                    self.password,
                                      self.phone_number,
                                        self.date_of_birth,
                                            self.gender])
          

    @classmethod  #think about this function
    def login(cls, email, password):
        with open(cls.csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["email"] == email and str(row["password"]) == str(password):
                    cleaned_row = {str(key): value for key, value in row.items()}
                    return cls(**cleaned_row)
        return None
    @classmethod
    def user_validation (cls,  email , password) :
        with open(cls.csv_file, mode="r") as file:
          csv_reader = csv.DictReader(file)
          for row in csv_reader:
            if row["email"] == email :
              if str(row["password"]) ==str( password) :
                  return 1 
              return 0 
          return -1 
                
                   
                        