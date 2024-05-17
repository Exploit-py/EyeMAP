
# EyeMap
.
This port-scanner uses threading for greater speed, it works very well on CTF's.

This project is for educational purposes, any unauthorized network use is categorized as illegal and I will not be held responsible.

### Required nmap for detect version! (-sV)

## Author

- [@Exploit-py](https://github.com/Exploit-py)


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/900169751349833778/1044107508081500170/image.png?ex=6648d7a4&is=66478624&hm=23c41aaa8fd0ced7fadee6ccc6711d7699f25a5b38e206ccd1cb320610704e2a&)

![App Screenshot](https://cdn.discordapp.com/attachments/900169751349833778/1044107896738283570/image.png?ex=6648d801&is=66478681&hm=ee8887168c469d4ab192e4c36a99065d571396feb9f84139377fdf08f23c32b2&)

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
