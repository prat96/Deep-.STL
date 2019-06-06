import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

warhammer = mesh.Mesh.from_file('./Datasets/warhammer.stl')

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
# your_mesh = mesh.Mesh.from_file('tests/stl_binary/HalfDonut.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(warhammer.vectors))

# Auto scale to the mesh size
scale = warhammer.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()