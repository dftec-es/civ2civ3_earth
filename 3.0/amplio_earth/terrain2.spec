[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]
artists = "
    Hogne Håskjold <haskjold@gmail.com>
    Tim F. Smith <yoohootim@hotmail.com>
    Yautja
    Daniel Speyer
    Eleazar
"

[file]
gfx = "amplio_earth/terrain2"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 96
dy = 48
pixel_border = 1

tiles = { "row", "column","tag"

;* previous coordinates now in forest.spec, hills.spec, and mountains.spec

}


[grid_coasts]

x_top_left = 1
y_top_left = 645
dx = 48
dy = 24
pixel_border = 1

tiles = { "row", "column","tag"

;* previous coordinates now in water.spec

}
