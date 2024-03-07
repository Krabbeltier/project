#!/usr/bin/env python
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#
# Ein Spiel von Ilja Liepelt 
# Copyright: GPL v2 or later
# Mail: ilja1974@protonmail.com
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# artikel die im game zur verfügung stehen
# eine feste liste derzeit
#
# name 		= artikel name
# ek 		= einkaufs preis
# vk 		= verkaufs preis
# prod_time	= zeit in minuten zum herstellen des artikels
#

# artikel struktur
#
class c_artikel:
		def __init__(self, art_name, ek, vk, prod_time):
			self.art_name 	= art_name
			self.ek 		= ek
			self.vk 		= vk
			self.prod_time 	= prod_time
		
# feste liste aller im game enthaltenen artikel
#
art_schaufel 	= c_artikel("Schaufel",		10,	25,	2)
art_boden		= c_artikel("Boden",		15,	35,	1)
art_saat_korn	= c_artikel("Korn",			5,	15,	10)
art_saat_obst	= c_artikel("Obst",			8,	20,	4)

# zusammen fassung der artikel
#
liste_artikel = []
liste_artikel.append(art_schaufel)
liste_artikel.append(art_boden)
liste_artikel.append(art_saat_korn)
liste_artikel.append(art_saat_obst)


# *** Main ***
#
if __name__ == "__main__":

	for art in liste_artikel:
		print(art.art_name)


