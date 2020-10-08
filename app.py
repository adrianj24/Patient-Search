# Python Developer Exercise 

# By Adrian Javier

# import Python modules
from flask import Flask, render_template, request
import pandas as pd

# Initialize Flask Application
app = Flask(__name__)

# route decorator to tell Flask which URL should trigger the function
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def my_form():
    return render_template('search.html')

# Utilized HTTP methods to return user input
@app.route('/search', methods=['POST','GET'])
def my_form_post():
    # Utilized Pandas library to read and manipulated data in csv file
    df = pd.read_csv(r"C:\Users\adria\Desktop\python_dev_exercise\data\patient_tb.csv")
    
    # Deleted patiends with duplicate data
    df = df.drop_duplicates()
    
    # Retrieved User input
    text = request.form['text']
    
    # Returns matches of patient's first name
    pat_name = df.loc[df["PatientFirstName"] == text.capitalize()]
    
    # Converted table data to html table code
    data = pat_name.to_html()
    
    # Rendered templated and pass 'content' to search.html
    return render_template('search.html', content=(data))

# Utilized 'debug=True' feature to speed up debugging process
if __name__ == "__main__":
    app.run(debug=True)