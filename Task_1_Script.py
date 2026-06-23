import vtk 
import sys 

### SAVING COMANDLINE ARGUMENTS###
input_file = sys.argv[1]
isovalue = float(sys.argv[2])
output_file = sys.argv[3]

print("saving arguments...")

### READING THE DATASET ###
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(input_file)
reader.Update()
imageData = reader.GetOutput()

print("input data loaded...")

### EXTRACTING DIMENTIONS FROM THE IMAGEDATA ###
dims = imageData.GetDimensions()
nx = dims[0]
ny = dims[1]

### EXTRACTING PRESSURE DATA FROM THE IMAGEDATA ###
pressure = imageData.GetPointData().GetScalars()


print("pressure data exctracted...")

### OUTPUT VARIABLES ###
points = vtk.vtkPoints()
lines = vtk.vtkCellArray()

### DEFINING INVERSE INTERPOLATION FUNCTION ###
def inverse_interpolation(p1, p2, v1, v2, c):
    if abs(v1-v2) < 1e-10:
        return p1
    m = (v1-c)/(v1-v2)
    x = p1[0] + m*(p2[0]-p1[0])
    y = p1[1] + m*(p2[1]-p1[1])
    z = p1[2]

    return (x, y, z)

### COMPUTING IDS OF EACH POINT OF EACH CELL ###
for i in range(ny-1):
    for j in range(nx-1):

        # point ids of the corners
        id0 = i*nx + j
        id1 = i*nx + (j+1)
        id2 = (i+1)*nx + (j+1)
        id3 = (i+1)*nx + j

        # point coordinates of the corners
        p0 = imageData.GetPoint(id0)
        p1 = imageData.GetPoint(id1)
        p2 = imageData.GetPoint(id2)
        p3 = imageData.GetPoint(id3)

        # pressure values at the corners 
        v0 = pressure.GetTuple1(id0)
        v1 = pressure.GetTuple1(id1)
        v2 = pressure.GetTuple1(id2)
        v3 = pressure.GetTuple1(id3)

        # identifying the edges intersected by the isocontour
        edges = []

        if(v0 - isovalue)*(v1-isovalue) <= 0:
            p = inverse_interpolation(p0, p1, v0, v1, isovalue)
            edges.append(p)

        if(v1 - isovalue)*(v2-isovalue) <= 0:
            p = inverse_interpolation(p1, p2, v1, v2, isovalue)
            edges.append(p)

        if(v2 - isovalue)*(v3-isovalue) <= 0:
            p = inverse_interpolation(p2, p3, v2, v3, isovalue)
            edges.append(p)

        if(v3 - isovalue)*(v0-isovalue) <= 0:
            p = inverse_interpolation(p3, p0, v3, v0, isovalue)
            edges.append(p)

        # creating line segments for the isocontour
        if len(edges) == 2:
            pid1 = points.InsertNextPoint(edges[0])
            pid2 = points.InsertNextPoint(edges[1])

            line = vtk.vtkLine()
            line.GetPointIds().SetId(0, pid1)
            line.GetPointIds().SetId(1, pid2)

            lines.InsertNextCell(line)

print("poly data created...")

### BUILDING POLYDATA ###
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetLines(lines)

print("poly data compiled...")

### WRITING THE OUTPUT FILE ###
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName(output_file)
writer.SetInputData(polydata)
writer.Write()

print("Saved: ", output_file)