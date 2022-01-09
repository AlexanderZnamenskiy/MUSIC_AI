# MUSIC AI
Dit is een project dat wordt ingeleverd als een eindexamen profielwerkstuk.

# Introduction
De belangrijkste file in de repositry is de musgen2.ipynb file. Een .ipynb file kan worden geopend in google colab maar ook in Visual Studio Code. Dit is een type file waarin het makkelijk is om verschillende delen van de code te runnen en er uitleg bij te geven. Deze repository bevat ook ons complete verslag en de _ databases die binnen de .ipynb file kunnen worden aangeroepen.

# Downloaden
Deze repository is makkelijk te clonen op je harde schrijf door (op windows) met de command prompt "te cd-en" naar een locatie zoals bijvoorbeeld:

```
cd C:/Users/User/Documents
```
en dan een command aanroepen:
```
git clone https://github.com/AlexanderZnamenskiy/MUSIC_AI.git.
```

# Testen
Om de code van musgen2.ipynb te runnen is het nodig om alle python blokjes af te gaan. Van tevoren is het ook belangrijk om de nodige componenten te installeren op je pc met behulp van pip install. Sommige audio componenten werken niet binnen Visual Studio Code, daarom worden de nodige audiofiles zoals bijvoorbeeld de example.midi en de output.midi direct geexporteerd naar de locale file. Een MIDI file kan soms te snel of te langzaam afspelen terwijl de melodie zelf duidelijk is. Om de snelheid aan te passen is er een mogelijkheid om de MIDI file direct te kopieren naar een simpele midi editor zoals FlStudio, Ableton LIVE of MUSESCORE.

# Downloaden nodige componenten
Als eerste is het belangrijk om in de pip file van je computer deze file te zetten: https://github.com/nwhitehead/pyfluidsynth. Verder moet je deze file unzippen en dan door middel van je command prompter en python binnen deze file de setup.py te runnen:

```
cd C:\Users\[USER]\AppData\Local\Programs\Python\[PYTHON VERSION]\Lib\site-packages\pyfluidsynth-master

python setup.py install
```

Verder kan je met de command
```
pip install --upgrade pyfluidsynth --user
```
pyFluidSynth in je library zetten. Nu kan je door
```
pip list
```
in te typen controleren of pyFluidSynth is geinstallerd.
