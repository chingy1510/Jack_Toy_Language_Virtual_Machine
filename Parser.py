# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:46:22 2017

@author: Carson Hanel
"""
import io

#Parser object as called for in Ch.7
class Parser:
    #Initializes the Parser object.
    #filecont is a list of the lines of the file to simulate C-style parsing
    def __init__(self, filename):
        self.curritr  = -1
        self.filecont = []
        self.filename = filename
        self.fstream  = io.open(filename, mode = 'r')
        for line in self.fstream:
            self.filecont.append(line)
        self.currcmd  = self.filecont[self.curritr]
    
    #Checks the currcmd iterator against the size of the list of the commands
    def hasMoreCommands(self):
        if(self.curritr == -1):
            return True
        if(self.curritr < len(self.filecont)):
            return True
        else:
            return False
        
    #Iterates to the next valid command
    def advance(self):
        if(self.hasMoreCommands()):
            self.curritr += 1
            self.currcmd  = self.filecont[self.curritr]
            if self.currcmd[:2] == "//" or self.currcmd == "":
                self.advance()
            else:
                return
        else:
            return
    
    #Makes use of the cmd dictionary to classify argument type
    def commandType(self):
        arithCMD3 = ["add","sub","neg",
                     "and","not",     ]
        arithCMD2 = ["eq" ,"gt" ,"lt" ,
                     "or"             ]       
        if self.currcmd[:2] in arithCMD2:
            return "C_ARITHMETIC"
        if self.currcmd[:3] in arithCMD3:
            return "C_ARITHMETIC"
        if self.currcmd[:2] == "if":
            return "C_IF"
        if self.currcmd[:3] == "pop":
            return "C_POP"
        if self.currcmd[:4] == "push":
            return "C_PUSH"
        if self.currcmd[:4] == "goto":
            return "C_GOTO"
        if self.currcmd[:4] == "call":
            return "C_CALL"
        if self.currcmd[:5] == "label":
            return "C_LABEL"
        if self.currcmd[:6] == "return":
            return "C_RETURN"
        if self.currcmd[:8] == "function":
            return "C_FUNCTION"
        return "C_NULL"
        
    def arg1(self):
        command = self.commandType()
        arg     = self.currcmd
        if command == "C_RETURN":
            return "null"
        segments = arg.split()
        return segments[1]
            
            
    #
    def arg2(self):
        twoargs = ["C_PUSH","C_POP","C_FUNCTION","C_CALL"]
        command = self.commandType()
        arg     = self.currcmd
        if command in twoargs:
            segments = arg.split()
            return segments[2]
        else:
            return "null"
            