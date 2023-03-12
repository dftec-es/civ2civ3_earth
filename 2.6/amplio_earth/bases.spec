[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    Hogne Håskjold <hogne@freeciv.org>[HH]
    Eleazar [El] (buoy)
    Vincent Croisier <vincent.croisier@advalvas.be>[VC] (ruins)
    GriffonSpade [GS] (fortresses and airbases)
    Pesloco and Fulger [PF] (naval mine)
    Sveinung Kvilhaugsvik [SK]
    Lexxie [Lx]
"

[file]
gfx = "amplio_earth/bases"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 96
dy = 72
pixel_border = 1

tiles = { "row", "column", "tag"
;[HH][GS]
 0,  0, "base.wonder_mg"
 0,  1, "base.airstrip_bg"
 0,  2, "base.airbase_bg"
 0,  4, "base.outpost_bg"
 0,  5, "base.fortress_bg"
;[Lx]
 0,  6, "base.castle_bg"

;[VC]
 0,  9, "base.ruins_bg"
;[El]
 1,  0, "base.buoy_mg"
;[PF]
 1,  1, "base.naval_mine_bg"
; [SK]
 1,  2, "extra.transport_hub_mg"

;[HH][GS]
 1,  4, "base.outpost_mg"
 1,  5, "base.fortress_mg"
 1,  6, "base.castle_mg"

 ;[HH]
 1,  8, "cd.occupied",
      "city.european_occupied_0",
      "city.classical_occupied_0",
      "city.asian_occupied_0",
      "city.tropical_occupied_0",
      "city.celtic_occupied_0",
      "city.babylonian_occupied_0",
      "city.industrial_occupied_0",
      "city.electricage_occupied_0",
      "city.modern_occupied_0",
      "city.postmodern_occupied_0"
;[HH]
 1,  9, "city.disorder"
;blank defaults
 0,  8, "cd.city",
      "cd.city_wall"
}
