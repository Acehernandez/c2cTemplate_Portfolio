from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('name', '')
     ##email = request.form.get('in ', '')
    return render_template("test")
