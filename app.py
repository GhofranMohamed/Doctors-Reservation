import flask 
from flask import request , flash , render_template ,redirect, url_for
from user import User 


app = flask.Flask("app.py")
app.secret_key = "secretkey"
User.initialize_csv()

#_____main funcions_______

def get_html(page_name):
  html_file = open(page_name + ".html")
  content = html_file.read()
  html_file.close()
  return content 

def get_notes () :
  notes_list = open("static/notes.txt")
  content = notes_list.read()
  notes_list.close()
  notes = content.split("\n")
  return notes

#______routes________

@app.route("/") 
def welcome_page():
  return render_template("index.html")

@app.route("/home") 
def home_page():
  return render_template("home.html")

@app.route("/signin") 
def signin_page():
  return render_template("signin.html")

@app.route("/signup") 
def signup_page():
  return render_template("signup.html")
 
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
    print(check)
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
    print(check)
    if check == 1 :
      user = User.login(email, password)
      if user :
        flash("Welcome "+ user.first_name , "success")
        return redirect(url_for("home_page")) 
    elif check == 0 :
      flash("The password or email isn't correct", "error")
      return render_template("signin.html")
    else :
      flash("This email doesn't have an account signup first", "error")
      return render_template("signin.html")


    
