class Weapon:
    """Weapon information"""
    alias = []
    cost = 0
    weap_id = 0
    bonus = 0
    def __init__(self, weap_id, cost, bonus,  *args):
        self.alias = args
        self.cost = cost
        self.weap_id = weap_id
        self.bonus = bonus


weapon_list = [
    Weapon(0, 0, 35, "fists", "fist", "punch", "melee"),
    Weapon(2, 50, 20, "pistol"),
    Weapon(3,  150, 5, "silenced_pistol", "sp", "silenced"),
    Weapon(4,  100, 25, "underwater_pistol", "uwp"),
    Weapon(5,  200, 0, "revolver", "rev"),
    Weapon(7,  150, 20, "compact_pistol" "compact"),
    Weapon(8,  400, -10, "handcannon", "hc"),
    Weapon(9,  300, 5, "uzi"),
    Weapon(10, 300, 10, "compact_uzi", "cuzi"),
    Weapon(12, 350, 0, "light_smg", "lsmg"),
    Weapon(13, 150, 5, "smg"),
    Weapon(14, 300, 0, "power_smg", "psmg"),
    Weapon(16, 300, 0, "sawn_off", "sawn"),
    Weapon(17, 250, 0, "pump"),
    Weapon(18, 400, -10, "db" ),
    Weapon(19, 300, 0, "trench"),
    Weapon(21, 200, 0, "light_ar","lar"),
    Weapon(22, 250, 0, "assault_rifle", "ar"),
    Weapon(23, 400, -5, "keymaster" ,"key"),
    Weapon(24, 300, 0, "heal_rifle", "heal"),
    Weapon(25, 100, 10, "underwater_rifle", "uwr"),
    Weapon(26, 200, 20, "musket", "musk"),
    Weapon(27, 200, 5, "ak", "power_rifle"),
    Weapon(29, 200, 5, "long_rifle", "lrif"),
    Weapon(30, 200, -5, "lev", "lever", "lever_action"),
    Weapon(31, 200, 0, "pli", "m16", "m1"),
    Weapon(32, 400, 0, "sniper", "sni"),
    Weapon(33, 300, 0, "bolt"),
    Weapon(36, 175, 5, "machine_gun", "mg"),
    Weapon(38, 350, -20, "gl"),
    Weapon(39, 300, -5, "heavy_gl", "hgl" ),
    Weapon(41, 350, -5, "rocket", "rl" ),
    Weapon(45, 300, -5, "acid", "acid_gun" ),
    Weapon(47, 200, 5, "mule", "muleslapper"),
    Weapon(49, 250, 0, "bow" ),
    Weapon(50, 200, 0, "xbow", "crossbow", "cross_bow"),
    Weapon(51, 150, 0, "grapple", "grapplehook", "grapple_hook", "hook"),
    Weapon(52, 100, 10, "knife" ),
    Weapon(53, 100, 10, "sword" ),
    Weapon(54, 25, 30, "wrench" ),
    Weapon(56, 125, 10, "magic" ),
    Weapon(57, 200, 5, "rail", "railgun" ),
    Weapon(61, 250, 0, "drone" ),
    Weapon(62, 150, 5, "fragnade", "grenade" ),
    Weapon(64, 100, 20, "emp" ),
    Weapon(65, 150, 5, "molotov" ),
    Weapon(67, 200, 0, "hnade", "healnade", 'heal_nade' ),
    Weapon(68, 100, 10, "gasnade", "gas_nade", "poison_nade", "pnade" ),
    Weapon(69, 100, 0, "flashbang", "flash"),
    Weapon(70, 200, 0, "skate", "sk8" ),
    Weapon(72, 25, 50, "vest", "suicide_vest"),
    Weapon(74, 10, 50, "pineapple" ),
    Weapon(75, 100, 0, "scuba" ),
    Weapon(78, 150, 0, "jp", "jet", "jetpack"),
    Weapon(79, 125, 20, "rang", "boomerang")
]


def get_weapon(weapon_name):
    for weapon in weapon_list:
        if weapon_name in weapon.alias:
            return weapon
    return None