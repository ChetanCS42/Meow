from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        email = request.form.get('email')

        # In a real app, you might store this data in a database.
        # For now, let's just print it to the console.
        print(f"Student Registered: {name}, {age}, {course}, {email}")
        
        # Redirect to a new page or show a success message
        return redirect(url_for('thank_you', name=name))

    return render_template('register.html')

# Route for a simple "Thank You" page after registration
@app.route('/thank_you/<name>')
def thank_you(name):
    return f"Thank you for registering, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
