-- Freeciv - Copyright (C) 2007 - The Freeciv Project
--   This program is free software; you can redistribute it and/or modify
--   it under the terms of the GNU General Public License as published by
--   the Free Software Foundation; either version 2, or (at your option)
--   any later version.
--
--   This program is distributed in the hope that it will be useful,
--   but WITHOUT ANY WARRANTY; without even the implied warranty of
--   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--   GNU General Public License for more details.

-- This file is for lua-functionality that is specific to a given
-- ruleset. When freeciv loads a ruleset, it also loads script
-- file called 'default.lua'. The one loaded if your ruleset
-- does not provide an override is default/default.lua.


-- Place Ruins at the location of the destroyed city.
function city_destroyed_callback(city, loser, destroyer)
  city.tile:create_extra("Ruins")
  -- continue processing
  return false
end

signal.connect("city_destroyed", "city_destroyed_callback")

-- Check if there is certain terrain in ANY CAdjacent tile.
function adjacent_to(tile, terrain_name)
  for adj_tile in tile:circle_iterate(1) do
    if adj_tile.id ~= tile.id then
      local adj_terr = adj_tile.terrain
      local adj_name = adj_terr:rule_name()
      if adj_name == terrain_name then
        return true
      end
    end
  end
  return false
end

-- Check if there is certain terrain in ALL CAdjacent tiles.
function surrounded_by(tile, terrain_name)
  for adj_tile in tile:circle_iterate(1) do
    if adj_tile.id ~= tile.id then
      local adj_terr = adj_tile.terrain
      local adj_name = adj_terr:rule_name()
      if adj_name ~= terrain_name then
        return false
      end
    end
  end
  return true
end

-- Add random labels to the map.
function place_map_labels()
  local rivers = 0
  local deeps = 0
  local oceans = 0
  local lakes = 0
  local swamps = 0
  local glaciers = 0
  local tundras = 0
  local deserts = 0
  local plains = 0
  local grasslands = 0
  local jungles = 0
  local forests = 0
  local hills = 0
  local mountains = 0

  local selected_river = 0
  local selected_deep = 0
  local selected_ocean = 0
  local selected_lake = 0
  local selected_swamp = 0
  local selected_glacier = 0
  local selected_tundra = 0
  local selected_desert = 0
  local selected_plain = 0
  local selected_grassland = 0
  local selected_jungle = 0
  local selected_forest = 0
  local selected_hill = 0
  local selected_mountain = 0

  -- Count the tiles that has a terrain type that may get a label.
  for place in whole_map_iterate() do
    local terr = place.terrain
    local tname = terr:rule_name()

    if place:has_extra("River") then
      rivers = rivers + 1
    elseif tname == "Deep Ocean" then
      deeps = deeps + 1
    elseif tname == "Ocean" then
      oceans = oceans + 1
    elseif tname == "Lake" then
      lakes = lakes + 1
    elseif tname == "Swamp" then
      swamps = swamps + 1
    elseif tname == "Glacier" then
      glaciers = glaciers + 1
    elseif tname == "Tundra" then
      tundras = tundras + 1
    elseif tname == "Desert" then
      deserts = deserts + 1
    elseif tname == "Plains" then
      plains = plains + 1
    elseif tname == "Grassland" then
      grasslands = grasslands + 1
    elseif tname == "Jungle" then
      jungles = jungles + 1
    elseif tname == "Forest" then
      forests = forests + 1
    elseif tname == "Hills" then
      hills = hills + 1
    elseif tname == "Mountains" then
      mountains = mountains + 1
    end
  end

  -- Decide if a label should be included and, in case it should, where.
    if random(1, 100) <= rivers then
      selected_river = random(1, rivers)
    end
    if random(1, 100) <= deeps then
      selected_deep = random(1, deeps)
    end
    if random(1, 100) <= oceans then
      selected_ocean = random(1, oceans)
    end
    if random(1, 100) <= lakes then
      selected_lake = random(1, lakes)
    end
    if random(1, 100) <= swamps then
      selected_swamp = random(1, swamps)
    end
    if random(1, 100) <= glaciers then
      selected_glacier = random(1, glaciers)
    end
    if random(1, 100) <= tundras then
      selected_tundra = random(1, tundras)
    end
    if random(1, 100) <= deserts then
      selected_desert = random(1, deserts)
    end
    if random(1, 100) <= plains then
      selected_plain = random(1, plains)
    end
    if random(1, 100) <= grasslands then
      selected_grassland = random(1, grasslands)
    end
    if random(1, 100) <= jungles then
      selected_jungle = random(1, jungles)
    end
    if random(1, 100) <= forests then
      selected_forest = random(1, forests)
    end
    if random(1, 100) <= hills then
      selected_hill = random(1, hills)
    end
    if random(1, 100) <= mountains then
      selected_mountain = random(1, mountains)
    end

  -- Place the included labels at the location determined above.
  for place in whole_map_iterate() do
    local terr = place.terrain
    local tname = terr:rule_name()

    if place:has_extra("River") then
      selected_river = selected_river - 1
      if selected_river == 0 then
        place:create_extra("Wonder")
        if tname == "Hills" then
          place:set_label(_("Grand Canyon"))
        elseif tname == "Mountains" then
          place:set_label(_("Deep Gorge"))
        elseif tname == "Tundra" then
          place:set_label(_("Fjords"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Waterfalls"))
        else
          place:set_label(_("Travertine Terraces"))
        end
      end
    elseif tname == "Deep Ocean" then
      selected_deep = selected_deep - 1
      if selected_deep == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Deep Ocean") then
          -- Fully surrounded
          place:set_label(_("Deep Trench"))
        else
          place:set_label(_("Thermal Vent"))
        end
      end
    elseif tname == "Ocean" then
      selected_ocean = selected_ocean - 1
      if selected_ocean == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Ocean") then
          -- Fully surrounded
          place:set_label(_("Atoll Chain"))
        elseif adjacent_to(place, "Glacier") then
          place:set_label(_("Glacier Bay"))
        elseif adjacent_to(place, "Deep Ocean") then
          place:set_label(_("Great Barrier Reef"))
        else
          -- Coast (not adjacent to glacier nor deep ocean)
          place:set_label(_("Great Blue Hole"))
        end
      end
    elseif tname == "Lake" then
      selected_lake = selected_lake - 1
      if selected_lake == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Lake") then
          -- Fully surrounded
          place:set_label(_("Great Lakes"))
        elseif not adjacent_to(place, "Lake") then
          -- Isolated
          place:set_label(_("Dead Sea"))
        else
          place:set_label(_("Rift Lake"))
        end
      end
    elseif tname == "Swamp" then
      selected_swamp = selected_swamp - 1
      if selected_swamp == 0 then
        place:create_extra("Wonder")
        if not adjacent_to(place, "Swamp") then
          -- Isolated
          place:set_label(_("Grand Prismatic Spring"))
        elseif adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("Mangrove Forest"))
        else
          place:set_label(_("Cenotes"))
        end
      end
    elseif tname == "Glacier" then
      selected_glacier = selected_glacier - 1
      if selected_glacier == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Glacier") then
          -- Fully surrounded
          place:set_label(_("Ice Sheet"))
        elseif not adjacent_to(place, "Glacier") then
          -- Isolated
          place:set_label(_("Frozen Lake"))
        elseif adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("Ice Shelf"))
        else
          place:set_label(_("Advancing Glacier"))
        end
      end
    elseif tname == "Tundra" then
      selected_tundra = selected_tundra - 1
      if selected_tundra == 0 then
        place:create_extra("Wonder")
        place:set_label(_("Geothermal Area"))
      end
    elseif tname == "Desert" then
      selected_desert = selected_desert - 1
      if selected_desert == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Desert") then
          -- Fully surrounded
          place:set_label(_("Sand Sea"))
        elseif not adjacent_to(place, "Desert") then
          -- Isolated
          place:set_label(_("Salt Flat"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Singing Dunes"))
        else
          place:set_label(_("White Desert"))
        end
      end
    elseif tname == "Plains" then
      selected_plain = selected_plain - 1
      if selected_plain == 0 then
        place:create_extra("Wonder")
        if adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("Long Beach"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Valley of Geysers"))
        else
          place:set_label(_("Rock Pillars"))
        end
      end
    elseif tname == "Grassland" then
      selected_grassland = selected_grassland - 1
      if selected_grassland == 0 then
        place:create_extra("Wonder")
        if adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("White Cliffs"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Giant Cave"))
        else
          place:set_label(_("Rock Formation"))
        end
      end
    elseif tname == "Jungle" then
      selected_jungle = selected_jungle - 1
      if selected_jungle == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Jungle") then
          -- Fully surrounded
          place:set_label(_("Rainforest"))
        elseif adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("Subterranean River"))
        else
          place:set_label(_("Sinkholes"))
        end
      end
    elseif tname == "Forest" then
      selected_forest = selected_forest - 1
      if selected_forest == 0 then
        place:create_extra("Wonder")
        if adjacent_to(place, "Mountains") then
          place:set_label(_("Stone Forest"))
        elseif surrounded_by(place, "Forest") then
          -- Fully surrounded
          place:set_label(_("Sequoia Forest"))
        else
          place:set_label(_("Millenary Trees"))
        end
      end
    elseif tname == "Hills" then
      selected_hill = selected_hill - 1
      if selected_hill == 0 then
        place:create_extra("Wonder")
        if not adjacent_to(place, "Hills") then
          if adjacent_to(place, "Mountains") then
            -- Isolated (but adjacent to mountains)
            place:set_label(_("Table Mountain"))
          else
            -- Isolated (not adjacent to hills nor mountains)
            place:set_label(_("Inselberg"))
          end
        elseif random(1, 100) <= 50 then
          place:set_label(_("Karst Landscape"))
        else
          place:set_label(_("Mud Volcanoes"))
        end
      end
    elseif tname == "Mountains" then
      selected_mountain = selected_mountain - 1
      if selected_mountain == 0 then
        place:create_extra("Wonder")
        if surrounded_by(place, "Mountains") then
          -- Fully surrounded
          place:set_label(_("Highest Peak"))
        elseif not adjacent_to(place, "Mountains") then
          -- Isolated
          place:set_label(_("Sacred Mount"))
        elseif adjacent_to(place, "Ocean") then
          -- Coast
          place:set_label(_("Cliff Coast"))
        elseif random(1, 100) <= 50 then
          place:set_label(_("Active Volcano"))
        else
          place:set_label(_("High Summit"))
        end
      end
    end
  end
  return false
end

signal.connect("map_generated", "place_map_labels")

-- Add random extra resources to the map.
function place_extra_resources(turn, year)

  if turn == 1 then
    for place in whole_map_iterate() do
      local terr = place.terrain
      local tname = terr:rule_name()

      if random(1, 100) <= 2 then
        if tname == "Desert"
          and not place:has_extra("Oasis")
          and not place:has_extra("Oil")
          and not place:has_extra("Incense") then
          place:create_extra("Niter")
        elseif tname == "Plains"
          and not place:has_extra("Wheat")
          and not place:has_extra("Buffalo")
          and not place:has_extra("Horses") then
          place:create_extra("Niter")
        elseif tname == "Swamp"
          and not place:has_extra("Peat")
          and not place:has_extra("Spice")
          and not place:has_extra("Sugar") then
          place:create_extra("Rubber")
        elseif tname == "Jungle"
          and not place:has_extra("Gems")
          and not place:has_extra("Fruit")
          and not place:has_extra("Ivory") then
          place:create_extra("Rubber")
        elseif tname == "Forest"
          and not place:has_extra("Pheasant")
          and not place:has_extra("Silk")
          and not place:has_extra("Deer") then
          place:create_extra("Rubber")
        elseif tname == "Tundra"
          and not place:has_extra("Game")
          and not place:has_extra("Furs") then
          place:create_extra("Aluminum")
        elseif tname == "Hills"
          and not place:has_extra("Coal")
          and not place:has_extra("Wine")
          and not place:has_extra("Marble") then
          place:create_extra("Aluminum")
        elseif tname == "Glacier"
          and not place:has_extra("Seals")
          and not place:has_extra("Oil") then
          place:create_extra("Uranium")
        elseif tname == "Mountains"
          and not place:has_extra("Gold")
          and not place:has_extra("Iron") then
          place:create_extra("Uranium")
        end
      end
    end
  end
end

signal.connect("turn_begin", "place_extra_resources")

-- Victory for the player with the highest score and culture
-- if they are more than 4 times the second-highest
function score_victory(turn, year)
  local leader = nil
  local score_1st = 0
  local score_2nd = 0
  local culture_1st = 0
  local culture_2nd = 0

  -- Enabled by custom ruleset effect (SETI Program)
  if effects.world_bonus("User_Effect_1") > 0 then
    for player in players_iterate() do
      local score = player:civilization_score()
      local culture = player:culture()

      if score > score_1st then
        score_1st = score
        -- save the score leader, that might not be the culture leader
        leader = player
      elseif score > score_2nd then
        score_2nd = score
      end
      if culture > culture_1st then
        culture_1st = culture
      elseif culture > culture_2nd then
        culture_2nd = culture
      end
    end

    if leader ~= nil then
      log.normal(_("Leading nation: %s, score: %d (%d > %d), culture: %d (%d > %d)"),
        leader.nation,
        leader:civilization_score(),
        score_1st,
        score_2nd,
        leader:culture(),
        culture_1st,
        culture_2nd)
      if leader:civilization_score() > 4 * score_2nd
        and leader:culture() > 4 * culture_2nd then
        -- if score leader has more culture than culture_2nd, it means it is the culture leader too
        leader:victory()
        return true
      end
    end
  end
  return false
end

signal.connect("turn_begin", "score_victory")

-- Action Log: Returns a function that describes a tile target
function tile_desc_func_gen(kind, owner_getter)
  return function (target)
    local owner
    if owner_getter(target) == nil then
      owner = _("unowned")
    else
      owner = owner_getter(target).nation:name_translation()
    end
    return _("%s %s (%d, %d)"):format(owner, kind, target.x, target.y)
  end
end

-- Action Log: Describe the target based on its kind
target_describer = {
  ["City"] = function (target)
    return _("%s city %s (id: %d)"):format(
        target.owner.nation:name_translation(), target.name, target.id)
  end,
  ["Unit"] = function (target)
    return _("%s %s (id: %d)"):format(
      target.owner.nation:name_translation(),
      target.utype:name_translation(), target.id)
  end,
  ["Stack"] = function (target)
    return _("unit stack at (%d, %d)"):format(target.x, target.y)
  end,
  ["Tile"] = tile_desc_func_gen("tile", function (target)
    return target.owner
  end),
  ["Extras"] = tile_desc_func_gen("tile extras", function (target)
    return target:extra_owner(Nil)
  end),
  ["Self"] = function (target) return "it self" end,
}

-- Action Log: Log all performed actions (enable by adding to signal.connect)
function action_started_callback(action, actor, target)
  log.normal(_("%d: %s (rule name: %s) performed by %s %s (id: %d) on %s"),
             game.current_turn(),
             action:name_translation(),
             action:rule_name(),
             actor.owner.nation:name_translation(),
             actor.utype:name_translation(),
             actor.id,
             target_describer[action:target_kind()](target))
end

-- Custom effects of performed actions
function action_finished_callback(action, success, actor, target)
  if action:rule_name() == "Bombard" then
  -- (unit_units) Place a Bombardment marker when a unit bombards from this tile.
    actor.tile:create_extra("Bombardment")
  elseif action:rule_name() == "Heal Unit" then
  -- (unit_unit) Kill the healer unit.
    if success then
      -- FIXME: this kill crashes when healer is being transported
      actor:kill("used",Nil)
    end
  elseif action:rule_name() == "User Action 1" then
  -- (unit_city) Place a marker that will cancel the trade routes.
    target.tile:create_extra("Goods")
  elseif action:rule_name() == "User Action 2" then
  -- (unit_tile) Place a Bombardment marker using a custom action.
  -- (Pillage action does not seem to send any signal)
    target:create_extra("Bombardment")
    if actor.utype:has_flag("AirBomber") then
      -- Remove all extras from the tile at once
      -- Extras are removed before the extras listed as their requirements, just in case
      target:remove_extra("Farmland")
      target:remove_extra("Irrigation")
      target:remove_extra("Oil Well")
      target:remove_extra("Mine")
      target:remove_extra("Lumber")
      target:remove_extra("Castle")
      target:remove_extra("Fortress")
      target:remove_extra("Fort")
      target:remove_extra("Airbase")
      target:remove_extra("Airstrip")
      target:remove_extra("Maglev")
      target:remove_extra("Railroad")
      target:remove_extra("Road")
      target:remove_extra("Canal")
      target:remove_extra("Buoy")
      target:remove_extra("Naval Mine")
      target:remove_extra("Oil Platform")
    end
  end
  return false
end

--signal.connect("action_started_unit_city", "action_started_callback")
--signal.connect("action_started_unit_unit", "action_started_callback")
--signal.connect("action_started_unit_units", "action_started_callback")
--signal.connect("action_started_unit_tile", "action_started_callback")
--signal.connect("action_started_unit_extras", "action_started_callback")
--signal.connect("action_started_unit_self", "action_started_callback")

signal.connect("action_finished_unit_city", "action_finished_callback")
signal.connect("action_finished_unit_unit", "action_finished_callback")
signal.connect("action_finished_unit_units", "action_finished_callback")
signal.connect("action_finished_unit_tile", "action_finished_callback")
--signal.connect("action_finished_unit_extras", "action_finished_callback")
--signal.connect("action_finished_unit_self", "action_finished_callback")

