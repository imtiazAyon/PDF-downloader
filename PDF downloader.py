import re
import time
import os
import shutil
import requests
from pathlib import Path

url = input('Enter URL: ')
file = input('Enter file name: ')
path = file+"/"


session = requests.Session()
session.headers.update({'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'})


if not os.path.exists(path):
	os.makedirs(path)
i = 0
while True:
	file_path = path +str(i).zfill(2)+".png"
	file_path = Path(file_path)
	url = re.sub(r"\&page=[0-9]+", '&page='+str(i), url.rstrip())
	i = i + 1
	R = requests.get(url, allow_redirects=True)
	if R.status_code == 400:
		i = i - 2
		print(f"Downloaded page {i}")
		break
	if R.status_code != 200:
		print(f"Error at page {i}: {url}")
	file_path.write_bytes(R.content)
	print(f"Downloaded page {i}...", end='\r')
	time.sleep(1)
#print(f"Converting into zip!")
#shutil.make_archive(path, 'zip', path)
print(f"Done!")