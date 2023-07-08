import string
from argparse import ArgumentParser
import random
import secrets
from pyfiglet import figlet_format

print(figlet_format("              P @ S S G 3 N", font='standard'))

parser = ArgumentParser(prog='PassGen', description='GENERATE SAFE PASSWORDS')

parser.add_argument("-n", "--nums", default=0, help="Number of digits in the pass", type=int)
parser.add_argument("-l", "--lower", default=0, help="Number of lowercase digits in the pass", type=int)
parser.add_argument("-u", "--upr", default=0, help="Number of uppercase digits in the pass", type=int)
parser.add_argument("-s", "--spec", default=0, help="Number of special digits in the pass", type=int)
parser.add_argument("-t", "--total", default=0, help="It will ignore all of the above and it will generate a totally random pass with the specified length", type=int)
parser.add_argument("-a", "--amount", default=1, help="The amount of generated passwords", type=int)
parser.add_argument("-o", "--output",  help="Outputs the passwords in a /name/.txt (naming the file is done while executing the script) when attched to the execution of the script")

args = parser.parse_args()

passwords = []

for _ in range(args.amount):
    password = []

    if args.total:
        password.extend([secrets.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(args.total)])
    else:
        password.extend([secrets.choice(string.digits) for _ in range(args.nums)])
        password.extend([secrets.choice(string.ascii_uppercase) for _ in range(args.upr)])
        password.extend([secrets.choice(string.ascii_lowercase) for _ in range(args.lower)])
        password.extend([secrets.choice(string.punctuation) for _ in range(args.spec)])

    random.shuffle(password)
    password = "".join(password)
    passwords.append(password)

if args.output:
    with open(args.output, 'w') as f:
        f.write('\n'.join(passwords))

print('\n'.join(passwords))
