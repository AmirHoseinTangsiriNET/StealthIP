import argparse
import os

def file_to_ip_format(file_path):
    with open(file_path, "rb") as file:
        bytes_data = file.read()
    segments = [".".join(str(b) for b in bytes_data[i:i+4]) for i in range(0, len(bytes_data), 4)]
    return "\n".join(segments)

def ip_format_to_file(encoded, output_path):
    lines = encoded.split('\n')
    bytes_data = bytearray()
    for line in lines:
        bytes_data.extend(int(code) for code in line.split('.'))
    with open(output_path, "wb") as file:
        file.write(bytes_data)

def encode_file(file_path):
    encrypted = file_to_ip_format(file_path)
    with open('IPlist.txt', 'w') as iplist:
        iplist.write(encrypted)
    print("IPList Created ;)")
    
def decode_file(file_path, output_format=None):
    with open(file_path, 'r') as file:
        encrypted_data = file.read()
    
    if not output_format:
        _, output_extension = os.path.splitext(file_path)
        output_format = output_extension[1:]
        
    output_path = os.path.splitext(file_path)[0] + 'Decrypted.' + output_format
    ip_format_to_file(encrypted_data, output_path)
    print("Decryption completed.")

def encode_file(file_path):
    encrypted = file_to_ip_format(file_path)
    file_name, file_extension = os.path.splitext(file_path)
    output_path = file_name + '.txt'
    with open(output_path, 'w') as output_file:
        output_file.write(encrypted)
    print("Encoded file saved as:", output_path)

def decode_directory(directory_path, output_format=None):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            if file_name.endswith('.txt'):
                decode_file(file_path, output_format)

def encode_directory(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            encode_file(file_path)

if __name__ == "__main__":
    print("""  
*********************************************************************
*                      StealthIP                                    *
*********************************************************************
*        https://github.com/AmirHoseinTangsiriNET/StealthIP         *
*                                                                   *
*********************************************************************
""")
    parser = argparse.ArgumentParser(description='Encode/Decode files In IP Format ')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Specify encoding or decoding mode')
    parser.add_argument('-f', '--file', help='Location of input file')
    parser.add_argument('-d', '--directory', help='Location of input directory')

    decode_group = parser.add_argument_group('Decode options')
    decode_group.add_argument('--output_format', help='Output file format (e.g. png, txt, exe, etc.)')

    args = parser.parse_args()

    if args.mode == 'encode':
        if args.file:
            encode_file(args.file)
        elif args.directory:
            encode_directory(args.directory)
    elif args.mode == 'decode':
        if args.file:
            decode_file(args.file, args.output_format)
        elif args.directory:
            decode_directory(args.directory, args.output_format)