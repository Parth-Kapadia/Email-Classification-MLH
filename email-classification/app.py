#!flask/bin/python
from flask import Flask,json,request,jsonify
from predict import start as dopredict
from training import start as start_training
import os 
from db import Persistent
import importlib
import predict as predictmodule

# from celery import Celery
# import redis
# from rq import Queue, Connection, Worker
#tmux 
#(Ctrl+b then d)

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    isAuthorize=True
    if 'org-id' in request.headers:
        org_id = request.headers['org-id']
        if org_id == None or org_id == '':
            isAuthorize=False
    else:
        isAuthorize=False
    
    if not(isAuthorize):
    
        return json.dumps({'error' : 'organization id is missing.'}), 401, {'Content-Type': 'application/json'}

    subject = request.json['subject']
    body = request.json['body']
    sender_email = request.json['sender_email']
    sender_name = request.json['sender_name']

    if 'html_body' in request.json:
        html_body = request.json['html_body']
    else:
        html_body = None

    if 'attachments' in request.json:
        attachments = request.json['attachments']
    else:
        attachments = None

    result = dopredict(subject, body, html_body, attachments, sender_email, sender_name, org_id)
    return json.dumps(result), 200, {'Content-Type': 'application/json'}


# @app.route('/api/v1.0/reload-model', methods=['POST'])
# def reload_model():
#     importlib.reload(predictmodule)
#     return json.dumps({
#                 "status" : "success",
#                 "message" : "configured model has been reload successfully."
#                 }), 200, {'Content-Type': 'application/json'} 


@app.route('/api/v1.0/train', methods=['POST'])
def train():
    isAuthorize=True
    if 'org-id' in request.headers:
        org_id = request.headers['org-id']
        if org_id == None or org_id == '':
            isAuthorize=False
    else:
        isAuthorize=False
    
    if not(isAuthorize):
        return json.dumps({'error' : 'organization id is missing.'}), 401, {'Content-Type': 'application/json'}

    response = Persistent.create_training_request(org_id)
    if response['exist'] == 'no':
        return json.dumps({
                "status" : "success",
                "message" : "trainig request job has been submitted, job id : " + str(response['job_id'])
                }), 200, {'Content-Type': 'application/json'}
    else:
        return json.dumps({
                "status" : "success",
                "message" : "trainig request is already submitted, job id : " + str(response['job_id'])
                }), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print('Application will start on port '+str(port))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True, use_reloader=False)