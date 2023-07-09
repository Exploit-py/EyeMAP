
# EyeMap
.
This port-scanner uses threading for greater speed, it works very well on CTF's.

This project is for educational purposes, any unauthorized network use is categorized as illegal and I will not be held responsible.

### Required nmap for detect version! (-sV)

## Author

- [@Exploit-py](https://github.com/Exploit-py)


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/900169751349833778/1044107508081500170/image.png)

![App Screenshot](https://cdn.discordapp.com/attachments/900169751349833778/1044107896738283570/image.png)

## Download

```bash
  git clone https://github.com/Exploit-py/EyeMap
```
```bash
  cd EyeMap/ && python3 setup.py
```

## Run

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
- **--port_range / -pR <port-range>**
- **--verbose / -v**
- **--threads / -T <threads>**
- **--serverVersion / -sV**
