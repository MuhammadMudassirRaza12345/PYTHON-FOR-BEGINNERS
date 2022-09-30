#You are given a string S consisting of  digits 0-9,commas and dots.
#Your task is to complete the regex_pattern defined below, which will be used to re.split() 
# all of the , and . symbols in S ,
# It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit..

 
regex_pattern = r"[,.]"	# Do not delete 'r'.  in you the characters which you donot process

import re
print("\n".join(re.split(regex_pattern, input())))