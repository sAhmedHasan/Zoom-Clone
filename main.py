# Import necessary libraries
from vidstream import *
import tkinter as tk
import tkinter as ttk
import socket
import threading

# Get local IP address
local_ip_address = socket.gethostbyname(socket.gethostname())
print(local_ip_address)

# Initialize streaming server and audio receiver
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

# Function to start listening for connections
def start_listening():
    # Create threads for server and receiver
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    # Start both threads
    t1.start()
    t2.start()

# Function to start camera streaming
def start_camera_stream():
    # Create camera client with target IP and port
    camera_client = CameraClient(text_target_ip.get(1.0, "end-1c"), 7777)
    # Create thread for camera streaming
    t3 = threading.Thread(target=camera_client.start_stream)
    # Start the thread
    t3.start()

# Function to start screen sharing
def start_screen_sharing():
    # Create screen share client with target IP and port
    screen_client = ScreenShareClient(text_target_ip.get(1.0, "end-1c"), 7777)
    # Create thread for screen sharing
    t4 = threading.Thread(target=screen_client.start_stream)
    # Start the thread
    t4.start()

# Function to start audio streaming
def start_audio_stream():
    # Create audio sender with target IP and port
    audio_sender = AudioSender(text_target_ip.get(1.0, "end-1c"), 6666)
    # Create thread for audio streaming
    t5 = threading.Thread(target=audio_sender.start_stream)
    # Start the thread
    t5.start()

# GUI Setup
window = tk.Tk()
window.title("Zoom Clone v0.01 Alpha")
window.geometry('500x400')

# Label for target IP
label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

# Text box for entering target IP
text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

# Button to start listening for connections
btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

# Button to start camera streaming
btn_camera = tk.Button(window, text="Start Camera Streaming", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

# Button to start screen sharing
btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

# Button to start audio streaming
btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

# Running the GUI
window.mainloop()
