import os
import sys
from flask import Flask, request, jsonify
# import asyncio
from utils import get_llm_output
from activity_recognition import get_activity, get_recommendation

## Pipeline
## 1. Get accelerometer data on api (for demo) ## implemented
## 2. Predict action : ## Implemented using HARGPT paper (https://arxiv.org/abs/2403.02727) as reference
## 3. Send action to llm : ## Implemented

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def process_request():
    content = request.get_json(silent=True)
    try:
        data = content['data']
    except Exception as e:
        print('no data in json', e)
        return jsonify({'message': 'JSON data can not be parsed!'})
    print(data)
    activity = get_activity(data)
    output = get_recommendation(activity, data)
    print(output)

    return output

if __name__ == "__main__":
    app.run(host='localhost', port=8989, debug=True)

