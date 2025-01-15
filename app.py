from flask import Flask, render_template, request
# Import your spam detection function
from model.model import detect_spam  # Adjust this based on your actual model path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the home page

@app.route('/detect', methods=['POST'])
def detect():
    email_text = request.form['email']  # Get email content from form submission
    prediction = detect_spam(email_text)  # Call your spam detection function
    return render_template('result.html', prediction=prediction)  # Render results

if __name__ == '__main__':
    app.run(debug=True)  # Run the app

