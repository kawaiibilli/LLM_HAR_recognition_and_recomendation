import numpy as np
import os
import sys
from flask import Flask
import asyncio
from utils import get_details, get_llm_output
from activity_recognition import get_activity, get_recommendation

## Pipeline
## 1. Get accelerometer data on api (for demo)
## 2. Predict action
## 3. Send action to llm

app = Flask(__name__)

@app.route('/api/<data>', methods=['GET', 'POST'])
async def main():
    content = request.get_json(silent=True)
    try:
        data = content['data']
    except Exception as e:
        print('no data in json', e)
    activity = get_activity(data)
    person_metadata = get_details(data)
    prompt = os.environ['PROMPT']
    output = await get_llm_output(activity, person_metadatam, prompt)
    
    write_to_db(output)

    return



