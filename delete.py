import os

root = "d:/"
extension = { '.torrent' };

for root, dirs, files in os.walk(root):
	for file in files:
		if file.endswith('.torrent'):
			print("file: " + os.path.join(root, file) )
			os.remove( os.path.join(root, file) )