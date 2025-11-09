'''
Unique Error Codes
Extract all unique error codes from:
    errors = [404, 200, 500, 404, 403, 200]
'''

errors = [404, 200, 500, 404, 403, 200]
unique_error_codes = set(errors)
print(unique_error_codes)