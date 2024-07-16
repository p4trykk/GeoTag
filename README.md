# GeoTag
The ‘GeoTagger’ application will allow users to describe photos through geotags, which are tags with information about the location of an object. Through an interactive interface, users will be able to assign geographic locations to photos using drag and drop techniques on the OpenStreetMap. The project will focus on ensuring high usability of the application through a simple and intuitive way of assigning geotags and grouping photos. Integrating the geographic data associated with each photo will enable users to view and manage photo files more easily.

## Project objectives:
- To create an interactive interface that allows users to assign geotags to photos,
- Implementation of photo grouping functions,
- Reading and writing geographic data from EXIF files,
- Enabling the preview of photos in the software interface.

## Built With
<img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=for-the-badge&logo=OpenStreetMap&logoColor=white">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">


## Use cases:
### Uploading a photo with EXIF metadata 
When the Geotagger application is opened, the user is taken to the homepage, where they can see a map and a button to upload files (Figure 1).
<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz1.png'></p>
The user then clicks the 'Upload file' button and selects a photo containing EXIF metadata from the local device (Figure 2).

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz2.png'></p>

After selecting a photo, the user clicks the ‘Upload file’ button, which starts the process of uploading the photo to the server. The application analyses the EXIF metadata to extract the geographical coordinates. Once the photo has been successfully uploaded and analysed, the app displays the geographical coordinates on the map and adds a marker at the appropriate location. The coordinates are also displayed below the map, allowing the user to easily locate where the photo was taken (Figure 3).


<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz3.png'></p>

### Manual update of coordinates for an existing image
The user opens the ‘Geotagger’ application and goes to the main page. He or she then selects a photo from the list of uploaded photos, which is available under ‘Complete coordinates for an existing photo’ (Figure 4).

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz4.png'></p>

Once the image is selected, the user drags the marker on the map to the new location and updates the text fields ‘New latitude’ and ‘New longitude’ with the new coordinates (Figure 5). 

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz5.png'></p>

Aby zatwierdzić zmiany, użytkownik klika przycisk "Aktualizuj współrzędne", co skutkuje zapisaniem nowych współrzędnych w bazie danych (przy każdym kolejnym wyborze tego zdjęcia marker automatycznie będzie wskazywał miejsce na podstawie zaktualizowanych współrzędnych).

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz6.png'></p>


### Deleting image
On the main page of the ‘Geotagger’ application, the user selects the photo he or she wants to delete from the list of uploaded photos. The user then clicks the cross button next to the selected photo (Figure 7). 

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz7.png'></p>

Aplikacja usuwa zdjęcie z bazy danych oraz z serwera. Po usunięciu zdjęcia, użytkownik może zobaczyć zaktualizowaną listę zdjęć, która nie zawiera już usuniętego zdjęcia.

### Displaying images on a map
The user opens the ‘Geotagger’ application and goes to the home page, where there is a map and a list of uploaded photos. When viewing the list of photos at the bottom of the screen, the user can click on the thumbnail of the photo to see its location on the map. When the user clicks on the thumbnail, the app moves the map to the location of the photo and positions the marker in the appropriate place. This makes it easy for the user to see where a particular photo was taken (Figure 8).

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz8.png'></p>

### Changing the interface theme
The user opens the ‘Geotagger’ application and navigates to the home page, where there is a button in the top right corner of the application window to switch the mode from white (daytime) to dark (nighttime). When the button is selected, the interface automatically adapts to the implemented assumptions (Figure 9).

<p align="center"><img src='https://github.com/p4trykk/GeoTag/blob/main/imgs/Obraz9.png'></p>

## Future development of application
The Geotagger project has a number of potential areas that could be improved to enhance its usability and appeal to users. Here are some suggestions for improvements:
- Additional image processing features: Consider adding advanced image processing features, such as object recognition or automatic feature detection in images. This could be implemented using libraries such as OpenCV, which offer advanced vision algorithms.
- Integration with more geolocation data sources: Currently, the project uses EXIF data from photo files. Integration with other geolocation data sources such as APIs from map providers (e.g. Google Maps, Mapbox) or geolocation services could be considered to enable more precise location determination.
- Support for other data formats: Increase support for different image data formats and their metadata, not only for standard JPEG images, but also for RAW and other formats that may contain detailed geolocation information.
- User interface personalisation: Adding options to personalise the user interface, such as choosing colour themes, customising page layouts or map data visibility preferences. This can enhance user experience and customisation of the application.
- Social features and sharing: Adding features to share photos of saved locations via social media or generate sharing links, making it easier for users to share their geolocalisation discoveries.
- Advanced geographic data analytics: Expanded analytical features such as generating reports with photo locations, statistics on popular locations or geographic trend analyses based on data collected in the app.
- Performance optimisation and scalability: Increase application performance by optimising code, using caching and cache techniques, and scaling infrastructure to support more users and data.
- Mobile application support: Consider extending the project to a mobile app that will allow users to more easily access the geotagging (marker staking) function of the photos directly from their mobile devices.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

art. 74 ust. 1 Ustawa o prawie autorskim i prawach pokrewnych, [Zakres ochrony programów komputerowych](https://lexlege.pl/ustawa-o-prawie-autorskim-i-prawach-pokrewnych/art-74/)















