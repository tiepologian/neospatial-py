neospatial-py
=============

Python Wrapper for Neo4j Spatial Plugin

### Requirements
* Install [neo4j/spatial](https://github.com/neo4j/spatial) server plugin

### Installation
```
sudo pip install neospatial
```

### Usage
```python
>>> from neospatial import *

>>> spatial = SpatialConnection("localhost", 7474)
>>> index = spatial.createIndex('geom')

>>> node1 = spatial.createNode(45.46775, 9.21056, {'name':'Gold Restaurant'})
>>> spatial.addNodeToIndex(node1, index)

>>> node2 = spatial.createNode(45.48107, 9.19997, {'name':'Ristorante Da Giannino'})
>>> spatial.addNodeToIndex(node2, index)

>>> result = spatial.findWithinDistance(index, 45.48608, 9.20018, 5)
>>> for i in result:
>>>     print i['data']['name']

>>> Ristorante Da Giannino
>>> Gold Restaurant
```
