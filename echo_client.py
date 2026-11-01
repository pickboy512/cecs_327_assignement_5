import socket
import ipaddress


def main():
    # Get the server's IP address and port from the user
    ip_addr = input("Server IP Address: ")
    port = input("Server Port: ")

    # Make sure the IP address and port are valid
    try:
        ipaddress.ip_address(ip_addr)
        port = int(port)
    except ValueError:
        print("Error: invalid IP address or port number.")
        return

    # Create the soccet and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip_addr, port))
    except (OSError, OverflowError):
        print("Error: could not connect to the server. Check the IP address and port.")
        return

    # Send messages 
    while True:
        message = input("Message (type 'quit' to exit): ")
        if message == "quit":
            break
        if not message:
            continue

        s.sendall(message.encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        print("Server response:", response)

    s.close()


if __name__ == "__main__":
    main()