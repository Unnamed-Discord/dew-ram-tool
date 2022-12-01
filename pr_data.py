# -*- coding: utf-8 -*- 


# MEMORY OFFSETS - edit based on your emulator/ROM.

# PARTY OFFSETS - Points to the first byte of the first Pokemon in the party.
PARTY_OFFSETS = {
"connygold": 0x3DB3,
"gold" : 0x0,
"emerald": 0x454EC,
"diamond": 0x279C40,
"redplusplus": 0x5570,
"white": 0x2410B4,
"radicalred": 0x45284,
"crystal": 0x60DF,
"white2" : 0x22AB0C,
"stormsilver": 0x288998
}

# OFFSET TABLE - These are required for the main script to locate data. All are relative to the PARTY_OFFSET

# The following are required to function:
# "party" - location of the first byte of the first party member
# "battle_party" - location of the first byte of the first party member while in battle (if not a DS game, it's probably the same as "party")
# "trainer_name" - location of the first byte of the player's trainer name
# "party_size" - location of the byte that counts the number of Pokemon in the party. Usually stored near the party data

# Other values are not required (and thus we stopped using them), but can add extra functionality:
# rival_name - location of the first byte of the rival's name
# time_hour - location of the hour byte of the play time
# time_min - location of the minutes byte of the play time
# time_sec - location of the second byte of the play time
# badges - location of the number of badges
# gender -  location of the player gender

OFFSET_TABLE = { \
"connygold": # ConnyGold Offsets
{ "party": PARTY_OFFSETS["connygold"], \
"battle_party": PARTY_OFFSETS["connygold"], \
"trainer_name": PARTY_OFFSETS["connygold"] - 0x887, \
"rival_name": PARTY_OFFSETS["connygold"] - 0x871, \
"party_size": PARTY_OFFSETS["connygold"] - 0x8, \
"time_hour": PARTY_OFFSETS["connygold"] - 0x84e, \
"time_min": PARTY_OFFSETS["connygold"] - 0x84d, \
"time_sec": PARTY_OFFSETS["connygold"] - 0x84c, \
"badges": PARTY_OFFSETS["connygold"] - 0x4ae, \
"gender": None },
\
"emerald": # Emerald Offsets
{ "party": PARTY_OFFSETS["emerald"], \
"battle_party": PARTY_OFFSETS["emerald"], \
"trainer_name": PARTY_OFFSETS["emerald"] + 0x56c, \
"rival_name": None, \
"party_size": PARTY_OFFSETS["emerald"] - 0x3, \
"time_hour": PARTY_OFFSETS["emerald"] + 0x586, \
"time_min": PARTY_OFFSETS["emerald"] + 0x588, \
"time_sec": PARTY_OFFSETS["emerald"] + 0x589, \
"badges": None, \
"gender": PARTY_OFFSETS["emerald"] + 0x574 },
\
"diamond": # Diamond Offsets
{ "party": PARTY_OFFSETS["diamond"], \
"battle_party": PARTY_OFFSETS["diamond"] + 0x4c52c, \
"trainer_name": PARTY_OFFSETS["diamond"] - 0x34, \
"rival_name": PARTY_OFFSETS["diamond"] + 0x2510, \
"party_size": PARTY_OFFSETS["diamond"] - 0x4, \
"time_hour": PARTY_OFFSETS["diamond"] - 0x12, \
"time_min": PARTY_OFFSETS["diamond"] - 0x12 + 2, \
"time_sec": PARTY_OFFSETS["diamond"] - 0x12 + 3, \
"badges": PARTY_OFFSETS["diamond"] - 0x1a, \
"gender": PARTY_OFFSETS["diamond"] - 0x1c },
\
"white": # White Offsets
{ "party": PARTY_OFFSETS["white"], \
"battle_party": PARTY_OFFSETS["white"] + 0x35884, \
"trainer_name": PARTY_OFFSETS["white"] + 0x5FC, \
"rival_name": None, \
"party_size": PARTY_OFFSETS["white"] - 0x4, \
"time_hour": None, \
"time_min": None, \
"time_sec": None, \
"badges": None, \
"gender": None },
\
"redplusplus": # Red++ Offsets
{ "party": PARTY_OFFSETS["redplusplus"], \
"battle_party": PARTY_OFFSETS["redplusplus"], \
"trainer_name": PARTY_OFFSETS["redplusplus"] - 0x13, \
"rival_name": PARTY_OFFSETS["redplusplus"] + 0x28d, \
"party_size": PARTY_OFFSETS["redplusplus"] - 0x8, \
"time_hour": PARTY_OFFSETS["redplusplus"] + 0x8a2, \
"time_min": PARTY_OFFSETS["redplusplus"] + 0x8a2 + 1, \
"time_sec": PARTY_OFFSETS["redplusplus"] + 0x8a2 + 2, \
"badges": PARTY_OFFSETS["redplusplus"] + 0x299, \
"gender": PARTY_OFFSETS["redplusplus"] + 0x604 },
\
"radicalred": # RadicalRed Offsets
{ "party": PARTY_OFFSETS["radicalred"], \
"battle_party": PARTY_OFFSETS["radicalred"], \
"trainer_name": PARTY_OFFSETS["radicalred"] + 0x304, \
"rival_name":  PARTY_OFFSETS["radicalred"] + 0x4cf4, \
"party_size": PARTY_OFFSETS["radicalred"] - 0x25b, \
"time_hour": None, \
"time_min": None, \
"time_sec": None, \
"badges": None, \
"gender": None },
\
"crystal": # Crystal Offsets
{ "party": PARTY_OFFSETS["crystal"], \
"battle_party": PARTY_OFFSETS["crystal"], \
"trainer_name": PARTY_OFFSETS["crystal"] - 0x862, \
"rival_name":  PARTY_OFFSETS["crystal"] - 0x84c, \
"party_size": PARTY_OFFSETS["crystal"] - 0x8, \
"time_hour": None, \
"time_min": None, \
"time_sec": None, \
"badges": None, \
"gender": None },
\
"white2": # White2 Offsets
{ "party": PARTY_OFFSETS["white2"], \
"battle_party": PARTY_OFFSETS["white2"] + 0x35884, \
"trainer_name": PARTY_OFFSETS["white2"] + 0x5FC, \
"rival_name": None, \
"party_size": PARTY_OFFSETS["white2"] - 0x4, \
"time_hour": None, \
"time_min": None, \
"time_sec": None, \
"badges": None, \
"gender": None },
\
"stormsilver": # Storm Silver
{ "party": PARTY_OFFSETS["stormsilver"], \
"battle_party": PARTY_OFFSETS["stormsilver"] + 0x4E9F0, \
"trainer_name": PARTY_OFFSETS["stormsilver"] - 0x34, \
"rival_name": None, \
"party_size": PARTY_OFFSETS["stormsilver"] - 0x4, \
"time_hour": None, \
"time_min": None, \
"time_sec": None, \
"badges": None, \
"gender": None },
}

# Probably don't need to change much beyond here

# character maps for gens 1-4
charmap = [ \
# gen 1
[ "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  "",  " ", \
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",\
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ":", ";", "[", "]",\
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",\
  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "é","'d","'l","'s","'t","'v",\
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
  "'", "ᴾᴋ","ᴹɴ","-","'r","'m", "?", "!", ".", "ァ", "ゥ", "ェ", "▷", "▶", "▼",	 "♂",\
  "$", "×", ".", "/", ",", "♀", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ],
# gen 2
[ "ᴾᴏ", "ᴷé", "“", "”", "・", "…", "ぁ", "ぇ", "ぉ", "", "", "", "", "", "", " ",\
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",\
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ":", ";", "[", "]",\
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",\
  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", " ", " ", " ", " ", " ",\
  "Ä", "Ö", "Ü", "ä", "ö", "ü", "",  "",  "",  "",  "",  "",  "",  "",  "",  "",\
  "'d", "'l", "'m", "'r", "'s", "'t", "'v", "", "", "", "", "", "", "", "", "←",\
  "'", "ᴾᴋ", "ᴹɴ", "-", " ", " ", "?", "!", ".", "&", "é", "→", "▷", "▶", "▼", "♂",\
  "$", "×", ".", "/", ",", "♀", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ],
# gen 3
[ " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", ".", "-", "・", \
  "…", "“", "”", "‘", "’", "♂", "♀", "$", ",", "×", "/", "A", "B", "C", "D", "E", \
  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", \
  "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
  "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ">", \
  ":", "Ä",	"Ö", "Ü", "ä", "ö", "ü", " ", " ", " ", " ", " ", " ", " ", " ", " " ],
# gen 4
{ 1: b'\xe3\x80\x80', 2: b'\xe3\x81\x81', 3: b'\xe3\x81\x82', 4: b'\xe3\x81\x83', 5: b'\xe3\x81\x84', 6: b'\xe3\x81\x85', 7: b'\xe3\x81\x86', 8: b'\xe3\x81\x87', 9: b'\xe3\x81\x88', 10: b'\xe3\x81\x89', 11: b'\xe3\x81\x8a', 12: b'\xe3\x81\x8b', 13: b'\xe3\x81\x8c', 14: b'\xe3\x81\x8d', 15: b'\xe3\x81\x8e', \
16: b'\xe3\x81\x8f', 17: b'\xe3\x81\x90', 18: b'\xe3\x81\x91', 19: b'\xe3\x81\x92', 20: b'\xe3\x81\x93', 21: b'\xe3\x81\x94', 22: b'\xe3\x81\x95', 23: b'\xe3\x81\x96', 24: b'\xe3\x81\x97', 25: b'\xe3\x81\x98', 26: b'\xe3\x81\x99', 27: b'\xe3\x81\x9a', 28: b'\xe3\x81\x9b', 29: b'\xe3\x81\x9c', 30: b'\xe3\x81\x9d', \
31: b'\xe3\x81\x9e', 32: b'\xe3\x81\x9f', 33: b'\xe3\x81\xa0', 34: b'\xe3\x81\xa1', 35: b'\xe3\x81\xa2', 36: b'\xe3\x81\xa3', 37: b'\xe3\x81\xa4', 38: b'\xe3\x81\xa5', 39: b'\xe3\x81\xa6', 40: b'\xe3\x81\xa7', 41: b'\xe3\x81\xa8', 42: b'\xe3\x81\xa9', 43: b'\xe3\x81\xaa', 44: b'\xe3\x81\xab', 45: b'\xe3\x81\xac', \
46: b'\xe3\x81\xad', 47: b'\xe3\x81\xae', 48: b'\xe3\x81\xaf', 49: b'\xe3\x81\xb0', 50: b'\xe3\x81\xb1', 51: b'\xe3\x81\xb2', 52: b'\xe3\x81\xb3', 53: b'\xe3\x81\xb4', 54: b'\xe3\x81\xb5', 55: b'\xe3\x81\xb6', 56: b'\xe3\x81\xb7', 57: b'\xe3\x81\xb8', 58: b'\xe3\x81\xb9', 59: b'\xe3\x81\xba', 60: b'\xe3\x81\xbb', \
61: b'\xe3\x81\xbc', 62: b'\xe3\x81\xbd', 63: b'\xe3\x81\xbe', 64: b'\xe3\x81\xbf', 65: b'\xe3\x82\x80', 66: b'\xe3\x82\x81', 67: b'\xe3\x82\x82', 68: b'\xe3\x82\x83', 69: b'\xe3\x82\x84', 70: b'\xe3\x82\x85', 71: b'\xe3\x82\x86', 72: b'\xe3\x82\x87', 73: b'\xe3\x82\x88', 74: b'\xe3\x82\x89', 75: b'\xe3\x82\x8a', \
76: b'\xe3\x82\x8b', 77: b'\xe3\x82\x8c', 78: b'\xe3\x82\x8d', 79: b'\xe3\x82\x8f', 80: b'\xe3\x82\x92', 81: b'\xe3\x82\x93', 82: b'\xe3\x82\xa1', 83: b'\xe3\x82\xa2', 84: b'\xe3\x82\xa3', 85: b'\xe3\x82\xa4', 86: b'\xe3\x82\xa5', 87: b'\xe3\x82\xa6', 88: b'\xe3\x82\xa7', 89: b'\xe3\x82\xa8', 90: b'\xe3\x82\xa9', \
91: b'\xe3\x82\xaa', 92: b'\xe3\x82\xab', 93: b'\xe3\x82\xac', 94: b'\xe3\x82\xad', 95: b'\xe3\x82\xae', 96: b'\xe3\x82\xaf', 97: b'\xe3\x82\xb0', 98: b'\xe3\x82\xb1', 99: b'\xe3\x82\xb2', 100: b'\xe3\x82\xb3', 101: b'\xe3\x82\xb4', 102: b'\xe3\x82\xb5', 103: b'\xe3\x82\xb6', 104: b'\xe3\x82\xb7', 105: b'\xe3\x82\xb8', \
106: b'\xe3\x82\xb9', 107: b'\xe3\x82\xba', 108: b'\xe3\x82\xbb', 109: b'\xe3\x82\xbc', 110: b'\xe3\x82\xbd', 111: b'\xe3\x82\xbe', 112: b'\xe3\x82\xbf', 113: b'\xe3\x83\x80', 114: b'\xe3\x83\x81', 115: b'\xe3\x83\x82', 116: b'\xe3\x83\x83', 117: b'\xe3\x83\x84', 118: b'\xe3\x83\x85', 119: b'\xe3\x83\x86', \
120: b'\xe3\x83\x87', 121: b'\xe3\x83\x88', 122: b'\xe3\x83\x89', 123: b'\xe3\x83\x8a', 124: b'\xe3\x83\x8b', 125: b'\xe3\x83\x8c', 126: b'\xe3\x83\x8d', 127: b'\xe3\x83\x8e', 128: b'\xe3\x83\x8f', 129: b'\xe3\x83\x90', 130: b'\xe3\x83\x91', 131: b'\xe3\x83\x92', 132: b'\xe3\x83\x93', 133: b'\xe3\x83\x94', \
134: b'\xe3\x83\x95', 135: b'\xe3\x83\x96', 136: b'\xe3\x83\x97', 137: b'\xe3\x83\x98', 138: b'\xe3\x83\x99', 139: b'\xe3\x83\x9a', 140: b'\xe3\x83\x9b', 141: b'\xe3\x83\x9c', 142: b'\xe3\x83\x9d', 143: b'\xe3\x83\x9e', 144: b'\xe3\x83\x9f', 145: b'\xe3\x83\xa0', 146: b'\xe3\x83\xa1', 147: b'\xe3\x83\xa2', \
148: b'\xe3\x83\xa3', 149: b'\xe3\x83\xa4', 150: b'\xe3\x83\xa5', 151: b'\xe3\x83\xa6', 152: b'\xe3\x83\xa7', 153: b'\xe3\x83\xa8', 154: b'\xe3\x83\xa9', 155: b'\xe3\x83\xaa', 156: b'\xe3\x83\xab', 157: b'\xe3\x83\xac', 158: b'\xe3\x83\xad', 159: b'\xe3\x83\xaf', 160: b'\xe3\x83\xb2', 161: b'\xe3\x83\xb3', \
162: b'\xef\xbc\x90', 163: b'\xef\xbc\x91', 164: b'\xef\xbc\x92', 165: b'\xef\xbc\x93', 166: b'\xef\xbc\x94', 167: b'\xef\xbc\x95', 168: b'\xef\xbc\x96', 169: b'\xef\xbc\x97', 170: b'\xef\xbc\x98', 171: b'\xef\xbc\x99', 172: b'\xef\xbc\xa1', 173: b'\xef\xbc\xa2', 174: b'\xef\xbc\xa3', 175: b'\xef\xbc\xa4', \
176: b'\xef\xbc\xa5', 177: b'\xef\xbc\xa6', 178: b'\xef\xbc\xa7', 179: b'\xef\xbc\xa8', 180: b'\xef\xbc\xa9', 181: b'\xef\xbc\xaa', 182: b'\xef\xbc\xab', 183: b'\xef\xbc\xac', 184: b'\xef\xbc\xad', 185: b'\xef\xbc\xae', 186: b'\xef\xbc\xaf', 187: b'\xef\xbc\xb0', 188: b'\xef\xbc\xb1', 189: b'\xef\xbc\xb2', \
190: b'\xef\xbc\xb3', 191: b'\xef\xbc\xb4', 192: b'\xef\xbc\xb5', 193: b'\xef\xbc\xb6', 194: b'\xef\xbc\xb7', 195: b'\xef\xbc\xb8', 196: b'\xef\xbc\xb9', 197: b'\xef\xbc\xba', 198: b'\xef\xbd\x81', 199: b'\xef\xbd\x82', 200: b'\xef\xbd\x83', 201: b'\xef\xbd\x84', 202: b'\xef\xbd\x85', 203: b'\xef\xbd\x86', \
204: b'\xef\xbd\x87', 205: b'\xef\xbd\x88', 206: b'\xef\xbd\x89', 207: b'\xef\xbd\x8a', 208: b'\xef\xbd\x8b', 209: b'\xef\xbd\x8c', 210: b'\xef\xbd\x8d', 211: b'\xef\xbd\x8e', 212: b'\xef\xbd\x8f', 213: b'\xef\xbd\x90', 214: b'\xef\xbd\x91', 215: b'\xef\xbd\x92', 216: b'\xef\xbd\x93', 217: b'\xef\xbd\x94', \
218: b'\xef\xbd\x95', 219: b'\xef\xbd\x96', 220: b'\xef\xbd\x97', 221: b'\xef\xbd\x98', 222: b'\xef\xbd\x99', 223: b'\xef\xbd\x9a', 225: b'\xef\xbc\x81', 226: b'\xef\xbc\x9f', 227: b'\xe3\x80\x81', 228: b'\xe3\x80\x82', 229: b'\xe2\x8b\xaf', 230: b'\xe3\x83\xbb', 231: b'\xef\xbc\x8f', 232: b'\xe3\x80\x8c', \
233: b'\xe3\x80\x8d', 234: b'\xe3\x80\x8e', 235: b'\xe3\x80\x8f', 236: b'\xef\xbc\x88', 237: b'\xef\xbc\x89', 238: b'\xe2\x91\xad', 239: b'\xe2\x91\xae', 240: b'\xef\xbc\x8b', 241: b'\xe3\x83\xbc', 242: b'\xe2\x91\xa7', 243: b'\xe2\x91\xa8', 244: b'\xef\xbc\x9d', 245: b'\xef\xbd\x9a', 246: b'\xef\xbc\x9a', \
247: b'\xef\xbc\x9b', 248: b'\xef\xbc\x8e', 249: b'\xef\xbc\x8c', 250: b'\xe2\x91\xaf', 251: b'\xe2\x91\xb0', 252: b'\xe2\x91\xb1', 253: b'\xe2\x91\xb2', 254: b'\xe2\x91\xb3', 255: b'\xe2\x91\xb4', 256: b'\xe2\x91\xb5', 257: b'\xe2\x91\xb6', 258: b'\xe2\x91\xb7', 259: b'\xe2\x91\xb8', 260: b'\xef\xbc\xa0', \
261: b'\xe2\x91\xb9', 262: b'\xef\xbc\x85', 263: b'\xe2\x91\xba', 264: b'\xe2\x91\xbb', 265: b'\xe2\x91\xbd', 266: b'\xe2\x9d\x84', 267: b'\xe2\x98\x8b', 268: b'\xe2\x99\x94', 269: b'\xe2\x99\x95', 270: b'\xe2\x98\x8a', 271: b'\xe2\x87\x97', 272: b'\xe2\x87\x98', 273: b'\xe2\x98\xbe', 274: b'\xc2\xa5', \
275: b'\xe2\x99\x88', 276: b'\xe2\x99\x89', 277: b'\xe2\x99\x8a', 278: b'\xe2\x99\x8b', 279: b'\xe2\x99\x8c', 280: b'\xe2\x99\x8d', 281: b'\xe2\x99\x8e', 282: b'\xe2\x99\x8f', 283: b'\xe2\x86\x90', 284: b'\xe2\x86\x91', 285: b'\xe2\x86\x93', 286: b'\xe2\x86\x92', 287: b'\xe2\x80\xa3', 288: b'\xef\xbc\x86', \
289: b'0', 290: b'1', 291: b'2', 292: b'3', 293: b'4', 294: b'5', 295: b'6', 296: b'7', 297: b'8', 298: b'9', 299: b'A', 300: b'B', 301: b'C', 302: b'D', 303: b'E', 304: b'F', 305: b'G', 306: b'H', 307: b'I', 308: b'J', 309: b'K', 310: b'L', 311: b'M', 312: b'N', 313: b'O', 314: b'P', 315: b'Q', 316: b'R', 317: b'S', \
318: b'T', 319: b'U', 320: b'V', 321: b'W', 322: b'X', 323: b'Y', 324: b'Z', 325: b'a', 326: b'b', 327: b'c', 328: b'd', 329: b'e', 330: b'f', 331: b'g', 332: b'h', 333: b'i', 334: b'j', 335: b'k', 336: b'l', 337: b'm', 338: b'n', 339: b'o', 340: b'p', 341: b'q', 342: b'r', 343: b's', 344: b't', 345: b'u', 346: b'v', \
347: b'w', 348: b'x', 349: b'y', 350: b'z', 351: b'\xc3\x80', 352: b'\xc3\x81', 353: b'\xc3\x82', 354: b'\xc3\x83', 355: b'\xc3\x84', 356: b'\xc3\x85', 357: b'\xc3\x86', 358: b'\xc3\x87', 359: b'\xc3\x88', 360: b'\xc3\x89', 361: b'\xc3\x8a', 362: b'\xc3\x8b', 363: b'\xc3\x8c', 364: b'\xc3\x8d', 365: b'\xc3\x8e', \
366: b'\xc3\x8f', 367: b'\xc3\x90', 368: b'\xc3\x91', 369: b'\xc3\x92', 370: b'\xc3\x93', 371: b'\xc3\x94', 372: b'\xc3\x95', 373: b'\xc3\x96', 374: b'\xc3\x97', 375: b'\xc3\x98', 376: b'\xc3\x99', 377: b'\xc3\x9a', 378: b'\xc3\x9b', 379: b'\xc3\x9c', 380: b'\xc3\x9d', 381: b'\xc3\x9e', 382: b'\xc3\x9f', \
383: b'\xc3\xa0', 384: b'\xc3\xa1', 385: b'\xc3\xa2', 386: b'\xc3\xa3', 387: b'\xc3\xa4', 388: b'\xc3\xa5', 389: b'\xc3\xa6', 390: b'\xc3\xa7', 391: b'\xc3\xa8', 392: b'\xc3\xa9', 393: b'\xc3\xaa', 394: b'\xc3\xab', 395: b'\xc3\xac', 396: b'\xc3\xad', 397: b'\xc3\xae', 398: b'\xc3\xaf', 399: b'\xc3\xb0', \
400: b'\xc3\xb1', 401: b'\xc3\xb2', 402: b'\xc3\xb3', 403: b'\xc3\xb4', 404: b'\xc3\xb5', 405: b'\xc3\xb6', 406: b'\xc3\xb7', 407: b'\xc3\xb8', 408: b'\xc3\xb9', 409: b'\xc3\xba', 410: b'\xc3\xbb', 411: b'\xc3\xbc', 412: b'\xc3\xbd', 413: b'\xc3\xbe', 414: b'\xc3\xbf', 415: b'\xc5\x92', 416: b'\xc5\x93', \
417: b'\xc5\x9e', 418: b'\xc5\x9f', 419: b'\xc2\xaa', 420: b'\xc2\xba', 421: b'\xc2\xb9', 422: b'\xc2\xb2', 423: b'\xc2\xb3', 424: b'$', 425: b'\xc2\xa1', 426: b'\xc2\xbf', 427: b'!', 428: b'?', 429: b',', 430: b'.', 431: b'\xe2\x91\xac', 432: b'\xef\xbd\xa5', 433: b'/', 434: b'\xe2\x80\x98', 435: b'\xe2\x80\x99', \
436: b'\xe2\x80\x9c', 437: b'\xe2\x80\x9d', 438: b'\xe2\x80\x9e', 439: b'\xe3\x80\x8a', 440: b'\xe3\x80\x8b', 441: b'(', 442: b')', 443: b'\xe2\x99\x82', 444: b'\xe2\x99\x80', 445: b'+', 446: b'-', 447: b'*', 448: b'#', 449: b'=', 450: b'&', 451: b'~', 452: b':', 453: b';', 454: b'\xe2\x91\xaf', 455: b'\xe2\x91\xb0', \
456: b'\xe2\x99\xa5', 457: b'\xe2\x91\xb2', 458: b'\xe2\x91\xb3', 459: b'\xe2\x91\xb4', 460: b'\xe2\x91\xb5', 461: b'\xe2\x91\xb6', 462: b'\xe2\x91\xb7', 463: b'\xe2\x91\xb8', 464: b'@', 465: b'\xe2\x91\xb9', 466: b'%', 467: b'\xe2\x91\xba', 468: b'\xe2\x91\xbb', 469: b'\xe2\x91\xbc', 470: b'\xe2\x91\xbd', \
471: b'\xe2\x91\xbe', 472: b'\xe2\x91\xbf', 473: b'\xe2\x92\x80', 474: b'\xe2\x92\x81', 475: b'\xe2\x92\x82', 476: b'\xe2\x92\x83', 477: b'\xe2\x92\x84', 478: b' ', 479: b'\xe2\x92\x85', 480: b'\xe2\x92\x86', 481: b'\xe2\x92\x87', 488: b'\xc2\xb0', 489: b'_', 490: b'\xef\xbc\xbf', 1025: b'\xea\xb0\x80', \
1026: b'\xea\xb0\x81', 1027: b'\xea\xb0\x84', 1028: b'\xea\xb0\x87', 1029: b'\xea\xb0\x88', 1030: b'\xea\xb0\x89', 1031: b'\xea\xb0\x8a', 1032: b'\xea\xb0\x90', 1033: b'\xea\xb0\x91', 1034: b'\xea\xb0\x92', 1035: b'\xea\xb0\x93', 1036: b'\xea\xb0\x94', 1037: b'\xea\xb0\x95', 1038: b'\xea\xb0\x96', \
1039: b'\xea\xb0\x97', 1040: b'\xea\xb0\x99', 1041: b'\xea\xb0\x9a', 1042: b'\xea\xb0\x9b', 1043: b'\xea\xb0\x9c', 1044: b'\xea\xb0\x9d', 1045: b'\xea\xb0\xa0', 1046: b'\xea\xb0\xa4', 1047: b'\xea\xb0\xac', 1048: b'\xea\xb0\xad', 1049: b'\xea\xb0\xaf', 1050: b'\xea\xb0\xb0', 1051: b'\xea\xb0\xb1', \
1052: b'\xea\xb0\xb8', 1053: b'\xea\xb0\xb9', 1054: b'\xea\xb0\xbc', 1055: b'\xea\xb1\x80', 1056: b'\xea\xb1\x8b', 1057: b'\xea\xb1\x8d', 1058: b'\xea\xb1\x94', 1059: b'\xea\xb1\x98', 1060: b'\xea\xb1\x9c', 1061: b'\xea\xb1\xb0', 1062: b'\xea\xb1\xb1', 1063: b'\xea\xb1\xb4', 1064: b'\xea\xb1\xb7', \
1065: b'\xea\xb1\xb8', 1066: b'\xea\xb1\xba', 1067: b'\xea\xb2\x80', 1068: b'\xea\xb2\x81', 1069: b'\xea\xb2\x83', 1070: b'\xea\xb2\x84', 1071: b'\xea\xb2\x85', 1072: b'\xea\xb2\x86', 1073: b'\xea\xb2\x89', 1074: b'\xea\xb2\x8a', 1075: b'\xea\xb2\x8b', 1076: b'\xea\xb2\x8c', 1077: b'\xea\xb2\x90', \
1078: b'\xea\xb2\x94', 1079: b'\xea\xb2\x9c', 1080: b'\xea\xb2\x9d', 1081: b'\xea\xb2\x9f', 1082: b'\xea\xb2\xa0', 1083: b'\xea\xb2\xa1', 1084: b'\xea\xb2\xa8', 1085: b'\xea\xb2\xa9', 1086: b'\xea\xb2\xaa', 1087: b'\xea\xb2\xac', 1088: b'\xea\xb2\xaf', 1089: b'\xea\xb2\xb0', 1090: b'\xea\xb2\xb8', \
1091: b'\xea\xb2\xb9', 1092: b'\xea\xb2\xbb', 1093: b'\xea\xb2\xbc', 1094: b'\xea\xb2\xbd', 1095: b'\xea\xb3\x81', 1096: b'\xea\xb3\x84', 1097: b'\xea\xb3\x88', 1098: b'\xea\xb3\x8c', 1099: b'\xea\xb3\x95', 1100: b'\xea\xb3\x97', 1101: b'\xea\xb3\xa0', 1102: b'\xea\xb3\xa1', 1103: b'\xea\xb3\xa4', \
1104: b'\xea\xb3\xa7', 1105: b'\xea\xb3\xa8', 1106: b'\xea\xb3\xaa', 1107: b'\xea\xb3\xac', 1108: b'\xea\xb3\xaf', 1109: b'\xea\xb3\xb0', 1110: b'\xea\xb3\xb1', 1111: b'\xea\xb3\xb3', 1112: b'\xea\xb3\xb5', 1113: b'\xea\xb3\xb6', 1114: b'\xea\xb3\xbc', 1115: b'\xea\xb3\xbd', 1116: b'\xea\xb4\x80', \
1117: b'\xea\xb4\x84', 1118: b'\xea\xb4\x86', 1119: b'\xea\xb4\x8c', 1120: b'\xea\xb4\x8d', 1121: b'\xea\xb4\x8f', 1122: b'\xea\xb4\x91', 1123: b'\xea\xb4\x98', 1124: b'\xea\xb4\x9c', 1125: b'\xea\xb4\xa0', 1126: b'\xea\xb4\xa9', 1127: b'\xea\xb4\xac', 1128: b'\xea\xb4\xad', 1129: b'\xea\xb4\xb4', \
1130: b'\xea\xb4\xb5', 1131: b'\xea\xb4\xb8', 1132: b'\xea\xb4\xbc', 1133: b'\xea\xb5\x84', 1134: b'\xea\xb5\x85', 1135: b'\xea\xb5\x87', 1136: b'\xea\xb5\x89', 1137: b'\xea\xb5\x90', 1138: b'\xea\xb5\x94', 1139: b'\xea\xb5\x98', 1140: b'\xea\xb5\xa1', 1141: b'\xea\xb5\xa3', 1142: b'\xea\xb5\xac', \
1143: b'\xea\xb5\xad', 1144: b'\xea\xb5\xb0', 1145: b'\xea\xb5\xb3', 1146: b'\xea\xb5\xb4', 1147: b'\xea\xb5\xb5', 1148: b'\xea\xb5\xb6', 1149: b'\xea\xb5\xbb', 1150: b'\xea\xb5\xbc', 1151: b'\xea\xb5\xbd', 1152: b'\xea\xb5\xbf', 1153: b'\xea\xb6\x81', 1154: b'\xea\xb6\x82', 1155: b'\xea\xb6\x88', \
1156: b'\xea\xb6\x89', 1157: b'\xea\xb6\x8c', 1158: b'\xea\xb6\x90', 1159: b'\xea\xb6\x9c', 1160: b'\xea\xb6\x9d', 1161: b'\xea\xb6\xa4', 1162: b'\xea\xb6\xb7', 1163: b'\xea\xb7\x80', 1164: b'\xea\xb7\x81', 1165: b'\xea\xb7\x84', 1166: b'\xea\xb7\x88', 1167: b'\xea\xb7\x90', 1168: b'\xea\xb7\x91', \
1169: b'\xea\xb7\x93', 1170: b'\xea\xb7\x9c', 1171: b'\xea\xb7\xa0', 1172: b'\xea\xb7\xa4', 1173: b'\xea\xb7\xb8', 1174: b'\xea\xb7\xb9', 1175: b'\xea\xb7\xbc', 1176: b'\xea\xb7\xbf', 1177: b'\xea\xb8\x80', 1178: b'\xea\xb8\x81', 1179: b'\xea\xb8\x88', 1180: b'\xea\xb8\x89', 1181: b'\xea\xb8\x8b', \
1182: b'\xea\xb8\x8d', 1183: b'\xea\xb8\x94', 1184: b'\xea\xb8\xb0', 1185: b'\xea\xb8\xb1', 1186: b'\xea\xb8\xb4', 1187: b'\xea\xb8\xb7', 1188: b'\xea\xb8\xb8', 1189: b'\xea\xb8\xba', 1190: b'\xea\xb9\x80', 1191: b'\xea\xb9\x81', 1192: b'\xea\xb9\x83', 1193: b'\xea\xb9\x85', 1194: b'\xea\xb9\x86', \
1195: b'\xea\xb9\x8a', 1196: b'\xea\xb9\x8c', 1197: b'\xea\xb9\x8d', 1198: b'\xea\xb9\x8e', 1199: b'\xea\xb9\x90', 1200: b'\xea\xb9\x94', 1201: b'\xea\xb9\x96', 1202: b'\xea\xb9\x9c', 1203: b'\xea\xb9\x9d', 1204: b'\xea\xb9\x9f', 1205: b'\xea\xb9\xa0', 1206: b'\xea\xb9\xa1', 1207: b'\xea\xb9\xa5', \
1208: b'\xea\xb9\xa8', 1209: b'\xea\xb9\xa9', 1210: b'\xea\xb9\xac', 1211: b'\xea\xb9\xb0', 1212: b'\xea\xb9\xb8', 1213: b'\xea\xb9\xb9', 1214: b'\xea\xb9\xbb', 1215: b'\xea\xb9\xbc', 1216: b'\xea\xb9\xbd', 1217: b'\xea\xba\x84', 1218: b'\xea\xba\x85', 1219: b'\xea\xba\x8c', 1220: b'\xea\xba\xbc', \
1221: b'\xea\xba\xbd', 1222: b'\xea\xba\xbe', 1223: b'\xea\xbb\x80', 1224: b'\xea\xbb\x84', 1225: b'\xea\xbb\x8c', 1226: b'\xea\xbb\x8d', 1227: b'\xea\xbb\x8f', 1228: b'\xea\xbb\x90', 1229: b'\xea\xbb\x91', 1230: b'\xea\xbb\x98', 1231: b'\xea\xbb\x99', 1232: b'\xea\xbb\x9c', 1233: b'\xea\xbb\xa8', \
1234: b'\xea\xbb\xab', 1235: b'\xea\xbb\xad', 1236: b'\xea\xbb\xb4', 1237: b'\xea\xbb\xb8', 1238: b'\xea\xbb\xbc', 1239: b'\xea\xbc\x87', 1240: b'\xea\xbc\x88', 1241: b'\xea\xbc\x8d', 1242: b'\xea\xbc\x90', 1243: b'\xea\xbc\xac', 1244: b'\xea\xbc\xad', 1245: b'\xea\xbc\xb0', 1246: b'\xea\xbc\xb2', \
1247: b'\xea\xbc\xb4', 1248: b'\xea\xbc\xbc', 1249: b'\xea\xbc\xbd', 1250: b'\xea\xbc\xbf', 1251: b'\xea\xbd\x81', 1252: b'\xea\xbd\x82', 1253: b'\xea\xbd\x83', 1254: b'\xea\xbd\x88', 1255: b'\xea\xbd\x89', 1256: b'\xea\xbd\x90', 1257: b'\xea\xbd\x9c', 1258: b'\xea\xbd\x9d', 1259: b'\xea\xbd\xa4', \
1260: b'\xea\xbd\xa5', 1261: b'\xea\xbd\xb9', 1262: b'\xea\xbe\x80', 1263: b'\xea\xbe\x84', 1264: b'\xea\xbe\x88', 1265: b'\xea\xbe\x90', 1266: b'\xea\xbe\x91', 1267: b'\xea\xbe\x95', 1268: b'\xea\xbe\x9c', 1269: b'\xea\xbe\xb8', 1270: b'\xea\xbe\xb9', 1271: b'\xea\xbe\xbc', 1272: b'\xea\xbf\x80', \
1273: b'\xea\xbf\x87', 1274: b'\xea\xbf\x88', 1275: b'\xea\xbf\x89', 1276: b'\xea\xbf\x8b', 1277: b'\xea\xbf\x8d', 1278: b'\xea\xbf\x8e', 1279: b'\xea\xbf\x94', 1280: b'\xea\xbf\x9c', 1281: b'\xea\xbf\xa8', 1282: b'\xea\xbf\xa9', 1283: b'\xea\xbf\xb0', 1284: b'\xea\xbf\xb1', 1285: b'\xea\xbf\xb4', \
1286: b'\xea\xbf\xb8', 1287: b'\xeb\x80\x80', 1288: b'\xeb\x80\x81', 1289: b'\xeb\x80\x84', 1290: b'\xeb\x80\x8c', 1291: b'\xeb\x80\x90', 1292: b'\xeb\x80\x94', 1293: b'\xeb\x80\x9c', 1294: b'\xeb\x80\x9d', 1295: b'\xeb\x80\xa8', 1296: b'\xeb\x81\x84', 1297: b'\xeb\x81\x85', 1298: b'\xeb\x81\x88', \
1299: b'\xeb\x81\x8a', 1300: b'\xeb\x81\x8c', 1301: b'\xeb\x81\x8e', 1302: b'\xeb\x81\x93', 1303: b'\xeb\x81\x94', 1304: b'\xeb\x81\x95', 1305: b'\xeb\x81\x97', 1306: b'\xeb\x81\x99', 1307: b'\xeb\x81\x9d', 1308: b'\xeb\x81\xbc', 1309: b'\xeb\x81\xbd', 1310: b'\xeb\x82\x80', 1311: b'\xeb\x82\x84', \
1312: b'\xeb\x82\x8c', 1313: b'\xeb\x82\x8d', 1314: b'\xeb\x82\x8f', 1315: b'\xeb\x82\x91', 1316: b'\xeb\x82\x98', 1317: b'\xeb\x82\x99', 1318: b'\xeb\x82\x9a', 1319: b'\xeb\x82\x9c', 1320: b'\xeb\x82\x9f', 1321: b'\xeb\x82\xa0', 1322: b'\xeb\x82\xa1', 1323: b'\xeb\x82\xa2', 1324: b'\xeb\x82\xa8', \
1325: b'\xeb\x82\xa9', 1326: b'\xeb\x82\xab', 1327: b'\xeb\x82\xac', 1328: b'\xeb\x82\xad', 1329: b'\xeb\x82\xae', 1330: b'\xeb\x82\xaf', 1331: b'\xeb\x82\xb1', 1332: b'\xeb\x82\xb3', 1333: b'\xeb\x82\xb4', 1334: b'\xeb\x82\xb5', 1335: b'\xeb\x82\xb8', 1336: b'\xeb\x82\xbc', 1337: b'\xeb\x83\x84', \
1338: b'\xeb\x83\x85', 1339: b'\xeb\x83\x87', 1340: b'\xeb\x83\x88', 1341: b'\xeb\x83\x89', 1342: b'\xeb\x83\x90', 1343: b'\xeb\x83\x91', 1344: b'\xeb\x83\x94', 1345: b'\xeb\x83\x98', 1346: b'\xeb\x83\xa0', 1347: b'\xeb\x83\xa5', 1348: b'\xeb\x84\x88', 1349: b'\xeb\x84\x89', 1350: b'\xeb\x84\x8b', \
1351: b'\xeb\x84\x8c', 1352: b'\xeb\x84\x90', 1353: b'\xeb\x84\x92', 1354: b'\xeb\x84\x93', 1355: b'\xeb\x84\x98', 1356: b'\xeb\x84\x99', 1357: b'\xeb\x84\x9b', 1358: b'\xeb\x84\x9c', 1359: b'\xeb\x84\x9d', 1360: b'\xeb\x84\xa3', 1361: b'\xeb\x84\xa4', 1362: b'\xeb\x84\xa5', 1363: b'\xeb\x84\xa8', \
1364: b'\xeb\x84\xac', 1365: b'\xeb\x84\xb4', 1366: b'\xeb\x84\xb5', 1367: b'\xeb\x84\xb7', 1368: b'\xeb\x84\xb8', 1369: b'\xeb\x84\xb9', 1370: b'\xeb\x85\x80', 1371: b'\xeb\x85\x81', 1372: b'\xeb\x85\x84', 1373: b'\xeb\x85\x88', 1374: b'\xeb\x85\x90', 1375: b'\xeb\x85\x91', 1376: b'\xeb\x85\x94', \
1377: b'\xeb\x85\x95', 1378: b'\xeb\x85\x98', 1379: b'\xeb\x85\x9c', 1380: b'\xeb\x85\xa0', 1381: b'\xeb\x85\xb8', 1382: b'\xeb\x85\xb9', 1383: b'\xeb\x85\xbc', 1384: b'\xeb\x86\x80', 1385: b'\xeb\x86\x82', 1386: b'\xeb\x86\x88', 1387: b'\xeb\x86\x89', 1388: b'\xeb\x86\x8b', 1389: b'\xeb\x86\x8d', \
1390: b'\xeb\x86\x92', 1391: b'\xeb\x86\x93', 1392: b'\xeb\x86\x94', 1393: b'\xeb\x86\x98', 1394: b'\xeb\x86\x9c', 1395: b'\xeb\x86\xa8', 1396: b'\xeb\x87\x8c', 1397: b'\xeb\x87\x90', 1398: b'\xeb\x87\x94', 1399: b'\xeb\x87\x9c', 1400: b'\xeb\x87\x9d', 1401: b'\xeb\x87\x9f', 1402: b'\xeb\x87\xa8', \
1403: b'\xeb\x87\xa9', 1404: b'\xeb\x87\xac', 1405: b'\xeb\x87\xb0', 1406: b'\xeb\x87\xb9', 1407: b'\xeb\x87\xbb', 1408: b'\xeb\x87\xbd', 1409: b'\xeb\x88\x84', 1410: b'\xeb\x88\x85', 1411: b'\xeb\x88\x88', 1412: b'\xeb\x88\x8b', 1413: b'\xeb\x88\x8c', 1414: b'\xeb\x88\x94', 1415: b'\xeb\x88\x95', \
1416: b'\xeb\x88\x97', 1417: b'\xeb\x88\x99', 1418: b'\xeb\x88\xa0', 1419: b'\xeb\x88\xb4', 1420: b'\xeb\x88\xbc', 1421: b'\xeb\x89\x98', 1422: b'\xeb\x89\x9c', 1423: b'\xeb\x89\xa0', 1424: b'\xeb\x89\xa8', 1425: b'\xeb\x89\xa9', 1426: b'\xeb\x89\xb4', 1427: b'\xeb\x89\xb5', 1428: b'\xeb\x89\xbc', \
1429: b'\xeb\x8a\x84', 1430: b'\xeb\x8a\x85', 1431: b'\xeb\x8a\x89', 1432: b'\xeb\x8a\x90', 1433: b'\xeb\x8a\x91', 1434: b'\xeb\x8a\x94', 1435: b'\xeb\x8a\x98', 1436: b'\xeb\x8a\x99', 1437: b'\xeb\x8a\x9a', 1438: b'\xeb\x8a\xa0', 1439: b'\xeb\x8a\xa1', 1440: b'\xeb\x8a\xa3', 1441: b'\xeb\x8a\xa5', \
1442: b'\xeb\x8a\xa6', 1443: b'\xeb\x8a\xaa', 1444: b'\xeb\x8a\xac', 1445: b'\xeb\x8a\xb0', 1446: b'\xeb\x8a\xb4', 1447: b'\xeb\x8b\x88', 1448: b'\xeb\x8b\x89', 1449: b'\xeb\x8b\x8c', 1450: b'\xeb\x8b\x90', 1451: b'\xeb\x8b\x92', 1452: b'\xeb\x8b\x98', 1453: b'\xeb\x8b\x99', 1454: b'\xeb\x8b\x9b', \
1455: b'\xeb\x8b\x9d', 1456: b'\xeb\x8b\xa2', 1457: b'\xeb\x8b\xa4', 1458: b'\xeb\x8b\xa5', 1459: b'\xeb\x8b\xa6', 1460: b'\xeb\x8b\xa8', 1461: b'\xeb\x8b\xab', 1462: b'\xeb\x8b\xac', 1463: b'\xeb\x8b\xad', 1464: b'\xeb\x8b\xae', 1465: b'\xeb\x8b\xaf', 1466: b'\xeb\x8b\xb3', 1467: b'\xeb\x8b\xb4', \
1468: b'\xeb\x8b\xb5', 1469: b'\xeb\x8b\xb7', 1470: b'\xeb\x8b\xb8', 1471: b'\xeb\x8b\xb9', 1472: b'\xeb\x8b\xba', 1473: b'\xeb\x8b\xbb', 1474: b'\xeb\x8b\xbf', 1475: b'\xeb\x8c\x80', 1476: b'\xeb\x8c\x81', 1477: b'\xeb\x8c\x84', 1478: b'\xeb\x8c\x88', 1479: b'\xeb\x8c\x90', 1480: b'\xeb\x8c\x91', \
1481: b'\xeb\x8c\x93', 1482: b'\xeb\x8c\x94', 1483: b'\xeb\x8c\x95', 1484: b'\xeb\x8c\x9c', 1485: b'\xeb\x8d\x94', 1486: b'\xeb\x8d\x95', 1487: b'\xeb\x8d\x96', 1488: b'\xeb\x8d\x98', 1489: b'\xeb\x8d\x9b', 1490: b'\xeb\x8d\x9c', 1491: b'\xeb\x8d\x9e', 1492: b'\xeb\x8d\x9f', 1493: b'\xeb\x8d\xa4', \
1494: b'\xeb\x8d\xa5', 1495: b'\xeb\x8d\xa7', 1496: b'\xeb\x8d\xa9', 1497: b'\xeb\x8d\xab', 1498: b'\xeb\x8d\xae', 1499: b'\xeb\x8d\xb0', 1500: b'\xeb\x8d\xb1', 1501: b'\xeb\x8d\xb4', 1502: b'\xeb\x8d\xb8', 1503: b'\xeb\x8e\x80', 1504: b'\xeb\x8e\x81', 1505: b'\xeb\x8e\x83', 1506: b'\xeb\x8e\x84', \
1507: b'\xeb\x8e\x85', 1508: b'\xeb\x8e\x8c', 1509: b'\xeb\x8e\x90', 1510: b'\xeb\x8e\x94', 1511: b'\xeb\x8e\xa0', 1512: b'\xeb\x8e\xa1', 1513: b'\xeb\x8e\xa8', 1514: b'\xeb\x8e\xac', 1515: b'\xeb\x8f\x84', 1516: b'\xeb\x8f\x85', 1517: b'\xeb\x8f\x88', 1518: b'\xeb\x8f\x8b', 1519: b'\xeb\x8f\x8c', \
1520: b'\xeb\x8f\x8e', 1521: b'\xeb\x8f\x90', 1522: b'\xeb\x8f\x94', 1523: b'\xeb\x8f\x95', 1524: b'\xeb\x8f\x97', 1525: b'\xeb\x8f\x99', 1526: b'\xeb\x8f\x9b', 1527: b'\xeb\x8f\x9d', 1528: b'\xeb\x8f\xa0', 1529: b'\xeb\x8f\xa4', 1530: b'\xeb\x8f\xa8', 1531: b'\xeb\x8f\xbc', 1532: b'\xeb\x90\x90', \
1533: b'\xeb\x90\x98', 1534: b'\xeb\x90\x9c', 1535: b'\xeb\x90\xa0', 1536: b'\xeb\x90\xa8', 1537: b'\xeb\x90\xa9', 1538: b'\xeb\x90\xab', 1539: b'\xeb\x90\xb4', 1540: b'\xeb\x91\x90', 1541: b'\xeb\x91\x91', 1542: b'\xeb\x91\x94', 1543: b'\xeb\x91\x98', 1544: b'\xeb\x91\xa0', 1545: b'\xeb\x91\xa1', \
1546: b'\xeb\x91\xa3', 1547: b'\xeb\x91\xa5', 1548: b'\xeb\x91\xac', 1549: b'\xeb\x92\x80', 1550: b'\xeb\x92\x88', 1551: b'\xeb\x92\x9d', 1552: b'\xeb\x92\xa4', 1553: b'\xeb\x92\xa8', 1554: b'\xeb\x92\xac', 1555: b'\xeb\x92\xb5', 1556: b'\xeb\x92\xb7', 1557: b'\xeb\x92\xb9', 1558: b'\xeb\x93\x80', \
1559: b'\xeb\x93\x84', 1560: b'\xeb\x93\x88', 1561: b'\xeb\x93\x90', 1562: b'\xeb\x93\x95', 1563: b'\xeb\x93\x9c', 1564: b'\xeb\x93\x9d', 1565: b'\xeb\x93\xa0', 1566: b'\xeb\x93\xa3', 1567: b'\xeb\x93\xa4', 1568: b'\xeb\x93\xa6', 1569: b'\xeb\x93\xac', 1570: b'\xeb\x93\xad', 1571: b'\xeb\x93\xaf', \
1572: b'\xeb\x93\xb1', 1573: b'\xeb\x93\xb8', 1574: b'\xeb\x94\x94', 1575: b'\xeb\x94\x95', 1576: b'\xeb\x94\x98', 1577: b'\xeb\x94\x9b', 1578: b'\xeb\x94\x9c', 1579: b'\xeb\x94\xa4', 1580: b'\xeb\x94\xa5', 1581: b'\xeb\x94\xa7', 1582: b'\xeb\x94\xa8', 1583: b'\xeb\x94\xa9', 1584: b'\xeb\x94\xaa', \
1585: b'\xeb\x94\xb0', 1586: b'\xeb\x94\xb1', 1587: b'\xeb\x94\xb4', 1588: b'\xeb\x94\xb8', 1589: b'\xeb\x95\x80', 1590: b'\xeb\x95\x81', 1591: b'\xeb\x95\x83', 1592: b'\xeb\x95\x84', 1593: b'\xeb\x95\x85', 1594: b'\xeb\x95\x8b', 1595: b'\xeb\x95\x8c', 1596: b'\xeb\x95\x8d', 1597: b'\xeb\x95\x90', \
1598: b'\xeb\x95\x94', 1599: b'\xeb\x95\x9c', 1600: b'\xeb\x95\x9d', 1601: b'\xeb\x95\x9f', 1602: b'\xeb\x95\xa0', 1603: b'\xeb\x95\xa1', 1604: b'\xeb\x96\xa0', 1605: b'\xeb\x96\xa1', 1606: b'\xeb\x96\xa4', 1607: b'\xeb\x96\xa8', 1608: b'\xeb\x96\xaa', 1609: b'\xeb\x96\xab', 1610: b'\xeb\x96\xb0', \
1611: b'\xeb\x96\xb1', 1612: b'\xeb\x96\xb3', 1613: b'\xeb\x96\xb4', 1614: b'\xeb\x96\xb5', 1615: b'\xeb\x96\xbb', 1616: b'\xeb\x96\xbc', 1617: b'\xeb\x96\xbd', 1618: b'\xeb\x97\x80', 1619: b'\xeb\x97\x84', 1620: b'\xeb\x97\x8c', 1621: b'\xeb\x97\x8d', 1622: b'\xeb\x97\x8f', 1623: b'\xeb\x97\x90', \
1624: b'\xeb\x97\x91', 1625: b'\xeb\x97\x98', 1626: b'\xeb\x97\xac', 1627: b'\xeb\x98\x90', 1628: b'\xeb\x98\x91', 1629: b'\xeb\x98\x94', 1630: b'\xeb\x98\x98', 1631: b'\xeb\x98\xa5', 1632: b'\xeb\x98\xac', 1633: b'\xeb\x98\xb4', 1634: b'\xeb\x99\x88', 1635: b'\xeb\x99\xa4', 1636: b'\xeb\x99\xa8', \
1637: b'\xeb\x9a\x9c', 1638: b'\xeb\x9a\x9d', 1639: b'\xeb\x9a\xa0', 1640: b'\xeb\x9a\xa4', 1641: b'\xeb\x9a\xab', 1642: b'\xeb\x9a\xac', 1643: b'\xeb\x9a\xb1', 1644: b'\xeb\x9b\x94', 1645: b'\xeb\x9b\xb0', 1646: b'\xeb\x9b\xb4', 1647: b'\xeb\x9b\xb8', 1648: b'\xeb\x9c\x80', 1649: b'\xeb\x9c\x81', \
1650: b'\xeb\x9c\x85', 1651: b'\xeb\x9c\xa8', 1652: b'\xeb\x9c\xa9', 1653: b'\xeb\x9c\xac', 1654: b'\xeb\x9c\xaf', 1655: b'\xeb\x9c\xb0', 1656: b'\xeb\x9c\xb8', 1657: b'\xeb\x9c\xb9', 1658: b'\xeb\x9c\xbb', 1659: b'\xeb\x9d\x84', 1660: b'\xeb\x9d\x88', 1661: b'\xeb\x9d\x8c', 1662: b'\xeb\x9d\x94', \
1663: b'\xeb\x9d\x95', 1664: b'\xeb\x9d\xa0', 1665: b'\xeb\x9d\xa4', 1666: b'\xeb\x9d\xa8', 1667: b'\xeb\x9d\xb0', 1668: b'\xeb\x9d\xb1', 1669: b'\xeb\x9d\xb3', 1670: b'\xeb\x9d\xb5', 1671: b'\xeb\x9d\xbc', 1672: b'\xeb\x9d\xbd', 1673: b'\xeb\x9e\x80', 1674: b'\xeb\x9e\x84', 1675: b'\xeb\x9e\x8c', \
1676: b'\xeb\x9e\x8d', 1677: b'\xeb\x9e\x8f', 1678: b'\xeb\x9e\x90', 1679: b'\xeb\x9e\x91', 1680: b'\xeb\x9e\x92', 1681: b'\xeb\x9e\x96', 1682: b'\xeb\x9e\x97', 1683: b'\xeb\x9e\x98', 1684: b'\xeb\x9e\x99', 1685: b'\xeb\x9e\x9c', 1686: b'\xeb\x9e\xa0', 1687: b'\xeb\x9e\xa8', 1688: b'\xeb\x9e\xa9', \
1689: b'\xeb\x9e\xab', 1690: b'\xeb\x9e\xac', 1691: b'\xeb\x9e\xad', 1692: b'\xeb\x9e\xb4', 1693: b'\xeb\x9e\xb5', 1694: b'\xeb\x9e\xb8', 1695: b'\xeb\x9f\x87', 1696: b'\xeb\x9f\x89', 1697: b'\xeb\x9f\xac', 1698: b'\xeb\x9f\xad', 1699: b'\xeb\x9f\xb0', 1700: b'\xeb\x9f\xb4', 1701: b'\xeb\x9f\xbc', \
1702: b'\xeb\x9f\xbd', 1703: b'\xeb\x9f\xbf', 1704: b'\xeb\xa0\x80', 1705: b'\xeb\xa0\x81', 1706: b'\xeb\xa0\x87', 1707: b'\xeb\xa0\x88', 1708: b'\xeb\xa0\x89', 1709: b'\xeb\xa0\x8c', 1710: b'\xeb\xa0\x90', 1711: b'\xeb\xa0\x98', 1712: b'\xeb\xa0\x99', 1713: b'\xeb\xa0\x9b', 1714: b'\xeb\xa0\x9d', \
1715: b'\xeb\xa0\xa4', 1716: b'\xeb\xa0\xa5', 1717: b'\xeb\xa0\xa8', 1718: b'\xeb\xa0\xac', 1719: b'\xeb\xa0\xb4', 1720: b'\xeb\xa0\xb5', 1721: b'\xeb\xa0\xb7', 1722: b'\xeb\xa0\xb8', 1723: b'\xeb\xa0\xb9', 1724: b'\xeb\xa1\x80', 1725: b'\xeb\xa1\x84', 1726: b'\xeb\xa1\x91', 1727: b'\xeb\xa1\x93', \
1728: b'\xeb\xa1\x9c', 1729: b'\xeb\xa1\x9d', 1730: b'\xeb\xa1\xa0', 1731: b'\xeb\xa1\xa4', 1732: b'\xeb\xa1\xac', 1733: b'\xeb\xa1\xad', 1734: b'\xeb\xa1\xaf', 1735: b'\xeb\xa1\xb1', 1736: b'\xeb\xa1\xb8', 1737: b'\xeb\xa1\xbc', 1738: b'\xeb\xa2\x8d', 1739: b'\xeb\xa2\xa8', 1740: b'\xeb\xa2\xb0', \
1741: b'\xeb\xa2\xb4', 1742: b'\xeb\xa2\xb8', 1743: b'\xeb\xa3\x80', 1744: b'\xeb\xa3\x81', 1745: b'\xeb\xa3\x83', 1746: b'\xeb\xa3\x85', 1747: b'\xeb\xa3\x8c', 1748: b'\xeb\xa3\x90', 1749: b'\xeb\xa3\x94', 1750: b'\xeb\xa3\x9d', 1751: b'\xeb\xa3\x9f', 1752: b'\xeb\xa3\xa1', 1753: b'\xeb\xa3\xa8', \
1754: b'\xeb\xa3\xa9', 1755: b'\xeb\xa3\xac', 1756: b'\xeb\xa3\xb0', 1757: b'\xeb\xa3\xb8', 1758: b'\xeb\xa3\xb9', 1759: b'\xeb\xa3\xbb', 1760: b'\xeb\xa3\xbd', 1761: b'\xeb\xa4\x84', 1762: b'\xeb\xa4\x98', 1763: b'\xeb\xa4\xa0', 1764: b'\xeb\xa4\xbc', 1765: b'\xeb\xa4\xbd', 1766: b'\xeb\xa5\x80', \
1767: b'\xeb\xa5\x84', 1768: b'\xeb\xa5\x8c', 1769: b'\xeb\xa5\x8f', 1770: b'\xeb\xa5\x91', 1771: b'\xeb\xa5\x98', 1772: b'\xeb\xa5\x99', 1773: b'\xeb\xa5\x9c', 1774: b'\xeb\xa5\xa0', 1775: b'\xeb\xa5\xa8', 1776: b'\xeb\xa5\xa9', 1777: b'\xeb\xa5\xab', 1778: b'\xeb\xa5\xad', 1779: b'\xeb\xa5\xb4', \
1780: b'\xeb\xa5\xb5', 1781: b'\xeb\xa5\xb8', 1782: b'\xeb\xa5\xbc', 1783: b'\xeb\xa6\x84', 1784: b'\xeb\xa6\x85', 1785: b'\xeb\xa6\x87', 1786: b'\xeb\xa6\x89', 1787: b'\xeb\xa6\x8a', 1788: b'\xeb\xa6\x8d', 1789: b'\xeb\xa6\x8e', 1790: b'\xeb\xa6\xac', 1791: b'\xeb\xa6\xad', 1792: b'\xeb\xa6\xb0', \
1793: b'\xeb\xa6\xb4', 1794: b'\xeb\xa6\xbc', 1795: b'\xeb\xa6\xbd', 1796: b'\xeb\xa6\xbf', 1797: b'\xeb\xa7\x81', 1798: b'\xeb\xa7\x88', 1799: b'\xeb\xa7\x89', 1800: b'\xeb\xa7\x8c', 1801: b'\xeb\xa7\x8e', 1802: b'\xeb\xa7\x8f', 1803: b'\xeb\xa7\x90', 1804: b'\xeb\xa7\x91', 1805: b'\xeb\xa7\x92', \
1806: b'\xeb\xa7\x98', 1807: b'\xeb\xa7\x99', 1808: b'\xeb\xa7\x9b', 1809: b'\xeb\xa7\x9d', 1810: b'\xeb\xa7\x9e', 1811: b'\xeb\xa7\xa1', 1812: b'\xeb\xa7\xa3', 1813: b'\xeb\xa7\xa4', 1814: b'\xeb\xa7\xa5', 1815: b'\xeb\xa7\xa8', 1816: b'\xeb\xa7\xac', 1817: b'\xeb\xa7\xb4', 1818: b'\xeb\xa7\xb5', \
1819: b'\xeb\xa7\xb7', 1820: b'\xeb\xa7\xb8', 1821: b'\xeb\xa7\xb9', 1822: b'\xeb\xa7\xba', 1823: b'\xeb\xa8\x80', 1824: b'\xeb\xa8\x81', 1825: b'\xeb\xa8\x88', 1826: b'\xeb\xa8\x95', 1827: b'\xeb\xa8\xb8', 1828: b'\xeb\xa8\xb9', 1829: b'\xeb\xa8\xbc', 1830: b'\xeb\xa9\x80', 1831: b'\xeb\xa9\x82', \
1832: b'\xeb\xa9\x88', 1833: b'\xeb\xa9\x89', 1834: b'\xeb\xa9\x8b', 1835: b'\xeb\xa9\x8d', 1836: b'\xeb\xa9\x8e', 1837: b'\xeb\xa9\x93', 1838: b'\xeb\xa9\x94', 1839: b'\xeb\xa9\x95', 1840: b'\xeb\xa9\x98', 1841: b'\xeb\xa9\x9c', 1842: b'\xeb\xa9\xa4', 1843: b'\xeb\xa9\xa5', 1844: b'\xeb\xa9\xa7', \
1845: b'\xeb\xa9\xa8', 1846: b'\xeb\xa9\xa9', 1847: b'\xeb\xa9\xb0', 1848: b'\xeb\xa9\xb1', 1849: b'\xeb\xa9\xb4', 1850: b'\xeb\xa9\xb8', 1851: b'\xeb\xaa\x83', 1852: b'\xeb\xaa\x84', 1853: b'\xeb\xaa\x85', 1854: b'\xeb\xaa\x87', 1855: b'\xeb\xaa\x8c', 1856: b'\xeb\xaa\xa8', 1857: b'\xeb\xaa\xa9', \
1858: b'\xeb\xaa\xab', 1859: b'\xeb\xaa\xac', 1860: b'\xeb\xaa\xb0', 1861: b'\xeb\xaa\xb2', 1862: b'\xeb\xaa\xb8', 1863: b'\xeb\xaa\xb9', 1864: b'\xeb\xaa\xbb', 1865: b'\xeb\xaa\xbd', 1866: b'\xeb\xab\x84', 1867: b'\xeb\xab\x88', 1868: b'\xeb\xab\x98', 1869: b'\xeb\xab\x99', 1870: b'\xeb\xab\xbc', \
1871: b'\xeb\xac\x80', 1872: b'\xeb\xac\x84', 1873: b'\xeb\xac\x8d', 1874: b'\xeb\xac\x8f', 1875: b'\xeb\xac\x91', 1876: b'\xeb\xac\x98', 1877: b'\xeb\xac\x9c', 1878: b'\xeb\xac\xa0', 1879: b'\xeb\xac\xa9', 1880: b'\xeb\xac\xab', 1881: b'\xeb\xac\xb4', 1882: b'\xeb\xac\xb5', 1883: b'\xeb\xac\xb6', \
1884: b'\xeb\xac\xb8', 1885: b'\xeb\xac\xbb', 1886: b'\xeb\xac\xbc', 1887: b'\xeb\xac\xbd', 1888: b'\xeb\xac\xbe', 1889: b'\xeb\xad\x84', 1890: b'\xeb\xad\x85', 1891: b'\xeb\xad\x87', 1892: b'\xeb\xad\x89', 1893: b'\xeb\xad\x8d', 1894: b'\xeb\xad\x8f', 1895: b'\xeb\xad\x90', 1896: b'\xeb\xad\x94', \
1897: b'\xeb\xad\x98', 1898: b'\xeb\xad\xa1', 1899: b'\xeb\xad\xa3', 1900: b'\xeb\xad\xac', 1901: b'\xeb\xae\x88', 1902: b'\xeb\xae\x8c', 1903: b'\xeb\xae\x90', 1904: b'\xeb\xae\xa4', 1905: b'\xeb\xae\xa8', 1906: b'\xeb\xae\xac', 1907: b'\xeb\xae\xb4', 1908: b'\xeb\xae\xb7', 1909: b'\xeb\xaf\x80', \
1910: b'\xeb\xaf\x84', 1911: b'\xeb\xaf\x88', 1912: b'\xeb\xaf\x90', 1913: b'\xeb\xaf\x93', 1914: b'\xeb\xaf\xb8', 1915: b'\xeb\xaf\xb9', 1916: b'\xeb\xaf\xbc', 1917: b'\xeb\xaf\xbf', 1918: b'\xeb\xb0\x80', 1919: b'\xeb\xb0\x82', 1920: b'\xeb\xb0\x88', 1921: b'\xeb\xb0\x89', 1922: b'\xeb\xb0\x8b', \
1923: b'\xeb\xb0\x8c', 1924: b'\xeb\xb0\x8d', 1925: b'\xeb\xb0\x8f', 1926: b'\xeb\xb0\x91', 1927: b'\xeb\xb0\x94', 1928: b'\xeb\xb0\x95', 1929: b'\xeb\xb0\x96', 1930: b'\xeb\xb0\x97', 1931: b'\xeb\xb0\x98', 1932: b'\xeb\xb0\x9b', 1933: b'\xeb\xb0\x9c', 1934: b'\xeb\xb0\x9d', 1935: b'\xeb\xb0\x9e', \
1936: b'\xeb\xb0\x9f', 1937: b'\xeb\xb0\xa4', 1938: b'\xeb\xb0\xa5', 1939: b'\xeb\xb0\xa7', 1940: b'\xeb\xb0\xa9', 1941: b'\xeb\xb0\xad', 1942: b'\xeb\xb0\xb0', 1943: b'\xeb\xb0\xb1', 1944: b'\xeb\xb0\xb4', 1945: b'\xeb\xb0\xb8', 1946: b'\xeb\xb1\x80', 1947: b'\xeb\xb1\x81', 1948: b'\xeb\xb1\x83', \
1949: b'\xeb\xb1\x84', 1950: b'\xeb\xb1\x85', 1951: b'\xeb\xb1\x89', 1952: b'\xeb\xb1\x8c', 1953: b'\xeb\xb1\x8d', 1954: b'\xeb\xb1\x90', 1955: b'\xeb\xb1\x9d', 1956: b'\xeb\xb2\x84', 1957: b'\xeb\xb2\x85', 1958: b'\xeb\xb2\x88', 1959: b'\xeb\xb2\x8b', 1960: b'\xeb\xb2\x8c', 1961: b'\xeb\xb2\x8e', \
1962: b'\xeb\xb2\x94', 1963: b'\xeb\xb2\x95', 1964: b'\xeb\xb2\x97', 1965: b'\xeb\xb2\x99', 1966: b'\xeb\xb2\x9a', 1967: b'\xeb\xb2\xa0', 1968: b'\xeb\xb2\xa1', 1969: b'\xeb\xb2\xa4', 1970: b'\xeb\xb2\xa7', 1971: b'\xeb\xb2\xa8', 1972: b'\xeb\xb2\xb0', 1973: b'\xeb\xb2\xb1', 1974: b'\xeb\xb2\xb3', \
1975: b'\xeb\xb2\xb4', 1976: b'\xeb\xb2\xb5', 1977: b'\xeb\xb2\xbc', 1978: b'\xeb\xb2\xbd', 1979: b'\xeb\xb3\x80', 1980: b'\xeb\xb3\x84', 1981: b'\xeb\xb3\x8d', 1982: b'\xeb\xb3\x8f', 1983: b'\xeb\xb3\x90', 1984: b'\xeb\xb3\x91', 1985: b'\xeb\xb3\x95', 1986: b'\xeb\xb3\x98', 1987: b'\xeb\xb3\x9c', \
1988: b'\xeb\xb3\xb4', 1989: b'\xeb\xb3\xb5', 1990: b'\xeb\xb3\xb6', 1991: b'\xeb\xb3\xb8', 1992: b'\xeb\xb3\xbc', 1993: b'\xeb\xb4\x84', 1994: b'\xeb\xb4\x85', 1995: b'\xeb\xb4\x87', 1996: b'\xeb\xb4\x89', 1997: b'\xeb\xb4\x90', 1998: b'\xeb\xb4\x94', 1999: b'\xeb\xb4\xa4', 2000: b'\xeb\xb4\xac', \
2001: b'\xeb\xb5\x80', 2002: b'\xeb\xb5\x88', 2003: b'\xeb\xb5\x89', 2004: b'\xeb\xb5\x8c', 2005: b'\xeb\xb5\x90', 2006: b'\xeb\xb5\x98', 2007: b'\xeb\xb5\x99', 2008: b'\xeb\xb5\xa4', 2009: b'\xeb\xb5\xa8', 2010: b'\xeb\xb6\x80', 2011: b'\xeb\xb6\x81', 2012: b'\xeb\xb6\x84', 2013: b'\xeb\xb6\x87', \
2014: b'\xeb\xb6\x88', 2015: b'\xeb\xb6\x89', 2016: b'\xeb\xb6\x8a', 2017: b'\xeb\xb6\x90', 2018: b'\xeb\xb6\x91', 2019: b'\xeb\xb6\x93', 2020: b'\xeb\xb6\x95', 2021: b'\xeb\xb6\x99', 2022: b'\xeb\xb6\x9a', 2023: b'\xeb\xb6\x9c', 2024: b'\xeb\xb6\xa4', 2025: b'\xeb\xb6\xb0', 2026: b'\xeb\xb6\xb8', \
2027: b'\xeb\xb7\x94', 2028: b'\xeb\xb7\x95', 2029: b'\xeb\xb7\x98', 2030: b'\xeb\xb7\x9c', 2031: b'\xeb\xb7\xa9', 2032: b'\xeb\xb7\xb0', 2033: b'\xeb\xb7\xb4', 2034: b'\xeb\xb7\xb8', 2035: b'\xeb\xb8\x80', 2036: b'\xeb\xb8\x83', 2037: b'\xeb\xb8\x85', 2038: b'\xeb\xb8\x8c', 2039: b'\xeb\xb8\x8d', \
2040: b'\xeb\xb8\x90', 2041: b'\xeb\xb8\x94', 2042: b'\xeb\xb8\x9c', 2043: b'\xeb\xb8\x9d', 2044: b'\xeb\xb8\x9f', 2045: b'\xeb\xb9\x84', 2046: b'\xeb\xb9\x85', 2047: b'\xeb\xb9\x88', 2048: b'\xeb\xb9\x8c', 2049: b'\xeb\xb9\x8e', 2050: b'\xeb\xb9\x94', 2051: b'\xeb\xb9\x95', 2052: b'\xeb\xb9\x97', \
2053: b'\xeb\xb9\x99', 2054: b'\xeb\xb9\x9a', 2055: b'\xeb\xb9\x9b', 2056: b'\xeb\xb9\xa0', 2057: b'\xeb\xb9\xa1', 2058: b'\xeb\xb9\xa4', 2059: b'\xeb\xb9\xa8', 2060: b'\xeb\xb9\xaa', 2061: b'\xeb\xb9\xb0', 2062: b'\xeb\xb9\xb1', 2063: b'\xeb\xb9\xb3', 2064: b'\xeb\xb9\xb4', 2065: b'\xeb\xb9\xb5', \
2066: b'\xeb\xb9\xbb', 2067: b'\xeb\xb9\xbc', 2068: b'\xeb\xb9\xbd', 2069: b'\xeb\xba\x80', 2070: b'\xeb\xba\x84', 2071: b'\xeb\xba\x8c', 2072: b'\xeb\xba\x8d', 2073: b'\xeb\xba\x8f', 2074: b'\xeb\xba\x90', 2075: b'\xeb\xba\x91', 2076: b'\xeb\xba\x98', 2077: b'\xeb\xba\x99', 2078: b'\xeb\xba\xa8', \
2079: b'\xeb\xbb\x90', 2080: b'\xeb\xbb\x91', 2081: b'\xeb\xbb\x94', 2082: b'\xeb\xbb\x97', 2083: b'\xeb\xbb\x98', 2084: b'\xeb\xbb\xa0', 2085: b'\xeb\xbb\xa3', 2086: b'\xeb\xbb\xa4', 2087: b'\xeb\xbb\xa5', 2088: b'\xeb\xbb\xac', 2089: b'\xeb\xbc\x81', 2090: b'\xeb\xbc\x88', 2091: b'\xeb\xbc\x89', \
2092: b'\xeb\xbc\x98', 2093: b'\xeb\xbc\x99', 2094: b'\xeb\xbc\x9b', 2095: b'\xeb\xbc\x9c', 2096: b'\xeb\xbc\x9d', 2097: b'\xeb\xbd\x80', 2098: b'\xeb\xbd\x81', 2099: b'\xeb\xbd\x84', 2100: b'\xeb\xbd\x88', 2101: b'\xeb\xbd\x90', 2102: b'\xeb\xbd\x91', 2103: b'\xeb\xbd\x95', 2104: b'\xeb\xbe\x94', \
2105: b'\xeb\xbe\xb0', 2106: b'\xeb\xbf\x85', 2107: b'\xeb\xbf\x8c', 2108: b'\xeb\xbf\x8d', 2109: b'\xeb\xbf\x90', 2110: b'\xeb\xbf\x94', 2111: b'\xeb\xbf\x9c', 2112: b'\xeb\xbf\x9f', 2113: b'\xeb\xbf\xa1', 2114: b'\xec\x80\xbc', 2115: b'\xec\x81\x91', 2116: b'\xec\x81\x98', 2117: b'\xec\x81\x9c', \
2118: b'\xec\x81\xa0', 2119: b'\xec\x81\xa8', 2120: b'\xec\x81\xa9', 2121: b'\xec\x82\x90', 2122: b'\xec\x82\x91', 2123: b'\xec\x82\x94', 2124: b'\xec\x82\x98', 2125: b'\xec\x82\xa0', 2126: b'\xec\x82\xa1', 2127: b'\xec\x82\xa3', 2128: b'\xec\x82\xa5', 2129: b'\xec\x82\xac', 2130: b'\xec\x82\xad', \
2131: b'\xec\x82\xaf', 2132: b'\xec\x82\xb0', 2133: b'\xec\x82\xb3', 2134: b'\xec\x82\xb4', 2135: b'\xec\x82\xb5', 2136: b'\xec\x82\xb6', 2137: b'\xec\x82\xbc', 2138: b'\xec\x82\xbd', 2139: b'\xec\x82\xbf', 2140: b'\xec\x83\x80', 2141: b'\xec\x83\x81', 2142: b'\xec\x83\x85', 2143: b'\xec\x83\x88', \
2144: b'\xec\x83\x89', 2145: b'\xec\x83\x8c', 2146: b'\xec\x83\x90', 2147: b'\xec\x83\x98', 2148: b'\xec\x83\x99', 2149: b'\xec\x83\x9b', 2150: b'\xec\x83\x9c', 2151: b'\xec\x83\x9d', 2152: b'\xec\x83\xa4', 2153: b'\xec\x83\xa5', 2154: b'\xec\x83\xa8', 2155: b'\xec\x83\xac', 2156: b'\xec\x83\xb4', \
2157: b'\xec\x83\xb5', 2158: b'\xec\x83\xb7', 2159: b'\xec\x83\xb9', 2160: b'\xec\x84\x80', 2161: b'\xec\x84\x84', 2162: b'\xec\x84\x88', 2163: b'\xec\x84\x90', 2164: b'\xec\x84\x95', 2165: b'\xec\x84\x9c', 2166: b'\xec\x84\x9d', 2167: b'\xec\x84\x9e', 2168: b'\xec\x84\x9f', 2169: b'\xec\x84\xa0', \
2170: b'\xec\x84\xa3', 2171: b'\xec\x84\xa4', 2172: b'\xec\x84\xa6', 2173: b'\xec\x84\xa7', 2174: b'\xec\x84\xac', 2175: b'\xec\x84\xad', 2176: b'\xec\x84\xaf', 2177: b'\xec\x84\xb0', 2178: b'\xec\x84\xb1', 2179: b'\xec\x84\xb6', 2180: b'\xec\x84\xb8', 2181: b'\xec\x84\xb9', 2182: b'\xec\x84\xbc', \
2183: b'\xec\x85\x80', 2184: b'\xec\x85\x88', 2185: b'\xec\x85\x89', 2186: b'\xec\x85\x8b', 2187: b'\xec\x85\x8c', 2188: b'\xec\x85\x8d', 2189: b'\xec\x85\x94', 2190: b'\xec\x85\x95', 2191: b'\xec\x85\x98', 2192: b'\xec\x85\x9c', 2193: b'\xec\x85\xa4', 2194: b'\xec\x85\xa5', 2195: b'\xec\x85\xa7', \
2196: b'\xec\x85\xa8', 2197: b'\xec\x85\xa9', 2198: b'\xec\x85\xb0', 2199: b'\xec\x85\xb4', 2200: b'\xec\x85\xb8', 2201: b'\xec\x86\x85', 2202: b'\xec\x86\x8c', 2203: b'\xec\x86\x8d', 2204: b'\xec\x86\x8e', 2205: b'\xec\x86\x90', 2206: b'\xec\x86\x94', 2207: b'\xec\x86\x96', 2208: b'\xec\x86\x9c', \
2209: b'\xec\x86\x9d', 2210: b'\xec\x86\x9f', 2211: b'\xec\x86\xa1', 2212: b'\xec\x86\xa5', 2213: b'\xec\x86\xa8', 2214: b'\xec\x86\xa9', 2215: b'\xec\x86\xac', 2216: b'\xec\x86\xb0', 2217: b'\xec\x86\xbd', 2218: b'\xec\x87\x84', 2219: b'\xec\x87\x88', 2220: b'\xec\x87\x8c', 2221: b'\xec\x87\x94', \
2222: b'\xec\x87\x97', 2223: b'\xec\x87\x98', 2224: b'\xec\x87\xa0', 2225: b'\xec\x87\xa4', 2226: b'\xec\x87\xa8', 2227: b'\xec\x87\xb0', 2228: b'\xec\x87\xb1', 2229: b'\xec\x87\xb3', 2230: b'\xec\x87\xbc', 2231: b'\xec\x87\xbd', 2232: b'\xec\x88\x80', 2233: b'\xec\x88\x84', 2234: b'\xec\x88\x8c', \
2235: b'\xec\x88\x8d', 2236: b'\xec\x88\x8f', 2237: b'\xec\x88\x91', 2238: b'\xec\x88\x98', 2239: b'\xec\x88\x99', 2240: b'\xec\x88\x9c', 2241: b'\xec\x88\x9f', 2242: b'\xec\x88\xa0', 2243: b'\xec\x88\xa8', 2244: b'\xec\x88\xa9', 2245: b'\xec\x88\xab', 2246: b'\xec\x88\xad', 2247: b'\xec\x88\xaf', \
2248: b'\xec\x88\xb1', 2249: b'\xec\x88\xb2', 2250: b'\xec\x88\xb4', 2251: b'\xec\x89\x88', 2252: b'\xec\x89\x90', 2253: b'\xec\x89\x91', 2254: b'\xec\x89\x94', 2255: b'\xec\x89\x98', 2256: b'\xec\x89\xa0', 2257: b'\xec\x89\xa5', 2258: b'\xec\x89\xac', 2259: b'\xec\x89\xad', 2260: b'\xec\x89\xb0', \
2261: b'\xec\x89\xb4', 2262: b'\xec\x89\xbc', 2263: b'\xec\x89\xbd', 2264: b'\xec\x89\xbf', 2265: b'\xec\x8a\x81', 2266: b'\xec\x8a\x88', 2267: b'\xec\x8a\x89', 2268: b'\xec\x8a\x90', 2269: b'\xec\x8a\x98', 2270: b'\xec\x8a\x9b', 2271: b'\xec\x8a\x9d', 2272: b'\xec\x8a\xa4', 2273: b'\xec\x8a\xa5', \
2274: b'\xec\x8a\xa8', 2275: b'\xec\x8a\xac', 2276: b'\xec\x8a\xad', 2277: b'\xec\x8a\xb4', 2278: b'\xec\x8a\xb5', 2279: b'\xec\x8a\xb7', 2280: b'\xec\x8a\xb9', 2281: b'\xec\x8b\x9c', 2282: b'\xec\x8b\x9d', 2283: b'\xec\x8b\xa0', 2284: b'\xec\x8b\xa3', 2285: b'\xec\x8b\xa4', 2286: b'\xec\x8b\xab', \
2287: b'\xec\x8b\xac', 2288: b'\xec\x8b\xad', 2289: b'\xec\x8b\xaf', 2290: b'\xec\x8b\xb1', 2291: b'\xec\x8b\xb6', 2292: b'\xec\x8b\xb8', 2293: b'\xec\x8b\xb9', 2294: b'\xec\x8b\xbb', 2295: b'\xec\x8b\xbc', 2296: b'\xec\x8c\x80', 2297: b'\xec\x8c\x88', 2298: b'\xec\x8c\x89', 2299: b'\xec\x8c\x8c', \
2300: b'\xec\x8c\x8d', 2301: b'\xec\x8c\x93', 2302: b'\xec\x8c\x94', 2303: b'\xec\x8c\x95', 2304: b'\xec\x8c\x98', 2305: b'\xec\x8c\x9c', 2306: b'\xec\x8c\xa4', 2307: b'\xec\x8c\xa5', 2308: b'\xec\x8c\xa8', 2309: b'\xec\x8c\xa9', 2310: b'\xec\x8d\x85', 2311: b'\xec\x8d\xa8', 2312: b'\xec\x8d\xa9', \
2313: b'\xec\x8d\xac', 2314: b'\xec\x8d\xb0', 2315: b'\xec\x8d\xb2', 2316: b'\xec\x8d\xb8', 2317: b'\xec\x8d\xb9', 2318: b'\xec\x8d\xbc', 2319: b'\xec\x8d\xbd', 2320: b'\xec\x8e\x84', 2321: b'\xec\x8e\x88', 2322: b'\xec\x8e\x8c', 2323: b'\xec\x8f\x80', 2324: b'\xec\x8f\x98', 2325: b'\xec\x8f\x99', \
2326: b'\xec\x8f\x9c', 2327: b'\xec\x8f\x9f', 2328: b'\xec\x8f\xa0', 2329: b'\xec\x8f\xa2', 2330: b'\xec\x8f\xa8', 2331: b'\xec\x8f\xa9', 2332: b'\xec\x8f\xad', 2333: b'\xec\x8f\xb4', 2334: b'\xec\x8f\xb5', 2335: b'\xec\x8f\xb8', 2336: b'\xec\x90\x88', 2337: b'\xec\x90\x90', 2338: b'\xec\x90\xa4', \
2339: b'\xec\x90\xac', 2340: b'\xec\x90\xb0', 2341: b'\xec\x90\xb4', 2342: b'\xec\x90\xbc', 2343: b'\xec\x90\xbd', 2344: b'\xec\x91\x88', 2345: b'\xec\x91\xa4', 2346: b'\xec\x91\xa5', 2347: b'\xec\x91\xa8', 2348: b'\xec\x91\xac', 2349: b'\xec\x91\xb4', 2350: b'\xec\x91\xb5', 2351: b'\xec\x91\xb9', \
2352: b'\xec\x92\x80', 2353: b'\xec\x92\x94', 2354: b'\xec\x92\x9c', 2355: b'\xec\x92\xb8', 2356: b'\xec\x92\xbc', 2357: b'\xec\x93\xa9', 2358: b'\xec\x93\xb0', 2359: b'\xec\x93\xb1', 2360: b'\xec\x93\xb4', 2361: b'\xec\x93\xb8', 2362: b'\xec\x93\xba', 2363: b'\xec\x93\xbf', 2364: b'\xec\x94\x80', \
2365: b'\xec\x94\x81', 2366: b'\xec\x94\x8c', 2367: b'\xec\x94\x90', 2368: b'\xec\x94\x94', 2369: b'\xec\x94\x9c', 2370: b'\xec\x94\xa8', 2371: b'\xec\x94\xa9', 2372: b'\xec\x94\xac', 2373: b'\xec\x94\xb0', 2374: b'\xec\x94\xb8', 2375: b'\xec\x94\xb9', 2376: b'\xec\x94\xbb', 2377: b'\xec\x94\xbd', \
2378: b'\xec\x95\x84', 2379: b'\xec\x95\x85', 2380: b'\xec\x95\x88', 2381: b'\xec\x95\x89', 2382: b'\xec\x95\x8a', 2383: b'\xec\x95\x8c', 2384: b'\xec\x95\x8d', 2385: b'\xec\x95\x8e', 2386: b'\xec\x95\x93', 2387: b'\xec\x95\x94', 2388: b'\xec\x95\x95', 2389: b'\xec\x95\x97', 2390: b'\xec\x95\x98', \
2391: b'\xec\x95\x99', 2392: b'\xec\x95\x9d', 2393: b'\xec\x95\x9e', 2394: b'\xec\x95\xa0', 2395: b'\xec\x95\xa1', 2396: b'\xec\x95\xa4', 2397: b'\xec\x95\xa8', 2398: b'\xec\x95\xb0', 2399: b'\xec\x95\xb1', 2400: b'\xec\x95\xb3', 2401: b'\xec\x95\xb4', 2402: b'\xec\x95\xb5', 2403: b'\xec\x95\xbc', \
2404: b'\xec\x95\xbd', 2405: b'\xec\x96\x80', 2406: b'\xec\x96\x84', 2407: b'\xec\x96\x87', 2408: b'\xec\x96\x8c', 2409: b'\xec\x96\x8d', 2410: b'\xec\x96\x8f', 2411: b'\xec\x96\x91', 2412: b'\xec\x96\x95', 2413: b'\xec\x96\x97', 2414: b'\xec\x96\x98', 2415: b'\xec\x96\x9c', 2416: b'\xec\x96\xa0', \
2417: b'\xec\x96\xa9', 2418: b'\xec\x96\xb4', 2419: b'\xec\x96\xb5', 2420: b'\xec\x96\xb8', 2421: b'\xec\x96\xb9', 2422: b'\xec\x96\xbb', 2423: b'\xec\x96\xbc', 2424: b'\xec\x96\xbd', 2425: b'\xec\x96\xbe', 2426: b'\xec\x97\x84', 2427: b'\xec\x97\x85', 2428: b'\xec\x97\x86', 2429: b'\xec\x97\x87', \
2430: b'\xec\x97\x88', 2431: b'\xec\x97\x89', 2432: b'\xec\x97\x8a', 2433: b'\xec\x97\x8c', 2434: b'\xec\x97\x8e', 2435: b'\xec\x97\x90', 2436: b'\xec\x97\x91', 2437: b'\xec\x97\x94', 2438: b'\xec\x97\x98', 2439: b'\xec\x97\xa0', 2440: b'\xec\x97\xa1', 2441: b'\xec\x97\xa3', 2442: b'\xec\x97\xa5', \
2443: b'\xec\x97\xac', 2444: b'\xec\x97\xad', 2445: b'\xec\x97\xae', 2446: b'\xec\x97\xb0', 2447: b'\xec\x97\xb4', 2448: b'\xec\x97\xb6', 2449: b'\xec\x97\xb7', 2450: b'\xec\x97\xbc', 2451: b'\xec\x97\xbd', 2452: b'\xec\x97\xbe', 2453: b'\xec\x97\xbf', 2454: b'\xec\x98\x80', 2455: b'\xec\x98\x81', \
2456: b'\xec\x98\x85', 2457: b'\xec\x98\x86', 2458: b'\xec\x98\x87', 2459: b'\xec\x98\x88', 2460: b'\xec\x98\x8c', 2461: b'\xec\x98\x90', 2462: b'\xec\x98\x98', 2463: b'\xec\x98\x99', 2464: b'\xec\x98\x9b', 2465: b'\xec\x98\x9c', 2466: b'\xec\x98\xa4', 2467: b'\xec\x98\xa5', 2468: b'\xec\x98\xa8', \
2469: b'\xec\x98\xac', 2470: b'\xec\x98\xad', 2471: b'\xec\x98\xae', 2472: b'\xec\x98\xb0', 2473: b'\xec\x98\xb3', 2474: b'\xec\x98\xb4', 2475: b'\xec\x98\xb5', 2476: b'\xec\x98\xb7', 2477: b'\xec\x98\xb9', 2478: b'\xec\x98\xbb', 2479: b'\xec\x99\x80', 2480: b'\xec\x99\x81', 2481: b'\xec\x99\x84', \
2482: b'\xec\x99\x88', 2483: b'\xec\x99\x90', 2484: b'\xec\x99\x91', 2485: b'\xec\x99\x93', 2486: b'\xec\x99\x94', 2487: b'\xec\x99\x95', 2488: b'\xec\x99\x9c', 2489: b'\xec\x99\x9d', 2490: b'\xec\x99\xa0', 2491: b'\xec\x99\xac', 2492: b'\xec\x99\xaf', 2493: b'\xec\x99\xb1', 2494: b'\xec\x99\xb8', \
2495: b'\xec\x99\xb9', 2496: b'\xec\x99\xbc', 2497: b'\xec\x9a\x80', 2498: b'\xec\x9a\x88', 2499: b'\xec\x9a\x89', 2500: b'\xec\x9a\x8b', 2501: b'\xec\x9a\x8d', 2502: b'\xec\x9a\x94', 2503: b'\xec\x9a\x95', 2504: b'\xec\x9a\x98', 2505: b'\xec\x9a\x9c', 2506: b'\xec\x9a\xa4', 2507: b'\xec\x9a\xa5', \
2508: b'\xec\x9a\xa7', 2509: b'\xec\x9a\xa9', 2510: b'\xec\x9a\xb0', 2511: b'\xec\x9a\xb1', 2512: b'\xec\x9a\xb4', 2513: b'\xec\x9a\xb8', 2514: b'\xec\x9a\xb9', 2515: b'\xec\x9a\xba', 2516: b'\xec\x9b\x80', 2517: b'\xec\x9b\x81', 2518: b'\xec\x9b\x83', 2519: b'\xec\x9b\x85', 2520: b'\xec\x9b\x8c', \
2521: b'\xec\x9b\x8d', 2522: b'\xec\x9b\x90', 2523: b'\xec\x9b\x94', 2524: b'\xec\x9b\x9c', 2525: b'\xec\x9b\x9d', 2526: b'\xec\x9b\xa0', 2527: b'\xec\x9b\xa1', 2528: b'\xec\x9b\xa8', 2529: b'\xec\x9b\xa9', 2530: b'\xec\x9b\xac', 2531: b'\xec\x9b\xb0', 2532: b'\xec\x9b\xb8', 2533: b'\xec\x9b\xb9', \
2534: b'\xec\x9b\xbd', 2535: b'\xec\x9c\x84', 2536: b'\xec\x9c\x85', 2537: b'\xec\x9c\x88', 2538: b'\xec\x9c\x8c', 2539: b'\xec\x9c\x94', 2540: b'\xec\x9c\x95', 2541: b'\xec\x9c\x97', 2542: b'\xec\x9c\x99', 2543: b'\xec\x9c\xa0', 2544: b'\xec\x9c\xa1', 2545: b'\xec\x9c\xa4', 2546: b'\xec\x9c\xa8', \
2547: b'\xec\x9c\xb0', 2548: b'\xec\x9c\xb1', 2549: b'\xec\x9c\xb3', 2550: b'\xec\x9c\xb5', 2551: b'\xec\x9c\xb7', 2552: b'\xec\x9c\xbc', 2553: b'\xec\x9c\xbd', 2554: b'\xec\x9d\x80', 2555: b'\xec\x9d\x84', 2556: b'\xec\x9d\x8a', 2557: b'\xec\x9d\x8c', 2558: b'\xec\x9d\x8d', 2559: b'\xec\x9d\x8f', \
2560: b'\xec\x9d\x91', 2561: b'\xec\x9d\x92', 2562: b'\xec\x9d\x93', 2563: b'\xec\x9d\x94', 2564: b'\xec\x9d\x95', 2565: b'\xec\x9d\x96', 2566: b'\xec\x9d\x97', 2567: b'\xec\x9d\x98', 2568: b'\xec\x9d\x9c', 2569: b'\xec\x9d\xa0', 2570: b'\xec\x9d\xa8', 2571: b'\xec\x9d\xab', 2572: b'\xec\x9d\xb4', \
2573: b'\xec\x9d\xb5', 2574: b'\xec\x9d\xb8', 2575: b'\xec\x9d\xbc', 2576: b'\xec\x9d\xbd', 2577: b'\xec\x9d\xbe', 2578: b'\xec\x9e\x83', 2579: b'\xec\x9e\x84', 2580: b'\xec\x9e\x85', 2581: b'\xec\x9e\x87', 2582: b'\xec\x9e\x88', 2583: b'\xec\x9e\x89', 2584: b'\xec\x9e\x8a', 2585: b'\xec\x9e\x8e', \
2586: b'\xec\x9e\x90', 2587: b'\xec\x9e\x91', 2588: b'\xec\x9e\x94', 2589: b'\xec\x9e\x96', 2590: b'\xec\x9e\x97', 2591: b'\xec\x9e\x98', 2592: b'\xec\x9e\x9a', 2593: b'\xec\x9e\xa0', 2594: b'\xec\x9e\xa1', 2595: b'\xec\x9e\xa3', 2596: b'\xec\x9e\xa4', 2597: b'\xec\x9e\xa5', 2598: b'\xec\x9e\xa6', \
2599: b'\xec\x9e\xac', 2600: b'\xec\x9e\xad', 2601: b'\xec\x9e\xb0', 2602: b'\xec\x9e\xb4', 2603: b'\xec\x9e\xbc', 2604: b'\xec\x9e\xbd', 2605: b'\xec\x9e\xbf', 2606: b'\xec\x9f\x80', 2607: b'\xec\x9f\x81', 2608: b'\xec\x9f\x88', 2609: b'\xec\x9f\x89', 2610: b'\xec\x9f\x8c', 2611: b'\xec\x9f\x8e', \
2612: b'\xec\x9f\x90', 2613: b'\xec\x9f\x98', 2614: b'\xec\x9f\x9d', 2615: b'\xec\x9f\xa4', 2616: b'\xec\x9f\xa8', 2617: b'\xec\x9f\xac', 2618: b'\xec\xa0\x80', 2619: b'\xec\xa0\x81', 2620: b'\xec\xa0\x84', 2621: b'\xec\xa0\x88', 2622: b'\xec\xa0\x8a', 2623: b'\xec\xa0\x90', 2624: b'\xec\xa0\x91', \
2625: b'\xec\xa0\x93', 2626: b'\xec\xa0\x95', 2627: b'\xec\xa0\x96', 2628: b'\xec\xa0\x9c', 2629: b'\xec\xa0\x9d', 2630: b'\xec\xa0\xa0', 2631: b'\xec\xa0\xa4', 2632: b'\xec\xa0\xac', 2633: b'\xec\xa0\xad', 2634: b'\xec\xa0\xaf', 2635: b'\xec\xa0\xb1', 2636: b'\xec\xa0\xb8', 2637: b'\xec\xa0\xbc', \
2638: b'\xec\xa1\x80', 2639: b'\xec\xa1\x88', 2640: b'\xec\xa1\x89', 2641: b'\xec\xa1\x8c', 2642: b'\xec\xa1\x8d', 2643: b'\xec\xa1\x94', 2644: b'\xec\xa1\xb0', 2645: b'\xec\xa1\xb1', 2646: b'\xec\xa1\xb4', 2647: b'\xec\xa1\xb8', 2648: b'\xec\xa1\xba', 2649: b'\xec\xa2\x80', 2650: b'\xec\xa2\x81', \
2651: b'\xec\xa2\x83', 2652: b'\xec\xa2\x85', 2653: b'\xec\xa2\x86', 2654: b'\xec\xa2\x87', 2655: b'\xec\xa2\x8b', 2656: b'\xec\xa2\x8c', 2657: b'\xec\xa2\x8d', 2658: b'\xec\xa2\x94', 2659: b'\xec\xa2\x9d', 2660: b'\xec\xa2\x9f', 2661: b'\xec\xa2\xa1', 2662: b'\xec\xa2\xa8', 2663: b'\xec\xa2\xbc', \
2664: b'\xec\xa2\xbd', 2665: b'\xec\xa3\x84', 2666: b'\xec\xa3\x88', 2667: b'\xec\xa3\x8c', 2668: b'\xec\xa3\x94', 2669: b'\xec\xa3\x95', 2670: b'\xec\xa3\x97', 2671: b'\xec\xa3\x99', 2672: b'\xec\xa3\xa0', 2673: b'\xec\xa3\xa1', 2674: b'\xec\xa3\xa4', 2675: b'\xec\xa3\xb5', 2676: b'\xec\xa3\xbc', \
2677: b'\xec\xa3\xbd', 2678: b'\xec\xa4\x80', 2679: b'\xec\xa4\x84', 2680: b'\xec\xa4\x85', 2681: b'\xec\xa4\x86', 2682: b'\xec\xa4\x8c', 2683: b'\xec\xa4\x8d', 2684: b'\xec\xa4\x8f', 2685: b'\xec\xa4\x91', 2686: b'\xec\xa4\x98', 2687: b'\xec\xa4\xac', 2688: b'\xec\xa4\xb4', 2689: b'\xec\xa5\x90', \
2690: b'\xec\xa5\x91', 2691: b'\xec\xa5\x94', 2692: b'\xec\xa5\x98', 2693: b'\xec\xa5\xa0', 2694: b'\xec\xa5\xa1', 2695: b'\xec\xa5\xa3', 2696: b'\xec\xa5\xac', 2697: b'\xec\xa5\xb0', 2698: b'\xec\xa5\xb4', 2699: b'\xec\xa5\xbc', 2700: b'\xec\xa6\x88', 2701: b'\xec\xa6\x89', 2702: b'\xec\xa6\x8c', \
2703: b'\xec\xa6\x90', 2704: b'\xec\xa6\x98', 2705: b'\xec\xa6\x99', 2706: b'\xec\xa6\x9b', 2707: b'\xec\xa6\x9d', 2708: b'\xec\xa7\x80', 2709: b'\xec\xa7\x81', 2710: b'\xec\xa7\x84', 2711: b'\xec\xa7\x87', 2712: b'\xec\xa7\x88', 2713: b'\xec\xa7\x8a', 2714: b'\xec\xa7\x90', 2715: b'\xec\xa7\x91', \
2716: b'\xec\xa7\x93', 2717: b'\xec\xa7\x95', 2718: b'\xec\xa7\x96', 2719: b'\xec\xa7\x99', 2720: b'\xec\xa7\x9a', 2721: b'\xec\xa7\x9c', 2722: b'\xec\xa7\x9d', 2723: b'\xec\xa7\xa0', 2724: b'\xec\xa7\xa2', 2725: b'\xec\xa7\xa4', 2726: b'\xec\xa7\xa7', 2727: b'\xec\xa7\xac', 2728: b'\xec\xa7\xad', \
2729: b'\xec\xa7\xaf', 2730: b'\xec\xa7\xb0', 2731: b'\xec\xa7\xb1', 2732: b'\xec\xa7\xb8', 2733: b'\xec\xa7\xb9', 2734: b'\xec\xa7\xbc', 2735: b'\xec\xa8\x80', 2736: b'\xec\xa8\x88', 2737: b'\xec\xa8\x89', 2738: b'\xec\xa8\x8b', 2739: b'\xec\xa8\x8c', 2740: b'\xec\xa8\x8d', 2741: b'\xec\xa8\x94', \
2742: b'\xec\xa8\x98', 2743: b'\xec\xa8\xa9', 2744: b'\xec\xa9\x8c', 2745: b'\xec\xa9\x8d', 2746: b'\xec\xa9\x90', 2747: b'\xec\xa9\x94', 2748: b'\xec\xa9\x9c', 2749: b'\xec\xa9\x9d', 2750: b'\xec\xa9\x9f', 2751: b'\xec\xa9\xa0', 2752: b'\xec\xa9\xa1', 2753: b'\xec\xa9\xa8', 2754: b'\xec\xa9\xbd', \
2755: b'\xec\xaa\x84', 2756: b'\xec\xaa\x98', 2757: b'\xec\xaa\xbc', 2758: b'\xec\xaa\xbd', 2759: b'\xec\xab\x80', 2760: b'\xec\xab\x84', 2761: b'\xec\xab\x8c', 2762: b'\xec\xab\x8d', 2763: b'\xec\xab\x8f', 2764: b'\xec\xab\x91', 2765: b'\xec\xab\x93', 2766: b'\xec\xab\x98', 2767: b'\xec\xab\x99', \
2768: b'\xec\xab\xa0', 2769: b'\xec\xab\xac', 2770: b'\xec\xab\xb4', 2771: b'\xec\xac\x88', 2772: b'\xec\xac\x90', 2773: b'\xec\xac\x94', 2774: b'\xec\xac\x98', 2775: b'\xec\xac\xa0', 2776: b'\xec\xac\xa1', 2777: b'\xec\xad\x81', 2778: b'\xec\xad\x88', 2779: b'\xec\xad\x89', 2780: b'\xec\xad\x8c', \
2781: b'\xec\xad\x90', 2782: b'\xec\xad\x98', 2783: b'\xec\xad\x99', 2784: b'\xec\xad\x9d', 2785: b'\xec\xad\xa4', 2786: b'\xec\xad\xb8', 2787: b'\xec\xad\xb9', 2788: b'\xec\xae\x9c', 2789: b'\xec\xae\xb8', 2790: b'\xec\xaf\x94', 2791: b'\xec\xaf\xa4', 2792: b'\xec\xaf\xa7', 2793: b'\xec\xaf\xa9', \
2794: b'\xec\xb0\x8c', 2795: b'\xec\xb0\x8d', 2796: b'\xec\xb0\x90', 2797: b'\xec\xb0\x94', 2798: b'\xec\xb0\x9c', 2799: b'\xec\xb0\x9d', 2800: b'\xec\xb0\xa1', 2801: b'\xec\xb0\xa2', 2802: b'\xec\xb0\xa7', 2803: b'\xec\xb0\xa8', 2804: b'\xec\xb0\xa9', 2805: b'\xec\xb0\xac', 2806: b'\xec\xb0\xae', \
2807: b'\xec\xb0\xb0', 2808: b'\xec\xb0\xb8', 2809: b'\xec\xb0\xb9', 2810: b'\xec\xb0\xbb', 2811: b'\xec\xb0\xbc', 2812: b'\xec\xb0\xbd', 2813: b'\xec\xb0\xbe', 2814: b'\xec\xb1\x84', 2815: b'\xec\xb1\x85', 2816: b'\xec\xb1\x88', 2817: b'\xec\xb1\x8c', 2818: b'\xec\xb1\x94', 2819: b'\xec\xb1\x95', \
2820: b'\xec\xb1\x97', 2821: b'\xec\xb1\x98', 2822: b'\xec\xb1\x99', 2823: b'\xec\xb1\xa0', 2824: b'\xec\xb1\xa4', 2825: b'\xec\xb1\xa6', 2826: b'\xec\xb1\xa8', 2827: b'\xec\xb1\xb0', 2828: b'\xec\xb1\xb5', 2829: b'\xec\xb2\x98', 2830: b'\xec\xb2\x99', 2831: b'\xec\xb2\x9c', 2832: b'\xec\xb2\xa0', \
2833: b'\xec\xb2\xa8', 2834: b'\xec\xb2\xa9', 2835: b'\xec\xb2\xab', 2836: b'\xec\xb2\xac', 2837: b'\xec\xb2\xad', 2838: b'\xec\xb2\xb4', 2839: b'\xec\xb2\xb5', 2840: b'\xec\xb2\xb8', 2841: b'\xec\xb2\xbc', 2842: b'\xec\xb3\x84', 2843: b'\xec\xb3\x85', 2844: b'\xec\xb3\x87', 2845: b'\xec\xb3\x89', \
2846: b'\xec\xb3\x90', 2847: b'\xec\xb3\x94', 2848: b'\xec\xb3\xa4', 2849: b'\xec\xb3\xac', 2850: b'\xec\xb3\xb0', 2851: b'\xec\xb4\x81', 2852: b'\xec\xb4\x88', 2853: b'\xec\xb4\x89', 2854: b'\xec\xb4\x8c', 2855: b'\xec\xb4\x90', 2856: b'\xec\xb4\x98', 2857: b'\xec\xb4\x99', 2858: b'\xec\xb4\x9b', \
2859: b'\xec\xb4\x9d', 2860: b'\xec\xb4\xa4', 2861: b'\xec\xb4\xa8', 2862: b'\xec\xb4\xac', 2863: b'\xec\xb4\xb9', 2864: b'\xec\xb5\x9c', 2865: b'\xec\xb5\xa0', 2866: b'\xec\xb5\xa4', 2867: b'\xec\xb5\xac', 2868: b'\xec\xb5\xad', 2869: b'\xec\xb5\xaf', 2870: b'\xec\xb5\xb1', 2871: b'\xec\xb5\xb8', \
2872: b'\xec\xb6\x88', 2873: b'\xec\xb6\x94', 2874: b'\xec\xb6\x95', 2875: b'\xec\xb6\x98', 2876: b'\xec\xb6\x9c', 2877: b'\xec\xb6\xa4', 2878: b'\xec\xb6\xa5', 2879: b'\xec\xb6\xa7', 2880: b'\xec\xb6\xa9', 2881: b'\xec\xb6\xb0', 2882: b'\xec\xb7\x84', 2883: b'\xec\xb7\x8c', 2884: b'\xec\xb7\x90', \
2885: b'\xec\xb7\xa8', 2886: b'\xec\xb7\xac', 2887: b'\xec\xb7\xb0', 2888: b'\xec\xb7\xb8', 2889: b'\xec\xb7\xb9', 2890: b'\xec\xb7\xbb', 2891: b'\xec\xb7\xbd', 2892: b'\xec\xb8\x84', 2893: b'\xec\xb8\x88', 2894: b'\xec\xb8\x8c', 2895: b'\xec\xb8\x94', 2896: b'\xec\xb8\x99', 2897: b'\xec\xb8\xa0', \
2898: b'\xec\xb8\xa1', 2899: b'\xec\xb8\xa4', 2900: b'\xec\xb8\xa8', 2901: b'\xec\xb8\xb0', 2902: b'\xec\xb8\xb1', 2903: b'\xec\xb8\xb3', 2904: b'\xec\xb8\xb5', 2905: b'\xec\xb9\x98', 2906: b'\xec\xb9\x99', 2907: b'\xec\xb9\x9c', 2908: b'\xec\xb9\x9f', 2909: b'\xec\xb9\xa0', 2910: b'\xec\xb9\xa1', \
2911: b'\xec\xb9\xa8', 2912: b'\xec\xb9\xa9', 2913: b'\xec\xb9\xab', 2914: b'\xec\xb9\xad', 2915: b'\xec\xb9\xb4', 2916: b'\xec\xb9\xb5', 2917: b'\xec\xb9\xb8', 2918: b'\xec\xb9\xbc', 2919: b'\xec\xba\x84', 2920: b'\xec\xba\x85', 2921: b'\xec\xba\x87', 2922: b'\xec\xba\x89', 2923: b'\xec\xba\x90', \
2924: b'\xec\xba\x91', 2925: b'\xec\xba\x94', 2926: b'\xec\xba\x98', 2927: b'\xec\xba\xa0', 2928: b'\xec\xba\xa1', 2929: b'\xec\xba\xa3', 2930: b'\xec\xba\xa4', 2931: b'\xec\xba\xa5', 2932: b'\xec\xba\xac', 2933: b'\xec\xba\xad', 2934: b'\xec\xbb\x81', 2935: b'\xec\xbb\xa4', 2936: b'\xec\xbb\xa5', \
2937: b'\xec\xbb\xa8', 2938: b'\xec\xbb\xab', 2939: b'\xec\xbb\xac', 2940: b'\xec\xbb\xb4', 2941: b'\xec\xbb\xb5', 2942: b'\xec\xbb\xb7', 2943: b'\xec\xbb\xb8', 2944: b'\xec\xbb\xb9', 2945: b'\xec\xbc\x80', 2946: b'\xec\xbc\x81', 2947: b'\xec\xbc\x84', 2948: b'\xec\xbc\x88', 2949: b'\xec\xbc\x90', \
2950: b'\xec\xbc\x91', 2951: b'\xec\xbc\x93', 2952: b'\xec\xbc\x95', 2953: b'\xec\xbc\x9c', 2954: b'\xec\xbc\xa0', 2955: b'\xec\xbc\xa4', 2956: b'\xec\xbc\xac', 2957: b'\xec\xbc\xad', 2958: b'\xec\xbc\xaf', 2959: b'\xec\xbc\xb0', 2960: b'\xec\xbc\xb1', 2961: b'\xec\xbc\xb8', 2962: b'\xec\xbd\x94', \
2963: b'\xec\xbd\x95', 2964: b'\xec\xbd\x98', 2965: b'\xec\xbd\x9c', 2966: b'\xec\xbd\xa4', 2967: b'\xec\xbd\xa5', 2968: b'\xec\xbd\xa7', 2969: b'\xec\xbd\xa9', 2970: b'\xec\xbd\xb0', 2971: b'\xec\xbd\xb1', 2972: b'\xec\xbd\xb4', 2973: b'\xec\xbd\xb8', 2974: b'\xec\xbe\x80', 2975: b'\xec\xbe\x85', \
2976: b'\xec\xbe\x8c', 2977: b'\xec\xbe\xa1', 2978: b'\xec\xbe\xa8', 2979: b'\xec\xbe\xb0', 2980: b'\xec\xbf\x84', 2981: b'\xec\xbf\xa0', 2982: b'\xec\xbf\xa1', 2983: b'\xec\xbf\xa4', 2984: b'\xec\xbf\xa8', 2985: b'\xec\xbf\xb0', 2986: b'\xec\xbf\xb1', 2987: b'\xec\xbf\xb3', 2988: b'\xec\xbf\xb5', \
2989: b'\xec\xbf\xbc', 2990: b'\xed\x80\x80', 2991: b'\xed\x80\x84', 2992: b'\xed\x80\x91', 2993: b'\xed\x80\x98', 2994: b'\xed\x80\xad', 2995: b'\xed\x80\xb4', 2996: b'\xed\x80\xb5', 2997: b'\xed\x80\xb8', 2998: b'\xed\x80\xbc', 2999: b'\xed\x81\x84', 3000: b'\xed\x81\x85', 3001: b'\xed\x81\x87', \
3002: b'\xed\x81\x89', 3003: b'\xed\x81\x90', 3004: b'\xed\x81\x94', 3005: b'\xed\x81\x98', 3006: b'\xed\x81\xa0', 3007: b'\xed\x81\xac', 3008: b'\xed\x81\xad', 3009: b'\xed\x81\xb0', 3010: b'\xed\x81\xb4', 3011: b'\xed\x81\xbc', 3012: b'\xed\x81\xbd', 3013: b'\xed\x82\x81', 3014: b'\xed\x82\xa4', \
3015: b'\xed\x82\xa5', 3016: b'\xed\x82\xa8', 3017: b'\xed\x82\xac', 3018: b'\xed\x82\xb4', 3019: b'\xed\x82\xb5', 3020: b'\xed\x82\xb7', 3021: b'\xed\x82\xb9', 3022: b'\xed\x83\x80', 3023: b'\xed\x83\x81', 3024: b'\xed\x83\x84', 3025: b'\xed\x83\x88', 3026: b'\xed\x83\x89', 3027: b'\xed\x83\x90', \
3028: b'\xed\x83\x91', 3029: b'\xed\x83\x93', 3030: b'\xed\x83\x94', 3031: b'\xed\x83\x95', 3032: b'\xed\x83\x9c', 3033: b'\xed\x83\x9d', 3034: b'\xed\x83\xa0', 3035: b'\xed\x83\xa4', 3036: b'\xed\x83\xac', 3037: b'\xed\x83\xad', 3038: b'\xed\x83\xaf', 3039: b'\xed\x83\xb0', 3040: b'\xed\x83\xb1', \
3041: b'\xed\x83\xb8', 3042: b'\xed\x84\x8d', 3043: b'\xed\x84\xb0', 3044: b'\xed\x84\xb1', 3045: b'\xed\x84\xb4', 3046: b'\xed\x84\xb8', 3047: b'\xed\x84\xba', 3048: b'\xed\x85\x80', 3049: b'\xed\x85\x81', 3050: b'\xed\x85\x83', 3051: b'\xed\x85\x84', 3052: b'\xed\x85\x85', 3053: b'\xed\x85\x8c', \
3054: b'\xed\x85\x8d', 3055: b'\xed\x85\x90', 3056: b'\xed\x85\x94', 3057: b'\xed\x85\x9c', 3058: b'\xed\x85\x9d', 3059: b'\xed\x85\x9f', 3060: b'\xed\x85\xa1', 3061: b'\xed\x85\xa8', 3062: b'\xed\x85\xac', 3063: b'\xed\x85\xbc', 3064: b'\xed\x86\x84', 3065: b'\xed\x86\x88', 3066: b'\xed\x86\xa0', \
3067: b'\xed\x86\xa1', 3068: b'\xed\x86\xa4', 3069: b'\xed\x86\xa8', 3070: b'\xed\x86\xb0', 3071: b'\xed\x86\xb1', 3072: b'\xed\x86\xb3', 3073: b'\xed\x86\xb5', 3074: b'\xed\x86\xba', 3075: b'\xed\x86\xbc', 3076: b'\xed\x87\x80', 3077: b'\xed\x87\x98', 3078: b'\xed\x87\xb4', 3079: b'\xed\x87\xb8', \
3080: b'\xed\x88\x87', 3081: b'\xed\x88\x89', 3082: b'\xed\x88\x90', 3083: b'\xed\x88\xac', 3084: b'\xed\x88\xad', 3085: b'\xed\x88\xb0', 3086: b'\xed\x88\xb4', 3087: b'\xed\x88\xbc', 3088: b'\xed\x88\xbd', 3089: b'\xed\x88\xbf', 3090: b'\xed\x89\x81', 3091: b'\xed\x89\x88', 3092: b'\xed\x89\x9c', \
3093: b'\xed\x89\xa4', 3094: b'\xed\x8a\x80', 3095: b'\xed\x8a\x81', 3096: b'\xed\x8a\x84', 3097: b'\xed\x8a\x88', 3098: b'\xed\x8a\x90', 3099: b'\xed\x8a\x91', 3100: b'\xed\x8a\x95', 3101: b'\xed\x8a\x9c', 3102: b'\xed\x8a\xa0', 3103: b'\xed\x8a\xa4', 3104: b'\xed\x8a\xac', 3105: b'\xed\x8a\xb1', \
3106: b'\xed\x8a\xb8', 3107: b'\xed\x8a\xb9', 3108: b'\xed\x8a\xbc', 3109: b'\xed\x8a\xbf', 3110: b'\xed\x8b\x80', 3111: b'\xed\x8b\x82', 3112: b'\xed\x8b\x88', 3113: b'\xed\x8b\x89', 3114: b'\xed\x8b\x8b', 3115: b'\xed\x8b\x94', 3116: b'\xed\x8b\x98', 3117: b'\xed\x8b\x9c', 3118: b'\xed\x8b\xa4', \
3119: b'\xed\x8b\xa5', 3120: b'\xed\x8b\xb0', 3121: b'\xed\x8b\xb1', 3122: b'\xed\x8b\xb4', 3123: b'\xed\x8b\xb8', 3124: b'\xed\x8c\x80', 3125: b'\xed\x8c\x81', 3126: b'\xed\x8c\x83', 3127: b'\xed\x8c\x85', 3128: b'\xed\x8c\x8c', 3129: b'\xed\x8c\x8d', 3130: b'\xed\x8c\x8e', 3131: b'\xed\x8c\x90', \
3132: b'\xed\x8c\x94', 3133: b'\xed\x8c\x96', 3134: b'\xed\x8c\x9c', 3135: b'\xed\x8c\x9d', 3136: b'\xed\x8c\x9f', 3137: b'\xed\x8c\xa0', 3138: b'\xed\x8c\xa1', 3139: b'\xed\x8c\xa5', 3140: b'\xed\x8c\xa8', 3141: b'\xed\x8c\xa9', 3142: b'\xed\x8c\xac', 3143: b'\xed\x8c\xb0', 3144: b'\xed\x8c\xb8', \
3145: b'\xed\x8c\xb9', 3146: b'\xed\x8c\xbb', 3147: b'\xed\x8c\xbc', 3148: b'\xed\x8c\xbd', 3149: b'\xed\x8d\x84', 3150: b'\xed\x8d\x85', 3151: b'\xed\x8d\xbc', 3152: b'\xed\x8d\xbd', 3153: b'\xed\x8e\x80', 3154: b'\xed\x8e\x84', 3155: b'\xed\x8e\x8c', 3156: b'\xed\x8e\x8d', 3157: b'\xed\x8e\x8f', \
3158: b'\xed\x8e\x90', 3159: b'\xed\x8e\x91', 3160: b'\xed\x8e\x98', 3161: b'\xed\x8e\x99', 3162: b'\xed\x8e\x9c', 3163: b'\xed\x8e\xa0', 3164: b'\xed\x8e\xa8', 3165: b'\xed\x8e\xa9', 3166: b'\xed\x8e\xab', 3167: b'\xed\x8e\xad', 3168: b'\xed\x8e\xb4', 3169: b'\xed\x8e\xb8', 3170: b'\xed\x8e\xbc', \
3171: b'\xed\x8f\x84', 3172: b'\xed\x8f\x85', 3173: b'\xed\x8f\x88', 3174: b'\xed\x8f\x89', 3175: b'\xed\x8f\x90', 3176: b'\xed\x8f\x98', 3177: b'\xed\x8f\xa1', 3178: b'\xed\x8f\xa3', 3179: b'\xed\x8f\xac', 3180: b'\xed\x8f\xad', 3181: b'\xed\x8f\xb0', 3182: b'\xed\x8f\xb4', 3183: b'\xed\x8f\xbc', \
3184: b'\xed\x8f\xbd', 3185: b'\xed\x8f\xbf', 3186: b'\xed\x90\x81', 3187: b'\xed\x90\x88', 3188: b'\xed\x90\x9d', 3189: b'\xed\x91\x80', 3190: b'\xed\x91\x84', 3191: b'\xed\x91\x9c', 3192: b'\xed\x91\xa0', 3193: b'\xed\x91\xa4', 3194: b'\xed\x91\xad', 3195: b'\xed\x91\xaf', 3196: b'\xed\x91\xb8', \
3197: b'\xed\x91\xb9', 3198: b'\xed\x91\xbc', 3199: b'\xed\x91\xbf', 3200: b'\xed\x92\x80', 3201: b'\xed\x92\x82', 3202: b'\xed\x92\x88', 3203: b'\xed\x92\x89', 3204: b'\xed\x92\x8b', 3205: b'\xed\x92\x8d', 3206: b'\xed\x92\x94', 3207: b'\xed\x92\xa9', 3208: b'\xed\x93\x8c', 3209: b'\xed\x93\x90', \
3210: b'\xed\x93\x94', 3211: b'\xed\x93\x9c', 3212: b'\xed\x93\x9f', 3213: b'\xed\x93\xa8', 3214: b'\xed\x93\xac', 3215: b'\xed\x93\xb0', 3216: b'\xed\x93\xb8', 3217: b'\xed\x93\xbb', 3218: b'\xed\x93\xbd', 3219: b'\xed\x94\x84', 3220: b'\xed\x94\x88', 3221: b'\xed\x94\x8c', 3222: b'\xed\x94\x94', \
3223: b'\xed\x94\x95', 3224: b'\xed\x94\x97', 3225: b'\xed\x94\xbc', 3226: b'\xed\x94\xbd', 3227: b'\xed\x95\x80', 3228: b'\xed\x95\x84', 3229: b'\xed\x95\x8c', 3230: b'\xed\x95\x8d', 3231: b'\xed\x95\x8f', 3232: b'\xed\x95\x91', 3233: b'\xed\x95\x98', 3234: b'\xed\x95\x99', 3235: b'\xed\x95\x9c', \
3236: b'\xed\x95\xa0', 3237: b'\xed\x95\xa5', 3238: b'\xed\x95\xa8', 3239: b'\xed\x95\xa9', 3240: b'\xed\x95\xab', 3241: b'\xed\x95\xad', 3242: b'\xed\x95\xb4', 3243: b'\xed\x95\xb5', 3244: b'\xed\x95\xb8', 3245: b'\xed\x95\xbc', 3246: b'\xed\x96\x84', 3247: b'\xed\x96\x85', 3248: b'\xed\x96\x87', \
3249: b'\xed\x96\x88', 3250: b'\xed\x96\x89', 3251: b'\xed\x96\x90', 3252: b'\xed\x96\xa5', 3253: b'\xed\x97\x88', 3254: b'\xed\x97\x89', 3255: b'\xed\x97\x8c', 3256: b'\xed\x97\x90', 3257: b'\xed\x97\x92', 3258: b'\xed\x97\x98', 3259: b'\xed\x97\x99', 3260: b'\xed\x97\x9b', 3261: b'\xed\x97\x9d', \
3262: b'\xed\x97\xa4', 3263: b'\xed\x97\xa5', 3264: b'\xed\x97\xa8', 3265: b'\xed\x97\xac', 3266: b'\xed\x97\xb4', 3267: b'\xed\x97\xb5', 3268: b'\xed\x97\xb7', 3269: b'\xed\x97\xb9', 3270: b'\xed\x98\x80', 3271: b'\xed\x98\x81', 3272: b'\xed\x98\x84', 3273: b'\xed\x98\x88', 3274: b'\xed\x98\x90', \
3275: b'\xed\x98\x91', 3276: b'\xed\x98\x93', 3277: b'\xed\x98\x94', 3278: b'\xed\x98\x95', 3279: b'\xed\x98\x9c', 3280: b'\xed\x98\xa0', 3281: b'\xed\x98\xa4', 3282: b'\xed\x98\xad', 3283: b'\xed\x98\xb8', 3284: b'\xed\x98\xb9', 3285: b'\xed\x98\xbc', 3286: b'\xed\x99\x80', 3287: b'\xed\x99\x85', \
3288: b'\xed\x99\x88', 3289: b'\xed\x99\x89', 3290: b'\xed\x99\x8b', 3291: b'\xed\x99\x8d', 3292: b'\xed\x99\x91', 3293: b'\xed\x99\x94', 3294: b'\xed\x99\x95', 3295: b'\xed\x99\x98', 3296: b'\xed\x99\x9c', 3297: b'\xed\x99\xa7', 3298: b'\xed\x99\xa9', 3299: b'\xed\x99\xb0', 3300: b'\xed\x99\xb1', \
3301: b'\xed\x99\xb4', 3302: b'\xed\x9a\x83', 3303: b'\xed\x9a\x85', 3304: b'\xed\x9a\x8c', 3305: b'\xed\x9a\x8d', 3306: b'\xed\x9a\x90', 3307: b'\xed\x9a\x94', 3308: b'\xed\x9a\x9d', 3309: b'\xed\x9a\x9f', 3310: b'\xed\x9a\xa1', 3311: b'\xed\x9a\xa8', 3312: b'\xed\x9a\xac', 3313: b'\xed\x9a\xb0', \
3314: b'\xed\x9a\xb9', 3315: b'\xed\x9a\xbb', 3316: b'\xed\x9b\x84', 3317: b'\xed\x9b\x85', 3318: b'\xed\x9b\x88', 3319: b'\xed\x9b\x8c', 3320: b'\xed\x9b\x91', 3321: b'\xed\x9b\x94', 3322: b'\xed\x9b\x97', 3323: b'\xed\x9b\x99', 3324: b'\xed\x9b\xa0', 3325: b'\xed\x9b\xa4', 3326: b'\xed\x9b\xa8', \
3327: b'\xed\x9b\xb0', 3328: b'\xed\x9b\xb5', 3329: b'\xed\x9b\xbc', 3330: b'\xed\x9b\xbd', 3331: b'\xed\x9c\x80', 3332: b'\xed\x9c\x84', 3333: b'\xed\x9c\x91', 3334: b'\xed\x9c\x98', 3335: b'\xed\x9c\x99', 3336: b'\xed\x9c\x9c', 3337: b'\xed\x9c\xa0', 3338: b'\xed\x9c\xa8', 3339: b'\xed\x9c\xa9', \
3340: b'\xed\x9c\xab', 3341: b'\xed\x9c\xad', 3342: b'\xed\x9c\xb4', 3343: b'\xed\x9c\xb5', 3344: b'\xed\x9c\xb8', 3345: b'\xed\x9c\xbc', 3346: b'\xed\x9d\x84', 3347: b'\xed\x9d\x87', 3348: b'\xed\x9d\x89', 3349: b'\xed\x9d\x90', 3350: b'\xed\x9d\x91', 3351: b'\xed\x9d\x94', 3352: b'\xed\x9d\x96', \
3353: b'\xed\x9d\x97', 3354: b'\xed\x9d\x98', 3355: b'\xed\x9d\x99', 3356: b'\xed\x9d\xa0', 3357: b'\xed\x9d\xa1', 3358: b'\xed\x9d\xa3', 3359: b'\xed\x9d\xa5', 3360: b'\xed\x9d\xa9', 3361: b'\xed\x9d\xac', 3362: b'\xed\x9d\xb0', 3363: b'\xed\x9d\xb4', 3364: b'\xed\x9d\xbc', 3365: b'\xed\x9d\xbd', \
3366: b'\xed\x9e\x81', 3367: b'\xed\x9e\x88', 3368: b'\xed\x9e\x89', 3369: b'\xed\x9e\x8c', 3370: b'\xed\x9e\x90', 3371: b'\xed\x9e\x98', 3372: b'\xed\x9e\x99', 3373: b'\xed\x9e\x9b', 3374: b'\xed\x9e\x9d', 3377: b'\xe1\x84\x80', 3378: b'\xe1\x84\x81', 3379: b'\xe1\x84\x82', 3380: b'\xe1\x84\x83', \
3381: b'\xe1\x84\x84', 3382: b'\xe1\x84\x85', 3383: b'\xe1\x84\x86', 3384: b'\xe1\x84\x87', 3385: b'\xe1\x84\x88', 3386: b'\xe1\x84\x89', 3387: b'\xe1\x84\x8a', 3388: b'\xe1\x84\x8b', 3389: b'\xe1\x84\x8c', 3390: b'\xe1\x84\x8d', 3391: b'\xe1\x84\x8e', 3392: b'\xe1\x84\x8f', 3393: b'\xe1\x84\x90', \
3394: b'\xe1\x84\x91', 3395: b'\xe1\x84\x92', 3396: b'\xe1\x85\xa1', 3397: b'\xe1\x85\xa2', 3398: b'\xe1\x85\xa3', 3399: b'\xe1\x85\xa4', 3400: b'\xe1\x85\xa5', 3401: b'\xe1\x85\xa6', 3402: b'\xe1\x85\xa7', 3403: b'\xe1\x85\xa8', 3404: b'\xe1\x85\xa9', 3405: b'\xe1\x85\xad', 3406: b'\xe1\x85\xae', \
3407: b'\xe1\x85\xb2', 3408: b'\xe1\x85\xb3', 3409: b'\xe1\x85\xb5', 3425: b'\xeb\xa2\x94', 3426: b'\xec\x8c\xb0', 3427: b'\xec\x8e\xbc', 3428: b'\xec\x93\x94', 3429: b'\xec\xac\xac', 65535: b' ' }
  ]

# item maps
itemmap = [ \
# gen 1
[ "None", "Master Ball", "Ultra Ball", "Great Ball", "Poké Ball", "Town Map", "Bicycle", "?????", "Safari Ball", \
"Pokédex", "Moon Stone", "Antidote", "Burn Heal", "Ice Heal", "Awakening", "Parlyz Heal", "Full Restore", "Max Potion", \
"Hyper Potion", "Super Potion", "Potion", "BoulderBadge", "CascadeBadge", "ThunderBadge", "RainbowBadge", "SoulBadge", \
"MarshBadge", "VolcanoBadge", "EarthBadge", "Escape Rope", "Repel", "Old Amber", "Fire Stone", "Thunderstone", "Water Stone", \
"HP Up", "Protein", "Iron", "Carbos", "Calcium", "Rare Candy", "Dome Fossil", "Helix Fossil", "Secret Key", "?????", \
"Bike Voucher", "X Accuracy", "Leaf Stone", "Card Key", "Nugget", "PP Up", "Poké Doll", "Full Heal", "Revive", "Max Revive", \
"Guard Spec.", "Super Repel", "Max Repel", "Dire Hit", "Coin", "Fresh Water", "Soda Pop", "Lemonade", "S.S. Ticket", \
"Gold Teeth", "X Attack", "X Defend", "X Speed", "X Special", "Coin Case", "Oak's Parcel", "Itemfinder", "Silph Scope", \
"Poké Flute", "Lift Key", "Exp. All", "Old Rod", "Good Rod", "Super Rod", "PP Up", "Ether", "Max Ether", "Elixer", \
"Max Elixer", "HM01", "HM02", "HM03", "HM04", "HM05", "TM01", "TM02", "TM03", "TM04", "TM05", "TM06", "TM07", "TM08", \
"TM09", "TM10", "TM11", "TM12", "TM13", "TM14", "TM15", "TM16", "TM17", "TM18", "TM19", "TM20", "TM21", "TM22", "TM23", \
"TM24", "TM25", "TM26", "TM27", "TM28", "TM29", "TM30", "TM31", "TM32", "TM33", "TM34", "TM35", "TM36", "TM37", "TM38", \
"TM39", "TM40", "TM41", "TM42", "TM43", "TM44", "TM45", "TM46", "TM47", "TM48", "TM49", "TM50", "TM51", "TM52", "TM53",\
 "TM54", "TM55"],
# gen 2
[ "None", "Master Ball", "Ultra Ball", "BrightPowder", "Great Ball", "Poké Ball", "Teru-sama", "Bicycle", \
"Moon Stone", "Antidote", "Burn Heal", "Ice Heal", "Awakening", "Parlyz Heal", "Full Restore", "Max Potion", \
"Hyper Potion", "Super Potion", "Potion", "Escape Rope", "Repel", "Max Elixer", "Fire Stone", "Thunderstone", \
"Water Stone", "Teru-sama", "HP Up", "Protein", "Iron", "Carbos", "Lucky Punch", "Calcium", \
"Rare Candy", "X Accuracy", "Leaf Stone", "Metal Powder", "Nugget", "Poké Doll", "Full Heal", "Revive", \
"Max Revive", "Guard Spec.", "Super Repel", "Max Repel", "Dire Hit", "Teru-sama", "Fresh Water", "Soda Pop", \
"Lemonade", "X Attack", "Teru-sama", "X Defend", "X Speed", "X Special", "Coin Case", "Itemfinder", \
"Teru-sama", "Exp.Share", "Old Rod", "Good Rod", "Silver Leaf", "Super Rod", "PP Up", "Ether", \
"Max Ether", "Elixer", "Red Scale", "SecretPotion", "S.S. Ticket", "Mystery Egg", "Clear Bell*", "Silver Wing", \
"Moomoo Milk", "Quick Claw", "PSNCureBerry", "Gold Leaf", "Soft Sand", "Sharp Beak", "PRZCureBerry", "Burnt Berry", \
"Ice Berry", "Poison Barb", "King's Rock", "Bitter Berry", "Mint Berry", "Red Apricorn", "TinyMushroom", "Big Mushroom", \
"SilverPowder", "Blu Apricorn", "Teru-sama", "Amulet Coin", "Ylw Apricorn", "Grn Apricorn", "Cleanse Tag", "Mystic Water", \
"TwistedSpoon", "Wht Apricorn", "Blackbelt", "Blk Apricorn", "Teru-sama", "Pnk Apricorn", "BlackGlasses", "SlowpokeTail", \
"Pink Bow", "Stick", "Smoke Ball", "NeverMeltIce", "Magnet", "MiracleBerry", "Pearl", "Big Pearl", \
"Everstone", "Spell Tag", "RageCandyBar", "GS Ball*", "Blue Card*", "Miracle Seed", "Thick Club", "Focus Band", \
"Teru-sama", "EnergyPowder", "Energy Root", "Heal Powder", "Revival Herb", "Hard Stone", "Lucky Egg", "Card Key", \
"Machine Part", "Egg Ticket*", "Lost Item", "Stardust", "Star Piece", "Basement Key", "Pass", "Teru-sama", \
"Teru-sama", "Teru-sama", "Charcoal", "Berry Juice", "Scope Lens", "Teru-sama", "Teru-sama", "Metal Coat", \
"Dragon Fang", "Teru-sama", "Leftovers", "Teru-sama", "Teru-sama", "Teru-sama", "MysteryBerry", "Dragon Scale", \
"Berserk Gene", "Teru-sama", "Teru-sama", "Teru-sama", "Sacred Ash", "Heavy Ball", "Flower Mail", "Level Ball", \
"Lure Ball", "Fast Ball", "Teru-sama", "Light Ball", "Friend Ball", "Moon Ball", "Love Ball", "Normal Box", \
"Gorgeous Box", "Sun Stone", "Polkadot Bow", "Teru-sama", "Up-Grade", "Berry", "Gold Berry", "SquirtBottle", \
"Teru-sama", "Park Ball", "Rainbow Wing", "Teru-sama", "Brick Piece", "Surf Mail", "Litebluemail", "Portraitmail", \
"Lovely Mail", "Eon Mail", "Morph Mail", "Bluesky Mail", "Music Mail", "Mirage Mail", "Teru-sama", "TM01", \
"TM02", "TM03", "TM04", "TM04", "TM05", "TM06", "TM07", "TM08", \
"TM09", "TM10", "TM11", "TM12", "TM13", "TM14", "TM15", "TM16", \
"TM17", "TM18", "TM19", "TM20", "TM21", "TM22", "TM23", "TM24", \
"TM25", "TM26", "TM27", "TM28", "TM28", "TM29", "TM30", "TM31", \
"TM32", "TM33", "TM34", "TM35", "TM36", "TM37", "TM38", "TM39", \
"TM40", "TM41", "TM42", "TM43", "TM44", "TM45", "TM46", "TM47", \
"TM48", "TM49", "TM50", "HM01", "HM02", "HM03", "HM04", "HM05", \
"HM06", "HM07", "HM08", "HM09", "HM10", "HM11", "HM12", "Cancel" ],
# gen 3
[ "None", "Master Ball", "Ultra Ball", "Great Ball", "Poké Ball", "Safari Ball", "Net Ball", "Dive Ball", \
"Nest Ball", "Repeat Ball", "Timer Ball", "Luxury Ball", "Premier Ball", "Potion", "Antidote", "Burn Heal", \
"Ice Heal", "Awakening", "Parlyz Heal", "Full Restore", "Max Potion", "Hyper Potion", "Super Potion", "Full Heal", \
"Revive", "Max Revive", "Fresh Water", "Soda Pop", "Lemonade", "Moomoo Milk", "EnergyPowder", "Energy Root", \
"Heal Powder", "Revival Herb", "Ether", "Max Ether", "Elixir", "Max Elixir", "Lava Cookie", "Blue Flute", \
"Yellow Flute", "Red Flute", "Black Flute", "White Flute", "Berry Juice", "Sacred Ash", "Shoal Salt", "Shoal Shell", \
"Red Shard", "Blue Shard", "Yellow Shard", "Green Shard", "unknown", "unknown", "unknown", "unknown", \
"unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "HP Up", \
"Protein", "Iron", "Carbos", "Calcium", "Rare Candy", "PP Up", "Zinc", "PP Max", \
"unknown", "Guard Spec.", "Dire Hit", "X Attack", "X Defend", "X Speed", "X Accuracy", "X Special", \
"Poké Doll", "Fluffy Tail", "unknown", "Super Repel", "Max Repel", "Escape Rope", "Repel", \
"unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "Sun Stone", "Moon Stone", \
"Fire Stone", "Thunderstone", "Water Stone", "Leaf Stone", "unknown", "unknown", "unknown", "unknown", \
"TinyMushroom", "Big Mushroom", "unknown", "Pearl", "Big Pearl", "Stardust", "Star Piece", "Nugget", \
"Heart Scale", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", \
"unknown", "unknown", "Orange Mail", "Harbor Mail", "Glitter Mail", "Mech Mail", "Wood Mail", "Wave Mail", \
"Bead Mail", "Shadow Mail", "Tropic Mail", "Dream Mail", "Fab Mail", "Retro Mail", "Cheri Berry", \
"Chesto Berry", "Pecha Berry", "Rawst Berry", "Aspear Berry", "Leppa Berry", "Oran Berry", "Persim Berry", "Lum Berry", \
"Sitrus Berry", "Figy Berry", "Wiki Berry", "Mago Berry", "Aguav Berry", "Iapapa Berry", "Razz Berry", "Bluk Berry", \
"Nanab Berry", "Wepear Berry", "Pinap Berry", "Pomeg Berry", "Kelpsy Berry", "Qualot Berry", "Hondew Berry", "Grepa Berry", \
"Tamato Berry", "Cornn Berry", "Magost Berry", "Rabuta Berry", "Nomel Berry", "Spelon Berry", "Pamtre Berry", "Watmel Berry", \
"Durin Berry", "Belue Berry", "Liechi Berry", "Ganlon Berry", "Salac Berry", "Petaya Berry", "Apicot Berry", "Lansat Berry", \
"Starf Berry", "Enigma Berry", "unknown", "unknown", "unknown", "BrightPowder", "White Herb", "Macho Brace", \
"Exp. Share", "Quick Claw", "Soothe Bell", "Mental Herb", "Choice Band", "King's Rock", "SilverPowder", "Amulet Coin", \
"Cleanse Tag", "Soul Dew", "DeepSeaTooth", "DeepSeaScale", "Smoke Ball", "Everstone", "Focus Band", "Lucky Egg", \
"Scope Lens", "Metal Coat", "Leftovers", "Dragon Scale", "Light Ball", "Soft Sand", "Hard Stone", "Miracle Seed", \
"BlackGlasses", "Black Belt", "Magnet", "Mystic Water", "Sharp Beak", "Poison Barb", "NeverMeltIce", "Spell Tag", \
"TwistedSpoon", "Charcoal", "Dragon Fang", "Silk Scarf", "Up-Grade", "Shell Bell", "Sea Incense", "Lax Incense", \
"Lucky Punch", "Metal Powder", "Thick Club", "Stick", "unknown", "unknown", "unknown", "unknown", \
"unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", \
"unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", \
"unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", "unknown", \
"Red Scarf", "Blue Scarf", "Pink Scarf", "Green Scarf", "Yellow Scarf", "Mach Bike", "Coin Case", "Itemfinder", \
"Old Rod", "Good Rod", "Super Rod", "S.S. Ticket", "Contest Pass", "unknown", "Wailmer Pail", "Devon Goods", \
"Soot Sack", "Basement Key", "Acro Bike", "Pokéblock Case", "Letter", "Eon Ticket", "Red Orb", "Blue Orb", \
"Scanner", "Go-Goggles", "Meteorite", "Rm. 1 Key", "Rm. 2 Key", "Rm. 4 Key", "Rm. 6 Key", "Storage Key", \
"Root Fossil", "Claw Fossil", "Devon Scope", "TM01", "TM02", "TM03", "TM04", "TM05", \
"TM06", "TM07", "TM08", "TM09", "TM10", "TM11", "TM12", "TM13", \
"TM14", "TM15", "TM16", "TM17", "TM18", "TM19", "TM20", "TM21", \
"TM22", "TM23", "TM24", "TM25", "TM26", "TM27", "TM28", "TM29", \
"TM30", "TM31", "TM32", "TM33", "TM34", "TM35", "TM36", "TM37", \
"TM38", "TM39", "TM40", "TM41", "TM42", "TM43", "TM44", "TM45", \
"TM46", "TM47", "TM48", "TM49", "TM50", "HM01", "HM02", "HM03", \
"HM04", "HM05", "HM06", "HM07", "HM08", "unknown", "unknown", "Oak's Parcel", \
"Poké Flute", "Secret Key", "Bike Voucher", "Gold Teeth", "Old Amber", "Card Key", "Lift Key", "Helix Fossil", \
"Dome Fossil", "Silph Scope", "Bicycle", "Town Map", "VS Seeker", "Fame Checker", "TM Case", "Berry Pouch", \
"Teachy TV", "Tri-Pass", "Rainbow Pass", "Tea", "MysticTicket", "AuroraTicket", "Powder Jar", "Ruby", \
"Sapphire", "Magma Emblem", "Old Sea Map" ],
# gen 4-8
[ "None", "Master Ball", "Ultra Ball", "Great Ball", "Poké Ball", "Safari Ball", "Net Ball", "Dive Ball", "Nest Ball", "Repeat Ball", "Timer Ball", \
"Luxury Ball", "Premier Ball", "Dusk Ball", "Heal Ball", "Quick Ball", "Cherish Ball", "Potion", "Antidote", "Burn Heal", "Ice Heal", "Awakening", \
"Paralyze Heal", "Full Restore", "Max Potion", "Hyper Potion", "Super Potion", "Full Heal", "Revive", "Max Revive", "Fresh Water", "Soda Pop", "Lemonade", \
"Moomoo Milk", "Energy Powder", "Energy Root", "Heal Powder", "Revival Herb", "Ether", "Max Ether", "Elixir", "Max Elixir", "Lava Cookie", "Berry Juice", \
"Sacred Ash", "HP Up", "Protein", "Iron", "Carbos", "Calcium", "Rare Candy", "PP Up", "Zinc", "PP Max", "Old Gateau", "Guard Spec.", "Dire Hit", "X Attack", \
"X Defense", "X Speed", "X Accuracy", "X Sp. Atk", "X Sp. Def", "Poké Doll", "Fluffy Tail", "Blue Flute", "Yellow Flute", "Red Flute", "Black Flute", \
"White Flute", "Shoal Salt", "Shoal Shell", "Red Shard", "Blue Shard", "Yellow Shard", "Green Shard", "Super Repel", "Max Repel", "Escape Rope", "Repel", \
"Sun Stone", "Moon Stone", "Fire Stone", "Thunder Stone", "Water Stone", "Leaf Stone", "Tiny Mushroom", "Big Mushroom", "Pearl", "Big Pearl", "Stardust", \
"Star Piece", "Nugget", "Heart Scale", "Honey", "Growth Mulch", "Damp Mulch", "Stable Mulch", "Gooey Mulch", "Root Fossil", "Claw Fossil", "Helix Fossil", \
"Dome Fossil", "Old Amber", "Armor Fossil", "Skull Fossil", "Rare Bone", "Shiny Stone", "Dusk Stone", "Dawn Stone", "Oval Stone", "Odd Keystone", \
"Griseous Orb", "Tea", "???", "Autograph", "Douse Drive", "Shock Drive", "Burn Drive", "Chill Drive", "???", "Pokémon Box", "Medicine Pocket", "TM Case", 
"Candy Jar", "Power-Up Pocket", "Clothing Trunk", "Catching Pocket", "Battle Pocket", "???", "???", "???", "???", "???", "Sweet Heart", "Adamant Orb", 
"Lustrous Orb", "Greet Mail", "Favored Mail", "RSVP Mail", "Thanks Mail", "Inquiry Mail", "Like Mail", "Reply Mail", "Bridge Mail S", "Bridge Mail D", 
"Bridge Mail T", "Bridge Mail V", "Bridge Mail M", "Cheri Berry", "Chesto Berry", "Pecha Berry", "Rawst Berry", "Aspear Berry", "Leppa Berry", "Oran Berry", 
"Persim Berry", "Lum Berry", "Sitrus Berry", "Figy Berry", "Wiki Berry", "Mago Berry", "Aguav Berry", "Iapapa Berry", "Razz Berry", "Bluk Berry", 
"Nanab Berry", "Wepear Berry", "Pinap Berry", "Pomeg Berry", "Kelpsy Berry", "Qualot Berry", "Hondew Berry", "Grepa Berry", "Tamato Berry", "Cornn Berry", 
"Magost Berry", "Rabuta Berry", "Nomel Berry", "Spelon Berry", "Pamtre Berry", "Watmel Berry", "Durin Berry", "Belue Berry", "Occa Berry", "Passho Berry", 
"Wacan Berry", "Rindo Berry", "Yache Berry", "Chople Berry", "Kebia Berry", "Shuca Berry", "Coba Berry", "Payapa Berry", "Tanga Berry", "Charti Berry", 
"Kasib Berry", "Haban Berry", "Colbur Berry", "Babiri Berry", "Chilan Berry", "Liechi Berry", "Ganlon Berry", "Salac Berry", "Petaya Berry", "Apicot Berry", 
"Lansat Berry", "Starf Berry", "Enigma Berry", "Micle Berry", "Custap Berry", "Jaboca Berry", "Rowap Berry", "Bright Powder", "White Herb", "Macho Brace", 
"Exp. Share", "Quick Claw", "Soothe Bell", "Mental Herb", "Choice Band", "King's Rock", "Silver Powder", "Amulet Coin", "Cleanse Tag", "Soul Dew", 
"Deep Sea Tooth", "Deep Sea Scale", "Smoke Ball", "Everstone", "Focus Band", "Lucky Egg", "Scope Lens", "Metal Coat", "Leftovers", "Dragon Scale", 
"Light Ball", "Soft Sand", "Hard Stone", "Miracle Seed", "Black Glasses", "Black Belt", "Magnet", "Mystic Water", "Sharp Beak", "Poison Barb", 
"Never-Melt Ice", "Spell Tag", "Twisted Spoon", "Charcoal", "Dragon Fang", "Silk Scarf", "Upgrade", "Shell Bell", "Sea Incense", "Lax Incense", 
"Lucky Punch", "Metal Powder", "Thick Club", "Leek", "Red Scarf", "Blue Scarf", "Pink Scarf", "Green Scarf", "Yellow Scarf", "Wide Lens", "Muscle Band", 
"Wise Glasses", "Expert Belt", "Light Clay", "Life Orb", "Power Herb", "Toxic Orb", "Flame Orb", "Quick Powder", "Focus Sash", "Zoom Lens", "Metronome", 
"Iron Ball", "Lagging Tail", "Destiny Knot", "Black Sludge", "Icy Rock", "Smooth Rock", "Heat Rock", "Damp Rock", "Grip Claw", "Choice Scarf", 
"Sticky Barb", "Power Bracer", "Power Belt", "Power Lens", "Power Band", "Power Anklet", "Power Weight", "Shed Shell", "Big Root", "Choice Specs", 
"Flame Plate", "Splash Plate", "Zap Plate", "Meadow Plate", "Icicle Plate", "Fist Plate", "Toxic Plate", "Earth Plate", "Sky Plate", "Mind Plate", 
"Insect Plate", "Stone Plate", "Spooky Plate", "Draco Plate", "Dread Plate", "Iron Plate", "Odd Incense", "Rock Incense", "Full Incense", "Wave Incense", 
"Rose Incense", "Luck Incense", "Pure Incense", "Protector", "Electirizer", "Magmarizer", "Dubious Disc", "Reaper Cloth", "Razor Claw", "Razor Fang", 
"TM01", "TM02", "TM03", "TM04", "TM05", "TM06", "TM07", "TM08", "TM09", "TM10", "TM11", "TM12", "TM13", "TM14", "TM15", "TM16", "TM17", "TM18", "TM19", 
"TM20", "TM21", "TM22", "TM23", "TM24", "TM25", "TM26", "TM27", "TM28", "TM29", "TM30", "TM31", "TM32", "TM33", "TM34", "TM35", "TM36", "TM37", "TM38", 
"TM39", "TM40", "TM41", "TM42", "TM43", "TM44", "TM45", "TM46", "TM47", "TM48", "TM49", "TM50", "TM51", "TM52", "TM53", "TM54", "TM55", "TM56", "TM57", 
"TM58", "TM59", "TM60", "TM61", "TM62", "TM63", "TM64", "TM65", "TM66", "TM67", "TM68", "TM69", "TM70", "TM71", "TM72", "TM73", "TM74", "TM75", "TM76", 
"TM77", "TM78", "TM79", "TM80", "TM81", "TM82", "TM83", "TM84", "TM85", "TM86", "TM87", "TM88", "TM89", "TM90", "TM91", "TM92", "HM01", "HM02", "HM03", 
"HM04", "HM05", "HM06", "???", "???", "Explorer Kit", "Loot Sack", "Rule Book", "Poké Radar", "Point Card", "Journal", "Seal Case", "Fashion Case", 
"Seal Bag", "Pal Pad", "Works Key", "Old Charm", "Galactic Key", "Red Chain", "Town Map", "Vs. Seeker", "Coin Case", "Old Rod", "Good Rod", "Super Rod", 
"Sprayduck", "Poffin Case", "Bike", "Suite Key", "Oak's Letter", "Lunar Wing", "Member Card", "Azure Flute", "S.S. Ticket", "Contest Pass", "Magma Stone", 
"Parcel", "Coupon 1", "Coupon 2", "Coupon 3", "Storage Key", "Secret Potion", "Vs. Recorder", "Gracidea", "Secret Key", "Apricorn Box", "Unown Report", 
"Berry Pots", "Dowsing Machine", "Blue Card", "Slowpoke Tail", "Clear Bell", "Card Key", "Basement Key", "Squirt Bottle", "Red Scale", "Lost Item", "Pass", 
"Machine Part", "Silver Wing", "Rainbow Wing", "Mystery Egg", "Red Apricorn", "Blue Apricorn", "Yellow Apricorn", "Green Apricorn", "Pink Apricorn", 
"White Apricorn", "Black Apricorn", "Fast Ball", "Level Ball", "Lure Ball", "Heavy Ball", "Love Ball", "Friend Ball", "Moon Ball", "Sport Ball", "Park Ball", 
"Photo Album", "GB Sounds", "Tidal Bell", "Rage Candy Bar", "Data Card 01", "Data Card 02", "Data Card 03", "Data Card 04", "Data Card 05", "Data Card 06", 
"Data Card 07", "Data Card 08", "Data Card 09", "Data Card 10", "Data Card 11", "Data Card 12", "Data Card 13", "Data Card 14", "Data Card 15", 
"Data Card 16", "Data Card 17", "Data Card 18", "Data Card 19", "Data Card 20", "Data Card 21", "Data Card 22", "Data Card 23", "Data Card 24", 
"Data Card 25", "Data Card 26", "Data Card 27", "Jade Orb", "Lock Capsule", "Red Orb", "Blue Orb", "Enigma Stone", "Prism Scale", "Eviolite", 
"Float Stone", "Rocky Helmet", "Air Balloon", "Red Card", "Ring Target", "Binding Band", "Absorb Bulb", "Cell Battery", "Eject Button", "Fire Gem", 
"Water Gem", "Electric Gem", "Grass Gem", "Ice Gem", "Fighting Gem", "Poison Gem", "Ground Gem", "Flying Gem", "Psychic Gem", "Bug Gem", "Rock Gem", 
"Ghost Gem", "Dragon Gem", "Dark Gem", "Steel Gem", "Normal Gem", "Health Feather", "Muscle Feather", "Resist Feather", "Genius Feather", "Clever Feather", 
"Swift Feather", "Pretty Feather", "Cover Fossil", "Plume Fossil", "Liberty Pass", "Pass Orb", "Dream Ball", "Poké Toy", "Prop Case", "Dragon Skull", 
"Balm Mushroom", "Big Nugget", "Pearl String", "Comet Shard", "Relic Copper", "Relic Silver", "Relic Gold", "Relic Vase", "Relic Band", "Relic Statue", 
"Relic Crown", "Casteliacone", "Dire Hit 2", "X Speed 2", "X Sp. Atk 2", "X Sp. Def 2", "X Defense 2", "X Attack 2", "X Accuracy 2", "X Speed 3", 
"X Sp. Atk 3", "X Sp. Def 3", "X Defense 3", "X Attack 3", "X Accuracy 3", "X Speed 6", "X Sp. Atk 6", "X Sp. Def 6", "X Defense 6", "X Attack 6", 
"X Accuracy 6", "Ability Urge", "Item Drop", "Item Urge", "Reset Urge", "Dire Hit 3", "Light Stone", "Dark Stone", "TM93", "TM94", "TM95", "Xtransceiver", 
"???", "Gram 1", "Gram 2", "Gram 3", "Xtransceiver", "Medal Box", "DNA Splicers", "DNA Splicers", "Permit", "Oval Charm", "Shiny Charm", "Plasma Card", 
"Grubby Hanky", "Colress Machine", "Dropped Item", "Dropped Item", "Reveal Glass", "Weakness Policy", "Assault Vest", "Holo Caster", "Prof's Letter", 
"Roller Skates", "Pixie Plate", "Ability Capsule", "Whipped Dream", "Sachet", "Luminous Moss", "Snowball", "Safety Goggles", "Poké Flute", "Rich Mulch", 
"Surprise Mulch", "Boost Mulch", "Amaze Mulch", "Gengarite", "Gardevoirite", "Ampharosite", "Venusaurite", "Charizardite X", "Blastoisinite", "Mewtwonite X", 
"Mewtwonite Y", "Blazikenite", "Medichamite", "Houndoominite", "Aggronite", "Banettite", "Tyranitarite", "Scizorite", "Pinsirite", "Aerodactylite", 
"Lucarionite", "Abomasite", "Kangaskhanite", "Gyaradosite", "Absolite", "Charizardite Y", "Alakazite", "Heracronite", "Mawilite", "Manectite", "Garchompite", 
"Latiasite", "Latiosite", "Roseli Berry", "Kee Berry", "Maranga Berry", "Sprinklotad", "TM96", "TM97", "TM98", "TM99", "TM100", "Power Plant Pass", 
"Mega Ring", "Intriguing Stone", "Common Stone", "Discount Coupon", "Elevator Key", "TMV Pass", "Honor of Kalos", "Adventure Guide", "Strange Souvenir", 
"Lens Case", "Makeup Bag", "Travel Trunk", "Lumiose Galette", "Shalour Sable", "Jaw Fossil", "Sail Fossil", "Looker Ticket", "Bike", "Holo Caster", 
"Fairy Gem", "Mega Charm", "Mega Glove", "Mach Bike", "Acro Bike", "Wailmer Pail", "Devon Parts", "Soot Sack", "Basement Key", "Pokéblock Kit", "Letter", 
"Eon Ticket", "Scanner", "Go-Goggles", "Meteorite", "Key to Room 1", "Key to Room 2", "Key to Room 4", "Key to Room 6", "Storage Key", "Devon Scope", 
"S.S. Ticket", "HM07", "Devon Scuba Gear", "Contest Costume", "Contest Costume", "Magma Suit", "Aqua Suit", "Pair of Tickets", "Mega Bracelet", 
"Mega Pendant", "Mega Glasses", "Mega Anchor", "Mega Stickpin", "Mega Tiara", "Mega Anklet", "Meteorite", "Swampertite", "Sceptilite", "Sablenite", 
"Altarianite", "Galladite", "Audinite", "Metagrossite", "Sharpedonite", "Slowbronite", "Steelixite", "Pidgeotite", "Glalitite", "Diancite", 
"Prison Bottle", "Mega Cuff", "Cameruptite", "Lopunnite", "Salamencite", "Beedrillite", "Meteorite", "Meteorite", "Key Stone", "Meteorite Shard", 
"Eon Flute", "Normalium Z", "Firium Z", "Waterium Z", "Electrium Z", "Grassium Z", "Icium Z", "Fightinium Z", "Poisonium Z", "Groundium Z", 
"Flyinium Z", "Psychium Z", "Buginium Z", "Rockium Z", "Ghostium Z", "Dragonium Z", "Darkinium Z", "Steelium Z", "Fairium Z", "Pikanium Z", 
"Bottle Cap", "Gold Bottle Cap", "Z-Ring", "Decidium Z", "Incinium Z", "Primarium Z", "Tapunium Z", "Marshadium Z", "Aloraichium Z", "Snorlium Z", 
"Eevium Z", "Mewnium Z", "Normalium Z", "Firium Z", "Waterium Z", "Electrium Z", "Grassium Z", "Icium Z", "Fightinium Z", "Poisonium Z", 
"Groundium Z", "Flyinium Z", "Psychium Z", "Buginium Z", "Rockium Z", "Ghostium Z", "Dragonium Z", "Darkinium Z", "Steelium Z", "Fairium Z", 
"Pikanium Z", "Decidium Z", "Incinium Z", "Primarium Z", "Tapunium Z", "Marshadium Z", "Aloraichium Z", "Snorlium Z", "Eevium Z", "Mewnium Z", 
"Pikashunium Z", "Pikashunium Z", "???", "???", "???", "???", "Forage Bag", "Fishing Rod", "Professor's Mask", "Festival Ticket", "Sparkling Stone", 
"Adrenaline Orb", "Zygarde Cube", "???", "Ice Stone", "Ride Pager", "Beast Ball", "Big Malasada", "Red Nectar", "Yellow Nectar", "Pink Nectar", 
"Purple Nectar", "Sun Flute", "Moon Flute", "???", "Enigmatic Card", "Silver Razz Berry", "Golden Razz Berry", "Silver Nanab Berry", 
"Golden Nanab Berry", "Silver Pinap Berry", "Golden Pinap Berry", "???", "???", "???", "???", "???", "Secret Key", "S.S. Ticket", "Silph Scope", 
"Parcel", "Card Key", "Gold Teeth", "Lift Key", "Terrain Extender", "Protective Pads", "Electric Seed", "Psychic Seed", "Misty Seed", 
"Grassy Seed", "Stretchy Spring", "Chalky Stone", "Marble", "Lone Earring", "Beach Glass", "Gold Leaf", "Silver Leaf", "Polished Mud Ball", 
"Tropical Shell", "Leaf Letter", "Leaf Letter", "Small Bouquet", "???", "???", "???", "Lure", "Super Lure", "Max Lure", "Pewter Crunchies", 
"Fighting Memory", "Flying Memory", "Poison Memory", "Ground Memory", "Rock Memory", "Bug Memory", "Ghost Memory", "Steel Memory", "Fire Memory", 
"Water Memory", "Grass Memory", "Electric Memory", "Psychic Memory", "Ice Memory", "Dragon Memory", "Dark Memory", "Fairy Memory", "Solganium Z", 
"Lunalium Z", "Ultranecrozium Z", "Mimikium Z", "Lycanium Z", "Kommonium Z", "Solganium Z", "Lunalium Z", "Ultranecrozium Z", "Mimikium Z", "Lycanium Z", 
"Kommonium Z", "Z-Power Ring", "Pink Petal", "Orange Petal", "Blue Petal", "Red Petal", "Green Petal", "Yellow Petal", "Purple Petal", "Rainbow Flower", 
"Surge Badge", "N-Solarizer", "N-Lunarizer", "N-Solarizer", "N-Lunarizer", "Ilima Normalium Z", "Left Poké Ball", "Roto Hatch", "Roto Bargain", 
"Roto Prize Money", "Roto Exp. Points", "Roto Friendship", "Roto Encounter", "Roto Stealth", "Roto HP Restore", "Roto PP Restore", "Roto Boost", 
"Roto Catch", "Health Candy", "Mighty Candy", "Tough Candy", "Smart Candy", "Courage Candy", "Quick Candy", "Health Candy L", "Mighty Candy L", 
"Tough Candy L", "Smart Candy L", "Courage Candy L", "Quick Candy L", "Health Candy XL", "Mighty Candy XL", "Tough Candy XL", "Smart Candy XL", 
"Courage Candy XL", "Quick Candy XL", "Bulbasaur Candy", "Charmander Candy", "Squirtle Candy", "Caterpie Candy", "Weedle Candy", "Pidgey Candy", 
"Rattata Candy", "Spearow Candy", "Ekans Candy", "Pikachu Candy", "Sandshrew Candy", "Nidoran♀ Candy", "Nidoran♂ Candy", "Clefairy Candy", "Vulpix Candy", 
"Jigglypuff Candy", "Zubat Candy", "Oddish Candy", "Paras Candy", "Venonat Candy", "Diglett Candy", "Meowth Candy", "Psyduck Candy", "Mankey Candy", 
"Growlithe Candy", "Poliwag Candy", "Abra Candy", "Machop Candy", "Bellsprout Candy", "Tentacool Candy", "Geodude Candy", "Ponyta Candy", "Slowpoke Candy", 
"Magnemite Candy", "Farfetch'd Candy", "Doduo Candy", "Seel Candy", "Grimer Candy", "Shellder Candy", "Gastly Candy", "Onix Candy", "Drowzee Candy", 
"Krabby Candy", "Voltorb Candy", "Exeggcute Candy", "Cubone Candy", "Hitmonlee Candy", "Hitmonchan Candy", "Lickitung Candy", "Koffing Candy", 
"Rhyhorn Candy", "Chansey Candy", "Tangela Candy", "Kangaskhan Candy", "Horsea Candy", "Goldeen Candy", "Staryu Candy", "Mr. Mime Candy", 
"Scyther Candy", "Jynx Candy", "Electabuzz Candy", "Magmar Candy", "Pinsir Candy", "Tauros Candy", "Magikarp Candy", "Lapras Candy", "Ditto Candy", 
"Eevee Candy", "Porygon Candy", "Omanyte Candy", "Kabuto Candy", "Aerodactyl Candy", "Snorlax Candy", "Articuno Candy", "Zapdos Candy", "Moltres Candy", 
"Dratini Candy", "Mewtwo Candy", "Mew Candy", "Meltan Candy", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", 
"???", "???", "???", "???", "Endorsement", "Pokémon Box Link", "Wishing Star", "Dynamax Band", "???", "???", "Fishing Rod", "Rotom Bike", "???", 
"???", "Sausages", "Bob's Food Tin", "Bach's Food Tin", "Tin of Beans", "Bread", "Pasta", "Mixed Mushrooms", "Smoke-Poke Tail", "Large Leek", 
"Fancy Apple", "Brittle Bones", "Pack of Potatoes", "Pungent Root", "Salad Mix", "Fried Food", "Boiled Egg", "Camping Gear", "???", "???", 
"Rusted Sword", "Rusted Shield", "Fossilized Bird", "Fossilized Fish", "Fossilized Drake", "Fossilized Dino", "Strawberry Sweet", "Love Sweet", 
"Berry Sweet", "Clover Sweet", "Flower Sweet", "Star Sweet", "Ribbon Sweet", "Sweet Apple", "Tart Apple", "Throat Spray", "Eject Pack", 
"Heavy-Duty Boots", "Blunder Policy", "Room Service", "Utility Umbrella", "Exp. Candy XS", "Exp. Candy S", "Exp. Candy M", "Exp. Candy L", 
"Exp. Candy XL", "Dynamax Candy", "TR00", "TR01", "TR02", "TR03", "TR04", "TR05", "TR06", "TR07", "TR08", "TR09", "TR10", "TR11", "TR12", 
"TR13", "TR14", "TR15", "TR16", "TR17", "TR18", "TR19", "TR20", "TR21", "TR22", "TR23", "TR24", "TR25", "TR26", "TR27", "TR28", "TR29", 
"TR30", "TR31", "TR32", "TR33", "TR34", "TR35", "TR36", "TR37", "TR38", "TR39", "TR40", "TR41", "TR42", "TR43", "TR44", "TR45", "TR46", 
"TR47", "TR48", "TR49", "TR50", "TR51", "TR52", "TR53", "TR54", "TR55", "TR56", "TR57", "TR58", "TR59", "TR60", "TR61", "TR62", "TR63", 
"TR64", "TR65", "TR66", "TR67", "TR68", "TR69", "TR70", "TR71", "TR72", "TR73", "TR74", "TR75", "TR76", "TR77", "TR78", "TR79", "TR80", 
"TR81", "TR82", "TR83", "TR84", "TR85", "TR86", "TR87", "TR88", "TR89", "TR90", "TR91", "TR92", "TR93", "TR94", "TR95", "TR96", "TR97", 
"TR98", "TR99", "TM00", "Lonely Mint", "Adamant Mint", "Naughty Mint", "Brave Mint", "Bold Mint", "Impish Mint", "Lax Mint", "Relaxed Mint", 
"Modest Mint", "Mild Mint", "Rash Mint", "Quiet Mint", "Calm Mint", "Gentle Mint", "Careful Mint", "Sassy Mint", "Timid Mint", "Hasty Mint", 
"Jolly Mint", "Naive Mint", "Serious Mint", "Wishing Piece", "Cracked Pot", "Chipped Pot", "Hi-tech Earbuds", "Fruit Bunch", "Moomoo Cheese", 
"Spice Mix", "Fresh Cream", "Packaged Curry", "Coconut Milk", "Instant Noodles", "Precooked Burger", "Gigantamix", "Wishing Chip", "Rotom Bike", 
"Catching Charm", "???", "Old Letter", "Band Autograph", "Sonia's Book", "???", "???", "???", "???", "???", "???", "Rotom Catalog", "★And458", 
"★And15", "★And337", "★And603", "★And390", "★Sgr6879", "★Sgr6859", "★Sgr6913", "★Sgr7348", "★Sgr7121", "★Sgr6746", "★Sgr7194", "★Sgr7337", 
"★Sgr7343", "★Sgr6812", "★Sgr7116", "★Sgr7264", "★Sgr7597", "★Del7882", "★Del7906", "★Del7852", "★Psc596", "★Psc361", "★Psc510", "★Psc437", 
"★Psc8773", "★Lep1865", "★Lep1829", "★Boo5340", "★Boo5506", "★Boo5435", "★Boo5602", "★Boo5733", "★Boo5235", "★Boo5351", "★Hya3748", "★Hya3903", 
"★Hya3418", "★Hya3482", "★Hya3845", "★Eri1084", "★Eri472", "★Eri1666", "★Eri897", "★Eri1231", "★Eri874", "★Eri1298", "★Eri1325", "★Eri984", 
"★Eri1464", "★Eri1393", "★Eri850", "★Tau1409", "★Tau1457", "★Tau1165", "★Tau1791", "★Tau1910", "★Tau1346", "★Tau1373", "★Tau1412", "★CMa2491", 
"★CMa2693", "★CMa2294", "★CMa2827", "★CMa2282", "★CMa2618", "★CMa2657", "★CMa2646", "★UMa4905", "★UMa4301", "★UMa5191", "★UMa5054", "★UMa4295", 
"★UMa4660", "★UMa4554", "★UMa4069", "★UMa3569", "★UMa3323", "★UMa4033", "★UMa4377", "★UMa4375", "★UMa4518", "★UMa3594", "★Vir5056", "★Vir4825", 
"★Vir4932", "★Vir4540", "★Vir4689", "★Vir5338", "★Vir4910", "★Vir5315", "★Vir5359", "★Vir5409", "★Vir5107", "★Ari617", "★Ari553", "★Ari546", 
"★Ari951", "★Ori1713", "★Ori2061", "★Ori1790", "★Ori1903", "★Ori1948", "★Ori2004", "★Ori1852", "★Ori1879", "★Ori1899", "★Ori1543", "★Cas21", 
"★Cas168", "★Cas403", "★Cas153", "★Cas542", "★Cas219", "★Cas265", "★Cnc3572", "★Cnc3208", "★Cnc3461", "★Cnc3449", "★Cnc3429", "★Cnc3627", 
"★Cnc3268", "★Cnc3249", "★Com4968", "★Crv4757", "★Crv4623", "★Crv4662", "★Crv4786", "★Aur1708", "★Aur2088", "★Aur1605", "★Aur2095", "★Aur1577", 
"★Aur1641", "★Aur1612", "★Pav7790", "★Cet911", "★Cet681", "★Cet188", "★Cet539", "★Cet804", "★Cep8974", "★Cep8162", "★Cep8238", "★Cep8417", 
"★Cen5267", "★Cen5288", "★Cen551", "★Cen5459", "★Cen5460", "★CMi2943", "★CMi2845", "★Equ8131", "★Vul7405", "★UMi424", "★UMi5563", "★UMi5735", 
"★UMi6789", "★Crt4287", "★Lyr7001", "★Lyr7178", "★Lyr7106", "★Lyr7298", "★Ara6585", "★Sco6134", "★Sco6527", "★Sco6553", "★Sco5953", "★Sco5984", 
"★Sco6508", "★Sco6084", "★Sco5944", "★Sco6630", "★Sco6027", "★Sco6247", "★Sco6252", "★Sco5928", "★Sco6241", "★Sco6165", "★Tri544", "★Leo3982", 
"★Leo4534", "★Leo4357", "★Leo4057", "★Leo4359", "★Leo4031", "★Leo3852", "★Leo3905", "★Leo3773", "★Gru8425", "★Gru8636", "★Gru8353", "★Lib5685", 
"★Lib5531", "★Lib5787", "★Lib5603", "★Pup3165", "★Pup3185", "★Pup3045", "★Cyg7924", "★Cyg7417", "★Cyg7796", "★Cyg8301", "★Cyg7949", "★Cyg7528", 
"★Oct7228", "★Col1956", "★Col2040", "★Col2177", "★Gem2990", "★Gem2891", "★Gem2421", "★Gem2473", "★Gem2216", "★Gem2777", "★Gem2650", "★Gem2286", 
"★Gem2484", "★Gem2930", "★Peg8775", "★Peg8781", "★Peg39", "★Peg8308", "★Peg8650", "★Peg8634", "★Peg8684", "★Peg8450", "★Peg8880", "★Peg8905", 
"★Oph6556", "★Oph6378", "★Oph6603", "★Oph6149", "★Oph6056", "★Oph6075", "★Ser5854", "★Ser7141", "★Ser5879", "★Her6406", "★Her6148", "★Her6410", 
"★Her6526", "★Her6117", "★Her6008", "★Per936", "★Per1017", "★Per1131", "★Per1228", "★Per834", "★Per941", "★Phe99", "★Phe338", "★Vel3634", 
"★Vel3485", "★Vel3734", "★Aqr8232", "★Aqr8414", "★Aqr8709", "★Aqr8518", "★Aqr7950", "★Aqr8499", "★Aqr8610", "★Aqr8264", "★Cru4853", "★Cru4730", 
"★Cru4763", "★Cru4700", "★Cru4656", "★PsA8728", "★TrA6217", "★Cap7776", "★Cap7754", "★Cap8278", "★Cap8322", "★Cap7773", "★Sge7479", "★Car2326", 
"★Car3685", "★Car3307", "★Car3699", "★Dra5744", "★Dra5291", "★Dra6705", "★Dra6536", "★Dra7310", "★Dra6688", "★Dra4434", "★Dra6370", "★Dra7462", 
"★Dra6396", "★Dra6132", "★Dra6636", "★CVn4915", "★CVn4785", "★CVn4846", "★Aql7595", "★Aql7557", "★Aql7525", "★Aql7602", "★Aql7235", "Max Honey", 
"Max Mushrooms", "Galarica Twig", "Galarica Cuff", "Style Card", "Armor Pass", "Rotom Bike", "Rotom Bike", "Exp. Charm", "Armorite Ore", "Mark Charm", 
"Reins of Unity", "Reins of Unity", "Galarica Wreath", "Legendary Clue 1", "Legendary Clue 2", "Legendary Clue 3", "Legendary Clue?", "Crown Pass", 
"Wooden Crown", "Radiant Petal", "White Mane Hair", "Black Mane Hair", "Iceroot Carrot", "Shaderoot Carrot", "Dynite Ore", "Carrot Seeds", "Ability Patch", 
"Reins of Unity" ]
]

# gender ratios by dex number, number = % chance of being female (-1 = genderless)
genderratiomap = \
[ -1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 0, 0, 0, 0.75, 0.75, 0.75, 0.75, \
0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, \
0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, -1, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, -1, -1, 0.5, 0.5, 0.5, 0.5, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, -1, -1, \
0.5, 0.5, 1, 0.25, 0.25, 0.5, 0, 0.5, 0.5, 0.5, -1, 0.125, 0.125, 0.125, 0.125, -1, 0.125, 0.125, 0.125, \
0.125, 0.125, 0.125, -1, -1, -1, 0.5, 0.5, 0.5, -1, -1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, \
0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.125, 0.125, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.125, 0.125, \
0.5, 0.5, 0.5, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, 0.5, 0.5, 0, 0, 1, 0.25, 0.25, \
1, 1, -1, -1, -1, 0.5, 0.5, 0.5, -1, -1, -1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.75, 0.5, 0.75, 0.75, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, 0.5, 0.5, 0.5, 0.5, -1, -1, 0.125, \
0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.125, 0.75, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, -1, -1, 0.125, 0.125, \
0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.125, 0.125, 0.125, 0.125, 0.5, 1, 0, 0.125, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.5, 0.5, 0.5, -1, -1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.125, 0.125, \
0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, 0.5, 0.5, 0.5, 0.25, 0.25, \
0.125, 0.5, 0.125, 0.125, 0.5, 0.5, -1, 0, 0.5, 0.5, 1, -1, -1, -1, -1, -1, -1, 0.5, -1, -1, 1, -1, -1, \
-1, -1, -1, -1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.125, 0.125, 0.125, 0.125, \
0.5, 0.5, 0.125, 0.125, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, 0.5, 0.5, 0.5, 0, 0, 1, 1, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, 0, 0, -1, -1, 0, -1, -1, -1, -1, 0.125, 0.125, 0.125, \
0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.875, 0.875, 1, 1, \
1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, \
0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.125, 1, 0.5, 0.5, 1, 1, 1, 0.75, 0.5, 0.5, 0.5, 0.5, \
0.5, 0.5, 0.5, -1, -1, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -1, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, \
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0.125, 0.125, 0.125, 0.125,\
 0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, \
 0.5, 0.5, -1, -1, 1, 1, 1, 0, 0, 0, 0.5, 0.5, 0.75, 0.5, 0.5, 0.5, 1, 1, -1, 0.5, 0.5, 0.5, 0.5, \
 0.5, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, -1, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, 0.125, 0.125, -1, -1, -1, \
 -1, -1, -1 ] 
 
abilities = \
[ "None", "Stench", "Drizzle", "Speed Boost", "Battle Armor", "Sturdy", "Damp", "Limber", "Sand Veil", \
"Static", "Volt Absorb", "Water Absorb", "Oblivious", "Cloud Nine", "Compound Eyes", "Insomnia", "Color Change", \
"Immunity", "Flash Fire", "Shield Dust", "Own Tempo", "Suction Cups", "Intimidate", "Shadow Tag", "Rough Skin", \
"Wonder Guard", "Levitate", "Effect Spore", "Synchronize", "Clear Body", "Natural Cure", "Lightning Rod", \
"Serene Grace", "Swift Swim", "Chlorophyll", "Illuminate", "Trace", "Huge Power", "Poison Point", "Inner Focus", \
"Magma Armor", "Water Veil", "Magnet Pull", "Soundproof", "Rain Dish", "Sand Stream", "Pressure", "Thick Fat", \
"Early Bird", "Flame Body", "Run Away", "Keen Eye", "Hyper Cutter", "Pickup", "Truant", "Hustle", "Cute Charm", \
"Plus", "Minus", "Forecast", "Sticky Hold", "Shed Skin", "Guts", "Marvel Scale", "Liquid Ooze", "Overgrow", \
"Blaze", "Torrent", "Swarm", "Rock Head", "Drought", "Arena Trap", "Vital Spirit", "White Smoke", "Pure Power", \
"Shell Armor", "Air Lock", "Tangled Feet", "Motor Drive", "Rivalry", "Steadfast", "Snow Cloak", "Gluttony", \
"Anger Point", "Unburden", "Heatproof", "Simple", "Dry Skin", "Download", "Iron Fist", "Poison Heal", \
"Adaptability", "Skill Link", "Hydration", "Solar Power", "Quick Feet", "Normalize", "Sniper", "Magic Guard", \
"No Guard", "Stall", "Technician", "Leaf Guard", "Klutz", "Mold Breaker", "Super Luck", "Aftermath", "Anticipation", \
"Forewarn", "Unaware", "Tinted Lens", "Filter", "Slow Start", "Scrappy", "Storm Drain", "Ice Body", "Solid Rock", \
"Snow Warning", "Honey Gather", "Frisk", "Reckless", "Multitype", "Flower Gift", "Bad Dreams", "Pickpocket", \
"Sheer Force", "Contrary", "Unnerve", "Defiant", "Defeatist", "Cursed Body", "Healer", "Friend Guard", \
"Weak Armor", "Heavy Metal", "Light Metal", "Multiscale", "Toxic Boost", "Flare Boost", "Harvest", "Telepathy", \
"Moody", "Overcoat", "Poison Touch", "Regenerator", "Big Pecks", "Sand Rush", "Wonder Skin", "Analytic", \
"Illusion", "Imposter", "Infiltrator", "Mummy", "Moxie", "Justified", "Rattled", "Magic Bounce", "Sap Sipper", \
"Prankster", "Sand Force", "Iron Barbs", "Zen Mode", "Victory Star", "Turboblaze", "Teravolt", "Aroma Veil", \
"Flower Veil", "Cheek Pouch", "Protean", "Fur Coat", "Magician", "Bulletproof", "Competitive", "Strong Jaw", \
"Refrigerate", "Sweet Veil", "Stance Change", "Gale Wings", "Mega Launcher", "Grass Pelt", "Symbiosis", "Tough Claws", \
"Pixilate", "Gooey", "Aerilate", "Parental Bond", "Dark Aura", "Fairy Aura", "Aura Break", "Primordial Sea", \
"Desolate Land", "Delta Stream", "Stamina", "Wimp Out", "Emergency Exit", "Water Compaction", "Merciless", \
"Shields Down", "Stakeout", "Water Bubble", "Steelworker", "Berserk", "Slush Rush", "Long Reach", "Liquid Voice", \
"Triage", "Galvanize", "Surge Surfer", "Schooling", "Disguise", "Battle Bond", "Power Construct", "Corrosion", \
"Comatose", "Queenly Majesty", "Innards Out", "Dancer", "Battery", "Fluffy", "Dazzling", "Soul-Heart", "Tangling Hair", \
"Receiver", "Power of Alchemy", "Beast Boost", "RKS System", "Electric Surge", "Psychic Surge", "Misty Surge", \
"Grassy Surge", "Full Metal Body", "Shadow Shield", "Prism Armor", "Neuroforce", "Intrepid Sword", "Dauntless Shield", \
"Libero", "Ball Fetch", "Cotton Down", "Propeller Tail", "Mirror Armor", "Gulp Missile", "Stalwart", "Steam Engine", \
"Punk Rock", "Sand Spit", "Ice Scales", "Ripen", "Ice Face", "Power Spot", "Mimicry", "Screen Cleaner", "Steely Spirit", \
"Perish Body", "Wandering Spirit", "Gorilla Tactics", "Neutralizing Gas", "Pastel Veil", "Hunger Switch", "Quick Draw", \
"Unseen Fist", "Curious Medicine", "Transistor", "Dragon's Maw", "Chilling Neigh", "Grim Neigh", "As One", "As One" ]

species_names = [ "?", "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", \
"Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", \
"Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", \
"Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", \
"Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", \
"Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", \
"Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", \
"Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", \
"Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", \
"Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", \
"Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", \
"Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", \
"Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", \
"Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", \
"Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", \
"Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", \
"Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", \
"Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", \
"Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", \
"Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", \
"Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", \
"Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", \
"Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", \
"Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", \
"Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", \
"Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", \
"Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", \
"Kirlia", "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", \
"Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", \
"Delcatty", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", \
"Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", \
"Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", \
"Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", \
"Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet", 
"Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", \
"Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", \
"Metagross", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", \
"Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", \
"Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", \
"Rampardos", "Shieldon", "Bastiodon", "Burmy", "Wormadam", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", \
"Cherubi", "Cherrim", "Shellos", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Mismagius", "Honchkrow", \
"Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny", "Chatot", \
"Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax", "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", \
"Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", \
"Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", \
"Porygon-Z", "Gallade", "Probopass", "Dusknoir", "Froslass", "Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", \
"Regigigas", "Giratina", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus", "Victini", "Snivy", "Servine", \
"Serperior", "Tepig", "Pignite", "Emboar", "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog", "Lillipup", "Herdier", \
"Stoutland", "Purrloin", "Liepard", "Pansage", "Simisage", "Pansear", "Simisear", "Panpour", "Simipour", "Munna", "Musharna", \
"Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika", "Roggenrola", "Boldore", "Gigalith", "Woobat", "Swoobat", "Drilbur", \
"Excadrill", "Audino", "Timburr", "Gurdurr", "Conkeldurr", "Tympole", "Palpitoad", "Seismitoad", "Throh", "Sawk", "Sewaddle", \
"Swadloon", "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Cottonee", "Whimsicott", "Petilil", "Lilligant", "Basculin", \
"Sandile", "Krokorok", "Krookodile", "Darumaka", "Darmanitan", "Maractus", "Dwebble", "Crustle", "Scraggy", "Scrafty", "Sigilyph", \
"Yamask", "Cofagrigus", "Tirtouga", "Carracosta", "Archen", "Archeops", "Trubbish", "Garbodor", "Zorua", "Zoroark", "Minccino", \
"Cinccino", "Gothita", "Gothorita", "Gothitelle", "Solosis", "Duosion", "Reuniclus", "Ducklett", "Swanna", "Vanillite", "Vanillish", \
"Vanilluxe", "Deerling", "Sawsbuck", "Emolga", "Karrablast", "Escavalier", "Foongus", "Amoonguss", "Frillish", "Jellicent", \
"Alomomola", "Joltik", "Galvantula", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang", "Tynamo", "Eelektrik", "Eelektross", \
"Elgyem", "Beheeyem", "Litwick", "Lampent", "Chandelure", "Axew", "Fraxure", "Haxorus", "Cubchoo", "Beartic", "Cryogonal", \
"Shelmet", "Accelgor", "Stunfisk", "Mienfoo", "Mienshao", "Druddigon", "Golett", "Golurk", "Pawniard", "Bisharp", "Bouffalant", \
"Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Heatmor", "Durant", "Deino", "Zweilous", "Hydreigon", "Larvesta", "Volcarona", \
"Cobalion", "Terrakion", "Virizion", "Tornadus", "Thundurus", "Reshiram", "Zekrom", "Landorus", "Kyurem", "Keldeo", "Meloetta", 
"Genesect", "Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen", "Delphox", "Froakie", "Frogadier", "Greninja", "Bunnelby", \
"Diggersby", "Fletchling", "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Litleo", "Pyroar", "Flabébé", \
"Floette", "Florges", "Skiddo", "Gogoat", "Pancham", "Pangoro", "Furfrou", "Espurr", "Meowstic", "Honedge", "Doublade", "Aegislash", \
"Spritzee", "Aromatisse", "Swirlix", "Slurpuff", "Inkay", "Malamar", "Binacle", "Barbaracle", "Skrelp", "Dragalge", "Clauncher", \
"Clawitzer", "Helioptile", "Heliolisk", "Tyrunt", "Tyrantrum", "Amaura", "Aurorus", "Sylveon", "Hawlucha", "Dedenne", "Carbink", \
"Goomy", "Sliggoo", "Goodra", "Klefki", "Phantump", "Trevenant", "Pumpkaboo", "Gourgeist", "Bergmite", "Avalugg", "Noibat", "Noivern", \
"Xerneas", "Yveltal", "Zygarde", "Diancie", "Hoopa", "Volcanion", "Rowlet", "Dartrix", "Decidueye", "Litten", "Torracat", "Incineroar", \
"Popplio", "Brionne", "Primarina", "Pikipek", "Trumbeak", "Toucannon", "Yungoos", "Gumshoos", "Grubbin", "Charjabug", "Vikavolt", \
"Crabrawler", "Crabominable", "Oricorio", "Cutiefly", "Ribombee", "Rockruff", "Lycanroc", "Wishiwashi", "Mareanie", "Toxapex", \
"Mudbray", "Mudsdale", "Dewpider", "Araquanid", "Fomantis", "Lurantis", "Morelull", "Shiinotic", "Salandit", "Salazzle", "Stufful", \
"Bewear", "Bounsweet", "Steenee", "Tsareena", "Comfey", "Oranguru", "Passimian", "Wimpod", "Golisopod", "Sandygast", "Palossand", \
"Pyukumuku", "Type: Null", "Silvally", "Minior", "Komala", "Turtonator", "Togedemaru", "Mimikyu", "Bruxish", "Drampa", "Dhelmise", \
"Jangmo-o", "Hakamo-o", "Kommo-o", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", \
"Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna", "Marshadow", "Poipole", \
"Naganadel", "Stakataka", "Blacephalon", "Zeraora", "Meltan", "Melmetal", "Grookey", "Thwackey", "Rillaboom", "Scorbunny", "Raboot", \
"Cinderace", "Sobble", "Drizzile", "Inteleon", "Skwovet", "Greedent", "Rookidee", "Corvisquire", "Corviknight", "Blipbug", "Dottler", \
"Orbeetle", "Nickit", "Thievul", "Gossifleur", "Eldegoss", "Wooloo", "Dubwool", "Chewtle", "Drednaw", "Yamper", "Boltund", "Rolycoly", \
"Carkol", "Coalossal", "Applin", "Flapple", "Appletun", "Silicobra", "Sandaconda", "Cramorant", "Arrokuda", "Barraskewda", "Toxel", \
"Toxtricity", "Sizzlipede", "Centiskorch", "Clobbopus", "Grapploct", "Sinistea", "Polteageist", "Hatenna", "Hattrem", "Hatterene", \
"Impidimp", "Morgrem", "Grimmsnarl", "Obstagoon", "Perrserker", "Cursola", "Sirfetch'd", "Mr. Rime", "Runerigus", "Milcery", \
"Alcremie", "Falinks", "Pincurchin", "Snom", "Frosmoth", "Stonjourner", "Eiscue", "Indeedee", "Morpeko", "Cufant", "Copperajah", \
"Dracozolt", "Arctozolt", "Dracovish", "Arctovish", "Duraludon", "Dreepy", "Drakloak", "Dragapult", "Zacian", "Zamazenta", \
"Eternatus", "Kubfu", "Urshifu", "Zarude", "Regieleki", "Regidrago", "Glastrier", "Spectrier", "Calyrex" ]

# Gen III map of "growth" data location, based on the PID
gen3_subs = [ \
[0,1,2,3], \
[0,1,3,2], \
[0,2,1,3], \
[0,2,3,1], \
[0,3,1,2], \
[0,3,2,1], \
[1,0,2,3], \
[1,0,3,2], \
[1,2,0,3], \
[1,2,3,0], \
[1,3,0,2], \
[1,3,2,0], \
[2,0,1,3], \
[2,0,3,1], \
[2,1,0,3], \
[2,1,3,0], \
[2,3,0,1], \
[2,3,1,0], \
[3,0,1,2], \
[3,0,2,1], \
[3,1,0,2], \
[3,1,2,0], \
[3,2,0,1], \
[3,2,1,0]  \
]


# Gym leader names (no longer used)
badges = [ \
[ "Br", "Mi", "LS", "Er", "Ko", "Sa", "Bl", "Bu" ],
[ "Fa", "Bu", "Wh", "Mo", "Ch", "Ja", "Pr", "Cl", "LS", "Sa", "Mi", "Er", "Jn", "Br", "Bl", "Bu" ],
[ "Ro", "Br", "Wa", "Fl", "No", "Wi", "TL", "W/J"],
[ "Ro", "Ga", "Ma", "CW", "Fa", "By", "Ca", "Vo"],
[ "Ch", "Ro", "Bu", "El", "Cl", "Sk", "Dr", "Ma"]
]

# Gen 3 ability map by National Dex #
gen3_abilities = [[0,0], [65, 0], [65, 0], [65, 0], [66, 0], [66, 0], [66, 0], [67, 0], [67, 0], [67, 0], [19, 0], [61, 0], [14, 0], \
[19, 0], [61, 0], [68, 0], [51, 0], [51, 0], [51, 0], [50, 62], [50, 62], [51, 0], [51, 0], [22, 61], [22, 61], [9, 0], [9, 0], [8, 0], \
[8, 0], [38, 0], [38, 0], [38, 0], [38, 0], [38, 0], [38, 0], [56, 0], [56, 0], [18, 0], [18, 0], [56, 0], [56, 0], [39, 0], [39, 0], \
[34, 0], [34, 0], [34, 0], [27, 0], [27, 0], [14, 0], [19, 0], [8, 71], [8, 71], [53, 0], [7, 0], [6, 13], [6, 13], [72, 0], [72, 0], \
[22, 18], [22, 18], [11, 6], [11, 6], [11, 6], [28, 39], [28, 39], [28, 39], [62, 0], [62, 0], [62, 0], [34, 0], [34, 0], [34, 0], \
[29, 64], [29, 64], [69, 5], [69, 5], [69, 5], [50, 18], [50, 18], [12, 20], [12, 20], [42, 5], [42, 5], [51, 39], [50, 48], [50, 48], \
[47, 0], [47, 0], [1, 60], [1, 60], [75, 0], [75, 0], [26, 0], [26, 0], [130, 0], [69, 5], [15, 0], [15, 0], [52, 75], [52, 75], [43, 9], \
[43, 9], [34, 0], [34, 0], [69, 31], [69, 31], [7, 0], [51, 0], [20, 12], [26, 0], [26, 0], [31, 69], [31, 69], [30, 32], [34, 0], \
[48, 0], [33, 0], [38, 0], [33, 41], [33, 41], [35, 30], [35, 30], [43, 0], [68, 0], [12, 0], [9, 0], [49, 0], [52, 0], [22, 0], [33, 0], \
[22, 0], [11, 75], [7, 0], [50, 0], [11, 0], [10, 0], [18, 0], [36, 0], [33, 75], [33, 75], [33, 4], [33, 4], [69, 46], [17, 47], \
[46, 0], [46, 0], [46, 0], [61, 0], [61, 0], [39, 0], [46, 0], [28, 0], [65, 0], [65, 0], [65, 0], [66, 0], [66, 0], [66, 0], [67, 0], \
[67, 0], [67, 0], [50, 51], [50, 51], [15, 51], [15, 51], [68, 48], [68, 48], [68, 15], [68, 15], [39, 0], [10, 35], [10, 35], [9, 0], \
[56, 0], [56, 0], [55, 32], [55, 32], [28, 48], [28, 48], [9, 0], [9, 0], [9, 0], [34, 0], [47, 37], [47, 37], [5, 69], [11, 6], [34, 0], \
[34, 0], [34, 0], [50, 53], [34, 0], [34, 0], [3, 14], [6, 11], [6, 11], [28, 0], [28, 0], [15, 0], [12, 20], [26, 0], [26, 0], [23, 0], \
[39, 48], [5, 0], [5, 0], [32, 50], [52, 8], [69, 5], [22, 50], [22, 0], [38, 33], [68, 0], [5, 0], [68, 62], [39, 51], [53, 0], [62, 0], \
[40, 49], [40, 49], [12, 0], [12, 0], [55, 30], [55, 0], [21, 0], [72, 55], [33, 11], [51, 5], [48, 18], [48, 18], [33, 0], [53, 0], [5, 0], \
[36, 0], [22, 0], [20, 0], [62, 0], [22, 0], [12, 0], [9, 0], [49, 0], [47, 0], [30, 32], [46, 0], [46, 0], [46, 0], [62, 0], [61, 0], \
[45, 0], [46, 0], [46, 0], [30, 0], [65, 0], [65, 0], [65, 0], [66, 0], [66, 0], [66, 0], [67, 0], [67, 0], [67, 0], [50, 0], [22, 0], \
[53, 0], [53, 0], [19, 0], [61, 0], [68, 0], [61, 0], [19, 0], [33, 44], [33, 44], [33, 44], [34, 48], [34, 48], [34, 48], [62, 0], \
[62, 0], [51, 0], [51, 0], [28, 36], [28, 36], [28, 36], [33, 0], [22, 0], [27, 0], [27, 0], [54, 0], [72, 0], [54, 0], [14, 0], \
[3, 0], [25, 0], [43, 0], [43, 0], [43, 0], [47, 62], [47, 62], [47, 37], [5, 42], [56, 0], [56, 0], [51, 0], [52, 22], [5, 69], \
[5, 69], [5, 69], [74, 0], [74, 0], [9, 31], [9, 31], [57, 0], [58, 0], [35, 68], [12, 0], [30, 38], [64, 60], [64, 60], [24, 0], \
[24, 0], [41, 12], [41, 12], [12, 0], [40, 0], [73, 0], [47, 20], [47, 20], [20, 0], [52, 71], [26, 0], [26, 0], [8, 0], [8, 0], \
[30, 0], [30, 0], [17, 0], [61, 0], [26, 0], [26, 0], [12, 0], [12, 0], [52, 75], [52, 75], [26, 0], [26, 0], [21, 0], [21, 0], \
[4, 0], [4, 0], [33, 0], [63, 0], [59, 0], [16, 0], [15, 0], [15, 0], [26, 0], [46, 0], [34, 0], [26, 0], [46, 0], [23, 0], [39, 0], \
[39, 0], [47, 0], [47, 0], [47, 0], [75, 0], [33, 0], [33, 0], [33, 69], [33, 0], [69, 0], [69, 0], [22, 0], [29, 0], [29, 0], \
[29, 0], [29, 0], [29, 0], [29, 0], [26, 0], [26, 0], [2, 0], [70, 0], [76, 0], [32, 0], [46, 0]]

# Radical Red adds new Pokemon and also overrides some existing abilities
radicalred_abilities = {
"183": [37, 157], # Marill
"184": [37, 157], # Azumarill
"207": [52 , 17], # Gligar
"396": [22, 0], # Starly
"397": [22, 0], # Staravia
"398": [22, 0], # Staraptor
"472": [52, 17], # Gliscor
"479": [26, 0], # Rotom
"479_1": [26, 0], # Rotom Heat
"479_2": [26, 0], # Rotom Wash
"479_3": [26, 0], # Rotom Frost
"479_4": [26, 0], # Rotom Fan
"480_4": [26, 0], # Rotom Mow
"535": [93, 33], # Tympole
"536": [93, 33], # Palpitoad
"537": [93, 33], # Seismitoad
"551": [22, 153], # Sandile
"552": [22, 153], # Krokorok
"553": [22, 153], # Krookodile
"607": [18, 23], # Litwick
"608": [18, 23], # Chandelure
}

# Radical Red adds new items and possibly may override some
radicalred_items = {
700: 538, # Eviolite
}

abilityass = [ ["Overgrow", "None"],\
["Overgrow", "None"],\
["Overgrow", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Shield Dust", "None"],\
["Shed Skin", "None"],\
["Compound Eyes", "None"],\
["Shield Dust", "None"],\
["Shed Skin", "None"],\
["Swarm", "None"],\
["Keen Eye", "None"],\
["Keen Eye", "None"],\
["Keen Eye", "None"],\
["Run Away", "Guts"],\
["Run Away", "Guts"],\
["Keen Eye", "None"],\
["Keen Eye", "None"],\
["Intimidate", "Shed Skin"],\
["Intimidate", "Shed Skin"],\
["Static", "None"],\
["Static", "None"],\
["Sand Veil", "None"],\
["Sand Veil", "None"],\
["Poison Point", "None"],\
["Poison Point", "None"],\
["Poison Point", "None"],\
["Poison Point", "None"],\
["Poison Point", "None"],\
["Poison Point", "None"],\
["Cute Charm", "None"],\
["Cute Charm", "None"],\
["Flash Fire", "None"],\
["Flash Fire", "None"],\
["Cute Charm", "None"],\
["Cute Charm", "None"],\
["Inner Focus", "None"],\
["Inner Focus", "None"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Effect Spore", "None"],\
["Effect Spore", "None"],\
["Compound Eyes", "None"],\
["Shield Dust", "None"],\
["Sand Veil", "Arena Trap"],\
["Sand Veil", "Arena Trap"],\
["Pickup", "None"],\
["Limber", "None"],\
["Damp", "Cloud Nine"],\
["Damp", "Cloud Nine"],\
["Vital Spirit", "None"],\
["Vital Spirit", "None"],\
["Intimidate", "Flash Fire"],\
["Intimidate", "Flash Fire"],\
["Water Absorb", "Damp"],\
["Water Absorb", "Damp"],\
["Water Absorb", "Damp"],\
["Synchronize", "Inner Focus"],\
["Synchronize", "Inner Focus"],\
["Synchronize", "Inner Focus"],\
["Guts", "None"],\
["Guts", "None"],\
["Guts", "None"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Clear Body", "Liquid Ooze"],\
["Clear Body", "Liquid Ooze"],\
["Rock Head", "Sturdy"],\
["Rock Head", "Sturdy"],\
["Rock Head", "Sturdy"],\
["Run Away", "Flash Fire"],\
["Run Away", "Flash Fire"],\
["Oblivious", "Own Tempo"],\
["Oblivious", "Own Tempo"],\
["Magnet Pull", "Sturdy"],\
["Magnet Pull", "Sturdy"],\
["Keen Eye", "Inner Focus"],\
["Run Away", "Early Bird"],\
["Run Away", "Early Bird"],\
["Thick Fat", "None"],\
["Thick Fat", "None"],\
["Stench", "Sticky Hold"],\
["Stench", "Sticky Hold"],\
["Shell Armor", "None"],\
["Shell Armor", "None"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Cursed Body", "None"],\
["Rock Head", "Sturdy"],\
["Insomnia", "None"],\
["Insomnia", "None"],\
["Hyper Cutter", "Shell Armor"],\
["Hyper Cutter", "Shell Armor"],\
["Soundproof", "Static"],\
["Soundproof", "Static"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Rock Head", "Lightning Rod"],\
["Rock Head", "Lightning Rod"],\
["Limber", "None"],\
["Keen Eye", "None"],\
["Own Tempo", "Oblivious"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Lightning Rod", "Rock Head"],\
["Lightning Rod", "Rock Head"],\
["Natural Cure", "Serene Grace"],\
["Chlorophyll", "None"],\
["Early Bird", "None"],\
["Swift Swim", "None"],\
["Poison Point", "None"],\
["Swift Swim", "Water Veil"],\
["Swift Swim", "Water Veil"],\
["Illuminate", "Natural Cure"],\
["Illuminate", "Natural Cure"],\
["Soundproof", "None"],\
["Swarm", "None"],\
["Oblivious", "None"],\
["Static", "None"],\
["Flame Body", "None"],\
["Hyper Cutter", "None"],\
["Intimidate", "None"],\
["Swift Swim", "None"],\
["Intimidate", "None"],\
["Water Absorb", "Shell Armor"],\
["Limber", "None"],\
["Run Away", "None"],\
["Water Absorb", "None"],\
["Volt Absorb", "None"],\
["Flash Fire", "None"],\
["Trace", "None"],\
["Swift Swim", "Shell Armor"],\
["Swift Swim", "Shell Armor"],\
["Swift Swim", "Battle Armor"],\
["Swift Swim", "Battle Armor"],\
["Rock Head", "Pressure"],\
["Immunity", "Thick Fat"],\
["Pressure", "None"],\
["Pressure", "None"],\
["Pressure", "None"],\
["Shed Skin", "None"],\
["Shed Skin", "None"],\
["Inner Focus", "None"],\
["Pressure", "None"],\
["Synchronize", "None"],\
["Overgrow", "None"],\
["Overgrow", "None"],\
["Overgrow", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Run Away", "Keen Eye"],\
["Run Away", "Keen Eye"],\
["Insomnia", "Keen Eye"],\
["Insomnia", "Keen Eye"],\
["Swarm", "Early Bird"],\
["Swarm", "Early Bird"],\
["Swarm", "Insomnia"],\
["Swarm", "Insomnia"],\
["Inner Focus", "None"],\
["Volt Absorb", "Illuminate"],\
["Volt Absorb", "Illuminate"],\
["Static", "None"],\
["Cute Charm", "None"],\
["Cute Charm", "None"],\
["Hustle", "Serene Grace"],\
["Hustle", "Serene Grace"],\
["Synchronize", "Early Bird"],\
["Synchronize", "Early Bird"],\
["Static", "None"],\
["Static", "None"],\
["Static", "None"],\
["Chlorophyll", "None"],\
["Thick Fat", "Huge Power"],\
["Thick Fat", "Huge Power"],\
["Sturdy", "Rock Head"],\
["Water Absorb", "Damp"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Run Away", "Pickup"],\
["Chlorophyll", "None"],\
["Chlorophyll", "None"],\
["Speed Boost", "Compound Eyes"],\
["Damp", "Water Absorb"],\
["Damp", "Water Absorb"],\
["Synchronize", "None"],\
["Synchronize", "None"],\
["Insomnia", "None"],\
["Oblivious", "Own Tempo"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Shadow Tag", "None"],\
["Inner Focus", "Early Bird"],\
["Sturdy", "None"],\
["Sturdy", "None"],\
["Serene Grace", "Run Away"],\
["Hyper Cutter", "Sand Veil"],\
["Rock Head", "Sturdy"],\
["Intimidate", "Run Away"],\
["Intimidate", "None"],\
["Poison Point", "Swift Swim"],\
["Swarm", "None"],\
["Sturdy", "None"],\
["Swarm", "Guts"],\
["Inner Focus", "Keen Eye"],\
["Pickup", "None"],\
["Guts", "None"],\
["Magma Armor", "Flame Body"],\
["Magma Armor", "Flame Body"],\
["Oblivious", "None"],\
["Oblivious", "None"],\
["Hustle", "Natural Cure"],\
["Hustle", "None"],\
["Suction Cups", "None"],\
["Vital Spirit", "Hustle"],\
["Swift Swim", "Water Absorb"],\
["Keen Eye", "Sturdy"],\
["Early Bird", "Flash Fire"],\
["Early Bird", "Flash Fire"],\
["Swift Swim", "None"],\
["Pickup", "None"],\
["Sturdy", "None"],\
["Trace", "None"],\
["Intimidate", "None"],\
["Own Tempo", "None"],\
["Guts", "None"],\
["Intimidate", "None"],\
["Oblivious", "None"],\
["Static", "None"],\
["Flame Body", "None"],\
["Thick Fat", "None"],\
["Natural Cure", "Serene Grace"],\
["Pressure", "None"],\
["Pressure", "None"],\
["Pressure", "None"],\
["Guts", "None"],\
["Shed Skin", "None"],\
["Sand Stream", "None"],\
["Pressure", "None"],\
["Pressure", "None"],\
["Natural Cure", "None"],\
["Overgrow", "None"],\
["Overgrow", "None"],\
["Overgrow", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Blaze", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Torrent", "None"],\
["Run Away", "None"],\
["Intimidate", "None"],\
["Pickup", "None"],\
["Pickup", "None"],\
["Shield Dust", "None"],\
["Shed Skin", "None"],\
["Swarm", "None"],\
["Shed Skin", "None"],\
["Shield Dust", "None"],\
["Swift Swim", "Rain Dish"],\
["Swift Swim", "Rain Dish"],\
["Swift Swim", "Rain Dish"],\
["Chlorophyll", "Early Bird"],\
["Chlorophyll", "Early Bird"],\
["Chlorophyll", "Early Bird"],\
["Guts", "None"],\
["Guts", "None"],\
["Keen Eye", "None"],\
["Keen Eye", "None"],\
["Synchronize", "Trace"],\
["Synchronize", "Trace"],\
["Synchronize", "Trace"],\
["Swift Swim", "None"],\
["Intimidate", "None"],\
["Effect Spore", "None"],\
["Effect Spore", "None"],\
["Truant", "None"],\
["Vital Spirit", "None"],\
["Truant", "None"],\
["Compound Eyes", "None"],\
["Speed Boost", "None"],\
["Wonder Guard", "None"],\
["Soundproof", "None"],\
["Soundproof", "None"],\
["Soundproof", "None"],\
["Thick Fat", "Guts"],\
["Thick Fat", "Guts"],\
["Thick Fat", "Huge Power"],\
["Sturdy", "Magnet Pull"],\
["Cute Charm", "None"],\
["Cute Charm", "None"],\
["Keen Eye", "None"],\
["Hyper Cutter", "Intimidate"],\
["Sturdy", "Rock Head"],\
["Sturdy", "Rock Head"],\
["Sturdy", "Rock Head"],\
["Pure Power", "None"],\
["Pure Power", "None"],\
["Static", "Lightning Rod"],\
["Static", "Lightning Rod"],\
["Plus", "None"],\
["Minus", "None"],\
["Illuminate", "Swarm"],\
["Oblivious", "None"],\
["Natural Cure", "Poison Point"],\
["Liquid Ooze", "Sticky Hold"],\
["Liquid Ooze", "Sticky Hold"],\
["Rough Skin", "None"],\
["Rough Skin", "None"],\
["Water Veil", "Oblivious"],\
["Water Veil", "Oblivious"],\
["Oblivious", "None"],\
["Magma Armor", "None"],\
["White Smoke", "None"],\
["Thick Fat", "Own Tempo"],\
["Thick Fat", "Own Tempo"],\
["Own Tempo", "None"],\
["Hyper Cutter", "Arena Trap"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Sand Veil", "None"],\
["Sand Veil", "None"],\
["Natural Cure", "None"],\
["Natural Cure", "None"],\
["Immunity", "None"],\
["Shed Skin", "None"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Oblivious", "None"],\
["Oblivious", "None"],\
["Hyper Cutter", "Shell Armor"],\
["Hyper Cutter", "Shell Armor"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Suction Cups", "None"],\
["Suction Cups", "None"],\
["Battle Armor", "None"],\
["Battle Armor", "None"],\
["Swift Swim", "None"],\
["Marvel Scale", "None"],\
["Forecast", "None"],\
["Color Change", "None"],\
["Insomnia", "None"],\
["Insomnia", "None"],\
["Levitate", "None"],\
["Pressure", "None"],\
["Chlorophyll", "None"],\
["Levitate", "None"],\
["Pressure", "None"],\
["Shadow Tag", "None"],\
["Inner Focus", "None"],\
["Inner Focus", "None"],\
["Thick Fat", "None"],\
["Thick Fat", "None"],\
["Thick Fat", "None"],\
["Shell Armor", "None"],\
["Swift Swim", "None"],\
["Swift Swim", "None"],\
["Swift Swim", "Rock Head"],\
["Swift Swim", "None"],\
["Rock Head", "None"],\
["Rock Head", "None"],\
["Intimidate", "None"],\
["Clear Body", "None"],\
["Clear Body", "None"],\
["Clear Body", "None"],\
["Clear Body", "None"],\
["Clear Body", "None"],\
["Clear Body", "None"],\
["Levitate", "None"],\
["Levitate", "None"],\
["Drizzle", "None"],\
["Drought", "None"],\
["Air Lock", "None"],\
["Serene Grace", "None"],\
["Pressure", "None"] ]
