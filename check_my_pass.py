import requests
import hashlib
import sys


with open('pass.txt', 'r') as my_file:
    read_file = [line.strip() for line in my_file]
    print(f'\nCheking password list with {len(read_file)} items.\n\nMore passwords can be added in the text file.\nThey will get checked next time you run the file.\n')
 

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data {res.status_code}. Check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check if pass is in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        secret_password = password[:3] + len(password[3:])*'*'
        if count:
            print(f'{secret_password} was found {count} times.')
        else:
            print(f'{secret_password} is not not compromised')
    return 'Done!'

if __name__ == "__main__":
    sys.exit(main(read_file))