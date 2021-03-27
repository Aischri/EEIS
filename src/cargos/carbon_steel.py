from cargo import Cargo

cargo = Cargo(
    id="carbon_steel",
    type_name="string(STR_CARGO_NAME_CARBON_STEEL)",
    unit_name="string(STR_CARGO_NAME_CARBON_STEEL)",
    type_abbreviation="string(STR_CID_CARBON_STEEL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STCB",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CARBON_STEEL)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=127,
    icon_indices=(12, 4),
)
