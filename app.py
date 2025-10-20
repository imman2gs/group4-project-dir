from flask import Flask, render_template

app = Flask(__name__)

# --- WELCOME PAGE ROUTE ---
# This handles the main website address (e.g., http://127.0.0.1:5000/)
@app.route('/')
def welcome():
    # Renders the 'welcome.html' file (your Welcome Page)
    return render_template('welcome.html')

# --- LOGIN PAGE ROUTE ---
# This handles the /login URL (e.g., http://127.0.0.1:5000/login)
@app.route('/login')
def login():
    # Renders the 'login.html' file
    return render_template('login.html')

# --- REGISTER PAGE ROUTE ---
# This handles the /register URL (e.g., http://127.0.0.1:5000/register)
@app.route('/register')
def register():
    # Renders the 'register.html' file
    return render_template('register.html')

if __name__ == '__main__':
    # Starts the Flask web server
    app.run(debug=True)