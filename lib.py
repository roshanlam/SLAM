from datetime import datetime
import time
from enum import IntEnum
import json
import os

class Status(IntEnum):
    running = 301
    failed = 302
    success = 303
    stale = 304

class SaveInfo:
    def __init__(self, name, info):
        self.InfoName = name
        self.InfoDate = datetime.today().strftime('%Y%m%d%H%M%S')
        self.InfoStatus = Status.stale
        self.InfoFileName = 'Data/'+ self.InfoName + '_.json'
        self.stopSavingInfoTime = 0
        self.Info = info

    def startSavingInfo(self):
        if self.InfoStatus is Status.running:
            raise Exception('{} is already being saved')
        self.InfoStatus = Status.running

    def stopSavingInfo(self, status):
        if not self.InfoStatus is status.running:
            raise Exception('Test {} is not Running'.format(self.InfoName))
        if not os.path.exists('Data'): os.makedirs('Data')
        self.stopSavingInfoTime = datetime.today().strftime('%d%H%M%S%f')
        self.InfoStatus = status
        info_status_dic = {}
        try:
            with open(self.InfoName) as test_status_file:
                info_status_dic = json.load(test_status_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            info_status_dic['InfoName'] = self.InfoName
            info_status_dic['InfoDate'] = {'date': []}
            info_status_dic['Info'] = self.Info
        info_date_dic = info_status_dic['InfoDate']
        info_date_dic['date'].append([self.InfoDate, self.InfoStatus])
        with open(self.InfoFileName, 'w') as file:
            json.dump(info_status_dic, file)

    def start(self):
        self.startSavingInfo()
        self.stopSavingInfo(Status.success)