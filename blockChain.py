#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:35:32 2018

@author: shymacbook
"""

# Module 1 - create block chain
    # Flask installed
    # postman installed
    
import datetime
import hashlib
import json
from flask import Flask, jsonify

#   part 1 - Build Blockchain
class Blockchain:
    #   initialize the chain, with a constructor
    def __init__(self):
        #   use list for the chain
        self.chain = []
        #   genesis block has arbitrary proof and previous hash value
        self.create_block(proof = 1, previous_hash = '0')  
        