
# CyberTalents
# LinuxCmd101
# Medium Challenge

import subprocess


with open('./One', 'r') as f:
	for word in f:

		word = '-p' + word[0:-1]
		print(f'testing out *{word}*')
		
		s = subprocess.run(['7z','x',word,'decodeme1.zip'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
		if (s.returncode == 2):
			subprocess.run(['rm','-rf','decodeme1'])
			continue
		print(f'found it: its ', word)
		break
