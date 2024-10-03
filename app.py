from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
import torch

# Define job-related skills, qualifications, and keywords
job_related_keywords = {
    'skills': ['python', 'java', 'javascript', 'typescript', 'react', 'angular', 'vue', 'node', 'express', 
               'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'terraform', 'ansible', 'jenkins', 
               'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'nlp', 'sql', 'nosql', 
               'mongodb', 'postgresql', 'mysql', 'oracle', 'sqlite', 'redis', 'elasticsearch', 
               'git', 'github', 'gitlab', 'ci/cd', 'flask', 'django', 'fastapi', 'spring boot', 
               'graphql', 'rest', 'soap', 'json', 'xml', 'css', 'html', 'sass', 'less', 
               'webpack', 'babel', 'typescript', 'c', 'c++', 'c#', 'go', 'rust', 'php', 
               'ruby', 'ruby on rails', 'scala', 'r', 'matlab', 'swift', 'kotlin', 'objective-c'],
    'degrees': ['bachelor', 'master', 'phd', 'associate', 'certification', 'degree', 'diploma'],
    'experience': ['entry level', 'junior', 'mid-level', 'senior', 'experienced', 'internship', 'contract'],
}

# Flask app setup
app = Flask(__name__)

# Extract keywords based on the predefined list
def extract_keywords(text, category):
    keywords = []
    for word in job_related_keywords[category]:
        if word.lower() in text.lower():
            keywords.append(word)
    return keywords

# Compare extracted keywords from resume and job description
def compare_keywords(job_desc_keywords, resume_keywords):
    matched = set(job_desc_keywords).intersection(set(resume_keywords))
    return list(matched), len(matched), len(job_desc_keywords)

# Compute overall match score and return matched details
def compute_score(job_description, resume_text):
    # Extract relevant fields
    job_skills = extract_keywords(job_description, 'skills')
    resume_skills = extract_keywords(resume_text, 'skills')
    
    job_degrees = extract_keywords(job_description, 'degrees')
    resume_degrees = extract_keywords(resume_text, 'degrees')

    job_experience = extract_keywords(job_description, 'experience')
    resume_experience = extract_keywords(resume_text, 'experience')

    # Skill Match
    matched_skills, skills_match, total_skills = compare_keywords(job_skills, resume_skills)

    # Degree Match
    matched_degrees, degree_match, total_degrees = compare_keywords(job_degrees, resume_degrees)

    # Experience Match
    matched_experience, experience_match, total_experience = compare_keywords(job_experience, resume_experience)

    # Skill Unmatched
    unmatched_skills = set(job_skills) - set(matched_skills)

    # Degree Unmatched
    unmatched_degrees = set(job_degrees) - set(matched_degrees)

    # Experience Unmatched
    unmatched_experience = set(job_experience) - set(matched_experience)

    # Compute the overall score (weighted average)
    overall_score = (skills_match / total_skills if total_skills > 0 else 0) * 0.6 + \
                    (degree_match / total_degrees if total_degrees > 0 else 0) * 0.2 + \
                    (experience_match / total_experience if total_experience > 0 else 0) * 0.2

    return {
        'matched_skills': matched_skills,
        'skills_match': skills_match,
        'skills_total': total_skills,
        'matched_degrees': matched_degrees,
        'degree_match': degree_match,
        'degree_total': total_degrees,
        'matched_experience': matched_experience,
        'experience_match': experience_match,
        'experience_total': total_experience,
        'unmatched_skills': unmatched_skills,
        'unmatched_degrees': unmatched_degrees,
        'unmatched_experience': unmatched_experience,
        'overall_score': overall_score * 100  # Convert to percentage
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    job_description = request.form['job_description']
    resume_text = request.form['resume']

    # Compute the ATS-like score based on keywords
    match_results = compute_score(job_description, resume_text)

    return render_template('result.html', 
                           matched_skills=match_results['matched_skills'],
                           skills_match=match_results['skills_match'],
                           unmatched_skills=match_results['unmatched_skills'],
                           skills_total=match_results['skills_total'],
                           matched_degrees=match_results['matched_degrees'],
                           degree_match=match_results['degree_match'],
                           unmatched_degrees=match_results['unmatched_degrees'],
                           degree_total=match_results['degree_total'],
                           matched_experience=match_results['matched_experience'],
                           experience_match=match_results['experience_match'],
                           unmatched_experience=match_results['unmatched_experience'],
                           experience_total=match_results['experience_total'],
                           overall_score=match_results['overall_score'])

if __name__ == "__main__":
    app.run(debug=True)
