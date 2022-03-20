import collections
import datetime
import fluidsynth
import glob
import numpy as np
import pathlib
import pandas as pd
import pretty_midi
import seaborn as sns
import tensorflow as tf

from IPython import display
from matplotlib import pyplot as plt
from typing import Dict, List, Optional, Sequence, Tuple

class notenClass:
    def __init__(self, toonHoogte, beginTijd, eindTijd, nootInterval, nootTijd):
        self.toonHoogte = toonHoogte
        self.beginTijd = beginTijd
        self.eindTijd = eindTijd
        self.nootInterval = nootInterval
        self.nootTijd = nootTijd

# NOG AANPASSEN OVER HET INSTRUMENT

# Zet MIDI bestand om in een array van noten met hun bijhorende eigenschappen (bijvoorbeeld: toonhoogte).
def midiNaarNoten(bestand):
    noten = notenClass([], [], [], [], [])

    # Piano: elk muziekstuk in de dataset wordt gespeeld met de piano.
    instrument = pretty_midi.PrettyMIDI(bestand).instruments[0]

    # Rangschik alle gespeelde noten door de piano op chronologische volgorde.
    notenGerangschikt = sorted(instrument.notes, key = (lambda noot : noot.start))

    # Orden alle noten met haar eigenschappen in de noten class.
    nootStart = notenGerangschikt[0].start
    for noot in notenGerangschikt:
        noten.toonHoogte.append(noot.pitch)
        noten.beginTijd.append(noot.start)
        noten.eindTijd.append(noot.end)
        noten.nootInterval.append(noot.start - nootStart)
        noten.nootTijd.append(noot.end - noot.start)
        nootStart = noot.start
  
    # Creeër een array die alle noten met haar eigenschappen bevat.
    notenArray = np.stack((noten.toonHoogte, noten.beginTijd, noten.eindTijd, noten.nootInterval, noten.nootTijd), axis = 1)
    
    return notenArray

# Directory van de dataset.
directory = pathlib.Path('data/maestro-v2.0.0')

# Bestanden binnen de dataset.
bestanden = []
for i in glob.glob('data/maestro-v2.0.0/*/*[.mid]*'):
    bestanden.append(i)

bestanden = glob.glob(str(directory/'**/*.midi*'))