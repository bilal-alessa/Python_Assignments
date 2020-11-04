import time
from datetime import datetime
import pytz

UTC = pytz.utc



Portland = pytz.timezone('PST8PDT')
London = pytz.timezone('Europe/London')
NYC = pytz.timezone('US/Eastern')
                    
varPortland = datetime.now(Portland).time().hour
varNYC = datetime.now(NYC).time().hour
varLondon = datetime.now(London).time().hour

                    
print('Portland Time:', varPortland)
print('NYC Time: ', varNYC)
print('London Time: ', varLondon)


if varPortland >= 9 and varPortland < 17: 
    print('Portland: OPEN')
else:
    print('Portland: CLOSED')

if varNYC >= 9 and varNYC < 17:
    print('NYC: OPEN')
else:
    print('NYC: CLOSED')

if varLondon >= 9 and varLondon < 17:
    print('London: OPEN')
else:
    print('London: CLOSED')



##
##if varPortland > 9:
##    print('Portland Is OPEN!')
##
### Locations are :
####        Portland, Or    PST8PDT
####        NYC             US/Eastern    
####        London, UK      Europe/London
####
###
###
###
