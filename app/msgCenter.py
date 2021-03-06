# -*- coding: utf-8 -*-
import yaml
import json
import logging
from flask import Flask
from flask import request
from msgCenterLib import msgHandler

with open('./app/msgCenter.yaml', encoding='utf8') as f:
    config = yaml.load(f)


app = Flask(__name__)


@app.route('/msg', methods=['POST'])
def msgApi():
    context = request.form.get("context")
    context = json.loads(context)
    logging.info('recive:%s' % context)
    mh = msgHandler.msgHandler(context)
    ret = mh.auto()
    return ret

@app.route('/test')
def test():
    return ''


if __name__ == '__main__':
    app.run(threaded=True)
