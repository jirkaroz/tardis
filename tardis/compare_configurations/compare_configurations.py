from tardis import run_tardis
#from tardis.gui import interface
import sys
import logging
from matplotlib import pyplot as plt
import numpy as np

def plot(mdl1, mdl2):
    plt.title('Spectrum')
    plt.xlabel('Wavelength (A)')
    plt.ylabel('Intensity')
    wavelength = mdl1.spectrum.wavelength.value
    if mdl1.spectrum.luminosity_density_lambda is None:
        luminosity_density_lambda = np.zeros_like(wavelength)
    else:
        luminosity_density_lambda =\
        mdl1.spectrum.luminosity_density_lambda.value
    plt.plot(wavelength, luminosity_density_lambda, label='b')

    wavelength = mdl2.spectrum.wavelength.value
    if mdl2.spectrum.luminosity_density_lambda is None:
        luminosity_density_lambda = np.zeros_like(wavelength)
    else:
        luminosity_density_lambda =\
        mdl2.spectrum.luminosity_density_lambda.value

    plt.plot(wavelength, luminosity_density_lambda, label='g')

def compare():
    logger = logging.getLogger(__name__)
    
    cfg1 = sys.argv[1]
    cfg2 = sys.argv[2]
    
    atom1 = None
    if len(sys.argv) > 3:
        atom1 = sys.argv[3]
    else:
        atom1 = None
    if len(sys.argv) > 4:
        atom2 = sys.argv[4]
    else:
        atom2 = atom1
    
    logger.info("Running simulation for configuraton 1")
    mdl1 = run_tardis(cfg1, atom1)    
    logger.info("Running simulation for configuraton 2")
    mdl2 = run_tardis(cfg2, atom2)
    
    plot(mdl1, mdl2)
    plt.show()

compare()
