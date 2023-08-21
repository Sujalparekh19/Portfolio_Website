from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Serve static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    description = request.form['description']
    
    # Store the data (you can use a database, file, or other storage method)
    # For demonstration purposes, let's just print the data
    print(f"New Form Submission:\nName: {name}\nEmail: {email}\nDescription: {description}")
    
    # Send a confirmation message to the user
    confirmation_message = "Sujal will contact you shortly."
    return redirect(url_for('thank_you'))
    
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
