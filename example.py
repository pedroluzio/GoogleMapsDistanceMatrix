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