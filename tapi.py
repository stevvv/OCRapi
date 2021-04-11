from flask import Flask, jsonify, request, json
from PIL import Image
import pytesseract as pt
import os, re
import logging
from datetime import datetime
from pytz import timezone
now_utc = datetime.now(timezone('UTC'))
t_india = now_utc.astimezone(timezone('Asia/Kolkata'))
logging.basicConfig(filename='log.txt', filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt=t_india.strftime(format='%H:%M:%S'),level=logging.ERROR)

# initialize our Flask application
app= Flask(__name__)

count = 0
@app.route("/<lang>", methods=["POST"])
def home(lang):
    img = Image.open(request.files['file'])
    custom_oem_psm_config = r'--psm 3'
    # print('SCREEN CONTENT BELOW : \n')
    logging.critical('Processing...')
    routput = pt.image_to_string(img, lang=lang, config=custom_oem_psm_config)
    output = re.sub('[\n\f\t]', ' ', routput)
    # output = output.replace('\n', ' ')
    # return jsonify({'ip': request.remote_addr}), 200
    logging.critical(request.remote_addr)
    response = app.response_class(response=json.dumps(output),status=200,
        mimetype='application/json')
    # with open("Output.txt", "w") as text_file:
    #     text_file.write("Detected Text On-Screen:\n {0}".format(output))
    return response

if __name__=='__main__':
    bind = os.getenv('FS_BIND', '0.0.0.0')
    # app.run(bind, port=9095, threaded=True, debug=False)
    app.run(threaded=True, debug=False)

