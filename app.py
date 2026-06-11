import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")
UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    difficulty = request.form['difficulty']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    from PyPDF2 import PdfReader 
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted  
    text = text[:3000]

    prompt = f"""
    You are an educational quiz generator.

    Generate content at {difficulty} difficulty level.

    From the following study material:
    15 MCQs
    5 paragraph question
    and give key points 

    present the questions in a clear and concise manner, ensuring they are relevant to the provided study material.

    Study Material:
    {text}
    """
    response = model.generate_content(prompt)

    questions = response.text
    
    return render_template(
        "index.html",
        pdf_file=file.filename,
        questions=questions
    )


if __name__ == '__main__':
    app.run(debug=True)