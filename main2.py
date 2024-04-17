# Importing necessary libraries
from vidstream import *
import tkinter as tk
import socket
import threading

# Getting the local IP address of the machine
local_ip_address = socket.gethostbyname(socket.gethostname())
print(local_ip_address)

# Initializing a streaming server and an audio receiver
server = StreamingServer(local_ip_address, 7777)
receiver = AudioReceiver(local_ip_address, 6666)

# Function to start listening for connections
def start_listening():
    # Creating threads for the server and receiver, and starting them
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

# Function to start streaming the camera feed
def start_camera_stream():
    # Creating a camera client with the target IP address entered by the user, and starting it in a thread
    camera_client = CameraClient(text_target_ip.get(1.0, "end-1c"), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

# Function to start screen sharing
def start_screen_sharing():
    # Creating a screen share client with the target IP address entered by the user, and starting it in a thread
    screen_client = ScreenShareClient(text_target_ip.get(1.0, "end-1c"), 9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

# Function to start streaming audio
def start_audio_stream():
    # Creating an audio sender with the target IP address entered by the user, and starting it in a thread
    audio_sender = AudioSender(text_target_ip.get(1.0, "end-1c"), 8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

# GUI setup
window = tk.Tk()
window.title("Zoom Clone v0.01 Alpha")
window.geometry('500x400')

# Label for entering the target IP address
label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

# Text box for entering the target IP address
text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

# Button to start listening for connections
btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

# Button to start streaming the camera feed
btn_camera = tk.Button(window, text="Start Camera Streaming", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

# Button to start screen sharing
btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

# Button to start streaming audio
btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

# Running the GUI
window.mainloop()
