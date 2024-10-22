import flask 
import csv
from flask import request , flash , render_template ,redirect, url_for, session
from user import User 
from appointments import Appointment
from doctors import Doctor
import json


app = flask.Flask("app.py")
app.secret_key = "secretkey"
User.initialize_csv()

#______routes________

@app.route("/") 
def welcome_page():
  return render_template("index.html")

@app.route("/home" ) 
def home_page():
  return render_template("home.html") 

#retrive name from local storage when user is still loged in 
@app.route("/back_home" , methods = ["GET"]) 
def back_home():
  if request.method == "GET":
    user_name = request.args.get("user_name")
    print(user_name)
    if user_name != "null" :
      flash ("Welcome back " + user_name , "success")
      return render_template("home.html")
    else :
      flash ("You must log in first", "error")
      return redirect(url_for("signin_page")) 

@app.route("/signin") 
def signin_page():
  return render_template("signin.html")

@app.route("/signup") 
def signup_page():
  return render_template("signup.html")

@app.route("/reservation" , methods = ["GET"]) 
def reservation_page():
  if request.method == "GET" :
    #json.dump convert to json string
    doctor_id = request.args.get("doctor_id")
    doctor = Doctor.get_doctor_by_id(doctor_id)
    available_slots = json.dumps(doctor["available_slots"])

    
    appointments = Appointment.get_doctor_appointments(doctor_id)
    appointments = json.dumps(appointments)
  
    return render_template("reservation.html" , doctor_id = doctor_id,  appointments = appointments , available_slots = available_slots)

@app.route("/edit") 
def edit_page():
  if request.method == "GET" :
    #json.dump convert to json string
    doctor_id = request.args.get("doctor_id")
    doctor = Doctor.get_doctor_by_id(doctor_id)

    available_slots = json.dumps(doctor["available_slots"])

    appointments = Appointment.get_doctor_appointments(doctor_id)
    appointments = json.dumps(appointments)

  return render_template("edit.html", appointments = appointments , available_slots = available_slots)

@app.route("/doctors") 
def doctors_page():
  doctors = Doctor.get_all_doctors()
  return render_template("doctors.html", doctors=doctors)

@app.route("/logout")
def logout():
  session.clear()
  flash("You are succuessfully loged out " , "success")
  return redirect(url_for("welcome_page"))

@app.route("/contact_us")
def contact_us():
  return render_template("contact.html")
 
@app.route("/newuser" , methods=["POST"])
def newuser():
  if request.method == "POST" :
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    email =request.form["email"]
    password = request.form["password"]
    phone_number = request.form["phonenumber"]
    date_of_birth = request.form["date_of_birth"]
    gender = request.form["gender"]
    user_id = sum(1 for _ in open(User.csv_file))
    check =   User.user_validation(email , password)
    if check == -1 :
      new_user = User(user_id, first_name, last_name, email, password, phone_number, date_of_birth, gender)
      new_user.signup() 
      flash("Signup successful! You can now log in.", "success")
      return redirect(url_for("signin_page"))
    else : 
      flash("Email already exists!", "error")
  return render_template("signup.html")  
 
  

@app.route("/login" , methods = ["POST"]) 
def login():
  if request.method == "POST" :
    email = request.form["useremail"]
    password = request.form["userpassword"]
    check = User.user_validation(email, password)

    if check == 1 :
      user = User.login(email, password)
      
      if user :
        session["user_id"] = user.user_id   #store name and ID to use later 
        session["user_name"] = user.first_name
        print(user)
        flash("Welcome "+ user.first_name , category="success")
        return redirect(url_for("home_page", user_name = user.first_name))
        
    elif check == 0 :
      flash("The password or email isn't correct", "error")
      return render_template("signin.html")
    else :
      flash("This email doesn't have an account signup first", "error")
      return render_template("signin.html")

@app.route("/reservation", methods=["GET", "POST"])
def reservation_form():

    if request.method == "POST" :
      
      user_id = session.get("user_id")
      user_name = session.get("user_name")
      date = request.form["date"]
      slot = request.form["slot"]
      doctor_id = request.form["doctor_id"]
      phone_number = request.form["phonenumber"]
      print(doctor_id)
      appointment_id = sum(1 for _ in open(Appointment.csv_file)) #counts rows of csv file to assign appointment ID 
      doctor = Doctor.get_doctor_by_id(doctor_id)
      doctor_name = doctor["name"]
      
      
      # Create appointment instance and save it
      appointment = Appointment(appointment_id, user_id, doctor_id, doctor_name, date, slot, phone_number)
      appointment.save()

      flash(f"Appointment made with Dr. {doctor_name}!", category="success")
      return redirect(url_for("home_page" , user_name = user_name))

@app.route("/my_appointments")
def my_appointments():
  user_id = session.get("user_id") 
  appointments = Appointment.get_user_appointments(user_id)

  if appointments == -1 :
    flash("You don't have any appointments yet", "error")
    return render_template("appointments.html")
  
  return render_template("appointments.html", appointments=appointments)

@app.route("/delete_appointment", methods = ["GET"])
def delete_appointment():
  if request.method == "GET" :
    appointment_id = request.args.get("appointment_id")
    user_id = session.get("user_id")
    doctor_id = request.args.get("doctor_id")
    Appointment.delete(appointment_id, user_id , doctor_id)
    flash("Appointment deleted succesfully", "success")
    return redirect(url_for("my_appointments"))

@app.route("/edit_appointment", methods = ["POST"])
def edit_appointment():
  if request.method == "POST" :
    user_id = session.get("user_id")
    appointment_id = request.form["appointment_id"]
    doctor_id = request.form["doctor_id"]
    new_date = request.form["date"]
    new_slot= request.form["slot"]
    
  Appointment.edit(appointment_id, user_id, doctor_id, new_date, new_slot)
  flash("Appointment edited succesfully", "success")
  return redirect(url_for("my_appointments"))  

@app.route("/doctor_search", methods = ["POST"])
def doctor_search():
  if request.method == "POST" :
    user_name = session.get("user_name")
    text = request.form["search"]
    doctors = Doctor.search(text)

    if doctors == -1 :
      flash("No doctors found", "error")
      return  redirect(url_for("home_page" , user_name = user_name))
    
  return render_template("doctors.html", doctors=doctors)  


    



    
  

    
