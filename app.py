from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
# from trafficVolumePrediction.utils.common import decodeImage
from trafficVolumePrediction.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.classifier = PredictionPipeline()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("dvc repro")
    return "Training done successfully!"

import numpy as np
def decodeData(data):
    decodedFeatures = []
    for key, val in data.items():
        if key in ['temp','rain_1h', 'snow_1h']:
            val = float(val)
        else:
            val = int(val)
        decodedFeatures.append(val)
    return np.array([decodedFeatures])

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    decodedFeatures = decodeData(data)
    print(decodedFeatures)
    # decodeImage(image, clApp.filename)
    result = clApp.classifier.predict(decodedFeatures)
    print("result")
    print(result) 
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=5000, debug=True) #local host
    # app.run(host='0.0.0.0', port=8080, debug=True) #local host
    # # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE