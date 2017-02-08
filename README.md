pincode-map
===========

This is Pinode validate and Map to Locality, City and State.

# Installation
git clone git@github.com:manti/pincode_map.git pincode_map

# Usage
from pincode_map import PincodeMap

## Validate

```python
pincode = PincodeMap()
print pincode.validate('IN', 560078)
```

### Get Details using Pincode
```python
pincode = PincodeMap()
print pincode.map('IN', 560078)
```
