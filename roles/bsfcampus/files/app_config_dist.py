### Make a copy of this file called 'app_config.py'
### and change the values of the parameters to what you actually want.

## MongoDB parameters
mongodb_db = 'mookbsf'
mongodb_host = '127.0.0.1'
mongodb_port = 27017
mongodb_username = None
mongodb_password = None

## A secret key for the Flask app
app_secret = 'jkhuhdsiluy876Y87TFGHFDtrdcghfcdszyi-r65U'

## This salt is used to encrpyt data. Use http://randomkeygen.com/ to generate a random string.
password_salt = '56REDTGFI76T7IZ6GHDLIuyiuydfgid-R67U'

## Is this a central or a local server? Choose 'central' or 'local'. Default: 'central'
server_type = 'local'

## If this is a local server, uncomment the three properties below
## Give the address and credentials to the associated central server
# central_server_api_host = 'http://HOSTNAME:PORT/'
# central_server_api_key = '' # username, email or api key
# central_server_api_secret = '' # password or secret
central_server_api_host = 'http://192.168.1.200:5000/'
central_server_api_key = 'koombook_proto' # username, email or api key
central_server_api_secret = 'floflo' # password or secret

## Specify a port other than default (optional)
## Default is 5001 if server_type == 'local', 5000 otherwise
port = 5000

## Specify the domains to allow as origins of CORS requests
allow_origins = "*"
