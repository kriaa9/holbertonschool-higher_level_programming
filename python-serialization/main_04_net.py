#!/usr/bin/env python3
import threading
import time

from task_04_net import start_server, send_data

def main():
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give server some time to start listening
    time.sleep(1)

    # Run the client to send data
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    # Ensure server thread ends
    server_thread.join()

if __name__ == "__main__":
    main()
