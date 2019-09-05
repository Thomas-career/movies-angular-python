def response_format(response):
    if response.get('message'):
        return response, 404
    if response.get('unauthorized'):
        return response, 401 
    if response.get('failed'):
        return response, 409  
    if response.get('success'):
        return response, 201           
    return response, 200
