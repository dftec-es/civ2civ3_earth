
[spec]

; Format and options of this spec file:
options = "+Freeciv-3.0-spec"

[info]

; Animal units
; All them made from Public Domain (CC0) images

artists = "
    Bardo [Bd]
    SilviaP [SP]
"

[file]
gfx = "amplio_earth/animals"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "u.wolf1"      ;
  0,  1, "u.canis1"     ;
  0,  3, "u.tiger1"     ;
  0,  4, "u.lion1"      ;
  0,  5, "u.bear1"      ;
  0,  6, "u.snake1"     ;
  0,  7, "u.crocodile1" ;
  0,  8, "u.gorilla1"   ;
  0,  9, "u.hippo1"     ;
  0, 10, "u.rhino1"     ;
  0, 11, "u.elephant1"  ;
  0, 13, "u.kraken1"    ;
  0, 14, "u.storm1"     ;
  2,  0, "u.wolf"       ; [Bd]
  2,  1, "u.panther"    ; [SP]
  2,  2, "u.leopard"    ; [SP]
  2,  3, "u.tiger"      ; [Bd]
  2,  4, "u.lion"       ; [SP]
  2,  5, "u.bear"       ; [Bd]
  2,  6, "u.snake"      ; [Bd]
  2,  7, "u.crocodile"  ; [SP]
  2,  8, "u.gorilla"    ; [Bd]
  2, 13, "u.kraken"     ; [Bd]
  2, 14, "u.storm"      ; [Bd]
}
