# MUSIC AI
Dit is een project dat wordt ingeleverd als een eindexamen profielwerkstuk.

# Introductie
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

Als je deze repositry cloned staat de FluidSynth API automatisch in je map. Wanneer de fluidsynt.py je map dan gaat afzoeken naar DLL's kan deze deze direct vinden. Als dat niet gebeurt. Zet dan de locatie van de DLL's in je PATH. Dit kan door in je settings de setting edit the system environment variables op te zoeken en daar de locatie toe te voegen bij waar staat PATH.

![image](https://user-images.githubusercontent.com/89349677/148691338-b5efd851-2e81-4337-b300-2b9caa2441b3.png)

![image](https://user-images.githubusercontent.com/89349677/148691350-aa5284d0-a720-4ca8-8b30-8e3be30705af.png)

![image](https://user-images.githubusercontent.com/89349677/148691397-17e4b905-c903-48e2-9cb8-d2f6acfbd9d7.png)

![image](https://user-images.githubusercontent.com/89349677/148691423-b035f9ae-7373-4826-a7b6-34b7efbfdead.png)

De locatie kan voor de zekerheid worden toegevoegd en in de system en in de user variables.

# Credits
Gemaakt door Alexander Znamenskiy en Maurice van de Streek van het Lorentz Casimir Lyceum
