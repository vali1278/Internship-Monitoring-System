from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty_dashboard.html')

@app.route('/daily-report')
def daily_report():
    return render_template('daily_report.html')

@app.route('/photo-upload')
def photo_upload():
    return render_template('photo_upload.html')

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
