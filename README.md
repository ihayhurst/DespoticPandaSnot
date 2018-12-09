# DespoticPandaSnot
```
Random Python bits as learning exercise
starting with #Character turn / dice fighting game
```
## Pokefight
./codefight.py
Select 1 to load the character file (the default in the code is very dull)
Select 4 to pich a character and battle. 

### TODO:
  - [x ] Break out into functions
  - [x] Read Deck from json file
  - [x] Spit out default deck as tempate
  - [x] Read Level and experience points from .pokefightlevel file
        Use *with* to ensure XP&Level committed to file by building context handler
        Avoided context handler for now by just reading saving the XP all the time
  - [x] Give Fighting attack risk strategy (wiki for how)
  - [ ] Use Fighting attack risk strategy for opponent (random or logic)
  - [ ] Commentry on battle (partially done)
  - [ ] Add visual health guage
  - [ ] Move from txt to GUI
