# Google Maps Distance Matrix
This project is developed in `Python` and allows you to create and export to a `.csv` file an array of distances between several points through Google Maps.

#### What do you need?
To get started use only the Google Maps API key. You can get yours in [Google Maps Plataform](http://maps.googleapis.com/).
Put your key on line number 14
```python
self.key = "YOUR_KEY_HERE"  
```

#### Functions
All distances are in meters.
 - Constructor()
	 - `matrix = Distances()`
 - addOrigin(origin)
	 - `matrix.addOrigin("Lisbon")`
 - addDestination(destination)
	 - `matrix.addDestination("Paris")`
 - printMatrix()
	 - `matrix.printMatrix()`
 - exportMatrix()
	 - `matrix.exportMatrix()`

## Example
```python
from Matrix import Matrix  
  
#Initialize  
matrix = Matrix()  
  
#Add Origins  
matrix.addOrigin("Marinha Grande")  
matrix.addOrigin("Lisbon")  
matrix.addOrigin("Paris")  
  
#Add Destinations  
matrix.addDestination("Marinha Grande")  
matrix.addDestination("Lisbon")  
matrix.addDestination("Paris")  
  
#Export Matrix  
matrix.exportMatrix('Matrix.csv')
```
#### Result

| Origin/Destiny | Marinha Grande | Lisbon | Paris |
|--|--|--|--|
|**Marinha Grande**|0|136192|1650630|
|**Lisbon**|136081|0|1736489|
|**Paris**|1651168|1735442|0|

