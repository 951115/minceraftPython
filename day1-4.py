# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:08:41 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

X=10.5
y=10.5
z=10.5
mc.player.setPos(x,y,z)
