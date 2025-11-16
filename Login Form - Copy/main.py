from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "fuck_you_bitch"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

with app.app_context():
    db.create_all()

# Email configuration - UPDATE THESE WITH YOUR ACTUAL EMAIL CREDENTIALS
SMTP_SERVER = "smtp.gmail.com"  # Change if using different provider
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@gmail.com"  # Your email
EMAIL_PASSWORD = "your_app_password"    # Your app password

def send_password_email(user_name, user_email, user_password):
    """
    Send an email with the user's password
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = user_email
        msg['Subject'] = "Your Password Recovery"
        
        # Email body
        body = f"""
        Hello {user_name},
        
        You requested your password recovery.
        
        Your password is: {user_password}
        
        Please keep this information secure.
        
        Best regards,
        Nexus Team
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, user_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_email = request.form.get("email")
        login_password = request.form.get("password")
        
        # Find user by email
        user = User.query.filter_by(email=login_email).first()

        if user and user.password == login_password:
            flash("Login successful!", "success")
            return render_template("login.html")
        else:
            flash("Invalid email or password", "error")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists! Try another one.", "error")
            return render_template("login.html")

        if password != confirm_password:
            flash("Password and Confirm Password do not match", "error")
            return render_template("login.html")

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return render_template("login.html")

    return render_template("login.html")

@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    if request.method == "POST":
        email = request.form.get("email")
        
        # Find user by email
        user = User.query.filter_by(email=email).first()
        
        if user:
            # Send email with password
            if send_password_email(user.name, user.email, user.password):
                flash("Password has been sent to your email!", "success")
            else:
                flash("Failed to send email. Please try again later.", "error")
        else:
            flash("Email not found in our system.", "error")
        
        return render_template("login.html")
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)