import string
from argparse import ArgumentParser
import random
import secrets


def print_colored_ascii_art():
   
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    
    cyan = "\033[96m"
    reset = "\033[0m"

    
    colored_ascii_art = (
       f"""

                   {cyan} ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
                  {cyan}  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
                  {cyan}  ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
                   {cyan} ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
                   {cyan} ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
                   {cyan} ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                               
                                              {red}   ░░░░                                                
                                            {red}  ░████████░░                                            
                                        {red}   ▓██████░ ▓██████░                                         
                                    {red}   ▒██████░       ░░███████                                      
                                {red} ░░███████░                ░███████░░                                
                            {red} ░▓███████░                       ░░████████░                               
                       {red}  ████████░ ░                              ░ ░████████░                       
                   {red}  ███████                                              ███████                    
                   {red}  ███░                                                    ░███                    
                   {red}  ▓███                                                    ░███                    
                   {red}   ███                                                    ███░                    
                    {red}  ███░                                                  ░███                     
                    {red}  ███░                                                  ░███                     
                    {red}  ▒███                                                  ▓███                     
                     {red}  ███░                                                 ███                      
                     {red}  ███░                                                ░███                      
                     {red}  ░███                                                ███░                      
                     {red}   ███▓                                              ░███                       
                      {red}   ███░                                            ░███                        
                       {red}  ░███░                                           ███░                        
                         {red} ░███                                          ███░                         
                          {red} ░███░                                      ░███░                          
                          {red}   ████░                                   ████░                           
                           {red}    ████                                ████░                             
                             {red}  ░░████                           ░████░░                              
                               {red}   ░█████░░                   ░█████░                                 
                                   {red}  ░█████░              ░█████░                                    
                                     {red}   ░█████░        ░█████▒                                       
                                        {red}  ░░█████    █████▓░                                         
                                          {red}    ░████████░                                             
                                               {red}  ░██░                                                                    
                                                                                    """
    )

    #
    print(colored_ascii_art)


print_colored_ascii_art()

print("""
-n 	--nums 	    Number of digits in the pass
-l 	--lower     Number of lowercase digits in the pass
-u 	--upr 	    Number of uppercase digits in the pass
-s 	--spec 	    Number of special digits in the pass
-t 	--total 	It will ignore all of the above and it will generate a totally random pass with the specified length
-a 	--amount 	The amount of generated passwords
-o 	--output 	Outputs the passwords in a /name/.txt (naming the file is done while executing the script) when attched to the execution of the script
!!! PLEASE DO NOT COPY  !!!
""")

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
