# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


# @app.route('/<file_address>')
# def print_address(file_address):
#     return f"<h1>{file_address}</h1>"


@app.route('/<fc>', methods=['POST', 'GET'])

def get_bidupdate(fc):
    render_template('bid_update.html')
    if request.method == "POST":
        bidupdate_file = request.form["bd_ad"]
        return f'<p>Forecast file: {fc}<br>' \
               f'Bid-Update file: {bidupdate_file}</p>'
    else:
        return render_template("bid_update.html")

    # return f"<p>you entered this address for forecast data: {file_address}</p>"


@app.route('/forecast', methods=['POST', 'GET'])
def forecast_get():
    if request.method == "POST":
        forecast_file = request.form["fc_ad"]
        return redirect(url_for('get_bidupdate', fc=forecast_file))
    else:
        return render_template("forecast.html")


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
