# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-09
# @Author  : derek.zhang

import configparser
import os

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
elementLocationPath = os.path.join(parentDirPath, u'demo\ElementLocation.ini')


class ParseConfigFile():

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(elementLocationPath)


    def getSection(self, sectionName):
        return dict(self.cf.items(sectionName))


    def getOptionValue(self, sectionName, optionName):
        return self.cf.get(sectionName,optionName)


if __name__ == "__main__":
    parse = ParseConfigFile()

    print(parse.getSection('163mail_login'))

    print(parse.getOptionValue('163mail_login','login_page.frame'))

    # print(elementLocationPath)
    # import configparser
    #
    # config = configparser.ConfigParser()
    # config.read(elementLocationPath)
    # print(dict(config.items('163mail_login')))