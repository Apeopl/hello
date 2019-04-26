#! /usr/bin/env python3
# .-*- coding:utf-8 .-*-

import pika
import time
import threading
import os
import json
import datetime
from multiprocessing import Process


# rabbitmq配置信息
MQ_CONFIG = {
    "host": "127.0.0.1",
    "port": 5672,
    "vhost": "/",
    "user": "admin",
    "passwd": "admin",
    "exchange": "ex_change",
    "serverid": "eslserver",
    "serverid2": "airserver"
}


class RabbitMQServer(object):
    _instance_lock = threading.Lock()

    def __init__(self, recv_serverid, send_serverid):
        self.exchange = MQ_CONFIG.get("exchange")
        self.channel = None
        self.connection = None
        self.recv_serverid = recv_serverid
        self.send_serverid = send_serverid
