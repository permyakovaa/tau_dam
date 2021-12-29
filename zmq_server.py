#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import zmq
import subprocess
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
UPLOADS_DIR = 'uploads/'

while True:
    #  Wait for next request from client
    message = socket.recv_json()

    message = json.loads(message)

    for task in message['tasks']:
        if task == 'video_preview':
            subprocess.call(['ffmpeg', '-y', '-i', UPLOADS_DIR + message['file_name'], '-ss', '00:00:01.000', '-vframes', '1', '-q:v', '10', UPLOADS_DIR + message['preview_file_name'], '-hide_banner', '-loglevel',  'error'])
        elif task == 'video_compressed':
            subprocess.call(['ffmpeg', '-y', '-i', UPLOADS_DIR + message['file_name'], '-crf', '28', UPLOADS_DIR + message['compressed_video_name']])
        elif task == 'image_preview':
            subprocess.call(['ffmpeg', '-y', '-i', UPLOADS_DIR + message['file_name'], '-q:v', '30', '-vf', 'scale=320:240', UPLOADS_DIR + message['preview_file_name']])

    # Send reply back to client
    socket.send_json({"status": "ok", "preview_file_name": message['preview_file_name']})
