import flask 
import csv
from flask import request , flash , render_template ,redirect, url_for, session
from user import User 
from appointments import Appointment
from doctors import Doctor


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
    flash ("Welcome back " + user_name , "success")
  return render_template("home.html")

@app.route("/signin") 
def signin_page():
  return render_template("signin.html")

@app.route("/signup") 
def signup_page():
  return render_template("signup.html")

@app.route("/reservation") 
def reservation_page():
  return render_template("reservation.html")

@app.route("/edit") 
def edit_page():
  return render_template("edit.html")

@app.route("/doctors") 
def doctors_page():
  doctors = Doctor.get_all_doctors()
  return render_template("doctors.html", doctors=doctors)
 
@app.route("/newuser" , methods=['POST'])
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
 
  

@app.route("/login" , methods = ['POST']) 
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
      
      user_id = session.get("u""ser_id")
      user_name = session.get("user_name")
      date = request.form["date"]
      time = request.form["time"]
      doctor_id = request.form["doctor_id"]
      phone_number = request.form["phonenumber"]
      appointment_id = sum(1 for _ in open(Appointment.csv_file)) #counts rows of csv file to assign appointment ID 
    
      # get doctor's name using Doctor class
      doctor_name = Doctor.get_doctor_name(doctor_id)
      
      if not doctor_name:
          flash("Doctor not found.", "error")
          return redirect(url_for('reservation_form', doctor_id=doctor_id))
      
      # Create appointment instance and save it
      appointment = Appointment(appointment_id, user_id, doctor_id, doctor_name, date, time, phone_number)
      appointment.save()

      flash(f"Appointment made with Dr. {doctor_name}!", category="success")
      return redirect(url_for("home_page" , user_name = user_name))

@app.route("/my_appointments")
def my_appointments():
  user_id = session.get('user_id') 
  appointments = Appointment.get_user_appointments(user_id)
  return render_template("appointments.html", appointments=appointments)

@app.route("/delete_appointment", methods = ["GET"])
def delete_appointment():
  if request.method == "GET" :
    appointment_id = request.args.get("appointment_id")
    user_id = session.get('user_id')
    Appointment.delete(appointment_id, user_id)
    flash("Appointment deleted succesfully", "success")
  return redirect(url_for('my_appointments'))

@app.route("/edit_appointment", methods = ["POST"])
def edit_appointment():
  if request.method == "POST" :
    user_id = session.get("user_id")
    appointment_id = request.form["appointment_id"]
    new_date = request.form["date"]
    new_time= request.form["time"]
    Appointment.edit(appointment_id, user_id, new_date, new_time)
    flash("Appointment edited succesfully", category="success")
  return redirect(url_for("my_appointments"))  


    



    
  

    
