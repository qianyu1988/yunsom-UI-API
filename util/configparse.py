# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-10
# @Author  : derek.zhang

import configparser

from config.VarConfig import loacationPath


class ConfigFileParse():

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(loacationPath)


    def getSection(self,sectionName):
        optionDict = dict(self.cf.items(sectionName))
        return optionDict


    def getOptionValue(self, sectionName,optionName):
        return self.cf.get(sectionName,optionName)


if __name__ == "__main__":

    cp = ConfigFileParse()
    print(cp.getSection('163mail_login'))
    print(cp.getOptionValue('163mail_login','login_page.switchbutton'))