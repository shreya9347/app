from flask import Flask, request,render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import optimizer

def create_app():
	app = Flask(__name__) 
	return app

app = create_app()
api = Api(app)
CORS(app)

@app.route('/')
def index():
    
    tickers = "AAPL TSLA"
    minRisk, maxReturn = optimizer.optimize(tickers)
    return render_template('index.html',min=minRisk,Max=maxReturn)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090)
