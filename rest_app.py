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
   
    key=['Returns', 'Volatility','Sharpe_Ratio','AAP_Weight','TSLA_Weight']
    return render_template('index.html',data=minRisk,data_1=maxReturn)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090)
