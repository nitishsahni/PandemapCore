from datetime import datetime
from .models import Place
# from .models import Place
from PIL import Image

from watson_machine_learning_client import WatsonMachineLearningAPIClient
import cv2
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

cos_credentials = {
    "apikey": "NULRnqqPdlhjS-ILOY-F-t2KDIijR65USlVgPtYeSIqN",
    "iam_apikey_description": "Auto-generated for key 6aff55e4-e55b-4160-83d5-1bea69fe2b3b",
    "iam_apikey_name": "sauravnitinbanka",
    "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
    "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/cba9cca2db3042de85a91f3b075e6463::serviceid:ServiceId-c5a7235f-1137-4a17-a1b2-b7be25fbb86c",
    "instance_id": "7a1ed647-3f63-49dd-8bc9-b783145cf09f",
    "url": "https://eu-gb.ml.cloud.ibm.com"
}

deployment = { 'metadata': { 'guid': '16342a7a-366e-4490-8389-e7d2c6e7e769',
                             'url': 'https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/7a1ed647-3f63-49dd-8bc9-b783145cf09f/deployments/16342a7a-366e-4490-8389-e7d2c6e7e769',
                             'created_at': '2020-06-16T19:59:17.139Z', 'modified_at': '2020-06-16T19:59:19.606Z' },
               'entity': { 'runtime_environment': 'python-3.6', 'name': 'Keras crowd count.',
                           'scoring_url': 'https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/7a1ed647-3f63-49dd-8bc9-b783145cf09f/deployments/16342a7a-366e-4490-8389-e7d2c6e7e769/online',
                           'deployable_asset': { 'name': 'MNIST - compressed keras model',
                                                 'url': 'https://eu-gb.ml.cloud.ibm.com/v3/wml_instances/7a1ed647-3f63-49dd-8bc9-b783145cf09f/published_models/1c5cb301-5497-4239-8af8-0da4491659a5',
                                                 'guid': '1c5cb301-5497-4239-8af8-0da4491659a5',
                                                 'created_at': '2020-06-16T19:59:17.111Z', 'type': 'model' },
                           'description': 'Description of deployment', 'status_details': { 'status': 'DEPLOY_SUCCESS' },
                           'model_type': 'tensorflow-1.15', 'status': 'DEPLOY_SUCCESS', 'type': 'online',
                           'deployed_version': {
                               'url': 'https://eu-gb.ml.cloud.ibm.com/v3/ml_assets/models/1c5cb301-5497-4239-8af8-0da4491659a5/versions/19d9fb47-2b47-4181-8290-a2acc04c3050',
                               'guid': '19d9fb47-2b47-4181-8290-a2acc04c3050' } } }


engine = create_engine('postgres://bfpcsqzi:1xfS83st-zspeZ48nUwpkpI5S259CGhs@hanno.db.elephantsql.com:5432/bfpcsqzi')

def get_prediction(http_ref):
    image = get_frame(http_ref)
    client = WatsonMachineLearningAPIClient(cos_credentials)
    prep = process_image(image).tolist()
    scoring_endpoint = client.deployments.get_scoring_url(deployment)
    scoring_payload = { 'values': prep }
    scores = client.deployments.score(scoring_endpoint, scoring_payload)
    return np.sum(np.array(scores['values']))


def process_image(img):
    data = []
    img = np.mean(img, axis=2)
    # img = cv2.imread(imga, 0)
    # img = np.array(img)
    img = (img - 127.5) / 128
    data.append([img])
    print('Image loaded!')
    print(img.shape)
    d = data[0]
    x_in = d[0]
    x_in = np.reshape(d[0], (1, d[0].shape[0], d[0].shape[1], 1))
    return x_in

def get_frame(http_ref):
    import cv2
    cap = cv2.VideoCapture(http_ref)
    ret, frame = cap.read()
    return frame


def payload():
    places = list(Place.objects.all())
    json = []
    for p in places:
        interval_count = round(float(get_prediction(p.http_ref)))
        print(interval_count)
        dict = {'place_id': p.id, 'timestamp' : datetime.now(), 'people_count': interval_count, 'user_info' : None}
        json.append(dict)
    json_df = pd.DataFrame(json)
    json_df.to_sql(con=engine, name='places_interval', if_exists='append', index=False)