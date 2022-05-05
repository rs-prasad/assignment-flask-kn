from flask import request, make_response
from .model import UserPost

# helper functions


def validate_post_data(data):
    username = data.get('username')
    text = data.get('text')
    try:
        lat = float(data.get('lat'))
    except:
        return [False, "invalid latitude"]
    try:
        lon = float(data.get('lon'))
    except:
        return [False, "invalid latitude"]

    if not isinstance(username, str) or len(username) <= 0:
        return [False, "invalid username"]
    elif not isinstance(text, str) or len(text) <= 0:
        return [False, "invalid text"]
    elif not isinstance(lat, float) or lat < -90 or lat > 90:
        return [False, "invalid latitude"]
    elif not isinstance(lon, float) or lon < -180 or lon > 180:
        return [False, "invalid longitude"]
    return[True, "no error"]


def add_posts():
    data = request.form
    [validation, error_msg] = validate_post_data(data)
    if(validation):
        username = data.get('username')
        text = data.get('text')
        lat = float(data.get('lat'))
        lon = float(data.get('lon'))
        UserPost.put_post_in_db(username=username, text=text, lat=lat, lon=lon)
        resp = make_response(
            {"status": "success", "msg": "data successfully added"})
        resp.status_code = 200
        resp.headers['Content-Type'] = 'Application/json'
        return resp
    return error_msg, 400
