'''
This file contain Ship library

@Author : Hisyam M
'''
import os
import json

class perahuID :
    '''
    '''
    def __init__(self):
        self.__tipeKapal = ""
        self.__kodeKapal = ""

class perahuMotor :
    '''
    This class contain properties and funtion of "perahu motor" type
    '''
    def __init__(self,nama,tanggalProduksi,lokasi,status):
        self._tipeKapal = "Perahu Motor"
        self._kodeKapal = "PM2022"
        self.nama = nama
        self.tanggalProduksi = tanggalProduksi
        self.lokasi = lokasi
        self.status = status

    def storeData(self) :
        data = {
            "nama" : self.nama,
            "kode" : self._kodeKapal,
            "produksi" : self.tanggalProduksi,
            "lokasi": self.lokasi,
            "status" : self.status
        }
        saveData(self._tipeKapal,data)

    def displayData(self) :
        print("Ship Properties : %s '%s' with code %s is located in %s.\nIt was produced at %s and current status is %s" % (self._tipeKapal,self.nama,self._kodeKapal,self.lokasi,self.tanggalProduksi,self.status))

class perahuLayar :
    '''
    This class contain properties and funtion of "perahu layar" type
    '''
    def __init__(self,nama,tanggalProduksi,lokasi,status):
        self._tipeKapal = "Perahu Layar"
        self._kodeKapal = "KL2022"
        self.nama = nama
        self.tanggalProduksi = tanggalProduksi
        self.lokasi = lokasi
        self.status = status

    def storeData(self) :
        data = {
            "nama" : self.nama,
            "kode" : self._kodeKapal,
            "produksi" : self.tanggalProduksi,
            "lokasi": self.lokasi,
            "status" : self.status
        }
        saveData(self._tipeKapal,data)

    def displayData(self) :
        print("Ship Properties : %s '%s' with code %s is located in %s.\nIt was produced at %s and current status is %s" % (self._tipeKapal,self.nama,self._kodeKapal,self.lokasi,self.tanggalProduksi,self.status))


class kapalPesiar :
    '''
    This class contain properties and funtion of "kapal pesiar" type
    '''
    def __init__(self,nama,tanggalProduksi,lokasi,status):
        self._tipeKapal = "Kapal Pesiar"
        self._kodeKapal = "KP2022"
        self.nama = nama
        self.tanggalProduksi = tanggalProduksi
        self.lokasi = lokasi
        self.status = status

    def storeData(self) :
        data = {
            "nama" : self.nama,
            "kode" : self._kodeKapal,
            "produksi" : self.tanggalProduksi,
            "lokasi": self.lokasi,
            "status" : self.status
        }
        saveData(self._tipeKapal,data)

    def displayData(self) :
        print("Ship Properties : %s '%s' with code %s is located in %s.\nIt was produced at %s and current status is %s" % (self._tipeKapal,self.nama,self._kodeKapal,self.lokasi,self.tanggalProduksi,self.status))

def readJson() :
    cur_path = os.path.dirname(__file__)
    path = os.path.relpath('..\\Lib\\dbShip.json', cur_path)
    jsonfile = open(path,'r')
    data = json.load(jsonfile)
    return data

def writeJson(dataInput) :
    cur_path = os.path.dirname(__file__)
    path = os.path.relpath('..\\Lib\\dbShip.json', cur_path)
    with open(path, 'w') as outfile:
        json.dump(dataInput, outfile,indent= 4, sort_keys=False)

def saveData(key,dataDict) :
    json_object = readJson()
    if key in json_object :
        json_object[key].append(dataDict)
    else :
        print("Type of ship is not registered yet")
    writeJson(json_object)

def getAllData() :
    json_object = readJson()
    for k, v in json_object.items() :
        print("\n{0} : ".format(k))
        for item in v :
            for k1,v1 in item.items() :
                print("- {0} : {1}".format(k1,v1))
            print("\n")
