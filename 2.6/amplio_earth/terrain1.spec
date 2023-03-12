
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
    Hogne Håskjold
    Daniel Speyer
    Yautja
    CapTVK
    Vegard Stolpnessaeter
    GriffonSpade
    Marko Lindqvist (maglev)
    Bardo (cattle, wool, tea, shellfish, incense, uranium, clam)
    Hutzli for FreeCol (corn, cotton, lumber, sugar, tobacco)
    Bluecarrot16 (horse, turkey), Patvanmackelberg (marble)
    
"

[file]
gfx = "amplio_earth/terrain1"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 96
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

; terrain
 0,  0, "t.l0.desert1"

 1,  0, "t.l0.plains1"

 2,  0, "t.l0.forest1"

 3,  0, "t.l0.hills1"

 4,  0, "t.l0.mountains1"

 5,  0, "t.l0.tundra1"

 6,  0, "t.l0.arctic1"

 7,  0, "t.l0.swamp1"

 8,  0, "t.l0.jungle1"
 
 9,  0, "t.l0.inaccessible1"
 
 10, 0, "t.l0.grassland1"

; Terrain special resources:
 0,  2, "ts.oasis"
 0,  4, "ts.oil"
 0,  6, "ts.incense"

 1,  3, "ts.buffalo"
 1,  4, "ts.wheat"
 1,  7, "ts.horses"

 2,  2, "ts.pheasant"
 2,  4, "ts.silk"
 2,  7, "ts.forest_game", "ts.deer"

 3,  2, "ts.coal"
 3,  4, "ts.wine"
 3,  6, "ts.marble"

 4,  2, "ts.gold"
 4,  4, "ts.iron"

 5,  3, "ts.tundra_game"
 5,  4, "ts.furs"

 6,  2, "ts.arctic_ivory", "ts.seals"
 6,  4, "ts.arctic_oil"

 7,  2, "ts.peat"
 7,  4, "ts.spice"
 7,  6, "ts.sugar"

 8,  2, "ts.gems"
 8,  4, "ts.fruit"
 8,  6, "ts.ivory"

 9,  2, "ts.fish"
 9,  4, "ts.whales"
 9,  6, "ts.shellfish"

 10, 3, "ts.cattle"
 10, 5, "ts.wool"
 10, 6, "ts.tea"

 11, 0, "ts.grassland_resources", "ts.river_resources"
 11, 2, "ts.corn"
 11, 4, "ts.cotton"
 11, 6, "ts.tobacco"

; 12, 2, "ts.turkey"
; 12, 4, "ts.clam"
 12, 6, "ts.salt"

; Extras:
 0,  8, "tx.oil_mine", "tx.oil_rig"
 1,  8, "tx.irrigation"
 2,  9, "tx.farmland"
 3,  8, "tx.mine"
 4,  8, "tx.lumber"
 5,  8, "tx.pollution"
 6,  9, "tx.village"
 7,  8, "tx.fallout"

 8,  8, "tx.uranium"
 9,  8, "tx.rubber"
 10, 8, "tx.niter"
 11, 8, "tx.aluminum"
 12, 8, "tx.bombardment"
 13, 9, "tx.storm"

;roads
 13, 0, "road.road_isolated"
 13, 1, "road.road_n"
 13, 2, "road.road_ne"
 13, 3, "road.road_e"
 13, 4, "road.road_se"
 13, 5, "road.road_s"
 13, 6, "road.road_sw"
 13, 7, "road.road_w"
 13, 8, "road.road_nw"

;rails
 14, 0, "road.rail_isolated"
 14, 1, "road.rail_n"
 14, 2, "road.rail_ne"
 14, 3, "road.rail_e"
 14, 4, "road.rail_se"
 14, 5, "road.rail_s"
 14, 6, "road.rail_sw"
 14, 7, "road.rail_w"
 14, 8, "road.rail_nw"

;maglev
 15, 0, "road.maglev_isolated"
 15, 1, "road.maglev_n"
 15, 2, "road.maglev_ne"
 15, 3, "road.maglev_e"
 15, 4, "road.maglev_se"
 15, 5, "road.maglev_s"
 15, 6, "road.maglev_sw"
 15, 7, "road.maglev_w"
 15, 8, "road.maglev_nw"

;add-ons
 17,  0, "t.dither_tile"
 17,  0, "tx.darkness"
 17,  2, "mask.tile"
 17,  2, "t.unknown1"
 6,   0, "t.blend.arctic" ;ice over neighbors
 17,  3, "t.blend.coast"
 17,  3, "t.blend.lake"
 17,  4, "user.attention"
 17,  5, "tx.fog"

;goto path sprites
 16,  7, "path.step"            ; turn boundary within path
 16,  8, "path.exhausted_mp"    ; tip of path, no MP left
 17,  7, "path.normal"          ; tip of path with MP remaining
 17,  8, "path.waypoint"
}
