from weapon_alias import get_weapon
from vices import get_vice
import copy
import array as arr
class Player:
    """Info attached to a bmgo player"""
    nade = 69
    balance = 200
    name = ""
    p_id = "0"
    vices = []
    team = "0"
    weapon1 = "52",
    weapon2 = "2",
    default = True
    update = 1
    def buy_weapon(self, keyword):
        
        weapon = get_weapon(keyword)
        if self.balance >= weapon.cost:
            self.balance -= weapon.cost
            self.default = False
            if weapon.weap_id >= 61:
                self.nade = weapon.weap_id
            else:
                if self.update == 1:
                    self.weapon1 = weapon.weap_id
                    self.update = 2
                else:
                    self.weapon2 = weapon.weap_id
                    self.update = 1
            return True
        return False

    def buy_vice(self, keyword):
        vice = get_vice(keyword)
        if self.balance >= vice.cost:
            if vice.cap != -1:
                if self.vices[vice.v_id] < vice.cap:
                    self.balance -= vice.cost
                    self.vices[vice.v_id] += 1
                    return True
        return False

    def receive_gift_vice(self, keyword, quantity):
        vice = get_vice(keyword)
        
        self.vices[vice.v_id] += quantity

    def gift_vice(self, keyword, quantity):
        vice = get_vice(keyword)
        if self.balance >= vice.cost * quantity:
            self.balance -= vice.cost * quantity
            return True
        return False

    def buy_vice_quantity(self, keyword, quantity):
        vice = get_vice(keyword)
        if self.balance >= vice.cost * quantity:
            if vice.cap == -1 or self.vices[vice.v_id] + quantity <= vice.cap:
                self.balance -= vice.cost * quantity
                self.vices[vice.v_id] += quantity
                return True
        return False


    def __init__(self, name, p_id, team):
        self.name = name
        self.p_id = p_id
        self.team = team
        self.vices = arr.array('i', [0] * 40)
