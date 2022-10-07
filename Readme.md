
# EyeMap
.
This port-scanner uses threading for greater speed, it works very well on CTF's.

This project is for educational purposes, any unauthorized network use is categorized as illegal and I will not be held responsible.

### (**Check if the host is up before running.**)

## Author

- [@Exploit-py](https://github.com/Exploit-py)


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/933791098827059204/1025171840450166884/unknown.png)

![App Screenshot](https://cdn.discordapp.com/attachments/933791098827059204/1025172279774154752/unknown.png)

![App Screenshot](https://cdn.discordapp.com/attachments/933791098827059204/1025172569957081108/unknown.png)

## Download

```bash
  git clone https://github.com/Exploit-py/EyeMap
```

## Execute

```bash
  ./eyemap.py <HOST>
```
```bash
  ./eyemap.py <HOST> -pR 65535
```
```bash
  ./eyemap.py <HOST> -pR 65535 -v
```
```bash
  ./eyemap.py <HOST> -sV
 ```
 ```bash
  ./eyemap.py <HOST> -pR 65535 -v -sV -T 100
 ```


## Functionalities
- **host -> required**
- **--port_range / -pR <>**
- **--verbose / -v**
- **--threads / -T <threads>**
- **--serverVersion / -sV**
