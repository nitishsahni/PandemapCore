postgres_cred_dict = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bfpcsqzi',
        'USER': 'bfpcsqzi',
        'PASSWORD': '1xfS83st-zspeZ48nUwpkpI5S259CGhs',
        'HOST': 'hanno.db.elephantsql.com',
    }

cos_credentials = {
    "apikey": "NULRnqqPdlhjS-ILOY-F-t2KDIijR65USlVgPtYeSIqN",
    "iam_apikey_description": "Auto-generated for key 6aff55e4-e55b-4160-83d5-1bea69fe2b3b",
    "iam_apikey_name": "sauravnitinbanka",
    "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
    "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/cba9cca2db3042de85a91f3b075e6463::serviceid:ServiceId-c5a7235f-1137-4a17-a1b2-b7be25fbb86c",
    "instance_id": "7a1ed647-3f63-49dd-8bc9-b783145cf09f",
    "url": "https://eu-gb.ml.cloud.ibm.com"
}

deployment_data = { 'metadata': { 'guid': '16342a7a-366e-4490-8389-e7d2c6e7e769',
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

CONN_LINK = "postgres://bfpcsqzi:1xfS83st-zspeZ48nUwpkpI5S259CGhs@hanno.db.elephantsql.com:5432/bfpcsqzi"
API_YELP = "1TlhWAlOrPvn_FjxcgoGWeaB_KMzVWtV44nM6YePhhkrav4fNgRa729aZ766eeX4-nfMjKCTNSIzdUiXMsOdQz4n6lTOK2SJcQ4TtwPpXei8KIQiczKJXGTBhW0KX3Yx"