"""
check the technology used by the website https:// with the help of Python library builtwith.
>>pip install builtwith
"""

import builtwith

info = builtwith.parse("http://capgemini.com")
print(info)

'''Output:
{'web-servers': ['Nginx'], 'javascript-frameworks': ['Lo-dash', 'jQuery', 'jQuery UI'], 
'web-frameworks': ['Twitter Bootstrap'], 'cms': ['WordPress'], 'programming-languages': ['PHP'], 
'blogs': ['PHP', 'WordPress']}
'''
