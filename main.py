from flask import Flask, render_template, request
from breweries import Breweries

# Create a Breweries object that allows the user to get breweries from the API.
breweries_api = Breweries()

# Flask
app = Flask(__name__)

# Flask home page that displays all the breweries
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("all.html", breweries= breweries_api.all())

# by_state app route allows the user to input then recieve a list of breweries from a specific state.
@app.route('/by_state', methods=['GET', 'POST'])
def state():
    if request.method == 'POST':
        state = request.form['state_entry']
        breweries = breweries_api.by_state(state)
        return render_template("state.html", breweries=breweries)

    return render_template("state.html")

# by_distance allows user to input then recieve a list of breweries closest to the user's latitude/longitude
@app.route('/by_distance', methods=['GET', 'POST'])
def distance():
    if request.method == 'POST':
        latitude = request.form['latitude_entry']
        longitude = request.form['longitude_entry']
        breweries = breweries_api.by_distance(latitude, longitude)
        return render_template("distance.html", breweries=breweries)

    return render_template("distance.html")

# by_type allows user to input then recieve a list of breweries of a certain size
@app.route('/by_type', methods=['GET', 'POST'])
def type():
    if request.method == 'POST':
        type = request.form['type_entry']
        breweries = breweries_api.by_type(type)
        return render_template("type.html", breweries=breweries)

    return render_template("type.html")

if __name__ == "__main__":
    app.run(debug=True)