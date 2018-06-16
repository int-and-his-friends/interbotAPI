# -*- coding: utf-8 -*-
import yaml
import json
import logging
from flask import Flask
from flask import request
from msgCenterLib import msgHandler

yamlFile = open('./app/ppyapp.yaml')
config = yaml.load(yamlFile)


app = Flask(__name__)


@app.route('/bp', methods=['POST'])
def bpApi():
    return 'bpApi test'


if __name__ == '__main__':
    app.run()
