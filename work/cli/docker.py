import os

def main():
    os.system("sudo pkill apache2")
    os.system("sudo docker pull mirrobots/simulator:latest")
    os.system("sudo docker run -p 80:80 -p 8080:8080 -p 9090:9090 --rm -i -t mirrobots/simulator:latest")

