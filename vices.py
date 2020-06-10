class Vice:
    cost = 0
    v_id = 0
    cap = -1
    alias = []
    def __init__(self, vice_id, cost, cap, *args):
        self.cost = cost
        self.v_id = vice_id
        self.alias = args
        self.cap = cap

vices_list = [
    Vice(0, 120, 30, "lager", "lag"),
    Vice(1, 50, -1, "cider"),
    Vice(2, 135, 10, "ale"),
    Vice(3, 80, -1, "moonshine", "moon"),
    Vice(4, 25, 50, "red_wine", "red", "rwine"),
    Vice(5, 50, 20, "whiskey"),
    Vice(6, 125, 5, "smokes", "smoke"),
    Vice(7, 30, 10, "martini"),
    Vice(8, 60, 30, "jagerbomb", "jager"),
    Vice(9, 65, 20, "tequila"),
    Vice(10, 500, 5, "cigar", "cigs", "cig"),
    Vice(11, 100, 3, "joint"),
    Vice(12, 50, 10, "stout"),
    Vice(13, 40, 30, "margarita", "marg"),
    Vice(14, 125, 3, "vodka", "vod"),
    Vice(15, 1000, -1, "gin_tonic", "gin", "tonic"),
    Vice(16, 40, 100, "bloody_mary", "mary", "bloody"),
    Vice(17, 40, 10, "screwdriver", "screw"),
    Vice(18, 40, 6, "sake"),
    Vice(19, 150, 5, "rubbing_alcohol", "rubbing"),
    Vice(20, 60, 50, "mead"),
    Vice(21, 60, 10, "white_wine", "white"),
    Vice(22, 200, 5, "porter", "port"),
    Vice(23, 30, 10, "hot_wings", "wings", "hot"),
    Vice(24, 75, 7, "energy_drink", "energy", "wugs"),
    Vice(25, 40, 10, "painkillers", "pain", "pk"),
    Vice(26, 250, -1, "dyson_iced_tea", "tea", "iced_tea", "dyson"),
    Vice(27, 60, 10, "hard_lemonade", "lemonade"),
    Vice(28, 40, 10, "beer"),
    Vice(29, 150, 10, "spliff"),
    Vice(30, 60, 10, "stimulants", "stims", "stim"),
    Vice(31, 85, 5, "absinthe", "abs"),
    Vice(32, 1000, -1, "rum"),
    Vice(33, 1000, -1, "champagne", "champ"),
    Vice(34, 45, 20, "vape_pen", "vape", "vapes"),
    Vice(35, 30, 50, "sherry"),
    Vice(36, 100, 5, "espresso", "esp"),
    Vice(37, 400, -1, "antacids", "ant"),
    Vice(38, 500, 5, "varian_cigar", "var", "varian"),
    Vice(39, 40, 5, "water", "h2o", "agua")
]

vice_description = [
    "Your max health has increase by XHP(3HP)	",
    "You have a X%(1%) chance to get Regeneration when you kill an enemy.",
    "Your overall damage has increased by X(2)	",
    "Your reload speed has increased by X%(2%). Stacks with Hard Lemonade.",
    "Your max health is increase by XHP(1HP) with every kill. Maximum 100hp per stack. Resets on death	",
    "You restore X%(2%) of your ammo capacity when you kill an enemy. Does not include throwable weapons.",
    "Your health is restored by 200% when you do the /smoke emote. Consumed on activation. Can be overhealed.	",
    "Your weapon change speed has increased X%(15%)",
    "Your projectiles have a X%(0.5%) chance to release an EMP charge. Does not do self-damage.	",
    "You heal by XHP(3HP) when you kill an enemy. Can be overhealed.",
    "You get 15 more money when an enemy dies.	",
    "You can double jump an extra X(1) time",
    "Your maximum ammo capacity for weapons is increased by X%(4%). Does not include throwable weapons.	",
    "Your attack speed has increased by X%(3%).",
    "You get a Triple Damage powerup when you do the /drink emote. Consumed on activation.	",
    "You heal by XHP(25HP) when opening a chest. Can be overhealed.",
    "You heal by XHP(1HP) every 5 seconds.	",
    "You have a X%(5%) chance to do 200 damage with a punch.",
    "Your damage with melee weapons has increased by X(6)	",
    "If your health falls under 25% you are healed to 100% and you get invisibility. Consumed on activation. Cures poison.",
    "Melee attacks heal you for 1.5% of the damage given. Can be overhealed	",
    "Every 6 seconds you are overhealed, you gain X(1) overall damage. Maximum 10 damage per stack. Resets when no longer overhealed.",
    "Your maximum throwable weapon capacity has increased by X(1)	",
    "Enemies you kill have a X%(1%) chance to spawn fire. Does not do self-damage.",
    "Your movement speed has increased by X%(2%)	",
    "You have X%(4%) resistance against melee damage.",
    "You get 10 extra :5bux: for losing a match",
    "All dual-wieldable weapons reload X%(5%) faster. Stacks with Moonshine. Dual-wielding not required.",
    "You have a X%(2%) chance to get 2 random powerups when the control point unlocks. Does not include BFG	",
    "All powerups last X(1) second(s) longer.",
    "You have a X%(1%) chance to completely dodge an attack.	",
    "You roll X%(7%) faster.",
    "For every 5000$ you have, you gain X%(0.1%) headshot resistance.	",
    "You heal by XHP (40HP) when a wave is completed or when you complete a mission. Can be overhealed.",
    "Every 6 seconds, you have a X%(2%) chance to emit a healing cloud. Can be overhealed. Does not heal enemies.	",
    "Your range for all throwable weapons has increased by X%(2%) and you pick up ammo/medkit boxes and revive players faster.",
    "When below 50% health, you gain X(10) overall damage.	",
    "You get 25 more :5bux: on assist",
    "You get 20 more :5bux: on winning a round",
    "Your explosive resistance has increased by X%(8%)"]

def get_vice(vice_name):
    for vice in vices_list:
        if vice_name in vice.alias:
            return vice
    return None