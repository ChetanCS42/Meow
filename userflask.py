from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        email = request.form.get('email')

        
        
        print(f"Student Registered: {name}, {age}, {course}, {email}")
        
        return redirect(url_for('thank_you', name=name))

    return render_template('regi.html')
    


@app.route('/thank_you/<name>')
def thank_you(name):
    return f"Thank you for registering, {name}!"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
