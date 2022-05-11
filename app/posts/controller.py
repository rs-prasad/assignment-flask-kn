import math
import datetime

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

def validate_cordinate_points(lat,lon):
    if lat == None or lat < -90 or lat > 90:
        return [False, "invalid latitude"]
    elif lon == None or lon < -180 or lon > 180:
        return [False, "invalid longitude"]
    return[True, "no error"]

def time_difference(created_time):
    current_time = datetime.datetime.now()
    td = current_time - created_time
    time_difference_object = {"days":td.days,"hours":td.seconds//3600,"minitues":(td.seconds%3600)//60}
    return time_difference_object

# view functions
def add_posts():
    username = request.form.get('username',default=None, type=str)
    text = request.form.get('text',default=None, type=str)
    lat = request.form.get("lat", default=None, type=float)
    lon = request.form.get("lon", default=None, type=float)
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

def get_posts(page):
    lat = request.form.get('lat',default=None,type=float)
    lon = request.form.get('lon',default=None,type=float)
    all_posts = UserPost.fetch_all_posts()

    [validation,errorMsg] = validate_cordinate_points(lat,lon)
    if(validation):
        # calculating relative distance
        dict_list = []
        for item in all_posts:
            displacement = round(math.sqrt((item.lat - lat)**2 +(item.lon - lon)**2),4)
            dict_list.append({"key":displacement,"value":item})
        dict_list.sort(key=lambda i:i["key"])

        # preparing resultant posts
        limit = 50
        start = (page-1)*limit + 1
        end = start + 50
        resultant_posts = []

        if(start >= len(dict_list)):
            return "No more posts",200
        for i in range(start, min(end,len(dict_list))):
            item = dict_list[i]
            timestamp = time_difference(item['value'].created_date)
            post = {"username":item['value'].username,"distance":item['key'],
                    "text":item['value'].text,"timestamp":timestamp}
            resultant_posts.append(post)
        return {"data":resultant_posts,"total_posts":len(dict_list)},200
    else:
        return errorMsg,400