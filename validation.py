import re

def validate_pan(pan):
    return bool(re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan))

def validate_aadhar(aadhar):
    return bool(re.match(r'^\d{12}$', aadhar))

def validate_income(income):
    return isinstance(income, (int, float)) and income > 0
