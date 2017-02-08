pincode-map
===========

This is Pincode validate and Map to Locality, City and State.

# Installation
pip install pincode_map

# Usage
```python
from pincode_map.pincodemap import PincodeMap
pincode = PincodeMap()
```
## Validate

```python
from pincode_map.pincodemap import PincodeMap
pincode = PincodeMap()
print pincode.validate('IN', 560078)
```

### Get Details using Pincode
```python
from pincode_map.pincodemap import PincodeMap
pincode = PincodeMap()
print pincode.map('IN', 560078)
```
