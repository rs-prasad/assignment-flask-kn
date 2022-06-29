This API is build using <b>Flask</b>.\
Create and activate the virtual environment by running
`python -m venv /venv` `/venv/Scripts/activate` in the command prompt.\
Install necessary dependencies by running `pip install -r requirements.txt`.\
Start flask app by running `python -m flask run` by default flask app will run on localhost `http://127.0.0.1:5000/`.

## API

### Weather

[GET] `/weather` - fetches weather data based on location. This api uses third party api (Open Weather).\
lat, lon should be provided as formData.\
-90 <= lat <= 90, -180 <= lon <= 180.

### Posts

[POST] `/posts` - saves post of user with timestamp and location coordinates in database.\
username, text, lat, lon should be provided as fromData.\
<br>
[GET] `/get-posts/<int:page>` - fetches posts near you.\
`<int:page>` takes page number to fetch.
lat, lon of user should be provided as formData.
