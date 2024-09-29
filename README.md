## Anonymous 
## Description
This Python tool helps you change your IP address to maintain anonymity while browsing. It uses the Tor network to route your traffic and requires the requests library and Tor service to function correctly.

## Features
Changes your IP address by connecting through the Tor network.
Allows for infinite IP changes or a specified number of changes.
Easy to install and use.

## Requirements
```
Python 3.x
requests library
Tor service
```
## Installation

## Clone the repository:

`git clone https://github.com/yourusername/Anon.git
cd Anonymous
`
## Install dependencies: 
If requests is not installed, the script will prompt you to install it automatically. However, you can manually install it using:

`pip3 install requests requests[socks]`

## Install Tor: 
The script checks if Tor is installed. If not, it will prompt you to install it. You can also install it 

## manually:
`
sudo apt update
sudo apt install tor -y
`
## Usage
Start the Tor service:

`service tor start`

## Run the script:

`python3 Anonymous.py`

```
Enter the time interval (in seconds) to wait before changing IP.
Enter the number of times to change your IP or leave it blank for infinite changes.
[+] Time to change your ip [type=60] >> 60
[+] How many times do you want to change your IP? enter to infinite IP change] >> 10
```
## Output
The script will display the current IP address after each change:

`[+] Your IP has been Changed to : 192.0.2.1`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ALHARAMM** - [GitHub Profile](https://github.com/ALHARAMM)
