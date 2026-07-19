from flask import Flask, render_templates, request, redirect, session
from db import Base, engine, SessionLocal 

import models
import pyPDF2
import docx
import json

app = Flask(__name__)
app.secret_key = "secret123"

Base.metadata.create_all(bind=engine)

#Home
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")

#--SignUp

@a

if __name__ == "__main__":
    app.run(debug=True)