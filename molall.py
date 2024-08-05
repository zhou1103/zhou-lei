import matplotlib.pyplot as plt
from ase import Atoms
from ase.io import write
from ase.visualize.plot import plot_atoms

molecules = {
    "H": [["H"], [[0, 0, 0]]],
    "C": [["C"], [[0, 0, 0]]],
    "N": [["N"], [[0, 0, 0]]],
    "O": [["O"], [[0, 0, 0]]],
    "S": [["S"], [[0, 0, 0]]],
    "CO": [["C", "O"], [[0, 0, 0], [0, 0, 1.15]]],
    "O2": [["O", "O"], [[0, 0, 0], [0, 1.21, 0]]],
    "H2": [["H", "H"], [[0, 0, 0], [0, 0, 0.74]]],
    "N2": [["N", "N"], [[0, 0, 0], [0, 1.1, 0]]],
    "NO": [["N", "O"], [[0, 0, 0], [0, 0, 1.15]]],
    "H2O": [["O", "H", "H"], [[0, 0, 0], [0.76, 0.585, 0.1], [-0.76, 0.585, 0.1]]],
    "CO2": [["C", "O", "O"], [[0, 0, 0], [0, 1.16, 0], [0, -1.16, 0]]],
    "N2O": [["N", "N", "O"], [[0, 0, 0], [0, 1.13, 0], [0, 2.31, 0]]],
    "NO2": [["N", "O", "O"], [[0, 0, 0], [0, 1.1, 0.465], [0, -1.1, 0.465]]],
    "NH3": [["N", "H", "H", "H"], [[0, 0, 0], [0.93, 0, 0.3], [-0.465, 0.806, 0.3], [-0.465, -0.806, 0.3]]],
    "CH4": [["C", "H", "H", "H", "H"], [[0.0, 0.0, 0.0],[0.6287, 0.6287, 0.6287],[-0.6287, -0.6287, 0.6287],[-0.6287, 0.6287, -0.6287],[0.6287, -0.6287, -0.6287]]],
    "H2O2": [["O", "O", "H", "H"], [[0, 0, 0], [0, 1.475, 0], [0.819, 1.555, 0.475], [-0.819, -0.078, 0.475]]],
    "HCHO": [["C", "O", "H", "H"], [[0, 0, 0], [0, 1.21, 0], [-0.943, -0.588, 0], [0.943, -0.58, 0]]],
    "CH3OH": [["C", "O", "H", "H", "H", "H"], [[0.0, 0.0, 0.0], [0, 1.427, 0], [0.515, -0.373, 0.892], [-1.03, -0.373, 0], [0.515, -0.373, -0.892], [0.905, 1.736, 0]]],
    "HCOOH": [["C", "O", "O", "H", "H"], [[0, 0, 0], [0, 1.343, 0], [0.99, -0.682, 0], [0.924, 1.621, 0], [-1.022, -0.4, 0]]],
    "C2H2": [["C", "C", "H", "H"], [[0, 0, 0], [0, 1.203, 0], [0, 2.266, 0], [0, -1.063, 0]]],
    "C2H4": [["C", "C", "H", "H", "H", "H"], [[0, 0, 0], [0, 1.339, 0], [0.929, 1.902, 0], [-0.929, 1.902, 0], [0.902, -0.563, 0], [-0.902, -0.563, 0]]],
    "C2H6": [["C", "C", "H", "H", "H", "H", "H", "H"], [[0, 0, 0], [0, 1.536, 0], [-1.019, 1.925, 0], [0.51, 1.925, -0.883], [0.51, 1.925, 0.883], [1.019, -0.389, 0], [-0.51, -0.389, 0.883], [-0.51, -0.389, -0.883]]],
    "CH3CHO": [["C", "C", "O", "H", "H", "H", "H"], [[0, 0, 0], [0, 1.494, 0], [1.056, 2.112, 0], [1.038, -0.397, 0.018], [-0.543, -0.367, 0.895], [-0.513, -0.367, -0.913], [-0.937, 2.035, 0]]],
    "C2H5OH": [["C", "C", "O", "H", "H", "H", "H", "H", "H"], [[0, 0, 0], [0, 1.512, 0], [-1.362, 1.95, 0], [-1.321, 2.92, 0], [1.045, -0.336, 0], [-0.535, -0.333, 0.887], [-0.535, -0.333, -0.887], [0.481, 1.919, 0.885], [0.481, 1.917, -0.885]]],
    "CH3COOH": [["C", "C", "O", "O", "H", "H", "H", "H"], [[0, 0, 0], [0, 1.495, 0], [-1.083, 2.09, 0], [1.189, 2.202, 0], [1.046, -0.372, -0.023], [-0.534, -0.369, -0.901], [-0.502, -0.391, 0.91], [1.049, 3.206, 0]]],
    "C3H6": [["C", "C", "C", "H", "H", "H", "H", "H", "H"], [[0, 0, 0], [-0.648, 1.168, 0], [-0.726, -1.312, 0], [1.085, 0, 0], [-0.088, 2.097, 0], [-1.733, 1.21, 0], [-0.446, -1.868, -0.942], [-0.431, -1.909, 0.863], [-1.829, -1.175, 0]]],
    "C3H8": [["C", "C", "C", "H", "H", "H", "H", "H", "H", "H", "H"], [[0, 0, 0], [0.849, 1.268, 0], [0.849, -1.268, 0], [-0.659, 0, 0.876], [-0.659, 0, -0.876], [0.212, 2.158, 0], [1.488, 1.327, 0.88], [1.488, 1.327, -0.88], [0.212, -2.158, 0], [1.488, -1.327, 0.88], [1.488, -1.327, -0.88]]]
}

n_molecules = len(molecules)
n_cols = 6
n_rows = (n_molecules + n_cols - 1) // n_cols

fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols*3, n_rows*3))

axes = axes.flatten()

for idx, (name, (symbols, positions)) in enumerate(molecules.items()):
    molecule = Atoms(symbols=symbols, positions=positions)
    
    molecule.center()
    if len(molecule) > 1:
        direction = molecule[1].position - molecule[0].position
        molecule.rotate(direction, 'x', rotate_cell=False)
    
    plot_atoms(molecule, ax=axes[idx], show_unit_cell=False)
    axes[idx].set_title(name)

    axes[idx].axis('off')

for ax in axes[n_molecules:]:
    ax.axis('off')

plt.tight_layout()
plt.savefig('molecule.png')