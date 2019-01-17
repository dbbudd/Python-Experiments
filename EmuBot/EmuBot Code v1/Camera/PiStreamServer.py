import io
import socket
import struct

import PIL
from PIL import Image


#Start a socket listening for conncetions on 0.0.0.0:8000 (0.0.0.0 means all interfaces)

server_socket = socket.socket()
socket_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

#Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')

try:
    while True:
        #Read the Length of the image as a 32-bit unsigned int. If the lenght is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        #Construct a stream to hold the image data and read the image
        # data from the conncetion
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        
        #Rewind the stream, open it as an image with PIL and do some processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        print("Image is %dx%d" % image.size)
        image.verify()
        print("Image is verified")
finally:
    connection.close()
    server_socket.close()

