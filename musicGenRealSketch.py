import datetime
import fluidsynth
import glob
import numpy as np
import pathlib
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

# Normalizeer de toonhoogte van een noot.
def normalizeerToonHoogte(notenArray, maxToonHoogte):
    notenArray = notenArray/[maxToonHoogte,1.0,1.0]
    return notenArray

# Zet MIDI bestand om in een array van noten met hun bijhorende eigenschappen (bijvoorbeeld: toonhoogte).
def midiNaarNoten(bestand):
    noten = notenClass([], [], [], [], [])
    piano = pretty_midi.PrettyMIDI(bestand).instruments[0]

    # Rangschik alle gespeelde noten door de piano op chronologische volgorde.
    notenGerangschikt = sorted(piano.notes, key = (lambda noot : noot.start))

    # Orden alle noten met haar eigenschappen in de noten class.
    beginVorigeNoot = notenGerangschikt[0].start
    for noot in notenGerangschikt:
        noten.toonHoogte.append(noot.pitch)
        noten.beginTijd.append(noot.start)
        noten.eindTijd.append(noot.end)
        noten.nootInterval.append(noot.start - beginVorigeNoot)
        noten.nootTijd.append(noot.end - noot.start)
        beginVorigeNoot = noot.start
  
    # Creeër een array die alle noten met haar eigenschappen bevat.
    notenArray = np.stack((noten.toonHoogte, noten.beginTijd, noten.eindTijd, noten.nootInterval, noten.nootTijd), axis = 1)
    
    return notenArray

# Deelt dataset op in batches met labels en genormalizeerde inputs.
def verwerkDataset(dataset, batchInputGrootte, maxToonHoogte = 128):
    batchInputGrootte += 1

    # Maak een nieuwe dataset die windows bevat van de dataset uit de input.
    windows = dataset.window(batchInputGrootte, shift=1,
                                drop_remainder=True)

    # Zet de windows om in batches en 'flatten' deze batches tot een nieuwe dataset.
    flatten = lambda x: x.batch(batchInputGrootte, drop_remainder=True)
    flattenedDataset = windows.flat_map(flatten)

    # Deel batch op in inputs en een bijbehorend label. En normalizeer de inputs. 
    def deelNormalizeerBatches(notenArray):
        inputs = notenArray[:-1]
        labels = notenArray[-1]
        labelsDictionary = {}
        labelsDictionary.update({'toonHoogte' : labels[0]})
        labelsDictionary.update({'nootInterval' : labels[1]})
        labelsDictionary.update({'nootTijd' : labels[2]})

        return normalizeerToonHoogte(inputs, maxToonHoogte), labelsDictionary

    # Pas bovenstaande functie toe tot elke batch in de dataset.
    # 2e argument in Dataset.map(), laat deze bovenstaande functie parallel toegepast worden door CPU.
    notenDataset = flattenedDataset.map(deelNormalizeerBatches, num_parallel_calls=tf.data.AUTOTUNE)

    return notenDataset

# Zet een array van noten met haar bijhorende eigenschappen om in een MIDI bestand.
def notenNaarMidi(noten, exportBestand, instrumentNaam = 'Acoustic Grand Piano', geluidsterkte = 100):
    bestand = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program(instrumentNaam))

    # Zet de array van noten om in Pretty_MIDI noten en voeg deze toe aan het gegeven instrument.
    startVorigeNoot = 0
    for noot in noten:
        nootInterval = noot[3]
        nootTijd = noot[4]
        beginTijd = float(startVorigeNoot + nootInterval)
        eindTijd = float(beginTijd + nootTijd)
        noot = pretty_midi.Note(velocity = geluidsterkte, pitch = int(noot[0]), start = beginTijd, end = eindTijd)
        instrument.notes.append(noot)
        startVorigeNoot = beginTijd

    bestand.instruments.append(instrument)

    # Exporteer de Pretty_MIDI object naar een .midi/.mid bestand in de directory van dit programma.
    bestand.write(exportBestand)
    return bestand

# Directory van de dataset.
directory = pathlib.Path('data/maestro-v2.0.0')

# Bestanden binnen de dataset.
bestanden = []
for i in glob.glob('data/maestro-v2.0.0/*/*[.mid]*'):
    bestanden.append(i)

bestanden = glob.glob(str(directory/'**/*.midi*'))

aantalBestanden = 5
alleNoten = []

# Orden alle noten met haar eigenschappen van het gebruikte aantal muziekstukken in een array.
for bestand in bestanden[:aantalBestanden]:
    noten = midiNaarNoten(bestand)
    alleNoten.append(noten)

nAlleNoten = len(alleNoten)
notenArray = np.concatenate(alleNoten)

# Verwijder de begin- en eindtijden voor alle noten.
trainingsNoten = np.delete(notenArray, [1,2], 1)

# Zet de array van trainingsnoten om in een dataset voor Tensorflow.
notenDataset = tf.data.Dataset.from_tensor_slices(trainingsNoten)

batchInputGrootte = 25
verwerkteDataset = verwerkDataset(notenDataset, batchInputGrootte)
