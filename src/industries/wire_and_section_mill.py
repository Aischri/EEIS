from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="wire_and_section_mill",
    accept_cargos_with_input_ratios=[("STCB", 4), ("ACID", 2), ("SOAP", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("STSE", 4),
        ("STWR", 3),
        ("ENSP", 1),
    ],  # balance is deliberate, steel sections need to feed wharf, vehicle chain is already well supplied
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="43",
    name="string(STR_IND_WIRE_AND_SECTION_MILL)",
    nearby_station_name="string(STR_STATION_ROD_MILL)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
)


industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "0"  # do not build during gameplay

industry.add_tile(
    id="wire_and_section_mill_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_ground = industry.add_spriteset(
    type="hard_standing_dirt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -33)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 31, -31, 0)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 31, -31, 0)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(500, 60, 64, 51, -31, -21)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(570, 60, 64, 51, -31, -21)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_shed_sw_ne_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=[],
    object_group_num=1,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_shed_sw_ne_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[],
    object_group_num=1,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_shed_se_nw_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
    object_group_num=1,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_shed_se_nw_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=[],
    object_group_num=1,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_small_shed_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "sw", "se"],
    object_group_num=2,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_small_shed_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
    object_group_num=2,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
    object_group_num=2,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_wire_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "sw", "se"],
    object_group_num=2,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_wire_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "sw", "se"],
    object_group_num=3,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_gantry_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
    object_group_num=3,
)
industry.add_spritelayout(
    id="wire_and_section_mill_spritelayout_gantry_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)

# this industry needs outpost layout as there are lots of cargos
# note there are two outposts, as this industry has sprites oriented sw_ne or se_nw, will select outpost to match main layout orientation
industry.add_industry_outpost_layout(
    id="wire_and_section_mill_industry_outpost_layout_se_nw",
    layout=[
        (0, 0, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_shed_se_nw_2"),
        (0, 1, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_shed_se_nw_2"),
        (0, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_tanks"),
        (1, 0, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_shed_se_nw_2"),
        (1, 1, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_2"),
        (1, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_small_shed_2"), # shed 2 used as it has smoke
    ],
)
industry.add_industry_outpost_layout(
    id="wire_and_section_mill_industry_outpost_layout_sw_ne",
    layout=[
        (0, 0, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_shed_sw_ne_1"),
        (0, 1, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_tanks"),
        (1, 0, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_shed_sw_ne_2"),
        (1, 1, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_small_shed_2"), # shed 2 used as it has smoke
        (2, 0, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_small_shed_1"),
        (2, 1, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_1"),
    ],
)
# core layouts are roughly 6x4 or 5x5
# long products mill uses non-standard layouts where some sprites only used for some orientiations (sw_ne or se_nw)
# this is to achieve the appearance of 'long'
industry.add_industry_layout(
    id="wire_and_section_mill_industry_layout_1",
    excluded_outpost_layouts=["wire_and_section_mill_industry_outpost_layout_se_nw"],
    layout=[
        (
            0,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            2,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            1,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            1,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            1,
            2,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            2,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (2, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_wire_1"),
        (
            3,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (3, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_wire_1"),
        (
            4,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            4,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_small_shed_2",
        ),
        (4, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_1"),
        (
            5,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_tanks",
        ),
        (
            5,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_small_shed_1",
        ),
        (5, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_1"),
    ],
)
industry.add_industry_layout(
    id="wire_and_section_mill_industry_layout_2",
    excluded_outpost_layouts=["wire_and_section_mill_industry_outpost_layout_sw_ne"],
    layout=[
        (
            0,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            2,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            3,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            4,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            5,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_tanks",
        ),
        (
            1,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            2,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            3,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            4,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_small_shed_2",
        ),
        (
            1,
            5,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_small_shed_1",
        ),
        (
            2,
            0,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_2",
        ),
        (
            2,
            1,
            "wire_and_section_mill_tile_1",
            "wire_and_section_mill_spritelayout_shed_se_nw_2",
        ),
        (2, 2, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_wire_2"),
        (2, 3, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_wire_2"),
        (2, 4, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_2"),
        (2, 5, "wire_and_section_mill_tile_1", "wire_and_section_mill_spritelayout_gantry_2"),
    ],
)
