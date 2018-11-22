#!/bin/bash

class MyGui:
    def makewidgets(self):
        Button(command = (lambda: self.onPress("Spam")))
    def onPress(self, message):

