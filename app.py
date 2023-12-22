from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


# Function to calculate simple interest
def calculate_interest(principal, rate, days):
    interest = (principal * rate * days) / 36500  # Assuming rate is in percentage
    return interest


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

        # Calculate the number of days outstanding
        days_outstanding = (end_date - start_date).days

        # Calculate interest
        interest = calculate_interest(principal, rate, days_outstanding)

        # Render the result
        return render_template('index.html', principal=principal, rate=rate, days_outstanding=days_outstanding,
                               interest=interest)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)