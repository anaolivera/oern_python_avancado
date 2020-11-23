# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:02:17 2020

@author: anacv
"""

def IMC(altura,peso):
    imc=peso/(altura**2)
    return imc

def IMCI(altura,peso):
    imc=1.3*peso/(altura**2.5)
    return imc
