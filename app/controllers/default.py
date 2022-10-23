from app import app
from flask import render_template
import json
import requests
import random
import datetime

@app.route('/')
def home():
    return 'ok'


@app.route('/api/meme', methods=['GET'])
def memes():
   url = 'https://api.imgflip.com/get_memes'
   req = requests.get(url).json()
   return req['data']['memes']

@app.route('/api/cep/<cep>/json', methods=['GET'])
def cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    req = requests.get(url).json()
    return req

@app.route('/api/cnpj/<cnpj>')
def cnpj(cnpj):
    url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
    req = requests.get(url).json()
    return req

@app.route('/api/ip/<ip>')
def ip(ip):
    url = f'http://ipwwho.is/{ip}'