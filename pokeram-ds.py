#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Requires Pillow, requests, and WeasyPrint (<=52.5)
# To install requirements easily, please use "pip install -r requirements.txt"

import ast
import time
import traceback
import os
import math
import io
from shutil import copyfile
from weasyprint import HTML, CSS
import requests
from PIL import Image, ImageChops
from pr_data import *
import copy
import traceback
import html
import unicodedata
import base64

# LOGGING OPTIONS - edit as needed
PRINT_VERBOSE = True # Verbose logging, shows more info including party stats
PRINT_DEBUG = False # Print extra debugging info to console
EXPORT_PARTY = False # Whether to export the current party to HTML_DIR/party/
SHOW_MISC_DATA = False # Whether to show misc. trainer/badge data in status.html - not fully implemented
SHOW_BOX_DATA = False # Whether to show current box data in status.html - not fully implemented
BYPASS_CHECKSUM = False # Whether to bypass checksum tests when reading memory data (Not recommended - but checksum is broken for some games)
# For the DS games, since memory is a bit wonky, you probably want BYPASS_CHECKSUM set to False. Otherwise it's prone to pull garbage data randomly

# CONFIG OPTIONS - edit as needed
GAME_GENERATION = 1 # Generation number of the current game
GAME_NAME = "brown" # Currently valid options: see pr_data.py
#HTML_DIR = "/var/www/html/tpp/new/" # Directory to save html and png output files
#SPRITE_DIR = HTML_DIR+"sprites/home/" # Directory to pull sprites from
HTML_DIR = "./html/" # local testing
SPRITE_DIR = "./sprites/home/" # local testing

'''
Ignore Checksum and MemoryRead errors, so we can run this unattended
'''
class ChecksumError(Exception):
    pass

class MemoryReadError(Exception):
    pass
        
'''
Pokemon data class
'''
class Pokemon:
    def __init__(self, pid = 0, spec = 0, spec_raw=0, gender = 0, shiny = False, item = 0, ot_id = 0, \
    ability = 0, ivs = {"hp": 0, "atk": 0, "def": 0, "spe": 0, "spa": 0, "spd": 0}, \
    status = 0, lvl = 0, happiness = 0, hp = 0, maxhp = 0, name = "", name_raw = [], \
    ot_name_raw = [], data= [], chk = 0, form = None, is_egg = False, gen=2):
        self.pid = pid
        self.spec = spec
        self.spec_raw = spec_raw
        self.gender = gender
        self.shiny = shiny
        self.item = item
        self.ot_id = ot_id
        self.ot_name_raw = ot_name_raw
        
        self.ability = ability
        self.ivs = ivs # in gen I/II, SpA = SpD and HP = 0.
        self.status = status
        self.lvl = lvl
        self.happiness = happiness
        self.hp = hp
        self.maxhp = maxhp
        self.name = name
        self.name_raw = name_raw
        self.is_egg = is_egg
        self.form = form
        
        self.data = data
        self.chk = chk
    
'''
Save data class
'''
class GameData:
    def __init__(self, trainer_name="", trainer_name_raw = [], time_hours = 0, \
    time_minutes = 0, time_seconds = 0, rival_name = "", party = [], partysize = 0, \
    badges = 0, box = [], boxsize = 0, trainer_gender = 0):
        self.trainer_name = trainer_name
        self.trainer_name_raw = trainer_name_raw
        self.trainer_gender = trainer_gender
        self.time_hours = time_hours
        self.time_minutes = time_minutes
        self.time_seconds = time_seconds
        self.rival_name = rival_name
        self.party = party
        self.partysize = partysize
        self.badges = badges
        self.box = box
        self.boxsize = boxsize

'''
Memory container class (contains game data, but also entire save state/RAM map)
'''
class MemData:
    def __init__(self, memory = [], gamedata = GameData()):
        self.memory = memory
        self.gamedata = gamedata

'''
Trimes border out of an image, with optional padding hborder and vborder
'''
def trimImage(im, hborder=0, vborder=0):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    bbox = (bbox[0]-hborder, bbox[1]+vborder, bbox[2]+hborder, bbox[3]-vborder)
    if bbox:
        return im.crop(bbox)

'''
Determines gender of a Gen I/II pokemon, using the gender ratio and the Atk/Def IVs
'''
def gen2Gender(ratio, atkiv):
    if ratio < 0:
        return -1
    elif ratio*16 >= atkiv:
        return 1
    else:
        return 0

'''
Determines shininess of Gen I/II pokemon, which is based on IVs
'''
def gen2Shiny(ivs):
    atkiv = ivs["atk"]
    defiv = ivs["def"]
    spdiv = ivs["spe"]
    speiv = ivs["spa"]
    
    if (speiv == spdiv == defiv == 10):
        if atkiv in [2,3,6,7,10,11,14,15]:
           return True
    return False
    
'''
Determines shininess of Red++ pokemon, which is based on IVs (but different than Gen 2)
'''
def gen1RPPShiny(ivs):
    atkiv = ivs["atk"]
    defiv = ivs["def"]
    spdiv = ivs["spe"]
    speiv = ivs["spa"]
    
    if (atkiv % 2 > 0):
        if defiv in [2,3,7,11]:
            if spdiv in [5,13]:
                if speiv == 15:
                    return True
    return False

'''
Determines shininess of a Gen 3+ pokemon, based on ID, Secret ID, and PV.
'''
def gen3Shiny(tid, sid, pid):
    pid_upper = (pid >> 16) & 0xFFFF
    pid_lower = pid & 0xFFFF
    return (tid ^ sid ^ pid_upper ^ pid_lower) < 8

'''
Exports party to PK(X) format
'''
def exportParty(memdata, gen=GAME_GENERATION, directory="party/"):
    for poke in memdata.gamedata.party:
        outStr = ('%03d ' % poke.spec)
        if (poke.shiny):
            outStr += "★ "
        outStr += "- " + poke.name + " - "
        if (poke.pid):
            outStr += str(hex(poke.pid))
        else:
            outStr += str(hex(poke.ot_id))
        if GAME_NAME in ["redplusplus"]:
            outStr += ".pk2"
        else:
            outStr += ".pk"+str(GAME_GENERATION)
        with open(directory+outStr, "wb") as pkm:
            # Convert Red++ mons to PK2
            if GAME_NAME in ["redplusplus"]:
                # 0x4 = item
                # 0x5 = moves
                # 0x9 = OT
                
                pk2 = [0] * 73
                
                if poke.spec < 252:
                    pk2[0] = pk2[3] = poke.spec
                else:
                    pk2[0] = pk2[3] = 0
                
                pk2[1] = 0x1
                pk2[2] = 0xFF
                pk2[5:9] = poke.data[8:12]
                for i in range(0xC, 0x20):
                    pk2[i-0xC+9] = poke.data[i]
                for i in range(0, len(poke.ot_name_raw)):
                    pk2[0x33+i] = poke.ot_name_raw[i]
                for i in range(0, len(poke.name_raw)):
                    pk2[0x3E+i] = poke.name_raw[i]
                
                # Convert Red++ shiny format to Gen 2 format
                if (poke.shiny):
                    ivs = poke.ivs
                    while (ivs["atk"] not in [2,3,6,7,10,11,14,15]):
                        ivs["atk"] = (ivs["atk"] + 1) % 16
                    ivs["def"] = ivs["spe"] = ivs["spd"] = 10
                    
                    iv_ad = iv_ss = 0
                    iv_ad |= ivs["def"]
                    iv_ad |= (ivs["atk"] << 4)
                    iv_ss |= ivs["spd"]
                    iv_ss |= (ivs["spe"] << 4)
                    
                    pk2[0x18] = iv_ad
                    pk2[0x19] = iv_ss
                    
                pkm.write(bytearray(pk2))
            else:
                pkm.write(poke.data)
            
    return

'''
Converts a game-encoded string to a standard string
'''
def convNameValue(data, gen=GAME_GENERATION):
    res = ""
    if (gen == 1):
        for char in data:
            if char < 0x70 or char > 0xFF:
                break
            res += charmap[0][char-0x70]
    elif (gen == 2):
        for char in data:
            if char < 0x70 or char > 0xFF:
                break
            res += charmap[1][char-0x70]
    elif (gen == 3):
        for char in data:
            if GAME_NAME == "radicalred" and char == 0x0:
                res += ' '
            elif char < 0xA0 or char > 0xFE:
                break
            else:
                res += charmap[2][char-0xA0]
    elif (gen == 4):
        for i in range(0, len(data), 2):
            char = data[i] | (data[i+1] << 8)
            if char == 0xFFFF:
                break
            if (char in charmap[3]):
                # print(G4ValueId[char])
                res += (charmap[3][char]).decode("utf-8")
            else:
                res += " "
    elif (gen == 5):
        for i in range(0, len(data), 2):
            char = data[i] | (data[i+1] << 8)
            if char == 0xFFFF:
                break
            if char == 0x246E:
                char = 0x2640
            elif char == 0x246D:
                char = 0x2642
            res += chr(char)

            #res += char.decode("utf-8")
            
            #// remap custom glyphs to unicode
            #s.Replace('\uE08F', '♀'); // ♀ (gen6+)
            #s.Replace('\uE08E', '♂'); // ♂ (gen6+)
            #s.Replace('\u246E', '♀'); // ♀ (gen5)
            #s.Replace('\u246D', '♂'); // ♂ (gen5)
    return str(res)

'''
Converts a standard string into game-encoded string. Useful for debugging.
'''
def revConvName(string, gen=GAME_GENERATION):
    res = []
    if (0 < gen < 4):
        for char in string:
            if (char in charmap[gen-1]):
                res.append(charmap[gen-1].index(char))
    elif (gen == 4):
        for char in string:
            if (char.encode("utf-8") in charmap[3].values()):
                res.append(list(charmap[3].keys())[list(charmap[3].values()).index(char.encode("utf-8"))])
    else:
        for char in string:
            res.append(ord(char))
    print(string, end=" = ")
    for char in res:
        print(hex(char), end=" ")
    print()
    return res

'''
Updates the memdata object from a *local* save file
'''
def updateRAM(memdata, memfile):   
    print("Reading RAM data...")
    with open(memfile, "rb", buffering=0) as gbfile:
        memdata.memory = gbfile.read()
    return memdata

'''
Updates memdata object based on a *remote* file.
'''
def updateRAMRemote(memdata, memurl):
    print("Reading RAM data...")
    memdata.memory = requests.get(memurl, headers={'Cache-Control': 'no-cache'}, timeout=10).content
    return memdata

'''
Retrieves and decrypts Pokemon data from memory.
'''
def getPokeFromMem(memory, party_offset, pokeSize, gen=GAME_GENERATION):
    ekm = memory[party_offset:party_offset+pokeSize]
    
    if PRINT_DEBUG:
        print("Encrypted PKM:")
        for byte in ekm:
            print(hex(byte), end = " ")
        print()
    
    # Gen 1, 2, and some romhacks have unencrypted pokemon
    if gen < 3 or GAME_NAME in ["radicalred"]:
        dkm = ekm
        calculated_chk = chk = 0
    elif gen == 3:
        pid = readByte32(ekm, 0)
        full_id = readByte32(ekm, 4)
        dec_key = full_id ^ pid
        dkm = gen3DecryptData(dec_key, ekm)
        calculated_chk = chk = 0 # fix later
    else:
        dkm = decryptAndUnshuf45(ekm)
        chk = ekm[6] | (ekm[7] << 8)
        calculated_chk = gen4CalcChecksum(dkm)
        
    if PRINT_DEBUG:
        print("Decrypted PKM:")
        for byte in dkm:
            print(hex(byte), end = " ")
        print()
    if not BYPASS_CHECKSUM:
        if (calculated_chk != chk):
            print("Checksum error! Calculated: {0} | Expected: {1}".format(hex(calculated_chk), hex(chk)))
            raise ChecksumError("Checksum did not match")
        if PRINT_DEBUG:
           print("Checksum ok!")
       
    return dkm, chk

'''
Reads a single byte from a memory array.
''' 
def readByte8(mem, off):
    return mem[off]

'''
Reads two bytes from a memory array, optinally reversing the byte order
'''
def readByte16(mem, off, rev=False):
    if rev:
        return mem[off+1] | (mem[off] << 8)
    else:
        return mem[off] | (mem[off+1] << 8)

'''
Reads four bytes from a memory array, optinally reversing the byte order
'''
def readByte32(mem, off):
    res = 0
    for i in range(0, 4):
        res |= (mem[off+i]) << i*8
    return res
    
'''
Determines Gen 4 gender based on the species and PID
'''
def gen4Gender(spec, pid):
    if spec > len(genderratiomap):
        return -1
    return int(not((pid % 256) > math.floor(254*genderratiomap[spec])))

'''
Determines Gen 3 gender based on the species and PID
'''
def gen3Gender(spec, pid):
    return gen4Gender(spec, pid)

'''
Determines Pokemon species based on internal indexes of Radical Red v2.3a (Fire Red romhack)
'''
def radicalRedSpecies(spec):
    # internal_id: [nat_dex_num, form_num]
    # since we don't know these they were added as needed
    spec_rr = { \
    1209: [77, 1], # Galarian Ponyta
    1210: [78, 1], # Galarian Rapidash
    714: [479, 2], # Rotom Wash
    }
    
    # Turtwig - Genesect
    if 439 < spec < 703:
        return [spec-53, None]
    # Chespin - Hoopa
    elif 757 < spec < 829:
        return [spec-108, None]
    # Rowlett - Marshadow
    elif 939 < spec < 1020:
        return [spec-217, None]
    # Grookey - Zarude
    elif 1037 < spec < 1186:
        return [spec-292, None]
    # All others that don't fit the pattern (form changes, etc.)
    elif spec in spec_rr:
        return spec_rr[spec]
    # Only possibility left is if it's an original Gen 3 mon
    elif spec < 440:
        spec_conv = gen3Species(spec)
        return [spec_conv, None]
    else:
        return [0, None]

'''
Converts a Gen 3 species index number to the national dex index.
'''
def gen3Species(spec):
    spec_table = \
    [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, \
      0,   252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, \
      275, 290, 291, 292, 276, 277, 285, 286, 327, 278, 279, 283, 284, 320, 321, 300, 301, 352, 343, 344, 299, 324, 302, 339, \
      340, 370, 341, 342, 349, 350, 318, 319, 328, 329, 330, 296, 297, 309, 310, 322, 323, 363, 364, 365, 331, 332, 361, 362, \
      337, 338, 298, 325, 326, 311, 312, 303, 307, 308, 333, 334, 360, 355, 356, 315, 287, 288, 289, 316, 317, 357, 293, 294, \
      295, 366, 367, 368, 359, 353, 354, 336, 335, 369, 304, 305, 306, 351, 313, 314, 345, 346, 347, 348, 280, 281, 282, 371, \
      372, 373, 374, 375, 376, 377, 378, 379, 382, 383, 384, 380, 381, 385, 386, 358, 0,   201, 201, 201, 201, 201, 201, 201, \
      201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201 ]

    if spec < 252:
        return spec
    elif spec > 440:
        return 0
    else:
        return spec_table[spec-252]

'''
Converts a Red++ species index to the national dex number.
'''
def rppToSpecies(spec):
    spec_table = \
    [ 249, 228, 229, 198, 430, 214, 196, 197, 471, 470, 700, 212, 208, 169, 186, 199, 182, 230, 242, 233, 474, 467, 466, 462, \
    464, 465, 463, 175, 176, 468, 215, 461, 227, 200, 429, 241, 170, 171, 218, 219, 324, 380, 381, 237, 236, 172, 173, 174, 238, \
    239, 240, 439, 440, 446, 263, 264, 250 ] 
    if spec > 208:
        return 0
    elif spec < 152:
        return spec
    else:
        return spec_table[spec-152]

def brownToSpecies(spec):
    try:
        return [species_map["gen1"].index(spec), 0]
    except ValueError:
        spec_brown = { \
            ## ADD NEW/UNKNOWN SPECIES HERE
            ## FORMAT:
            ##
            ## Spec_Raw: [NatDex, FormNum],
            ##
            ## EXAMPLE:
            ##
            ## 1209: [77, 1], # Galarian Ponyta
        }
        if spec in spec_brown:
            return spec_brown[spec]
        return [0, 0]

'''
Converts a national dex number to a Red++ species index.
'''
def specToRpp(spec):
    spec_table = \
    [ 249, 228, 229, 198, 430, 214, 196, 197, 471, 470, 700, 212, 208, 169, 186, 199, 182, 230, 242, 233, 474, 467, 466, 462, \
    464, 465, 463, 175, 176, 468, 215, 461, 227, 200, 429, 241, 170, 171, 218, 219, 324, 380, 381, 237, 236, 172, 173, 174, 238, \
    239, 240, 439, 440, 446, 263, 264, 250 ] 
    if spec < 152:
        return spec
    elif spec in spec_table:
        return spec_table.index(spec)+152
    else:
        return 0

'''
Converts a national dex number to a Gen 1 species index.
'''      
def specToGen1(spec):
    if spec < len(species_map["gen1"]):
        return species_map["gen1"][spec]
    else:
        return 255
    
'''
Truncates an int to 8 bits.
'''
def trunc_8(num):
    return num & 0xFF

'''
Truncates an int to 16 bits.
'''
def trunc_16(num):
    return num & 0xFFFF

'''
Calculates the checksum for a Gen 4 Pokemon.
'''
def gen4CalcChecksum(dkm):
    chk = 0
    for i in range(0x8, 0x87, 2):
        byte = dkm[i] | (dkm[i+1] << 8)
        chk += byte
    return chk & 0xFFFF

'''
Unshuffles a shuffled PK4 based on its shuffle value. Copied from kwsch/PKHeX.
'''
def gen4Unshuf(data, sv, blockSize):
    blockPosition = [ \
    [0, 1, 2, 3], \
    [0, 1, 3, 2], \
    [0, 2, 1, 3], \
    [0, 3, 1, 2], \
    [0, 2, 3, 1], \
    [0, 3, 2, 1], \
    [1, 0, 2, 3], \
    [1, 0, 3, 2], \
    [2, 0, 1, 3], \
    [3, 0, 1, 2], \
    [2, 0, 3, 1], \
    [3, 0, 2, 1], \
    [1, 2, 0, 3], \
    [1, 3, 0, 2], \
    [2, 1, 0, 3], \
    [3, 1, 0, 2], \
    [2, 3, 0, 1], \
    [3, 2, 0, 1], \
    [1, 2, 3, 0], \
    [1, 3, 2, 0], \
    [2, 1, 3, 0], \
    [3, 1, 2, 0], \
    [2, 3, 1, 0], \
    [3, 2, 1, 0] ]
    
    sdata = copy.deepcopy(data)
    index = sv % 24
    start = 8
    for block in range(0, 4):
        ofs = blockPosition[index][block]
        data_offset = (ofs*blockSize) + start
        sdata_offset = (block*blockSize) + start
        sdata[sdata_offset:sdata_offset+blockSize] = (data[data_offset:data_offset+blockSize])
    return sdata;

'''
Gen 4 recursive PRNG function to decrypt PK4 bytes. Copied from kwsch/PKHeX.
'''
def decryptRand(data, seed, i):
    seed = (0x41C64E6D * seed) + 0x00006073;
    data[i] ^= trunc_8(seed >> 16)
    data[i + 1] ^= trunc_8(seed >> 24)
    
    return seed, data

'''
Decrypts an array of bytes within a PK4. Copied from kwsch/PKHeX.
'''
def decryptArray(data, seed, start, end):
    i = start
    
    while (i < end):
        seed, data = decryptRand(data, seed, i)
        i += 2
        seed, data = decryptRand(data, seed, i)
        i += 2
    
    return data

'''
Decrypts an encrypted PK4/PK5 data array. Copied from kwsch/PKHeX.
'''
def decryptPKM45(data, pv, chk, blockSize):
    start = 8;
    end = (4 * blockSize) + start
    data = decryptArray(data, chk, start, end) # Blocks
    if (len(data) > end):
        data = decryptArray(data, pv, end, len(data)); # Party Stats
    return data

'''
Decrypts and then unshuffles an encrypted PK4/PK5. Copied from kwsch/PKHeX.
'''
def decryptAndUnshuf45(ekm):
    ekm = bytearray(ekm)
    pv = 0
    for j in range(0, 4):
        pv |= (ekm[j] << j*8)
    chk = ekm[6] | (ekm[7] << 8)
    sv = (pv >> 13 & 31);
    
    ekm = decryptPKM45(ekm, pv, chk, 32)    
    unshuf = gen4Unshuf(ekm, sv, 32)
    return unshuf

'''
Decrypts the Gen 3 data chunk containing various Pokemon data
'''
def gen3DecryptData(dec_key, ekm):
    ekm = bytearray(ekm)
    start = 32
    end = 80
    enc_data = ekm[start:end]
    dec_data = []
    checksum = 0
    for i in range(0, 12):
        chunk = 0
        for j in range(0, 4):
            chunk |= (enc_data[i*4+j]) << j*8
        chunk = chunk^dec_key
        checksum += chunk
        for j in range(0, 4):
            dec_data.append((chunk >> j*8) & 0xFF)
    print("Checksum: " + str(checksum%0xFFFF))
    dkm = ekm
    for i in range(0, len(dec_data)):
        dkm[start+i] = dec_data[i]
    return dkm

'''
Updates the gamedata variables based on current memory.
'''
def updateVars(gamedata, memory, game=GAME_NAME, gen=GAME_GENERATION):
    off_party = OFFSET_TABLE[game]["party"]
    off_battle = OFFSET_TABLE[game]["battle_party"]
    off_name = OFFSET_TABLE[game]["trainer_name"]
    off_rival = OFFSET_TABLE[game]["rival_name"]
    off_partysize = OFFSET_TABLE[game]["party_size"]
    off_time_hour = OFFSET_TABLE[game]["time_hour"]
    off_time_min = OFFSET_TABLE[game]["time_min"]
    off_time_sec = OFFSET_TABLE[game]["time_sec"]
    off_badges = OFFSET_TABLE[game]["badges"]
    off_gender = OFFSET_TABLE[game]["gender"]
    
    pokeSizes = [44, 48, 100, 236, 220] # Size in bytes of .pkm per generation
    pokeSize = pokeSizes[gen-1]
    
    namelen = 0
    if (gen < 4):
        namelen = 0x8
    elif (3 < gen < 6):
        namelen = 0x10
    
    gamedata.trainer_name_raw = memory[off_name:off_name+namelen]
    gamedata.trainer_name = convNameValue(gamedata.trainer_name_raw, gen)
    
    if (off_gender):
        gamedata.trainer_gender = memory[off_gender]
    else:
        gamedata.trainer_gender = 0
        
    if (off_rival):
        rival_name_raw = memory[off_rival:off_rival+namelen]
        gamedata.rival_name = convNameValue(rival_name_raw, gen)
    elif GAME_NAME in ["ruby", "sapphire", "emerald"]:
        if (gamedata.trainer_gender == 0):
            gamedata.rival_name = "MAY"
        else:
            gamedata.rival_name = "BRENDAN"

# We never really used game time for anything, so for now it is commented out
#    gamedata.time_hours = memory[off_time_hour]
#    gamedata.time_minutes = memory[off_time_min]
#    gamedata.time_seconds = memory[off_time_sec]
    if (off_badges):
        gamedata.badges = memory[off_badges]
    if (gen == 2 or GAME_NAME in ["redplusplus", "heartgold", "soulsilver"]):
        num_badges = 0
        kantobadges = memory[off_badges+1]
        num_badges |= (kantobadges << 8)
    num_badges = bin(gamedata.badges).count("1")
    gamedata.partysize = memory[off_partysize]
    #if (gen == 1):
    #    gamedata.partysize -= 1
    gamedata.boxsize = 0
    
    if PRINT_VERBOSE:
        print("Trainer: {0} | Time: {1}:{2}:{3} | Badges: {4}".format(gamedata.trainer_name, \
        gamedata.time_hours, gamedata.time_minutes, gamedata.time_seconds, \
        num_badges))
        print("Rival: "+gamedata.rival_name)
    
    if PRINT_VERBOSE:
        print("\n-PARTY-")
    
    party = []
    for i in range(0, gamedata.partysize): 
        party.append(Pokemon())
    for i in range(0, gamedata.partysize):
        try:
            party[i].data, party[i].chk = getPokeFromMem(memory, i*pokeSize+off_battle, pokeSize)
        except ChecksumError:
            print("Error reading battle party. Trying OW...")
            for i in range(0, gamedata.partysize): 
                try:
                    party[i].data, party[i].chk = getPokeFromMem(memory, i*pokeSize+off_party, pokeSize)
                except ChecksumError:
                    raise MemoryReadError("Error reading data from memory")
                    return None
            break
            
    for i in range(0, gamedata.partysize):  
        dkm = party[i].data
                
        # Shared stuff
        if (2 < gen < 6):
            party[i].pid = readByte32(dkm, 0x0)
            ot_id = readByte16(dkm, 0xc)
            ot_sid = readByte16(dkm, 0xe)
        
        # Not shared stuff
        if (gen == 1):
            ot_id = readByte16(dkm, 0xC)
            party[i].ot_id = ot_id
            if GAME_NAME == "redplusplus":
                party[i].spec = rppToSpecies(dkm[0x0])
            elif GAME_NAME == "brown":
                party[i].spec_raw = dkm[0]
                spec_form = brownToSpecies(dkm[0x0])
                party[i].spec = spec_form[0]
                party[i].form = spec_form[1]
            party[i].lvl = dkm[0x21]
            party[i].status = dkm[0x4]
            party[i].hp = readByte16(dkm, 0x1, True)
            party[i].maxhp = readByte16(dkm, 0x22, True)
            
            name_off = OFFSET_TABLE[game]["party"]+0x14a+11*i
            party[i].name_raw = memory[name_off:name_off+10]
            otname_off = OFFSET_TABLE[game]["party"]+0x108+11*i
            party[i].ot_name_raw = memory[otname_off:otname_off+10]
            
            party[i].name = convNameValue(party[i].name_raw, gen)
            
            iv_ad = dkm[0x1b]
            iv_ss = dkm[0x1c]
            party[i].ivs["atk"] = (iv_ad&0xF0)>>4
            party[i].ivs["def"] = (iv_ad&0x0F)
            party[i].ivs["spe"] = (iv_ss&0xF0)>>4
            party[i].ivs["spa"] = party[i].ivs["spd"] = (iv_ss&0x0F)
            party[i].ivs["hp"] = ((party[i].ivs["atk"]&1) << 3) | ((party[i].ivs["def"]&1) << 2) | \
            ((party[i].ivs["spe"]&1) << 1) | ((party[i].ivs["spa"]&1))
            
            if (GAME_NAME == "redplusplus"):
                party[i].shiny = gen1RPPShiny(party[i].ivs)
            party[i].gender = gen2Gender(genderratiomap[party[i].spec], party[i].ivs["atk"])
                
        elif (gen == 2):
            ot_id = readByte16(dkm, 0x6)
            party[i].spec = dkm[0x0]
            party[i].item = dkm[0x1]
            party[i].happiness = dkm[0x1b]
            party[i].lvl = dkm[0x1f]
            party[i].status = dkm[0x20]
            party[i].hp = readByte16(dkm, 0x22)
            party[i].maxhp = readByte16(dkm, 0x24)
            
            name_off = OFFSET_TABLE[game]["party"]+0x162+11*i
            party[i].name_raw = dkm[name_off:name_off+10]
            party[i].name = convNameValue(party[i].name_raw, gen)
            
            iv_ad = dkm[0x15]
            iv_ss = dkm[0x16]
            party[i].ivs["atk"] = (iv_ad&0xF0)>>4
            party[i].ivs["def"] = (iv_ad&0x0F)
            party[i].ivs["spe"] = (iv_ss&0xF0)>>4
            party[i].ivs["spa"] = party[i].ivs["spd"] = (iv_ss&0x0F)
            party[i].ivs["hp"] = ((party[i].ivs["atk"]&1) << 3) | ((party[i].ivs["def"]&1) << 2) | \
            ((party[i].ivs["spe"]&1) << 1) | ((party[i].ivs["spa"]&1))
            
            party[i].shiny = genIIShiny(party[i].ivs)
            party[i].gender = genIIGender(genderratiomap[party[i].spec], party[i].ivs["atk"])
            
        elif (gen == 3):
            # Some Gen 3 hacks hardcode the same shuffle order for every PKM
            if GAME_NAME in ["radicalred"]:
                gr_offset = 0
                at_offset = 12
                ev_offset = 24
                mi_offset = 36
            else:
                subs = gen3_subs[party[i].pid % 24]
                gr_offset = subs.index(0) * 12
                at_offset = subs.index(1) * 12
                ev_offset = subs.index(2) * 12
                mi_offset = subs.index(3) * 12
            
            party[i].spec_raw = readByte16(dkm, 32+gr_offset)
            
            if GAME_NAME in ["radicalred"]:
                spec_form = radicalRedSpecies(party[i].spec_raw)
                party[i].spec = spec_form[0]
                party[i].form = spec_form[1]
            else:
                party[i].spec = gen3Species(party[i].spec_raw)
            
            party[i].item = readByte16(dkm, 32+gr_offset+2)
            party[i].gender = gen3Gender(party[i].spec, party[i].pid)
            
            iv_byte = readByte32(dkm, 32+mi_offset+4)
            party[i].ivs["hp"] = iv_byte & 31
            party[i].ivs["atk"] = (iv_byte >> 5) & 31
            party[i].ivs["def"] = (iv_byte >> 10) & 31
            party[i].ivs["spe"] = (iv_byte >> 15) & 31
            party[i].ivs["spa"] = (iv_byte >> 20) & 31
            party[i].ivs["spd"] = (iv_byte >> 25) & 31
            party[i].is_egg = (iv_byte >> 30) & 1
            
            ability_bit = (iv_byte >> 31) & 1
            spec_str = str(party[i].spec)
            if (party[i].form):
                spec_str += "_{}".format(party[i].form)
            if GAME_NAME == "radicalred" and spec_str in radicalred_abilities:
                hasSecondAbility = radicalred_abilities[spec_str][ability_bit]
                if hasSecondAbility:
                    party[i].ability = hasSecondAbility
                else:
                    party[i].ability = radicalred_abilities[spec_str][0]
            elif party[i].spec < len(gen3_abilities):
                hasSecondAbility = gen3_abilities[party[i].spec][ability_bit]
                if (hasSecondAbility):
                    party[i].ability = hasSecondAbility
                else:
                    party[i].ability = gen3_abilities[party[i].spec][0]
            
            party[i].name_raw = dkm[8:18]
            party[i].name = convNameValue(party[i].name_raw, GAME_GENERATION)
            party[i].lvl = dkm[84]
            party[i].hp = readByte16(dkm, 86)
            party[i].maxhp = readByte16(dkm, 88)
            party[i].status = readByte32(dkm, 80)
            party[i].happiness = dkm[32+9]
            
            party[i].shiny = gen3Shiny(ot_id, ot_sid, party[i].pid)
        elif (gen == 4):
            party[i].spec = readByte16(dkm, 0x8)
            party[i].item = readByte16(dkm, 0xa)
            party[i].happiness = dkm[0x14]
            party[i].ability = dkm[0x15]
            party[i].gender = gen4Gender(party[i].spec, party[i].pid)
            party[i].name_raw = dkm[0x48:0x5e]
            party[i].name = convNameValue(party[i].name_raw, gen)
            party[i].lvl = dkm[0x8C]
            party[i].hp = readByte16(dkm, 0x8e)
            party[i].maxhp = readByte16(dkm, 0x90)
            party[i].status = dkm[0x88]
            
            iv_byte = readByte32(dkm, 0x38)
            party[i].ivs["hp"] = iv_byte & 31
            party[i].ivs["atk"] = (iv_byte >> 5) & 31
            party[i].ivs["def"] = (iv_byte >> 10) & 31
            party[i].ivs["spe"] = (iv_byte >> 15) & 31
            party[i].ivs["spa"] = (iv_byte >> 20) & 31
            party[i].ivs["spd"] = (iv_byte >> 25) & 31
            party[i].is_egg = (iv_byte >> 30) & 1
            
            party[i].shiny = gen3Shiny(ot_id, ot_sid, party[i].pid)      
        elif (gen == 5):
            party[i].spec = readByte16(dkm, 0x8)
            party[i].item = readByte16(dkm, 0xa)
            party[i].ability = dkm[0x15]
            party[i].gender = gen4Gender(party[i].spec, party[i].pid)
            party[i].name_raw = dkm[0x48:0x5e]
            party[i].name = convNameValue(party[i].name_raw, gen)
            party[i].lvl = dkm[0x8C]
            party[i].hp = readByte16(dkm, 0x8e)
            party[i].maxhp = readByte16(dkm, 0x90)
            party[i].status = dkm[0x88]
            
            iv_byte = readByte32(dkm, 0x38)
            party[i].ivs["hp"] = iv_byte & 31
            party[i].ivs["atk"] = (iv_byte >> 5) & 31
            party[i].ivs["def"] = (iv_byte >> 10) & 31
            party[i].ivs["spe"] = (iv_byte >> 15) & 31
            party[i].ivs["spa"] = (iv_byte >> 20) & 31
            party[i].ivs["spd"] = (iv_byte >> 25) & 31
            party[i].is_egg = (iv_byte >> 30) & 1
            
            party[i].shiny = gen3Shiny(ot_id, ot_sid, party[i].pid)      
        
        # Sanitize data
        item_pre_san = party[i].item
        if GAME_GENERATION > 3:
            if party[i].item not in range(0, len(itemmap[3])):
                party[i].item = 0
        elif GAME_NAME == "radicalred" and party[i].item in radicalred_items:
            pass
        elif party[i].item not in range(0, len(itemmap[gen-1])):
            party[i].item = 0
            
        if party[i].ability not in range(0, len(abilities)):
            party[i].ability = 0
        
        if PRINT_VERBOSE:
            print("- {0}: {1} -".format(i+1, party[i].name))
            
            if GAME_NAME in ["radicalred", "brown"]:
                print("Spe_R: {}".format(party[i].spec_raw), end=" | ")
            print("ID: {} ({})".format(party[i].spec, species_names[party[i].spec]), end=" | ")
            print("Frm: {}".format(party[i].form), end=" | ")
            # print("Itm_Raw: {}".format(item_pre_san), end=" | ")
            print("Hap: {}".format(party[i].happiness), end=" | ")
            print("ItID: {}".format(party[i].item))
            
            if GAME_GENERATION > 3:
                itemname = itemmap[3][party[i].item]
            elif GAME_NAME in ["radicalred"] and party[i].item in radicalred_items:
                itemname = itemmap[3][radicalred_items[party[i].item]]
            else:
                itemname = itemmap[gen-1][party[i].item]
            print("Lv: {0} | Ab: {1} | It: {2} | HP: {3}/{4}".format(party[i].lvl, \
            abilities[party[i].ability], itemname, party[i].hp, party[i].maxhp))
            print("IVs: HP {0} | Atk {1} | Def {2} | Spe {3} | SpA {4} | SpD {5}".format(party[i].ivs["hp"], \
        party[i].ivs["atk"], party[i].ivs["def"], party[i].ivs["spe"], party[i].ivs["spa"], party[i].ivs["spd"]))
        
    gamedata.party = party
    return gamedata

''' 
Remove the temporary files.
'''
def cleanUpFiles():
    for file in ["tmp.mem", "tmp.mbc", "tmp.gbc", "tmp.png", "status.html"]:
        if os.path.exists(file):
            os.remove(file)

'''
Converts an HTML string to a PNG file. Requires weasyprint <= 52.5
'''
def htmlToPNG(data, outfile, border=0):
    # Convert to PNG
    html = HTML(string=data.encode("utf-8"))
    css = CSS(string="body {\
                            background-color: transparent;\
                            color: #99aab5;\
                            font-size: 90%\
                        }")
    html.write_png("tmp.png", stylesheets=[css], presentational_hints=True)
    im = Image.open("tmp.png")
    im = trimImage(im, border)
    im.save(outfile, "PNG")

def base64Img(path):
    return base64.b64encode(open(path, 'rb').read()).decode('utf-8')

'''
Update status.html with the relevant info. Probably better ways to do this, but for now it's manually constructed from scratch each loop.
'''
def updateStatFile(gamedata, statfile):
    # Stat file is buffered to minimize file access
    statFileStr = ""
    
    # Encoding data
    statFileStr += ("<meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-type\"> <meta content=\"jpg\" name=\"imgkit-format\">")
    
    # Responsive scale
    statFileStr += ("<body style=\"font-size:75%vmax;color: #99aab5;font-family: Tahoma, sans-serif;\">") 
    
    # Write misc. save info
    if (SHOW_MISC_DATA):
        statFileStr += ("Trainer: "+gamedata.trainer_name)
        statFileStr += (" | Rival: ")
        statFileStr += (gamedata.rival_name)
        
        statFileStr += ("<br>\n")
        statFileStr += ("Playtime: {0}:{1}:{2}".format(gamedata.time_hours,gamedata.time_minutes,gamedata.time_seconds))
        
        statFileStr += ("<br>\n")
        numBadges = bin(gamedata.badges).count("1")
        statFileStr += ("Badges: "+str(numBadges)+" "+"<br><br>\n")

    # Write party info
    statFileStr += ("<b><table style=\"font-size:3vh;font-weight: bold;\"><tr>")
    for i in range(0, gamedata.partysize):
        if gamedata.party[i].spec > -1:
            #if i % 3 == 0:
            #   statFileStr += ("</tr><tr>")
            statFileStr += ("<td style=\"padding: 5px;vertical-align: middle;text-align: center;line-height: 75%\">")
            colorStr = ""
            if (gamedata.party[i].status):
                status = gamedata.party[i].status
                if (status & 7): # asleeep
                    colorStr = "#36393f"
                elif ((status>>3) & 1): # poisoned
                    colorStr = "#9b84ee"
                elif ((status>>4) & 1): # burned
                    colorStr = "#f04747"
                elif ((status>>5) & 1): # frozen
                    colorStr = "#44ddbf"
                elif ((status>>6) & 1): # paralyzed
                    colorStr = "#faa61a"
                elif ((status>>4) & 1): # badly poisoned
                    colorStr = "#9b84ee"
                statFileStr += ("<span style=\"color:"+colorStr+";\">")
            elif gamedata.party[i].gender == 0:
                statFileStr += ("<span style=\"color:#7289da;\">")
            elif gamedata.party[i].gender == 1:
                statFileStr += ("<span style=\"color:#f47b68;\">")
            else:
                statFileStr += ("<span>")
            if (len(gamedata.party[i].name) > 7):
                statFileStr += ("<small><small><small><small>"+gamedata.party[i].name+"</small>")
            else:
                statFileStr += ("<small><small>"+gamedata.party[i].name)
            statFileStr += ("</span> ")
            
            statFileStr += ("<small><small><small>Lv </small>"+str(gamedata.party[i].lvl)+"</small></small></small><br>\n")
            if GAME_GENERATION > 2:
                statFileStr += ("<small><small>"+abilities[gamedata.party[i].ability]+"</small></small><br>\n")
            # Held Items
            if GAME_GENERATION > 1:
                data_uri = base64Img(SPRITE_DIR+"item.png")
                statFileStr += "<img src=\"data:image/png;base64,{0}\"> ".format(data_uri)
                
                if GAME_GENERATION > 3:
                    itemname = itemmap[3][gamedata.party[i].item]
                elif GAME_NAME in ["radicalred"] and gamedata.party[i].item in radicalred_items:
                    itemname = itemmap[3][radicalred_items[gamedata.party[i].item]]
                else:
                    itemname = itemmap[GAME_GENERATION-1][gamedata.party[i].item]
                statFileStr += ("<small><small>"+itemname+"</small></small><br>\n")
            
            statFileStr += ("<small>HP: ")
            if (gamedata.party[i].hp/gamedata.party[i].maxhp < 0.2):
                statFileStr += "<span style=\"color:#f47b68;\">"
            elif (gamedata.party[i].hp/gamedata.party[i].maxhp <= 0.5):
                statFileStr += "<span style=\"color:#faa61a;\">"
            else:
                statFileStr += "<span>"
            statFileStr += (str(gamedata.party[i].hp)+"</span> / "+str(gamedata.party[i].maxhp)+"</small><br>\n")
            
            # Mon Species
            species = ""
            if (gamedata.party[i].is_egg):
                species = "egg"
            else:
                if gamedata.party[i].shiny:
                    species = "shiny/"
                if (GAME_NAME == "redplusplus"):
                    species += str(specToRpp(gamedata.party[i].spec))
                else:
                    species += str(gamedata.party[i].spec)
                if gamedata.party[i].form:
                    species += "_" + str(gamedata.party[i].form)
            # Sprite
            data_uri = base64Img(SPRITE_DIR+str(species)+".png")
            statFileStr += ("<img style=\"vertical-align: 25px;width: 4em;height: auto;interpolation-mode: nearest-neighbor;image-rendering: crisp-edges;image-rendering: pixelated;\" src=\"data:image/png;base64,{0}\">".format(data_uri))
    if (SHOW_BOX_DATA):
        statFileStr += "</table>Current Box:<br>"
        for i in range(0, gamedata.boxsize):
           if gamedata.box[i].spec > 0:
               if i % 8 == 0:
                    statFileStr += ("<br>")
               species = 0
               if (gamedata.party[i].is_egg):
                    species = "egg"
               else:
                    if gamedata.box[i].shiny:
                       species = "shiny/"+str(gamedata.box[i].spec)
                    else:
                       species = str(gamedata.box[i].spec)
               data_uri = base64Img(HTML_DIR+"sprites/"+GAME_NAME+"/"+str(species)+".png")
               statFileStr += ("<img style=\"vertical-align: 25px;width: 8vw;height: auto;interpolation-mode: nearest-neighbor;image-rendering: crisp-edges;image-rendering: pixelated;\" src=\"data:image/png;base64,{0}\">".format(data_uri))
    
    with open(statfile, "wb", buffering=0) as statFile:
        statFile.write(statFileStr.encode("utf-8"))
    
    htmlToPNG(statFileStr, HTML_DIR+"status.png", 5)

'''
Extracts the last frame from a GIF, saving it as a PNG.
'''
def extractFrameGif(url, out):
    #if not os.path.exists(out):
    #    os.makedirs(out)
    gif_data = requests.get(url, headers={'Cache-Control': 'no-cache'}, timeout=10).content
    gif = Image.open(io.BytesIO(gif_data))
    gif.seek(gif.n_frames-1)
    
    gif.save(out, "PNG")

'''
Game update "loop". It doesn't actually loop since I found it's easier to avoid errors if we loop at a shell/terminal level.
It does however wait for five seconds before exiting-- so it loops at a regular interval.
'''
def updateLoop():
    try:       
        stateStr = "https://screenshake.club/share/dew/save.state?="
        imageStr = "https://screenshake.club/share/dew/output.gif?="
        timeStr = str(int(time.time()))
        memdata = MemData()
        #memdata = updateRAMRemote(memdata, stateStr+timeStr)
        memdata = updateRAM(memdata, "brown_test.state")
        memdata.gamedata = updateVars(memdata.gamedata, memdata.memory)
        updateStatFile(memdata.gamedata, "status.html")
        copyfile("status.html", HTML_DIR+"status.html")
        extractFrameGif(imageStr+timeStr, HTML_DIR+"current.png")
        
        cleanUpFiles()
        if EXPORT_PARTY:
            exportParty(memdata, GAME_GENERATION, HTML_DIR+"party/"+GAME_NAME+"/")
        if PRINT_VERBOSE:
            print("\nWaiting to exit.")
    except Exception:
        print(traceback.format_exc())

def main():
    updateLoop()
    time.sleep(5)
    
if __name__ == "__main__":
    main()
