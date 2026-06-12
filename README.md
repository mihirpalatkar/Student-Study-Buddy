# Student-Study-Buddy

AI-powered educational platform that transforms PDF study material into structured learning resources using Google's Gemini AI.

## Overview

Student Study Buddy is a Flask-based web application designed to enhance exam preparation by automatically generating assessment and revision material from uploaded PDF notes.

The system extracts content from academic documents and leverages Generative AI to create quizzes, descriptive questions, and concise revision notes, helping students learn more efficiently from existing study resources.

---

## Key Features

### Intelligent PDF Analysis

* Upload PDF study notes and academic material
* Automatic text extraction and processing
* In-browser PDF preview

### AI-Generated Assessments

Generate learning resources instantly from uploaded notes:

* 15 Multiple Choice Questions (MCQs)
* 5 Descriptive / Long-Answer Questions
* Revision Key Points
* Difficulty-based question generation

### Custom Difficulty Levels

* Easy
* Medium
* Hard

### Modern Learning Interface

* Responsive design
* Clean dark-themed dashboard
* Side-by-side PDF and generated content view
* Interactive file upload experience

---

## System Architecture

```text
PDF Upload
    │
    ▼
Text Extraction (PyPDF2)
    │
    ▼
Prompt Engineering Layer
    │
    ▼
Gemini AI Processing
    │
    ▼
Generated Learning Resources
    ├── MCQs
    ├── Descriptive Questions
    └── Key Revision Notes
```

---

## Technology Stack

### Backend

* Python
* Flask

### Artificial Intelligence

* Google Gemini API
* Google GenAI SDK

### Frontend

* HTML5
* CSS3

### Document Processing

* PyPDF2

### Configuration Management

* python-dotenv

### Version Control

* Git
* GitHub

---

## Project Structure

```text
Student-Study-Buddy/
│
├── app.py
├── README.md
├── .env
├── .gitignore
│
├── static/
│   ├── style.css
│   └── uploaded_files
│
├── templates/
│   └── index.html
│
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mihirpalatkar/Student-Study-Buddy.git

cd Student-Study-Buddy
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Launch Application

```bash
python app.py
```

Navigate to:

```text
http://127.0.0.1:5000
```

---

## Screenshots

### Home Interface

<img width="1917" height="1012" alt="home page" src="https://github.com/user-attachments/assets/67ad4d27-8782-4560-a318-6068485d8e27" />


### Quiz Generation Dashboard

<img width="1917" height="871" alt="Output" src="https://github.com/user-attachments/assets/e75b2f53-2ef0-4cb9-ac85-c8c0bccd4327" />


---

## Future Enhancements

* Flashcard Generation
* AI-Based Summarization
* Export Quiz to PDF
* OCR Support for Scanned Documents
* User Authentication
* Quiz History Tracking
* Interactive Quiz Mode
* Learning Analytics Dashboard
* Multi-Language Support

---

## Challenges Solved

* Extracting structured information from PDF documents
* Integrating Generative AI into a Flask application
* Prompt engineering for educational content generation
* Secure API key management using environment variables
* Building a responsive user interface for learning workflows

---

## Skills Demonstrated

* Python Development
* Flask Web Applications
* AI API Integration
* Prompt Engineering
* PDF Data Processing
* Frontend Development
* Environment Configuration
* Git & GitHub Version Control

---

## Author

**Mihir Palatkar**

Aspiring Software Developer with a focus on Artificial Intelligence, Full-Stack Development, and Educational Technology.

---

## License

This project is intended for educational and learning purposes.

---

### If you found this project useful, consider giving it a star on GitHub.
