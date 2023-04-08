# Civ2Civ3 Earth (Modpack for Freeciv)
"civ2civ3_earth" is a fork of the ruleset civ2civ3 (shipped with freeciv since v2.5), from the same author. It includes new features, tries to improve balance, and is more suitable for playing on Earth maps, or similar scenarios. It includes its own tileset "amplio_earth", and a world map scenario, adapted to be played with these rules.


![Tileset view](/Screenshots/civ2civ3_earth-tileset.jpg?raw=true "Tileset view")

Tagged versions have been tested and are ready to be played. The latest one uses to be available to install with the "modpack installer" tool shipped with freeciv.

How to use freeciv modpack installer to install it from github:
* Depending which freeciv client you installed, you will probably have one modpack installer tool called something like "freeciv-mp-gtk3". Launch it. 
* Where it says "Modpack URL", paste the following link (the one that matches your freeciv version):
https://raw.githubusercontent.com/dftec-es/civ2civ3_earth/master/2.6/civ2civ3_earth-2.6.modpack
https://raw.githubusercontent.com/dftec-es/civ2civ3_earth/master/3.0/civ2civ3_earth-3.0.mpdl
* Press install modpack

How to install it manually from github:
* Download the latest pack from the "tags" section.
* Extract to the same folder where "saves" folder is located (where savegames are stored).<br/>
In linux it uses to be: /home/username/.freeciv/
* Launch freeciv, start a new game, select the ruleset civ2civ3_earth, and load the tileset amplio_earth when asked.<br/>
If the tileset is not loaded, try to open freeciv Client settings &rarr; Local options &rarr; Graphics tab &rarr; Tileset (Square), and select "amplio_earth"

The installed files and folders should look like this:
```sh
/.freeciv/2.6/amplio_earth/
/.freeciv/2.6/civ2civ3_earth/
/.freeciv/2.6/scenarios/
/.freeciv/2.6/amplio_earth.tilespec
/.freeciv/2.6/civ2civ3_earth.serv
```
where /2.6/ should match the freeciv version that you had installed.

