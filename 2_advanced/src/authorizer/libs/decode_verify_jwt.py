# Copyright 2017-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.

import urllib
import json
import time
import os
import logging
from jose import jwk, jwt
from jose.utils import base64url_decode

region = os.environ['Region']
userpool_id = os.environ['UserPoolId']

keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(region, userpool_id)
# instead of re-downloading the public keys every time
# we download them only on cold start
# https://aws.amazon.com/blogs/compute/container-reuse-in-lambda/
response = urllib.request.urlopen(keys_url)
keys = json.loads(response.read())['keys']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def decode_and_verify(event):
    token = event['authorizationToken']
    # get the kid from the headers prior to verification
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']
    # search for the kid in the downloaded public keys
    key_index = -1
    for i in range(len(keys)):
        if kid == keys[i]['kid']:
            key_index = i
            break
    if key_index == -1:
        raise Exception('Public key not found in jwks.json')
    # construct the public key
    public_key = jwk.construct(keys[key_index])
    # get the last two sections of the token,
    # message and signature (encoded in base64)
    message, encoded_signature = str(token).rsplit('.', 1)
    # decode the signature
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
    # verify the signature
    if not public_key.verify(message.encode('utf-8'), decoded_signature):        
        raise Exception('Public key not found in jwks.json')

    logger.info('Signature successfully verified')
    # since we passed the verification, we can now safely
    # use the unverified claims
    claims = jwt.get_unverified_claims(token)
    # additionally we can verify the token expiration
    if time.time() > claims['exp']:        
        raise Exception('Token is expired')
        
    # and the Audience  (use claims['client_id'] if verifying an access token)
    #if claims['aud'] != app_client_id:
    #    raise Exception('Token was not issued for this audience')
        
    # now we can use the claims
    logger.info(claims)
    return claims
        