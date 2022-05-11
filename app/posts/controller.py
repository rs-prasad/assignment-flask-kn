from flask import request, make_response
from .model import UserPost

# helper functions


def validate_post_data(username,text,lat,lon):
    if username == None or len(username) <= 0:
        return [False, "invalid username"]
    elif text == None or len(text) <= 0 or len(text)>1000:
        return [False, "invalid text"]
    elif lat == None or lat < -90 or lat > 90:
        return [False, "invalid latitude"]
    elif lon == None or lon < -180 or lon > 180:
        return [False, "invalid longitude"]
    return[True, "no error"]


def add_posts():
    username = request.form.get('username',default=None, type=str)
    text = request.form.get('text',default=None, type=str)
    lat = request.form.get("lat", default=None, type=float)
    lon = request.form.get("lon", default=None, type=float)
    print(lat, lon) ###
    [validation, error_msg] = validate_post_data(username,text,lat,lon)
    if(validation):
        id = 1
        try:
            id = UserPost.get_last_id() + 1
        except:
            print("table does not exist")
            
        is_post_added = UserPost.put_post_in_db(id=id,username=username, text=text, lat=lat, lon=lon)
        if(is_post_added==True):
            resp = make_response(
                {"status": "success", "msg": "data successfully added"})
            resp.status_code = 200
            resp.headers['Content-Type'] = 'Application/json'
            return resp
        else:
            return is_post_added,500
    else:
        return error_msg, 400
