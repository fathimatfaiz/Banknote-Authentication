# -*- coding: utf-8 -*-
"""
Created on sun sep 20:51 2024

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float