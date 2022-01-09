'''
This file is main program to execute ship Lib

@Author : Hisyam 
'''
from ship import *
import datetime

newPerahu = perahuMotor("Perahu Arjuna",(datetime.datetime(2021,5,23)).strftime("%x"),"Gudang B","available")
# newPerahu.storeData()
# newPerahu.displayData()

newPesiar = kapalPesiar("Jaya Abadi",(datetime.datetime(2022,1,2)).strftime("%x"),"Gudang A","booked")
# newPesiar.storeData()
# newPesiar.displayData()

newLayar = perahuLayar("Putra Bali",(datetime.datetime(2020,3,21)).strftime("%x"),"Gudang C","sold")
# newLayar.storeData()
# newLayar.displayData()
# getAllData()
print("Polymorism Example ")
for shiplist in (newLayar,newPerahu,newPesiar):
    shiplist.displayData()