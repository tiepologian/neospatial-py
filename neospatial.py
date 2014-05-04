#!/usr/bin/python

import requests
import json

class SpatialConnection:
    def __init__(self, host, port):
        self.hostname = host
        self.port = port
        return

    def createIndex(self, name):
        payload = {"name":name, "config":{"provider":"spatial","geometry_type":"point","lat":"lat","lon":"lon"}}
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post("http://"+self.hostname+":"+str(self.port)+"/db/data/index/node/", data=json.dumps(payload), headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            return name
        else:
            raise Exception("Error Executing Query")

    def createNode(self, lat, lon, props={}):
        payload = {"lat":lat,"lon":lon}
        payload.update(props)
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post("http://"+self.hostname+":"+str(self.port)+"/db/data/node/", data=json.dumps(payload), headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            return r.json()['self']
        else:
            raise Exception("Error Executing Query")

    def addNodeToIndex(self, node, index):
        payload = {"layer":index,"node":node}
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post("http://"+self.hostname+":"+str(self.port)+"/db/data/ext/SpatialPlugin/graphdb/addNodeToLayer", data=json.dumps(payload), headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            return node
        else:
            raise Exception("Error Executing Query")

    def findWithinDistance(self, index, lat, lon, distance):
        payload = {"layer":index,"pointY":lat,"pointX":lon,"distanceInKm":distance}
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post("http://"+self.hostname+":"+str(self.port)+"/db/data/ext/SpatialPlugin/graphdb/findGeometriesWithinDistance", data=json.dumps(payload), headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            result = []
            for i in r.json():
                result.append({'id':i['self'],'data':i['data']})
            return result
        else:
            raise Exception("Error Executing Query")

    def findWithinBoundingBox(self, index, minX, maxX, minY, maxY):
        payload = {"layer":index,"minx":minX,"maxx":maxX,"miny":minY,"maxy":maxY}
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post("http://"+self.hostname+":"+str(self.port)+"/db/data/ext/SpatialPlugin/graphdb/findGeometriesInBBox", data=json.dumps(payload), headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            result = []
            for i in r.json():
                result.append({'id':i['self'],'data':i['data']})
            return result
        else:
            raise Exception("Error Executing Query")

