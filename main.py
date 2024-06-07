from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import exifread
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geotag.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    photos = Photo.query.all()
    return render_template('home.html', photos=photos)

def get_exif_data(file_path):
    with Image.open(file_path) as img:
        exif_data = img._getexif()
    if not exif_data:
        return None, None

    lat = lng = None
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]

            if "GPSLatitude" in gps_data and "GPSLongitude" in gps_data and "GPSLatitudeRef" in gps_data and "GPSLongitudeRef" in gps_data:
                lat = convert_to_degrees(gps_data["GPSLatitude"], gps_data["GPSLatitudeRef"])
                lng = convert_to_degrees(gps_data["GPSLongitude"], gps_data["GPSLongitudeRef"])

    return lat, lng

def convert_to_degrees(value, ref):
    #d, m, s = [float(x.num) / float(x.den) for x in value]
    d, m, s = value
    degrees = d + (m / 60.0) + (s / 3600.0)
    if ref in ['S', 'W']:
        degrees = -degrees
    return degrees

@app.route('/photos')
def photos():
    photos = Photo.query.all()
    return render_template('photos.html', photos=photos)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        lat, lng = get_exif_data(file_path)
        
        new_photo = Photo(filename=filename, lat=lat, lng=lng)
        db.session.add(new_photo)
        db.session.commit()
        
        return jsonify({
            'id': new_photo.id,
            'image_url': url_for('uploaded_file', filename=filename),
            'lat': lat,
            'lng': lng
        })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    app.logger.debug('Received data: %s', data)
    photo_id = data.get('photo_id')
    lat = data.get('lat')
    lng = data.get('lng')

    if photo_id is None:
        return jsonify({'error': 'Photo ID not provided'}), 400
    
    photo = Photo.query.get(photo_id)
    if photo:
        photo.lat = lat
        photo.lng = lng
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'error': 'Photo not found.'}), 404

@app.route('/delete_photo', methods=['POST'])
def delete_photo():
    data = request.get_json()
    photo_id = data.get('photo_id')
    
    if photo_id is None:
        return jsonify({'error': 'Photo ID not provided'}), 400 
    
    photo = Photo.query.get(photo_id)
    if photo:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        db.session.delete(photo)
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Photo not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)