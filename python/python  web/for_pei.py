from flask import request
searchuser = request.args.get('user', '')
return searchuser
searchkey = request.args.get('key', '')
return searchkey
