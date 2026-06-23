
Task 1: 2D Isocontour Extraction

------------------------------------------------------------------------------------

## DESCRIPTION

This program extracts an isocontour from a 2D scalar field stored in a VTK ImageData (.vti) file.

The contour extraction algorithm is implemented from scratch using edge-intersection testing and linear interpolation. No VTK contour extraction filters are used.

The extracted contour is stored as a vtkPolyData object and written to a VTK PolyData (.vtp) file that can be visualized in ParaView.

------------------------------------------------------------------------------------

## REQUIREMENTS

Python 3

VTK Python package

Install VTK using:

pip install vtk

------------------------------------------------------------------------------------

## INPUT PARAMETERS

The script requires three command-line arguments:

1. Input VTI file
   Path to the 2D scalar field dataset.

2. Isovalue
   Scalar value at which the contour should be extracted.

3. Output VTP file
   Name of the output contour file.

------------------------------------------------------------------------------------

## USAGE

Use command prompt or terminal, while being in the same folder as of the script and the input file,

Command:

python isocontour.py <input_vti_file> <isovalue> <output_vtp_file>

Example 1:

python isocontour.py Isabel_2D.vti -500 contour.vtp

Example 2:

python isocontour.py Isabel_2D.vti 100 contour_100.vtp

------------------------------------------------------------------------------------

## OUTPUT

The program generates a VTK PolyData (.vtp) file containing the extracted contour lines.

Example:

Input:
Isabel_2D.vti
Isovalue = -500

Output:
contour.vtp

------------------------------------------------------------------------------------

## VISUALIZATION

The generated .vtp file can be opened directly in ParaView.

Steps:

1. Open ParaView.
2. Click File → Open.
3. Select the generated .vtp file.
4. Click Apply.
5. Change contour color if it is not clearly visible.

------------------------------------------------------------------------------------

## NOTES

* The script works for any valid isovalue within the scalar range of the dataset.
* The contour is generated using linear interpolation along cell edges.
* Ambiguous marching-square cases are not explicitly resolved, as specified in the assignment instructions.
______________________________________________________________________________________

Task 2: Volume Rendering using VTK Ray Casting

### Description

This program performs 3D volume rendering of the provided Hurricane Simulation dataset using VTK's ray-casting volume renderer (`vtkSmartVolumeMapper`).

The script applies:

* Color Transfer Function
* Opacity Transfer Function
* Optional Phong Shading
* Volume Outline using `vtkOutlineFilter`

A 1000 × 1000 render window is created to display the rendered volume.

------------------------------------------------------------------------------------

### Requirements

* Python 3
* VTK

Install VTK using:

pip install vtk

------------------------------------------------------------------------------------

### Files

* `volume_render.py` : Python script for volume rendering
* Input dataset : VTK Image Data (`.vti`)

------------------------------------------------------------------------------------

### Usage

python volume_render.py <input_volume.vti> <shading>

------------------------------------------------------------------------------------

### Parameters

`<input_volume.vti>` : Path to the 3D scalar volume dataset.

`<shading>` : Controls whether Phong shading is enabled.

0 --> Disable Phong Shading 
1 --> Enable Phong Shading  

------------------------------------------------------------------------------------

### Output

The script opens an interactive VTK rendering window displaying:

* Ray-casted volume rendering
* Dataset outline
* Transfer function based coloring
* Optional Phong shaded visualization

Close the rendering window to terminate the program.

------------------------------------------------------------------------------------

### Notes

* The script uses `vtkSmartVolumeMapper()` for ray-casting based volume rendering.
* The dataset must be in VTK Image Data (`.vti`) format.
* All transfer-function values and shading parameters are implemented exactly as specified in the assignment.
