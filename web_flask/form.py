from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def post_form():
    return render_template("form.html")


@app.route('/submit', methods=['POST'])
def handle_form_submission():
    name = request.form.get('name')
    email = request.form.get('email')
    # Process the data here
    return 'Form submitted!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
