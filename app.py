from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from trafficVolumePrediction.components import decodeData
from trafficVolumePrediction.pipeline.predict import PredictionPipeline
from trafficVolumePrediction.components import data_validation
from trafficVolumePrediction import logger

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
    logger.info("Training done successfully!")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        data = request.json['data']
        data = data_validation(data)
        decodedFeatures = decodeData(data)
        result = clApp.classifier.predict(decodedFeatures)
        logger.info("Successfully result is responded to UI")
        return jsonify(result)
    except Exception as e:
        logger.info(f"Exception is raised {e}")
        return jsonify([{'traffic': "Error processing"}])

if __name__ == "__main__":
    clApp = ClientApp()

    # app.run(host='127.0.0.1', port=5000, debug=True) #local host
    app.run(host='0.0.0.0', port=8080) #local host
    # # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE