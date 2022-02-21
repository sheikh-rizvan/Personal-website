from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import json
from flask_mail import Mail
import datetime

# reading json file
local_server = True

with open("config.json", "r") as c:
    params = json.load(c)["params"]


app = Flask(__name__)

local_server = True

app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-pwd']
)

mail = Mail(app)


# configuring database uri
if local_server == True:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]


db = SQLAlchemy(app)


class Contacts(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    msg = db.Column(db.String(1500), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    



@app.route("/")
def home():
    return render_template("index.html", params=params)


@app.route("/portfolio-details")
def portfolio_details():
    return render_template("portfolio-details.html", params=params)


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get("message")
        entry = Contacts(name=name, email=email, subject=subject, msg=msg, date=datetime.datetime.now())
        
        db.session.add(entry)
        db.session.commit()

        mail.send_message("New Message from Portfolio: " + name, sender=email, recipients=[params['gmail-user']], body=subject + "\n" + msg + '\n' + email )
        
        body = "Hi "+name+",\n Thank you! for contacting me. I will get back to you soon.\n\n\nThanks and regards,\nRizvan Sheikh\nMob:+91-9890087848 \n\n\n This is a Auto-Generated email."
        if mail.send_message("Thank You for contacting me. "+name, sender=params['gmail-user'], recipients=[email], body=body):
          
            return "Email sent successfully. We will reach you soon!"
        else:
            return "Opps.. Something went wrong!!! Unabel to send your lovely message to Rizvan." 


@app.route('/download')
def download():
    p = "static/assets/resume/resume.docx"
    return send_file(p, as_attachment=True)


app.run(debug=True)
