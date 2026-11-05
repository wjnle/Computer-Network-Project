"""Terminal client for the CS3201 Online Image Description System."""

import argparse
from pathlib import Path
import socket

HEADER_SIZE = 10
MAX_MESSAGE_BYTES = 5 * 1024 * 1024
MAX_COMMAND_BYTES = 1024


def recv_exact(conn, count):
    data = bytearray()
    while len(data) < count:
        chunk = conn.recv(count - len(data))
        if not chunk:
            if not data:
                return None
            raise ConnectionError("Connection closed during a message")
        data.extend(chunk)
    return bytes(data)


def receive_message(conn):
    header = recv_exact(conn, HEADER_SIZE)
    if header is None:
        raise ConnectionError("Server closed the connection")
    if not header.isdigit():
        raise ValueError("Invalid message header")
    length = int(header)
    if not 1 <= length <= MAX_MESSAGE_BYTES:
        raise ValueError("Invalid message length")
    payload = recv_exact(conn, length)
    if payload is None:
        raise ConnectionError("Connection closed before message data")
    return payload


def send_message(conn, payload):
    if not 1 <= len(payload) <= MAX_MESSAGE_BYTES:
        raise ValueError("Invalid message length")
    conn.sendall(f"{len(payload):010d}".encode("ascii") + payload)


def print_reply(conn):
    reply = receive_message(conn).decode("utf-8")
    for line in reply.splitlines():
        print("server: " + line)
    return reply


def read_upload(path_text):
    path = Path(path_text)
    try:
        if not path.is_file():
            print("client: ERROR - File not found")
            return None
        if path.stat().st_size > MAX_MESSAGE_BYTES:
            print("client: ERROR - File exceeds 5 MiB")
            return None
        with path.open("rb") as source:
            data = source.read(MAX_MESSAGE_BYTES + 1)
        if not data:
            print("client: ERROR - File is empty")
            return None
        if len(data) > MAX_MESSAGE_BYTES:
            print("client: ERROR - File exceeds 5 MiB")
            return None
        filename = path.name
        if (len(filename) > 255 or any(c in filename for c in "/\\\r\n\x00")
                or not filename):
            print("client: ERROR - Invalid filename")
            return None
        return filename, data
    except (OSError, ValueError) as error:
        print("client: ERROR - Cannot read file: " + str(error))
        return None


def save_download(path_text, data):
    try:
        with open(path_text, "xb") as destination:
            destination.write(data)
        print("client: Saved to " + path_text)
    except FileExistsError:
        print("client: ERROR - Output file already exists")
    except (OSError, ValueError) as error:
        print("client: ERROR - Cannot save file: " + str(error))


def run_client(conn):
    while True:
        command = input("client: ").strip().upper()
        upload = None
        output_path = None
        if command == "UPLOAD":
            upload = read_upload(input("client: "))
            if upload is None:
                continue
            request = "UPLOAD " + upload[0]
        elif command in {"DESCRIBE", "DOWNLOAD", "REMOVE"}:
            image_id = input("client: ").strip()
            if command == "DOWNLOAD":
                output_path = input("client: ")
            request = command + " " + image_id
        else:
            request = command or " "
        payload = request.encode("utf-8")
        if len(payload) > MAX_COMMAND_BYTES:
            print("client: ERROR - Command exceeds 1024 bytes")
            continue
        send_message(conn, payload)
        if upload is not None:
            send_message(conn, upload[1])
        reply = print_reply(conn)
        if command == "DOWNLOAD" and reply.startswith("OK "):
            data = receive_message(conn)
            save_download(output_path, data)
        if command == "QUIT" and reply == "OK":
            return


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host", help="Server IPv4 address")
    parser.add_argument("port", type=int, help="Server TCP port (normally 18333)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("Port must be between 1 and 65535")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.settimeout(300)
            conn.connect((args.host, args.port))
            run_client(conn)
    except (EOFError, KeyboardInterrupt):
        print()
    except (OSError, ConnectionError, ValueError) as error:
        print("client: ERROR - " + str(error))


if __name__ == "__main__":
    main()
