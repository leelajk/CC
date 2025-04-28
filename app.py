from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    result = None
    if request.method == 'POST':
        try:
            temperature = float(request.form['temperature'])
            conversion_type = request.form['conversion']

            if conversion_type == 'CtoF':
                result = (temperature * 9/5) + 32
            elif conversion_type == 'FtoC':
                result = (temperature - 32) * 5/9

        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
