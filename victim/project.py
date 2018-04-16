import sys

def is_user(s):
	lower = s.lower()

	if 'user' in lower:
		return True
	elif 'u' == lower:
		return True
	elif 'email' in lower:
		return True
	else:
		return False 

def is_pass(s):
	lower = s.lower()

	if 'pass' in lower:
		return True
	elif 'p' == lower:
		return True
	else:
		return False 

def parse_creds():
	lines = []
	cred_filename = sys.argv[1]

	with open('.cred', 'r') as f:
		line = f.readline()
		l = line.replace('\t\n', '')
		while line:
			if l:
				kv = line.replace('\n', '').split('\t')
				keys = kv[0].split(',')
				vals = kv[1].split(',')

				username = ''
				password = ''
				for i, k in enumerate(keys):
					if is_user(k):
						username = vals[i]
					elif is_pass(k):
						password = vals[i]
					
					if username and password:
						lines.append(tuple([username, password]))
						username = ''
						password = ''

			line = f.readline()
			l = line.replace('\t\n', '')

		f.close()

	return lines

def write_creds_to_file(creds):
	with open('.prize', 'w') as f:
		for c in creds:
			line = '{} {}\n'.format(c[0], c[1])
			f.write(line)

		f.close()

def main():
	creds = parse_creds()
	write_creds_to_file(creds)

if __name__ == '__main__':
	main()
