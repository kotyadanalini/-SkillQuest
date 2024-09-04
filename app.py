from flask import Flask, render_template, request

app = Flask(__name__)


roadmap = {
    "Data Scientist": {
        "skills": ["Python", "SQL", "Machine Learning", "Data Visualization"],
        "courses": ["Python for Data Science", "SQL for Data Analysis", "Machine Learning for Dummies", "Tableau for Data Visualization"]
    },
    "Software Engineer": {
        "skills": ["Java", "C++", "Data Structures", "Algorithms"],
        "courses": ["Java Programming", "C++ Programming", "Data Structures and Algorithms", "Cracking the Coding Interview"]
    },
    "Web Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "Responsive Design"],
        "courses": ["HTML and CSS Fundamentals", "JavaScript Basics", "Advanced Web Development", "Responsive Web Design"]
    },
    "Front-end Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "Frameworks (e.g., React, Angular)"],
        "courses": ["Advanced HTML and CSS", "JavaScript Frameworks", "Front-end Development Bootcamp", "Responsive Web Design"]
    },
    "Full Stack Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "Backend Development", "Databases"],
        "courses": ["Full Stack Web Development", "Backend Programming with Node.js", "Databases for Developers", "RESTful APIs"]
    },
    "Java Developer": {
        "skills": ["Java", "Spring Framework", "Database Management"],
        "courses": ["Java Programming", "Spring Framework Essentials", "Database Management with JDBC", "RESTful Web Services with Java"]
    },
    "Python Developer": {
        "skills": ["Python", "Flask/Django", "SQL/NoSQL Databases"],
        "courses": ["Python Programming", "Web Development with Flask", "Django for Beginners", "Database Management with Python"]
    },
    "C++ Developer": {
        "skills": ["C++", "Object-Oriented Programming", "STL", "Boost Libraries"],
        "courses": ["C++ Programming", "Object-Oriented Design in C++", "STL Fundamentals", "Boost Libraries Overview"]
    },
    "Data Analyst": {
        "skills": ["SQL", "Excel", "Data Visualization", "Statistics"],
        "courses": ["SQL for Data Analysis", "Advanced Excel", "Data Visualization with Python", "Statistics Fundamentals"]
    },
    "Cybersecurity Analyst": {
        "skills": ["Network Security", "Ethical Hacking", "Cyber Threat Intelligence", "Security Tools"],
        "courses": ["Cybersecurity Fundamentals", "Ethical Hacking Essentials", "Cyber Threat Intelligence Analysis", "Security Tools and Techniques"]
    },
    "UI/UX Designer": {
        "skills": ["User Research", "Wireframing", "Prototyping", "UI/UX Tools"],
        "courses": ["UI/UX Fundamentals", "Wireframing for Designers", "Prototyping Techniques", "UI/UX Tools Mastery"]
    },
    "DevOps Engineer": {
        "skills": ["Continuous Integration/Continuous Deployment (CI/CD)", "Containerization", "Infrastructure as Code (IaC)", "Monitoring Tools"],
        "courses": ["CI/CD Pipelines", "Containerization with Docker", "IaC with Terraform", "Monitoring and Logging in DevOps"]
    }
}

def get_role_roadmap(role):
    for key in roadmap.keys():
        if role.lower() == key.lower():
            return roadmap[key]
    return None

@app.route('/')
def index():
    roles=roadmap.keys()
    return render_template('index.html',roles=roles)

@app.route('/roadmap', methods=['POST'])
def get_roadmap():
    role = request.form['role']
    roadmap_data = get_role_roadmap(role)
    if roadmap_data is not None:
        return render_template('roadmap.html', role=role, skills=roadmap_data['skills'], courses=roadmap_data['courses'])
    else:
        return render_template('index.html', message=f"I'm sorry, I don't have a roadmap for {role} yet. Please choose from the provided roles.", roles=roadmap.keys())

if __name__ == '__main__':
    app.run(debug=True)
