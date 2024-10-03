# ATS-Scanner

This project is an ATS (Applicant Tracking System) like scanner built using Flask and BERT. It helps job seekers evaluate how well their resume matches a job description by comparing relevant keywords, skills, and experience. The application uses an expanded list of keywords to simulate how an ATS system might rank resumes based on matching criteria.

## Features

- Compares the skills, experience, and qualifications in the resume with the job description.
- Provides a detailed breakdown of matched and missing keywords.
- Outputs an overall match percentage score.
- Simple and intuitive web interface built with Flask.

## How It Works

- **Extracts Keywords**: The system extracts keywords from both the job description and resume, including skills, degrees, certifications, and experience levels.
- **Matches and Scores**: Compares the extracted keywords and provides a match percentage based on relevance to the job description.

## How to Run It

### Prerequisites

- Python 3.x installed on your machine.
- Install the required dependencies listed in the requirements.txt file.

### Step 1: Clone the Repository

```bash
git clone https://github.com/DoniyorI/ATS-Scanner.git
cd ATS-Scanner
```

### Step 2: Create and Activate a Virtual Environment (Optional but recommended)

Create a virtual environment to avoid conflicts with other Python packages.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application

```bash
flask run --host=0.0.0.0 --port=5000
```

### Step 5: Access the Application

Open your browser and go to `http://localhost:5000/`. You can now use the web interface to paste in a job description and a resume to see how well they match.

## Project Structure

* **app.py**: The main Flask application file.
* **templates/**: Contains the HTML files for the web interface.
* **static/**: Contains any static files like CSS, JavaScript (if needed).
* **README.md**: This file, explaining how the project works.
* **requirements.txt**: Lists the Python packages required to run the project.

## License

This project is licensed under the MIT License.