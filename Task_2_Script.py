import vtk
import sys

if len(sys.argv) != 3:
    print("Usage: python volume_render.py <input.vti> <shading(0/1)>")
    sys.exit(1)

input_file = sys.argv[1]
use_shading = int(sys.argv[2])

# Read Volume Data

reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(input_file)
reader.Update()

volume_data = reader.GetOutput()

print("Volume dataset loaded successfully.")

# Color Transfer Function

color_tf = vtk.vtkColorTransferFunction()

color_tf.AddRGBPoint(-4931.54, 0.0, 1.0, 1.0)
color_tf.AddRGBPoint(-2508.95, 0.0, 0.0, 1.0)
color_tf.AddRGBPoint(-1873.90, 0.0, 0.0, 0.5)
color_tf.AddRGBPoint(-1027.16, 1.0, 0.0, 0.0)
color_tf.AddRGBPoint(-298.031, 1.0, 0.4, 0.0)
color_tf.AddRGBPoint(2594.97, 1.0, 1.0, 0.0)

# Opacity Transfer Function

opacity_tf = vtk.vtkPiecewiseFunction()

opacity_tf.AddPoint(-4931.54, 1.0)
opacity_tf.AddPoint(101.815, 0.002)
opacity_tf.AddPoint(2594.97, 0.0)

# Volume Property

volume_property = vtk.vtkVolumeProperty()

volume_property.SetColor(color_tf)
volume_property.SetScalarOpacity(opacity_tf)

volume_property.SetInterpolationTypeToLinear()

# Phong Shading

if use_shading:
    volume_property.ShadeOn()

    volume_property.SetAmbient(0.5)
    volume_property.SetDiffuse(0.5)
    volume_property.SetSpecular(0.5)

    print("Phong Shading Enabled")
else:
    volume_property.ShadeOff()
    print("Phong Shading Disabled")

# Ray Casting Volume Mapper

mapper = vtk.vtkSmartVolumeMapper()
mapper.SetInputData(volume_data)

# Volume Actor

volume = vtk.vtkVolume()
volume.SetMapper(mapper)
volume.SetProperty(volume_property)

# Outline Filter

outline_filter = vtk.vtkOutlineFilter()
outline_filter.SetInputData(volume_data)

outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(
    outline_filter.GetOutputPort()
)

outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)

# Renderer

renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)
renderer.AddActor(outline_actor)

renderer.SetBackground(1.0, 1.0, 1.0)

# Render Window

render_window = vtk.vtkRenderWindow()

render_window.AddRenderer(renderer)
render_window.SetSize(1000, 1000)

# Interactor

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start Rendering

render_window.Render()
interactor.Start()