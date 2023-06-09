import json
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predictImage

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['PUT'])
def getData():
    if request.method == 'PUT':
        try:
            print("request received")
            data = request.get_json()
            image = data['data']
            predictions, result = predictImage(image)
            # Convert the ndarray to a Python list
            predictions = predictions.tolist()
            response = {
                'predictions': predictions,
                'result': result
            }
            # Return the response as JSON
            return jsonify(response), 200
        except:
            print("Error")
    else:
        return "Error", 500

if __name__ == '__main__':
    print("app started above")
    app.run()
    print("app started")
    
