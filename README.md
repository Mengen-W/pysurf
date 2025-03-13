# Pysurf
This is the documentation for the open-source Python code - pysurf. This code will generate phase diagrams for surfaces of perovskites from density functional theory calculations. 

Powered by Pandas, Numpy, and Matplotlib, the code reads the formation energy calculated at chemical potentials = 0 eV and chemical compositions from a .csv file, evaluates the most stable surfaces under the user-defined chemical potential region, and generates a color contour plot for the phase diagram.

An example is given for the surface phase diagram of cesium lead iodide, and the code is easily generalized to other materials.

## Usage
Download the pysurf.py code and the data folder, and replace the surface_energy.csv with your raw data.

## License
This code is made available under the MIT license.

## Requirements
pysurf.py is compatible with Python 3 and the following open source Python packages should be installed:

* numpy

* matplotlib

* pandas

## Contact
Mengen Wang, SUNY Binghamton (mengenwang@binghamton.edu)

Kejia Li, SUNY Binghamton 

## Citation
J. Phys. Chem. C 2025, 129, 7, 3809–3816

@article{li2024_cspbi3_surface,

  title={Density Functional Theory Study of Surface Stability and Phase Diagram of Orthorhombic CsPbI3},
  
  author={Li, Kejia and Wang, Mengen},
  
  journal={The Journal of Physical Chemistry C},
  
  volume={129},
  
  number={7},
  
  pages={3809},
  
  year={2025},

  url={https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.4c07358
  },
  
  publisher={ACS Publications}
}
