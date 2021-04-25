import argparse
import requests
from sys import argv 
import time

def check(url):
	response = requests.get(url)
	status=response.status_code
	if status == 405:
		print("[*]Website is vulnerable to xmlrpc\n")
	else:
		print("[*] Website is not vulnerable\n")


def update(url):
	try:
		if "https" not in url:
			if "http" not in url:
				url = "https://" + url + "/xmlrpc.php"
				check(url)
			else:
				url =  url + "/xmlrpc.php"
				check(url)

		else:
			url = url + "/xmlrpc.php"
			check(url)
				
	except:
		print("Internet is not connected\n")

def main():

	parser = argparse.ArgumentParser(description='Xmlrpc Vulnerability Detector ')
	parser.add_argument('-u',action='store',dest='url',default=None,help='Enter the url to scan',required=True)
	results = parser.parse_args()# collect cmd line args
	url = results.url
	print ("\n[*] Made by @Ashutosh [*]")
	time.sleep(2)
	print ("\n[*] Checking the url:"+ url +"\n")
	update(url)

if __name__ == '__main__':
	main()
