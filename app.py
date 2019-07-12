from flask import Flask
from flask import render_template, request
import boto3


app = Flask(__name__)

@app.route('/')
def index():

    # init aws s3 resource
    s3 = boto3.resource('s3')

    # get param value
    bucket = request.args.get('bucket')
    action = request.args.get('action')

    if action == 'create-bucket':

        return 'Created bucket {}'.format(bucket)

    elif action == 'delete':
        # delete
        return 'Deleted {}'.format(bucket)

    elif action == 'upload':
        # upload file db.sqlite3
        return 'Uploaded !'
    else:
        items = []
        if bucket is None:
            # incase no bucket name in request then list all buckets
            buckets = s3.buckets.all()
            for item in buckets:
                items.append(item.name)
        else:
            # list content in a specific bucket
            buckets = s3.Bucket(bucket).objects.all()
            for item in buckets:
                items.append(item.key)
        return render_template('index.html', buckets=items, name='phuong')
