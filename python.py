from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barata')
def barata():
    return render_template('barata.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/lujo')
def lujo():
    return render_template('lujo.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/semi')
def semi():
    return render_template('semi.html')

@app.route('/reserva_lujo')
def reserva_lujo():
    return render_template('reserva-lujo.html')





if __name__ == '__main__':
    app.run(debug=True)

    