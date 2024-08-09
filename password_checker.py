import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	print(res)
	if res.status_code != 200:
		raise RunTimeError(f'Error fetching: {res.status_code}, check the api and try again')
	return res

def password_leak_counter(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count 
	return 0

def pwned_api_checker(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first_5_chars, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first_5_chars) 
	return password_leak_counter(response, tail)

def main(args):
	for password in args:
		count = pwned_api_checker(password)
		if count:
			print(f'{password} was found {count} times...you should probably change your password')
		else:
			print(f'{password} was NOT found...carry on!')

main(sys.argv[1:])
