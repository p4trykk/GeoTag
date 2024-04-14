from flask import Flask, render_template, request, jsonify
import exifread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/save', methods=['POST'])
def save_coordinates():
    lat = request.form['lat']
    lng = request.form['lng']
    return jsonify({'success': True})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        lat, lng = get_exif_data(file)
        return jsonify({'lat': lat, 'lng': lng})


def get_exif_data(file):
    tags = exifread.process_file(file)
    lat_ref = tags.get('GPS GPSLatitudeRef')
    lat = tags.get('GPS GPSLatitude')
    lon_ref = tags.get('GPS GPSLongitudeRef')
    lon = tags.get('GPS GPSLongitude')

    if lat and lon and lat_ref and lon_ref:
        lat_value = lat.values[0].num / lat.values[0].den
        lon_value = lon.values[0].num / lon.values[0].den
        lat_degrees = lat_value + lat.values[1].num / (lat.values[1].den * 60) + lat.values[2].num / (lat.values[2].den * 3600)
        lon_degrees = lon_value + lon.values[1].num / (lon.values[1].den * 60) + lon.values[2].num / (lon.values[2].den * 3600)

        if lat_ref.values == 'S':
            lat_degrees = -lat_degrees
        if lon_ref.values == 'W':
            lon_degrees = -lon_degrees

        return lat_degrees, lon_degrees
    else:
        return None, None
        

if __name__ == '__main__':
    app.run(debug=True)