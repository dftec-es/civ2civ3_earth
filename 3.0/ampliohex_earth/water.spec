
[spec]

; Format and options of this spec file:
options = "+Freeciv-3.0-spec"

[info]

artists = "
    Hogne Håskjold
    Tim F. Smith <yoohootim@hotmail.com>
    Yautja
    Daniel Speyer
    Eleazar
"

[file]
gfx = "amplio_earth/water"

[grid_coasts]

x_top_left = 1
y_top_left = 437
dx = 48
dy = 24
pixel_border = 1

tiles = { "row", "column", "tag"

; ocean (water-ice):
 0, 0,  "t.l1.coast_cell_u_w_w_w" ;vacant cell
 0, 2,  "t.l1.coast_cell_u_i_w_w"
 0, 4,  "t.l1.coast_cell_u_w_i_w"
 0, 6,  "t.l1.coast_cell_u_i_i_w"
 0, 8,  "t.l1.coast_cell_u_w_w_i"
 0, 10, "t.l1.coast_cell_u_i_w_i"
 0, 12, "t.l1.coast_cell_u_w_i_i"
 0, 14, "t.l1.coast_cell_u_i_i_i"
 
 1, 0,  "t.l1.coast_cell_d_w_w_w" ;vacant cell
 1, 2,  "t.l1.coast_cell_d_i_w_w"
 1, 4,  "t.l1.coast_cell_d_w_i_w"
 1, 6,  "t.l1.coast_cell_d_i_i_w"
 1, 8,  "t.l1.coast_cell_d_w_w_i"
 1, 10, "t.l1.coast_cell_d_i_w_i"
 1, 12, "t.l1.coast_cell_d_w_i_i"
 1, 14, "t.l1.coast_cell_d_i_i_i"

 2, 0,  "t.l1.coast_cell_l_w_w_w" ;vacant cell
 2, 2,  "t.l1.coast_cell_l_i_w_w"
 2, 4,  "t.l1.coast_cell_l_w_i_w"
 2, 6,  "t.l1.coast_cell_l_i_i_w"
 2, 8,  "t.l1.coast_cell_l_w_w_i"
 2, 10, "t.l1.coast_cell_l_i_w_i"
 2, 12, "t.l1.coast_cell_l_w_i_i"
 2, 14, "t.l1.coast_cell_l_i_i_i"

 2, 1,  "t.l1.coast_cell_r_w_w_w"
 2, 3,  "t.l1.coast_cell_r_i_w_w"
 2, 5,  "t.l1.coast_cell_r_w_i_w"
 2, 7,  "t.l1.coast_cell_r_i_i_w"
 2, 9,  "t.l1.coast_cell_r_w_w_i"
 2, 11, "t.l1.coast_cell_r_i_w_i"
 2, 13, "t.l1.coast_cell_r_w_i_i"
 2, 15, "t.l1.coast_cell_r_i_i_i"

; ocean (shallow-land):
; 3, 0,  "t.l0.coast_cell_u_s_s_s" ;vacant cell
; 3, 2,  "t.l0.coast_cell_u_l_s_s"
; 3, 4,  "t.l0.coast_cell_u_s_l_s"
; 3, 6,  "t.l0.coast_cell_u_l_l_s"
; 3, 8,  "t.l0.coast_cell_u_s_s_l"
; 3, 10, "t.l0.coast_cell_u_l_s_l"
; 3, 12, "t.l0.coast_cell_u_s_l_l"
; 3, 14, "t.l0.coast_cell_u_l_l_l"
;
; 4, 0,  "t.l0.coast_cell_d_s_s_s" ;vacant cell
; 4, 2,  "t.l0.coast_cell_d_l_s_s"
; 4, 4,  "t.l0.coast_cell_d_s_l_s"
; 4, 6,  "t.l0.coast_cell_d_l_l_s"
; 4, 8,  "t.l0.coast_cell_d_s_s_l"
; 4, 10, "t.l0.coast_cell_d_l_s_l"
; 4, 12, "t.l0.coast_cell_d_s_l_l"
; 4, 14, "t.l0.coast_cell_d_l_l_l"
;
; 5, 0,  "t.l0.coast_cell_l_s_s_s" ;vacant cell
; 5, 2,  "t.l0.coast_cell_l_l_s_s"
; 5, 4,  "t.l0.coast_cell_l_s_l_s"
; 5, 6,  "t.l0.coast_cell_l_l_l_s"
; 5, 8,  "t.l0.coast_cell_l_s_s_l"
; 5, 10, "t.l0.coast_cell_l_l_s_l"
; 5, 12, "t.l0.coast_cell_l_s_l_l"
; 5, 14, "t.l0.coast_cell_l_l_l_l"
;
; 5, 1,  "t.l0.coast_cell_r_s_s_s"
; 5, 3,  "t.l0.coast_cell_r_l_s_s"
; 5, 5,  "t.l0.coast_cell_r_s_l_s"
; 5, 7,  "t.l0.coast_cell_r_l_l_s"
; 5, 9,  "t.l0.coast_cell_r_s_s_l"
; 5, 11, "t.l0.coast_cell_r_l_s_l"
; 5, 13, "t.l0.coast_cell_r_s_l_l"
; 5, 15, "t.l0.coast_cell_r_l_l_l"

; deep ocean (water-ice):
 0, 0,  "t.l1.floor_cell_u_w_w_w" ;vacant cell
 0, 2,  "t.l1.floor_cell_u_i_w_w"
 0, 4,  "t.l1.floor_cell_u_w_i_w"
 0, 6,  "t.l1.floor_cell_u_i_i_w"
 0, 8,  "t.l1.floor_cell_u_w_w_i"
 0, 10, "t.l1.floor_cell_u_i_w_i"
 0, 12, "t.l1.floor_cell_u_w_i_i"
 0, 14, "t.l1.floor_cell_u_i_i_i"
 
 1, 0,  "t.l1.floor_cell_d_w_w_w" ;vacant cell
 1, 2,  "t.l1.floor_cell_d_i_w_w"
 1, 4,  "t.l1.floor_cell_d_w_i_w"
 1, 6,  "t.l1.floor_cell_d_i_i_w"
 1, 8,  "t.l1.floor_cell_d_w_w_i"
 1, 10, "t.l1.floor_cell_d_i_w_i"
 1, 12, "t.l1.floor_cell_d_w_i_i"
 1, 14, "t.l1.floor_cell_d_i_i_i"

 2, 0,  "t.l1.floor_cell_l_w_w_w" ;vacant cell
 2, 2,  "t.l1.floor_cell_l_i_w_w"
 2, 4,  "t.l1.floor_cell_l_w_i_w"
 2, 6,  "t.l1.floor_cell_l_i_i_w"
 2, 8,  "t.l1.floor_cell_l_w_w_i"
 2, 10, "t.l1.floor_cell_l_i_w_i"
 2, 12, "t.l1.floor_cell_l_w_i_i"
 2, 14, "t.l1.floor_cell_l_i_i_i"

 2, 1,  "t.l1.floor_cell_r_w_w_w"
 2, 3,  "t.l1.floor_cell_r_i_w_w"
 2, 5,  "t.l1.floor_cell_r_w_i_w"
 2, 7,  "t.l1.floor_cell_r_i_i_w"
 2, 9,  "t.l1.floor_cell_r_w_w_i"
 2, 11, "t.l1.floor_cell_r_i_w_i"
 2, 13, "t.l1.floor_cell_r_w_i_i"
 2, 15, "t.l1.floor_cell_r_i_i_i"

; deep ocean (deep-shallow):
; 6, 0,  "t.l0.floor_cell_u_d_d_d" ;vacant cell
; 6, 2,  "t.l0.floor_cell_u_s_d_d"
; 6, 4,  "t.l0.floor_cell_u_d_s_d"
; 6, 6,  "t.l0.floor_cell_u_s_s_d"
; 6, 8,  "t.l0.floor_cell_u_d_d_s"
; 6, 10, "t.l0.floor_cell_u_s_d_s"
; 6, 12, "t.l0.floor_cell_u_d_s_s"
; 6, 14, "t.l0.floor_cell_u_s_s_s"
;
; 7, 0,  "t.l0.floor_cell_d_d_d_d" ;vacant cell
; 7, 2,  "t.l0.floor_cell_d_s_d_d"
; 7, 4,  "t.l0.floor_cell_d_d_s_d"
; 7, 6,  "t.l0.floor_cell_d_s_s_d"
; 7, 8,  "t.l0.floor_cell_d_d_d_s"
; 7, 10, "t.l0.floor_cell_d_s_d_s"
; 7, 12, "t.l0.floor_cell_d_d_s_s"
; 7, 14, "t.l0.floor_cell_d_s_s_s"
;
; 8, 0,  "t.l0.floor_cell_l_d_d_d" ;vacant cell
; 8, 2,  "t.l0.floor_cell_l_s_d_d"
; 8, 4,  "t.l0.floor_cell_l_d_s_d"
; 8, 6,  "t.l0.floor_cell_l_s_s_d"
; 8, 8,  "t.l0.floor_cell_l_d_d_s"
; 8, 10, "t.l0.floor_cell_l_s_d_s"
; 8, 12, "t.l0.floor_cell_l_d_s_s"
; 8, 14, "t.l0.floor_cell_l_s_s_s"
;
; 8, 1,  "t.l0.floor_cell_r_d_d_d"
; 8, 3,  "t.l0.floor_cell_r_s_d_d"
; 8, 5,  "t.l0.floor_cell_r_d_s_d"
; 8, 7,  "t.l0.floor_cell_r_s_s_d"
; 8, 9,  "t.l0.floor_cell_r_d_d_s"
; 8, 11, "t.l0.floor_cell_r_s_d_s"
; 8, 13, "t.l0.floor_cell_r_d_s_s"
; 8, 15, "t.l0.floor_cell_r_s_s_s"

; lake tiles (shallow-land):
 9, 0,  "t.l0.lake_cell_u_s_s_s" ;vacant cell
 9, 2,  "t.l0.lake_cell_u_l_s_s"
 9, 4,  "t.l0.lake_cell_u_s_l_s"
 9, 6,  "t.l0.lake_cell_u_l_l_s"
 9, 8,  "t.l0.lake_cell_u_s_s_l"
 9, 10, "t.l0.lake_cell_u_l_s_l"
 9, 12, "t.l0.lake_cell_u_s_l_l"
 9, 14, "t.l0.lake_cell_u_l_l_l"
 
 10, 0,  "t.l0.lake_cell_d_s_s_s" ;vacant cell
 10, 2,  "t.l0.lake_cell_d_l_s_s"
 10, 4,  "t.l0.lake_cell_d_s_l_s"
 10, 6,  "t.l0.lake_cell_d_l_l_s"
 10, 8,  "t.l0.lake_cell_d_s_s_l"
 10, 10, "t.l0.lake_cell_d_l_s_l"
 10, 12, "t.l0.lake_cell_d_s_l_l"
 10, 14, "t.l0.lake_cell_d_l_l_l"

 11, 0,  "t.l0.lake_cell_l_s_s_s" ;vacant cell
 11, 2,  "t.l0.lake_cell_l_l_s_s"
 11, 4,  "t.l0.lake_cell_l_s_l_s"
 11, 6,  "t.l0.lake_cell_l_l_l_s"
 11, 8,  "t.l0.lake_cell_l_s_s_l"
 11, 10, "t.l0.lake_cell_l_l_s_l"
 11, 12, "t.l0.lake_cell_l_s_l_l"
 11, 14, "t.l0.lake_cell_l_l_l_l"

 11, 1,  "t.l0.lake_cell_r_s_s_s"
 11, 3,  "t.l0.lake_cell_r_l_s_s"
 11, 5,  "t.l0.lake_cell_r_s_l_s"
 11, 7,  "t.l0.lake_cell_r_l_l_s"
 11, 9,  "t.l0.lake_cell_r_s_s_l"
 11, 11, "t.l0.lake_cell_r_l_s_l"
 11, 13, "t.l0.lake_cell_r_s_l_l"
 11, 15, "t.l0.lake_cell_r_l_l_l"
}
