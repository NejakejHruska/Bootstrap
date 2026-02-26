from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/flexbox')
def flexbox():
    return render_template('flexbox.htm')

@app.route('/flexbox2')
def shop_flexbox():
    return render_template('shop-flexbox.htm')

if __name__ == '__main__':
    app.run(debug=True)