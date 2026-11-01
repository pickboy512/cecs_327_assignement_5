import socket


def main():
    # Get the port 
    try:
        port = int(input("Port to listen on: "))
    except ValueError:
        print("Error: invalid port number.")
        return

    # Create the socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", port))
    except (OSError, OverflowError):
        print("Error: invalid port")
        return
    s.listen(5)
    print(f"Server listening on port {port}...")

    # Accept clients
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)

        # Receive messages and send  back
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print("Received:", message)
            conn.sendall(message.upper().encode("utf-8"))

        print("Client disconnected")
        conn.close()


if __name__ == "__main__":
    main()