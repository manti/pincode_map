try:
    import simplejson as json
except :
    import json

import re
import string
import os

__all__ = [
    'PincodeMap',
]

################################################################################


class PincodeMap():
    """
    Base implementation Pincode Validator.
    """

    def __init__(self, country='IN'):
        """Initialize country."""
        self.country = country
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
    def validate(self, country, pincode):
        """
        validate pincode based on country code 
        """
        if not(isinstance(pincode, int) or isinstance(pincode, str)):
          raise ValueError('Invalid input')
        else:
            pincode = str(pincode)

        if country =='IN':
            return not re.match("\d{6}", pincode) == None and len(pincode) == 6

        elif country == 'BZ':    
            return not re.match("\d{5}\-\d{3}", pincode) == None and len(pincode) == 9

        return False

    def map(self, country, pincode):

      if not(isinstance(pincode, int) or isinstance(pincode, str)):
          raise ValueError('Invalid input')
      else:
        pincode = str(pincode)
        if not self.validate(country, pincode):
          raise ValueError('Invalid Pincode Code')

      pincode_details = json.load(open(self.__location__+'/resources/'+country+'.json'))

      return pincode_details[str(pincode)]

################################################################################