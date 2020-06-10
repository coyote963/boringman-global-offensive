# import the enum type for rcon events
from rcontypes import rcon_event, rcon_receive
# import json parsing to translate server messages into JSON type
import json
from helpers import send_request, send_packet
from datetime import datetime
from player_data import Player
from weapon_alias import get_weapon
from weapons import Weapon_Enum
import threading
from helpers import get_socket
import time
from vices import get_vice, vice_description
import re

def find_player(player_name):
    for player in player_list:
        if player_name == player.name:
            return player
    return None


def find_by_id(p_id):
    for player in player_list:
        if player.p_id == p_id:
            return player
    return None
#optional: add in automatic table lookup for translating PlayerID's to Player Profile + Store
# from update_cache import get_handle_cache
# player dict for this scope only, useful for packets that only have playerId
# player_dict = {}
# handle_cache = get_handle_cache(player_dict)
player_list = []

# Handling a price check chat event
def handle_check_price(event_id, message_string, sock):
    if event_id == rcon_event.chat_message.value:
        js = json.loads(message_string)
        if js['Message'].startswith("price"):
            cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "provide a vice or weapon name, use underscores ( _ ) for spaces", "8421376")
            vicename = js['Message'].split(" ")[1]
            vice = get_vice(vicename)
            if vice is not None:
                cmd = 'pm "{}" "Price is {} :gold: Cap is {}. Description: {}" "{}"'.format(js['Name'], str(vice.cost), str(vice.cap), vice_description[vice.v_id], "8421376")
            else:
                weapname = js['Message'].split(" ")[1]
                weap = get_weapon(weapname)
                if weap is not None:
                    cmd = 'pm "{}" "Price is {} :gold: Weapon bonus is {}" "{}"'.format(js['Name'], str(weap.cost), str(weap.bonus), "8421376")
            send_packet(sock, cmd, rcon_receive.command.value)

def handle_buy_vice(event_id, message_string, sock):
    if event_id == rcon_event.chat_message.value:
        js = json.loads(message_string)
        if js['Message'].startswith("vice"):
            cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "provide a vice name, underscores ( _ ) for spaces", "8421376")
            if len(js['Message'].split(" ")) > 1:
                vicename = js['Message'].split(" ")[1]
                vice = get_vice(vicename)
                if vice is not None:
                    p = find_player(js["Name"])
                    if p is not None:
                        if p.buy_vice(vicename):
                            cmd = 'setvice "{}" "{}" "{}"'.format(p.name, vice.v_id, p.vices[vice.v_id])
                        else:
                            cmd = 'pm "{}" "Insufficient funds, you have {} :gold: and {} costs {} :gold:, It could also be that you have reached the maximum of this vice [{}]" "{}"'.format(js['Name'], p.balance, vice.alias[0] ,vice.cost, vice.cap, "8421376")
                    else:
                        cmd = 'pm "{}" "Please try again after this round" ""8421376""'.format(js["Name"])
            send_packet(sock, cmd, rcon_receive.command.value)

def handle_buy_quantity(event_id, message_string, sock):
    if event_id == rcon_event.chat_message.value:
        js = json.loads(message_string)
        if js['Message'].startswith("mvice"):
            cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "provide a vice name, underscores ( _ ) for spaces, and a valid quantity ex [vices whiskey 2]", "8421376")
            if len(js['Message'].split(" ")) > 2:
                vicename = js['Message'].split(" ")[1]
                vicequantity = js["Message"].split(" ")[2]
                vice = get_vice(vicename)
                if vice is not None and vicequantity.isnumeric():
                    p = find_player(js["Name"])
                    if p is not None:
                        if p.buy_vice_quantity(vicename, int(vicequantity)):
                            cmd = 'setvice "{}" "{}" "{}"'.format(p.name, vice.v_id, p.vices[vice.v_id])
                        else:
                            cmd = 'pm "{}" "Insufficient funds, you have {} :gold: and it costs {} :gold: It could also be that you have reached the maximum allowed number of this vice! [{}]" "{}"'.format(js['Name'], p.balance, vice.cost * int(vicequantity), vice.cap, "8421376")
                    else:
                        cmd = 'pm "{}" "Please try again after this round" "8421376"'.format(js["Name"])
            send_packet(sock, cmd, rcon_receive.command.value)

def handle_gift(event_id, message_string, sock):
    if event_id == rcon_event.chat_message.value:
        # parse the json
        js = json.loads(message_string)
        # if the server message is from a player
        if 'PlayerID' in js and js['PlayerID'] != '-1':
            if js['Message'].startswith("gift"):
                cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "provide a vice name, underscores ( _ ) for spaces, and a valid quantity ex [gift \"coyote and bird\" whiskey 2]", "8421376")
                m = re.search(r"gift \"(.+?)\" (\w+) (\w+)", js["Message"])
                if m is not None:
                    try:
                        gifter = find_player(js["Name"])
                        giftee = find_player(m.group(1))
                        v = get_vice(m.group(2))
                        q = int(m.group(3))

                        enough_money = gifter.gift_vice(v.alias[0], q)
                        if enough_money:
                            if giftee.vices[v.v_id] + q <= v.cap:
                                giftee.receive_gift_vice(v.alias[0], q)
                                cmd = 'setvice "{}" "{}" "{}"'.format(giftee.name, v.v_id, giftee.vices[v.v_id])
                            else:
                                cmd = 'pm "{}" "Could not gift vice: The recipient has too many of this vice" "{}"'.format(js['Name'], "8421376")
                    except Exception as e:
                        print(str(e))
                        cmd = 'pm "{}" "Could not gift vice" "{}"'.format(js['Name'], "8421376")
                send_packet(sock, cmd, rcon_receive.command.value)


def handle_join(event_id, message_string, sock):
    if event_id == rcon_event.player_connect.value:
        js = json.loads(message_string)
        cmd = 'pm "{}" "Commands: buy, balance, vice, price. You cannot use commands until you spawn so be patient" "{}"'.format(js['PlayerName'], "8421376")
        send_packet(sock, cmd, rcon_receive.command.value)



def handle_chat(event_id, message_string, sock):
    # if passed in event_id is a chat_message
    if event_id == rcon_event.chat_message.value:
        # parse the json
        js = json.loads(message_string)
        # if the server message is from a player
        if 'PlayerID' in js and js['PlayerID'] != '-1':

            if js['Message'].startswith("buy"):
                if len(js['Message'].split(" ")) > 1:
                    weapon = get_weapon(js['Message'].split(" ")[1])
                    if weapon is not None:
                        p = find_player(js['Name'])
                        if p is not None:
                            if p.buy_weapon(js['Message'].split(" ")[1]):
                                cmd = 'forceweap "{}" "{}" "{}" "{}" "false"'.format(js['Name'], p.weapon1, p.weapon2, p.nade)
                                print(cmd)
                                send_packet(sock, cmd, rcon_receive.command.value)
                            else:
                                cmd = 'pm "{}" "Insufficient funds, you have {} :gold: and it costs {} :gold:" "{}"'.format(js['Name'], p.balance, weapon.cost, "8421376")
                                send_packet(sock, cmd, rcon_receive.command.value)
                    else:
                        cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "Not a valid weapon name, make sure to use underscores for spaces", "8421376")
                        send_packet(sock, cmd, rcon_receive.command.value)
                else:
                    cmd = 'pm "{}" "{}" "{}"'.format(js['Name'], "provide a weapon name, underscores ( _ ) for spaces", "8421376")
                    send_packet(sock, cmd, rcon_receive.command.value)

def handle_spawn(event_id, message_string, sock):
    if event_id == rcon_event.player_spawn.value:
        js = json.loads(message_string)
        player = find_player(js["Name"]) 
        if player is None:
            player_list.append(Player(js["Name"],js['PlayerID'], js["Team"]))


def handle_match(event_id, message_string, sock):
    if event_id == rcon_event.tdm_switch_sides.value or event_id == rcon_event.match_end.value:
        player_list.clear()
        cmd = 'resetvicesall'
        send_packet(sock, cmd, rcon_receive.command.value)

def handle_player_death(event_id, message_string, sock):
    if event_id == rcon_event.player_death.value:

        js = json.loads(message_string)
        killer = find_by_id(js['KillerID'])
        if int(js["KillerWeapon"]) >= 0:
            weaponused = Weapon_Enum(int(js["KillerWeapon"]))
            weapon = get_weapon(weaponused.name)
            if weapon is not None:
                if killer is not None:
                    killer.balance += 50 + weapon.bonus + 15 * killer.vices[10]
                assister = find_by_id(js["AssisterID"])
                if assister is not None:
                    assister.balance += 25 + 25 * assister.vices[37]

def handle_round(event_id, message_string, sock):
    if event_id == rcon_event.tdm_round_end.value:
        js = json.loads(message_string)
        for player in player_list:
            if player.team == js['Winner']:
                player.balance += 100 + 40 * player.vices[38]
            else:
                player.balance += 50 + 10 * player.vices[26]

def handle_round_start(event_id, message_string, sock):
    if event_id == rcon_event.tdm_round_start.value:
        x = threading.Thread(target= set_weaps, args=(sock,))
        x.start()



def set_weaps(sock):
    for p in player_list:
        if not p.default:
            cmd = 'forceweap "{}" "{}" "{}" "{}" "false"'.format(p.name, p.weapon1, p.weapon2, p.nade)
            send_packet(sock, cmd, rcon_receive.command.value)
            time.sleep(0.1)


def handle_balance(event_id, message_string, sock):
    if event_id == rcon_event.chat_message.value:
        js = json.loads(message_string)

        if js["Message"].startswith("balance"):
            p = find_player(js["Name"])
            if p is not None:
                cmd = 'pm "{}" "You have {} :gold:" "{}"'.format(js['Name'], p.balance, "8421376")
                send_packet(sock, cmd, rcon_receive.command.value)
            else:
                cmd = 'pm "{}" "No Information" "{}"'.format(js['Name'], "8421376")
                send_packet(sock, cmd, rcon_receive.command.value)

example_functions  = [
    handle_spawn,
    handle_chat, 
    handle_player_death, 
    handle_round,
    handle_round_start, 
    handle_balance,
    handle_match,
    handle_buy_quantity,
    handle_buy_vice,
    handle_check_price,
    handle_gift,
    handle_join
] # include handle_cache if you are using it