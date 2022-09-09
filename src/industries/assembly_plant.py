from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="assembly_plant",
    accept_cargos_with_input_ratios=[
        ("VPTS", 2),
        ("VBOD", 2),
        ("VENG", 2),
        ("TYRE", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("VEHI", 6), ("ENSP", 1), ("FMSP", 1)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="141",
    name="string(STR_IND_ASSEMBLY_PLANT)",
    nearby_station_name="string(STR_STATION_AUTOMOTIVE)",
    fund_cost_multiplier="145",
)

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "1"  # low chance of build during gameplay

industry.add_tile(
    id="assembly_plant_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -49)],
)
# spriteset_2 was deprecated
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 80, -31, -49)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 80, -31, -49)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 80, -31, -49)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 80, -31, -49)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 80, -31, -49)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 80, -31, -49)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 80, -31, -49)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 80, -31, -49)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 80, -31, -49)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(640, 100, 64, 80, -31, -49)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="assembly_plant_spritelayout_rear_assembly_hall_windows",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    object_group=1,
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_central_assembly_hall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    object_group=1,
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_front_assembly_hall_windows",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    object_group=1,
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_front_assembly_hall_doors",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    object_group=1,
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_goods_in_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_offices",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    object_group=2,
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_tyres",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_vehicles_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_vehicles_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="assembly_plant_spritelayout_vehicles_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_12],
    fences=["nw", "ne", "se", "sw"],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="assembly_plant_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (0, 0, "assembly_plant_tile_1", "assembly_plant_spritelayout_rear_assembly_hall_windows"),
        (0, 1, "assembly_plant_tile_1", "assembly_plant_spritelayout_central_assembly_hall"),
        (0, 2, "assembly_plant_tile_1", "assembly_plant_spritelayout_front_assembly_hall_doors"),
        (1, 0, "assembly_plant_tile_1", "assembly_plant_spritelayout_offices"),
        (1, 1, "assembly_plant_tile_1", "assembly_plant_spritelayout_tyres"),
        (1, 2, "assembly_plant_tile_1", "assembly_plant_spritelayout_offices"),
    ],
)
industry.add_industry_layout(
    id="assembly_plant_industry_layout_1",
    layout=[
        (
            0,
            0,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_rear_assembly_hall_windows",
        ),
        (
            0,
            1,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_central_assembly_hall",
        ),
        (
            0,
            2,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_central_assembly_hall",
        ),
        (
            0,
            3,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_front_assembly_hall_doors",
        ),
        (
            1,
            0,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_rear_assembly_hall_windows",
        ),
        (
            1,
            1,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_central_assembly_hall",
        ),
        (
            1,
            2,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_central_assembly_hall",
        ),
        (
            1,
            3,
            "assembly_plant_tile_1",
            "assembly_plant_spritelayout_front_assembly_hall_windows",
        ),
        (2, 0, "assembly_plant_tile_1", "assembly_plant_spritelayout_goods_in_1"),
        (2, 1, "assembly_plant_tile_1", "assembly_plant_spritelayout_offices"),
        (2, 2, "assembly_plant_tile_1", "assembly_plant_spritelayout_offices"),
        (2, 3, "assembly_plant_tile_1", "assembly_plant_spritelayout_tyres"),
    ],
)
