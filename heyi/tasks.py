#第一步，解决从本地文件读取 token
from invoke import task, run
from pprint import pprint as pp
import requests
import sys, os
import json

private_token_file_name = "private_token"
def get_token():
    """从本地文件里读取token"""
    with open(os.path.join(os.path.dirname(__file__), private_token_file_name),
              'r',
              encoding='utf-8') as f:
        return f.readline().strip()

#path1 = os.path.join(os.path.dirname(__file__), private_token_file_name)
print(get_token())
parameters = {
    "private_token": get_token(),
    'per_page': 10,
    'encoding': 'utf-8'
    #    'simple':'true',
    #    "timeout" : 10
}
print(parameters)