# OCRapi
You could deploy this api on a server and get the output on any device with internet, could also work locally
You send a post request to the api and get a json response on any device.
the movive was to make OCR platform independent
uses Tesseract OCR
could be deployed on heroku \n
you could try post command : curl -F "file=@/home/steven/Projects/API/ocr.jpg" https://socr.herokuapp.com/eng
in file pass path to your own image

multilingual : English and Hindi for now

stevvv/screentext works with this api


