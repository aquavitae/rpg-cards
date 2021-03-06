def load_all_spells():
    return [
        # "Abi-Dalzim's Horrid Wilting",          # 8th      Necromancy                 1 action  VSM    ee 15, xge 150
        # "Absorb Elements",                      # 1st      Abjuration                 1 reaction  S    ee 15, xge 150
        # "Acid Splash",                          # Cantrip  Conjuration                1 action  VS    phb 211
        # "Aganazzar's Scorcher",                 # 2nd      Evocation                  1 action  VSM    ee 15, xge 150
        # "Aid",                                  # 2nd      Abjuration                 1 action  VSM    phb 211
        # "Alarm",                                # 1st      Abjuration            yes  1 minute  VSM    phb 211
        # "Alter Self",                           # 2nd      Transmutation              1 action  VS  yes  phb 211
        # "Animal Friendship",                    # 1st      Enchantment                1 action  VSM    phb 212
        # "Animal Messenger",                     # 2nd      Enchantment           yes  1 action  VSM    phb 212

        # "Animal Shapes",                        # 8th      Transmutation              1 action  VS  yes  phb 212
        # "Animate Dead",                         # 3rd      Necromancy                 1 minute  VSM    phb 212
        # "Animate Objects",                      # 5th      Transmutation              1 action  VS  yes  phb 213
        # "Antilife Shell",                       # 5th      Abjuration                 1 action  VS  yes  phb 213
        # "Antimagic Field",                      # 8th      Abjuration                 1 action  VSM  yes  phb 213
        "Antipathy/Sympathy",                   # 8th      Enchantment                1 hour  VSM    phb 214
        # "Arcane Eye",                           # 4th      Divination                 1 action  VSM  yes  phb 214
        "Arcane Gate",                          # 6th      Conjuration                1 action  VS  yes  phb 214
        # "Arcane Lock",                          # 2nd      Abjuration                 1 action  VSMgp    phb 215

        # "Armor of Agathys",                     # 1st      Abjuration                 1 action  VSM    phb 215
        # "Arms of Hadar",                        # 1st      Conjuration                1 action  VS    phb 215
        "Astral Projection",                    # 9th      Necromancy                 1 hour  VSMgp    phb 215
        # "Augury",                               # 2nd      Divination            yes  1 minute  VSMgp    phb 215
        # "Aura of Life",                         # 4th      Abjuration                 1 action  V  yes  phb 216
        # "Aura of Purity",                       # 4th      Abjuration                 1 action  V  yes  phb 216
        # "Aura of Vitality",                     # 3rd      Evocation                  1 action  V  yes  phb 216
        # "Awaken",                               # 5th      Transmutation              8 hours  VSMgp    phb 216
        # "Bane",                                 # 1st      Enchantment                1 action  VSM  yes  phb 216

        # "Banishing Smite",                      # 5th      Abjuration                 1 bonus action  V  yes  phb 216
        # "Banishment",                           # 4th      Abjuration                 1 action  VSM  yes  phb 217
        # "Barkskin",                             # 2nd      Transmutation              1 action  VSM  yes  phb 217
        # "Beacon of Hope",                       # 3rd      Abjuration                 1 action  VS  yes  phb 217
        # "Beast Bond",                           # 1st      Divination                 1 action  VSM  yes  ee 15, xge 150
        # "Beast Sense",                          # 2nd      Divination            yes  1 action  S  yes  phb 217
        # "Bestow Curse",                         # 3rd      Necromancy                 1 action  VS  yes  phb 218
        # "Bigby's Hand",                         # 5th      Evocation                  1 action  VSM  yes  phb 218
        # "Blade Barrier",                        # 6th      Evocation                  1 action  VS  yes  phb 218

        # "Blade Ward",                           # Cantrip  Abjuration                 1 action  VS    phb 218
        # "Bless",                                # 1st      Enchantment                1 action  VSM  yes  phb 219
        # "Blight",                               # 4th      Necromancy                 1 action  VS    phb 219
        # "Blinding Smite",                       # 3rd      Evocation                  1 bonus action  V  yes  phb 219
        # "Blindness/Deafness",                   # 2nd      Necromancy                 1 action  V    phb 219
        # "Blink",                                # 3rd      Transmutation              1 action  VS    phb 219
        # "Blur",                                 # 2nd      Illusion                   1 action  V  yes  phb 219
        "Bones of the Earth",                   # 6th      Transmutation              1 action  VS    ee 15, xge 150
        # "Booming Blade",                        # Cantrip  Evocation                  1 action  VM    scag 142

        # "Branding Smite",                       # 2nd      Evocation                  1 bonus action  V  yes  phb 219
        # "Burning Hands",                        # 1st      Evocation                  1 action  VS    phb 220
        # "Call Lightning",                       # 3rd      Conjuration                1 action  VS  yes  phb 220
        # "Calm Emotions",                        # 2nd      Enchantment                1 action  VS  yes  phb 221
        # "Catapult",                             # 1st      Transmutation              1 action  S    ee 15, xge 150
        # "Catnap",                               # 3rd      Enchantment                1 action  SM    xge 151
        # "Cause Fear",                           # 1st      Necromancy                 1 action  V  yes  xge 151
        "Ceremony",                             # 1st      Abjuration            yes  1 hour  VSMgp    xge 151
        # "Chain Lightning",                      # 6th      Evocation                  1 action  VSM    phb 221

        "Chaos Bolt",                           # 1st      Evocation                  1 action  VS    xge 151
        # "Charm Monster",                        # 4th      Enchantment                1 action  VS    xge 151
        # "Charm Person",                         # 1st      Enchantment                1 action  VS    phb 221
        # "Chill Touch",                          # Cantrip  Necromancy                 1 action  VS    phb 221
        # "Chromatic Orb",                        # 1st      Evocation                  1 action  VSMgp    phb 221
        # "Circle of Death",                      # 6th      Necromancy                 1 action  VSMgp    phb 221
        # "Circle of Power",                      # 5th      Abjuration                 1 action  V  yes  phb 221
        # "Clairvoyance",                         # 3rd      Divination                 10 minutes  VSMgp  yes  phb 222
        # "Clone",                                # 8th      Necromancy                 1 hour  VSMgp    phb 222

        # "Cloud of Daggers",                     # 2nd      Conjuration                1 action  VSM  yes  phb 222
        # "Cloudkill",                            # 5th      Conjuration                1 action  VS  yes  phb 222
        # "Color Spray",                          # 1st      Illusion                   1 action  VSM    phb 222
        # "Command",                              # 1st      Enchantment                1 action  V    phb 223
        # "Commune",                              # 5th      Divination            yes  1 minute  VSM    phb 223
        # "Commune with Nature",                  # 5th      Divination            yes  1 minute  VS    phb 224
        # "Compelled Duel",                       # 1st      Enchantment                1 bonus action  V  yes  phb 224
        # "Comprehend Languages",                 # 1st      Divination            yes  1 action  VSM    phb 224
        # "Compulsion",                           # 4th      Enchantment                1 action  VS  yes  phb 224

        # "Cone of Cold",                         # 5th      Evocation                  1 action  VSM    phb 224
        # "Confusion",                            # 4th      Enchantment                1 action  VSM  yes  phb 224
        # "Conjure Animals",                      # 3rd      Conjuration                1 action  VS  yes  phb 225
        # "Conjure Barrage",                      # 3rd      Conjuration                1 action  VSM    phb 225
        # "Conjure Celestial",                    # 7th      Conjuration                1 minute  VS  yes  phb 225
        # "Conjure Elemental",                    # 5th      Conjuration                1 minute  VSM  yes  phb 225
        # "Conjure Fey",                          # 6th      Conjuration                1 minute  VS  yes  phb 226
        # "Conjure Minor Elementals",             # 4th      Conjuration                1 minute  VS  yes  phb 226
        # "Conjure Volley",                       # 5th      Conjuration                1 action  VSM    phb 226

        # "Conjure Woodland Beings",              # 4th      Conjuration                1 action  VSM  yes  phb 226
        # "Contact Other Plane",                  # 5th      Divination            yes  1 minute  V    phb 226
        "Contagion",                            # 5th      Necromancy                 1 action  VS    phb 227
        "Contingency",                          # 6th      Evocation                  10 minutes  VSMgp    phb 227
        # "Continual Flame",                      # 2nd      Evocation                  1 action  VSMgp    phb 227
        # "Control Flames",                       # Cantrip  Transmutation              1 action  S    ee 16, xge 152
        # "Control Water",                        # 4th      Transmutation              1 action  VSM  yes  phb 227
        # "Control Weather",                      # 8th      Transmutation              10 minutes  VSM  yes  phb 228
        "Control Winds",                        # 5th      Transmutation              1 action  VS  yes  ee 16

        # "Cordon of Arrows",                     # 2nd      Transmutation              1 action  VSM    phb 228
        # "Counterspell",                         # 3rd      Abjuration                 1 reaction  S    phb 228
        # "Create Bonfire",                       # Cantrip  Conjuration                1 action  VS  yes  ee 16, xge 152
        # "Create Food and Water",                # 3rd      Conjuration                1 action  VS    phb 229
        "Create Homunculus",                    # 6th      Transmutation              1 hour  VSMgp    xge 152
        # "Create or Destroy Water",              # 1st      Transmutation              1 action  VSM    phb 229
        "Create Undead",                        # 6th      Necromancy                 1 minute  VSMgp    phb 229
        # "Creation",                             # 5th      Illusion                   1 minute  VSM    phb 229
        # "Crown of Madness",                     # 2nd      Enchantment                1 action  VS  yes  phb 229

        "Crown of Stars",                       # 7th      Evocation                  1 action  VS    xge 152
        # "Crusader's Mantle",                    # 3rd      Evocation                  1 action  V  yes  phb 230
        # "Cure Wounds",                          # 1st      Evocation                  1 action  VS    phb 230
        # "Dancing Lights",                       # Cantrip  Evocation                  1 action  VSM  yes  phb 230
        # "Danse Macabre",                        # 5th      Necromancy                 1 action  VS  yes  xge 153
        # "Darkness",                             # 2nd      Evocation                  1 action  VM  yes  phb 230
        # "Darkvision",                           # 2nd      Transmutation              1 action  VSM    phb 230
        # "Dawn",                                 # 5th      Evocation                  1 action  VSMgp  yes  xge 153
        # "Daylight",                             # 3rd      Evocation                  1 action  VS    phb 230

        # "Death Ward",                           # 4th      Abjuration                 1 action  VS    phb 230
        "Delayed Blast Fireball",               # 7th      Evocation                  1 action  VSM  yes  phb 230
        # "Demiplane",                            # 8th      Conjuration                1 action  S    phb 231
        # "Destructive Wave",                     # 5th      Evocation                  1 action  V    phb 231
        # "Detect Evil and Good",                 # 1st      Divination                 1 action  VS  yes  phb 231
        # "Detect Magic",                         # 1st      Divination            yes  1 action  VS  yes  phb 231
        # "Detect Poison and Disease",            # 1st      Divination            yes  1 action  VSM  yes  phb 231
        "Detect Thoughts",                      # 2nd      Divination                 1 action  VSM  yes  phb 231
        # "Dimension Door",                       # 4th      Conjuration                1 action  V    phb 233

        # "Disguise Self",                        # 1st      Illusion                   1 action  VS    phb 233
        # "Disintegrate",                         # 6th      Transmutation              1 action  VSM    phb 233
        # "Dispel Evil and Good",                 # 5th      Abjuration                 1 action  VSM  yes  phb 233
        # "Dispel Magic",                         # 3rd      Abjuration                 1 action  VS    phb 234
        # "Dissonant Whispers",                   # 1st      Enchantment                1 action  V    phb 234
        # "Divination",                           # 4th      Divination            yes  1 action  VSMgp    phb 234
        # "Divine Favor",                         # 1st      Evocation                  1 bonus action  VS  yes  phb 234
        # "Divine Word",                          # 7th      Evocation                  1 bonus action  V    phb 234
        "Dominate Beast",                       # 4th      Enchantment                1 action  VS  yes  phb 234

        "Dominate Monster",                     # 8th      Enchantment                1 action  VS  yes  phb 235
        "Dominate Person",                      # 5th      Enchantment                1 action  VS  yes  phb 235
        # "Dragon's Breath",                      # 2nd      Transmutation              1 bonus action  VSM  yes  xge 154
        # "Drawmij's Instant Summons",            # 6th      Conjuration           yes  1 minute  VSMgp    phb 235
        "Dream",                                # 5th      Illusion                   1 minute  VSM    phb 236
        "Druid Grove",                          # 6th      Abjuration                 10 minutes  VSM    xge 154
        # "Druidcraft",                           # Cantrip  Transmutation              1 action  VS    phb 236
        "Dust Devil",                           # 2nd      Conjuration                1 action  VSM  yes  ee 17, xge 154
        # "Earth Tremor",                         # 1st      Evocation                  1 action  VS    ee 17, xge 155

        # "Earthbind",                            # 2nd      Transmutation              1 action  V  yes  ee 17, xge 154
        "Earthquake",                           # 8th      Evocation                  1 action  VSM  yes  phb 236
        # "Eldritch Blast",                       # Cantrip  Evocation                  1 action  VS    phb 237
        # "Elemental Bane",                       # 4th      Transmutation              1 action  VS  yes  ee 17, xge 155
        # "Elemental Weapon",                     # 3rd      Transmutation              1 action  VS  yes  phb 237
        # "Enemies Abound",                       # 3rd      Enchantment                1 action  VS  yes  xge 155
        # "Enervation",                           # 5th      Necromancy                 1 action  VS  yes  xge 155
        "Enhance Ability",                      # 2nd      Transmutation              1 action  VSM  yes  phb 237
        # "Enlarge/Reduce",                       # 2nd      Transmutation              1 action  VSM  yes  phb 237

        # "Ensnaring Strike",                     # 1st      Conjuration                1 bonus action  V  yes  phb 237
        # "Entangle",                             # 1st      Conjuration                1 action  VS  yes  phb 238
        # "Enthrall",                             # 2nd      Enchantment                1 action  VS    phb 238
        # "Erupting Earth",                       # 3rd      Transmutation              1 action  VSM    ee 17, xge 155
        "Etherealness",                         # 7th      Transmutation              1 action  VS    phb 238
        # "Evard's Black Tentacles",              # 4th      Conjuration                1 action  VSM  yes  phb 238
        # "Expeditious Retreat",                  # 1st      Transmutation              1 bonus action  VS  yes  phb 238
        # "Eyebite",                              # 6th      Necromancy                 1 action  VS  yes  phb 238
        # "Fabricate",                            # 4th      Transmutation              10 minutes  VS    phb 239

        # "Faerie Fire",                          # 1st      Evocation                  1 action  V  yes  phb 239
        # "False Life",                           # 1st      Necromancy                 1 action  VSM    phb 239
        # "Far Step",                             # 5th      Conjuration                1 bonus action  V  yes  xge 155
        # "Fear",                                 # 3rd      Illusion                   1 action  VSM  yes  phb 239
        # "Feather Fall",                         # 1st      Transmutation              1 reaction  VM    phb 239
        # "Feeblemind",                           # 8th      Enchantment                1 action  VSM    phb 239
        # "Feign Death",                          # 3rd      Necromancy            yes  1 action  VSM    phb 240
        "Find Familiar",                        # 1st      Conjuration           yes  1 hour  VSMgp    phb 240
        "Find Greater Steed",                   # 4th      Conjuration                10 minutes  VS    xge 156

        "Find Steed",                           # 2nd      Conjuration                10 minutes  VS    phb 240
        # "Find the Path",                        # 6th      Divination                 1 minute  VSMgp  yes  phb 240
        # "Find Traps",                           # 2nd      Divination                 1 action  VS    phb 241
        # "Finger of Death",                      # 7th      Necromancy                 1 action  VS    phb 241
        # "Fire Bolt",                            # Cantrip  Evocation                  1 action  VS    phb 242
        # "Fire Shield",                          # 4th      Evocation                  1 action  VSM    phb 242
        # "Fire Storm",                           # 7th      Evocation                  1 action  VS    phb 242
        # "Fireball",                             # 3rd      Evocation                  1 action  VSM    phb 241
        # "Flame Arrows",                         # 3rd      Transmutation              1 action  VS  yes  ee 18, xge 156

        # "Flame Blade",                          # 2nd      Evocation                  1 bonus action  VSM  yes  phb 242
        # "Flame Strike",                         # 5th      Evocation                  1 action  VSM    phb 242
        "Flaming Sphere",                       # 2nd      Conjuration                1 action  VSM  yes  phb 242
        "Flesh to Stone",                       # 6th      Transmutation              1 action  VSM  yes  phb 243
        # "Fly",                                  # 3rd      Transmutation              1 action  VSM  yes  phb 243
        # "Fog Cloud",                            # 1st      Conjuration                1 action  VS  yes  phb 243
        "Forbiddance",                          # 6th      Abjuration            yes  10 minutes  VSMgp    phb 243
        "Forcecage",                            # 7th      Evocation                  1 action  VSMgp    phb 243
        # "Foresight",                            # 9th      Divination                 1 minute  VSM    phb 244

        # "Freedom of Movement",                  # 4th      Abjuration                 1 action  VSM    phb 244
        # "Friends",                              # Cantrip  Enchantment                1 action  SM  yes  phb 244
        # "Frostbite",                            # Cantrip  Evocation                  1 action  VS    ee 18, xge 156
        # "Gaseous Form",                         # 3rd      Transmutation              1 action  VSM  yes  phb 244
        "Gate",                                 # 9th      Conjuration                1 action  VSMgp  yes  phb 244
        # "Geas",                                 # 5th      Enchantment                1 minute  V    phb 244
        # "Gentle Repose",                        # 2nd      Necromancy            yes  1 action  VSM    phb 245
        # "Giant Insect",                         # 4th      Transmutation              1 action  VS  yes  phb 245
        # "Glibness",                             # 8th      Transmutation              1 action  V    phb 245

        # "Globe of Invulnerability",             # 6th      Abjuration                 1 action  VSM  yes  phb 245
        "Glyph of Warding",                     # 3rd      Abjuration                 1 hour  VSMgp    phb 245
        # "Goodberry",                            # 1st      Transmutation              1 action  VSM    phb 246
        # "Grasping Vine",                        # 4th      Conjuration                1 bonus action  VS  yes  phb 246
        # "Grease",                               # 1st      Conjuration                1 action  VSM    phb 246
        # "Greater Invisibility",                 # 4th      Illusion                   1 action  VS  yes  phb 246
        # "Greater Restoration",                  # 5th      Abjuration                 1 action  VSMgp    phb 246
        # "Green-Flame Blade",                    # Cantrip  Evocation                  1 action  VM    scag 143
        # "Guardian of Faith",                    # 4th      Conjuration                1 action  V    phb 246

        "Guardian of Nature",                   # 4th      Transmutation              1 bonus action  V  yes  xge 157
        "Guards and Wards",                     # 6th      Abjuration                 10 minutes  VSMgp    phb 248
        # "Guidance",                             # Cantrip  Divination                 1 action  VS  yes  phb 248
        # "Guiding Bolt",                         # 1st      Evocation                  1 action  VS    phb 248
        # "Gust",                                 # Cantrip  Transmutation              1 action  VS    ee 19, xge 157
        # "Gust of Wind",                         # 2nd      Evocation                  1 action  VSM  yes  phb 248
        # "Hail of Thorns",                       # 1st      Conjuration                1 bonus action  V  yes  phb 249
        "Hallow",                               # 5th      Evocation                  24 hours  VSMgp    phb 249
        # "Hallucinatory Terrain",                # 4th      Illusion                   10 minutes  VSM    phb 249

        # "Harm",                                 # 6th      Necromancy                 1 action  VS    phb 249
        # "Haste",                                # 3rd      Transmutation              1 action  VSM  yes  phb 250
        # "Heal",                                 # 6th      Evocation                  1 action  VS    phb 250
        # "Healing Spirit",                       # 2nd      Conjuration                1 bonus action  VS  yes  xge 157
        # "Healing Word",                         # 1st      Evocation                  1 bonus action  V    phb 250
        # "Heat Metal",                           # 2nd      Transmutation              1 action  VSM  yes  phb 250
        # "Hellish Rebuke",                       # 1st      Evocation                  1 reaction  VS    phb 250
        # "Heroes' Feast",                        # 6th      Conjuration                10 minutes  VSMgp    phb 250
        # "Heroism",                              # 1st      Enchantment                1 action  VS  yes  phb 250

        # "Hex",                                  # 1st      Enchantment                1 bonus action  VSM  yes  phb 251
        # "Hold Monster",                         # 5th      Enchantment                1 action  VSM  yes  phb 251
        # "Hold Person",                          # 2nd      Enchantment                1 action  VSM  yes  phb 251
        # "Holy Aura",                            # 8th      Abjuration                 1 action  VSMgp  yes  phb 251
        # "Holy Weapon",                          # 5th      Evocation                  1 bonus action  VS  yes  xge 157
        # "Hunger of Hadar",                      # 3rd      Conjuration                1 action  VSM  yes  phb 251
        # "Hunter's Mark",                        # 1st      Divination                 1 bonus action  V  yes  phb 251
        # "Hypnotic Pattern",                     # 3rd      Illusion                   1 action  SM  yes  phb 252
        # "Ice Knife",                            # 1st      Conjuration                1 action  SM    ee 19, xge 157

        # "Ice Storm",                            # 4th      Evocation                  1 action  VSM    phb 252
        # "Identify",                             # 1st      Divination            yes  1 minute  VSMgp    phb 252
        "Illusory Dragon",                      # 8th      Illusion                   1 action  S  yes  xge 157
        # "Illusory Script",                      # 1st      Illusion              yes  1 minute  SMgp    phb 252
        # "Immolation",                           # 5th      Evocation                  1 action  V  yes  ee 19, xge 158
        "Imprisonment",                         # 9th      Abjuration                 1 minute  VSMgp    phb 252
        # "Incendiary Cloud",                     # 8th      Conjuration                1 action  VS  yes  phb 253
        "Infernal Calling",                     # 5th      Conjuration                1 minute  VSMgp  yes  xge 158
        # "Infestation",                          # Cantrip  Conjuration                1 action  VSM    xge 158

        # "Inflict Wounds",                       # 1st      Necromancy                 1 action  VS    phb 253
        # "Insect Plague",                        # 5th      Conjuration                1 action  VSM  yes  phb 254
        # "Investiture of Flame",                 # 6th      Transmutation              1 action  VS  yes  ee 19, xge 159
        "Investiture of Ice",                   # 6th      Transmutation              1 action  VS  yes  ee 19, xge 159
        # "Investiture of Stone",                 # 6th      Transmutation              1 action  VS  yes  ee 19, xge 159
        # "Investiture of Wind",                  # 6th      Transmutation              1 action  VS  yes  ee 20, xge 160
        # "Invisibility",                         # 2nd      Illusion                   1 action  VSM  yes  phb 254
        # "Invulnerability",                      # 9th      Abjuration                 1 action  VSMgp  yes  xge 160
        # "Jump",                                 # 1st      Transmutation              1 action  VSM    phb 254

        # "Knock",                                # 2nd      Transmutation              1 action  V    phb 254
        # "Legend Lore",                          # 5th      Divination                 10 minutes  VSMgp    phb 254
        "Leomund's Secret Chest",               # 4th      Conjuration                1 action  VSMgp    phb 254
        # "Leomund's Tiny Hut",                   # 3rd      Evocation             yes  1 minute  VSM    phb 255
        # "Lesser Restoration",                   # 2nd      Abjuration                 1 action  VS    phb 255
        # "Levitate",                             # 2nd      Transmutation              1 action  VSM  yes  phb 255
        # "Life Transference",                    # 3rd      Necromancy                 1 action  VS    xge 160
        # "Light",                                # Cantrip  Evocation                  1 action  VM    phb 255
        # "Lightning Arrow",                      # 3rd      Transmutation              1 bonus action  VS  yes  phb 255

        # "Lightning Bolt",                       # 3rd      Evocation                  1 action  VSM    phb 255
        # "Lightning Lure",                       # Cantrip  Evocation                  1 action  V    scag 143
        # "Locate Animals or Plants",             # 2nd      Divination            yes  1 action  VSM    phb 256
        # "Locate Creature",                      # 4th      Divination                 1 action  VSM  yes  phb 256
        # "Locate Object",                        # 2nd      Divination                 1 action  VSM  yes  phb 256
        # "Longstrider",                          # 1st      Transmutation              1 action  VSM    phb 256
        # "Maddening Darkness",                   # 8th      Evocation                  1 action  VM  yes  xge 160
        "Maelstrom",                            # 5th      Evocation                  1 action  VSM  yes  ee 20, xge 160
        # "Mage Armor",                           # 1st      Abjuration                 1 action  VSM    phb 256

        # "Mage Hand",                            # Cantrip  Conjuration                1 action  VS    phb 256
        # "Magic Circle",                         # 3rd      Abjuration                 1 minute  VSMgp    phb 256
        "Magic Jar",                            # 6th      Necromancy                 1 minute  VSMgp    phb 257
        # "Magic Missile",                        # 1st      Evocation                  1 action  VS    phb 257
        "Magic Mouth",                          # 2nd      Illusion              yes  1 minute  VSMgp    phb 257
        "Magic Stone",                          # Cantrip  Transmutation              1 bonus action  VS    ee 20, xge 160
        # "Magic Weapon",                         # 2nd      Transmutation              1 bonus action  VS  yes  phb 257
        # "Major Image",                          # 3rd      Illusion                   1 action  VSM  yes  phb 258
        # "Mass Cure Wounds",                     # 5th      Evocation                  1 action  VS    phb 258

        # "Mass Heal",                            # 9th      Evocation                  1 action  VS    phb 258
        # "Mass Healing Word",                    # 3rd      Evocation                  1 bonus action  V    phb 258
        "Mass Polymorph",                       # 9th      Transmutation              1 action  VSM  yes  xge 160
        "Mass Suggestion",                      # 6th      Enchantment                1 action  VM    phb 258
        "Maximilian's Earthen Grasp",           # 2nd      Transmutation              1 action  VSM  yes  ee 20, xge 161
        # "Maze",                                 # 8th      Conjuration                1 action  VS  yes  phb 258
        "Meld into Stone",                      # 3rd      Transmutation         yes  1 action  VS    phb 259
        # "Melf's Acid Arrow",                    # 2nd      Evocation                  1 action  VSM    phb 259
        "Melf's Minute Meteors",                # 3rd      Evocation                  1 action  VSM  yes  ee 20, xge 161

        # "Mending",                              # Cantrip  Transmutation              1 minute  VSM    phb 259
        "Mental Prison",                        # 6th      Illusion                   1 action  S  yes  xge 161
        # "Message",                              # Cantrip  Transmutation              1 action  VSM    phb 259
        # "Meteor Swarm",                         # 9th      Evocation                  1 action  VS    phb 259
        "Mighty Fortress",                      # 8th      Conjuration                1 minute  VSMgp    xge 161
        # "Mind Blank",                           # 8th      Abjuration                 1 action  VS    phb 259
        # "Mind Spike",                           # 2nd      Divination                 1 action  S  yes  xge 162
        # "Minor Illusion",                       # Cantrip  Illusion                   1 action  SM    phb 260
        # "Mirage Arcane",                        # 7th      Illusion                   10 minutes  VS    phb 260

        # "Mirror Image",                         # 2nd      Illusion                   1 action  VS    phb 260
        # "Mislead",                              # 5th      Illusion                   1 action  S  yes  phb 260
        # "Misty Step",                           # 2nd      Conjuration                1 bonus action  V    phb 260
        "Modify Memory",                        # 5th      Enchantment                1 action  VS  yes  phb 261
        # "Mold Earth",                           # Cantrip  Transmutation              1 action  S    ee 21, xge 162
        # "Moonbeam",                             # 2nd      Evocation                  1 action  VSM  yes  phb 261
        # "Mordenkainen's Faithful Hound",        # 4th      Conjuration                1 action  VSM    phb 261
        "Mordenkainen's Magnificent Mansion",   # 7th      Conjuration                1 minute  VSMgp    phb 261
        "Mordenkainen's Private Sanctum",       # 4th      Abjuration                 10 minutes  VSM    phb 262

        # "Mordenkainen's Sword",                 # 7th      Evocation                  1 action  VSMgp  yes  phb 262
        "Move Earth",                           # 6th      Transmutation              1 action  VSM  yes  phb 263
        # "Negative Energy Flood",                # 5th      Necromancy                 1 action  VM    xge 163
        # "Nondetection",                         # 3rd      Abjuration                 1 action  VSMgp    phb 263
        "Nystul's Magic Aura",                  # 2nd      Illusion                   1 action  VSM    phb 263
        "Otiluke's Freezing Sphere",            # 6th      Evocation                  1 action  VSM    phb 263
        "Otiluke's Resilient Sphere",           # 4th      Evocation                  1 action  VSM  yes  phb 264
        "Otto's Irresistible Dance",            # 6th      Enchantment                1 action  V  yes  phb 264
        # "Pass without Trace",                   # 2nd      Abjuration                 1 action  VSM  yes  phb 264

        # "Passwall",                             # 5th      Transmutation              1 action  VSM    phb 264
        "Phantasmal Force",                     # 2nd      Illusion                   1 action  VSM  yes  phb 264
        # "Phantasmal Killer",                    # 4th      Illusion                   1 action  VS  yes  phb 265
        # "Phantom Steed",                        # 3rd      Illusion              yes  1 minute  VS    phb 265
        "Planar Ally",                          # 6th      Conjuration                10 minutes  VS    phb 265
        "Planar Binding",                       # 5th      Abjuration                 1 hour  VSMgp    phb 265
        # "Plane Shift",                          # 7th      Conjuration                1 action  VSMgp    phb 266
        # "Plant Growth",                         # 3rd      Transmutation              1 action  VS    phb 266
        # "Poison Spray",                         # Cantrip  Conjuration                1 action  VS    phb 266

        # "Polymorph",                            # 4th      Transmutation              1 action  VSM  yes  phb 266
        # "Power Word Heal",                      # 9th      Evocation                  1 action  VS    phb 266
        # "Power Word Kill",                      # 9th      Enchantment                1 action  V    phb 266
        # "Power Word Pain",                      # 7th      Enchantment                1 action  V    xge 163
        # "Power Word Stun",                      # 8th      Enchantment                1 action  V    phb 267
        # "Prayer of Healing",                    # 2nd      Evocation               10 minutes  V    phb 267
        # "Prestidigitation",                     # Cantrip  Transmutation              1 action  VS    phb 267
        "Primal Savagery",                      # Cantrip  Transmutation              1 action  S    xge 163
        "Primordial Ward",                      # 6th      Abjuration                 1 action  VS  yes  ee 21, xge 163

        "Prismatic Spray",                      # 7th      Evocation                  1 action  VS    phb 267
        "Prismatic Wall",                       # 9th      Abjuration                 1 action  VS    phb 267
        # "Produce Flame",                        # Cantrip  Conjuration                1 action  VS    phb 269
        "Programmed Illusion",                  # 6th      Illusion                   1 action  VSMgp    phb 269
        "Project Image",                        # 7th      Illusion                   1 action  VSMgp  yes  phb 270
        # "Protection from Energy",               # 3rd      Abjuration                 1 action  VS  yes  phb 270
        # "Protection from Evil and Good",        # 1st      Abjuration                 1 action  VSM  yes  phb 270
        # "Protection from Poison",               # 2nd      Abjuration                 1 action  VS    phb 270
        # "Psychic Scream",                       # 9th      Enchantment                1 action  S    xge 163

        # "Purify Food and Drink",                # 1st      Transmutation         yes  1 action  VS    phb 270
        # "Pyrotechnics",                         # 2nd      Transmutation              1 action  VS    ee 21, xge 163
        "Raise Dead",                           # 5th      Necromancy                 1 hour  VSMgp    phb 270
        # "Rary's Telepathic Bond",               # 5th      Divination            yes  1 action  VSM    phb 270
        # "Ray of Enfeeblement",                  # 2nd      Necromancy                 1 action  VS  yes  phb 271
        # "Ray of Frost",                         # Cantrip  Evocation                  1 action  VS    phb 271
        # "Ray of Sickness",                      # 1st      Necromancy                 1 action  VS    phb 271
        # "Regenerate",                           # 7th      Transmutation              1 minute  VSM    phb 271
        "Reincarnate",                          # 5th      Transmutation              1 hour  VSMgp    phb 271

        # "Remove Curse",                         # 3rd      Abjuration                 1 action  VS    phb 271
        # "Resistance",                           # Cantrip  Abjuration                 1 action  VSM  yes  phb 272
        "Resurrection",                         # 7th      Necromancy                 1 hour  VSMgp    phb 272
        # "Reverse Gravity",                      # 7th      Transmutation              1 action  VSM  yes  phb 272
        # "Revivify",                             # 3rd      Necromancy                 1 action  VSMgp    phb 272
        # "Rope Trick",                           # 2nd      Transmutation              1 action  VSM    phb 272
        # "Sacred Flame",                         # Cantrip  Evocation                  1 action  VS    phb 272
        # "Sanctuary",                            # 1st      Abjuration                 1 bonus action  VSM    phb 272
        # "Scatter",                              # 6th      Abjuration                 1 action  V    xge 164

        # "Scorching Ray",                        # 2nd      Evocation                  1 action  VS    phb 273
        "Scrying",                              # 5th      Divination              10 minutes  VSMgp  yes  phb 273
        # "Searing Smite",                        # 1st      Evocation                  1 bonus action  V  yes  phb 274
        # "See Invisibility",                     # 2nd      Divination                 1 action  VSM    phb 274
        # "Seeming",                              # 5th      Illusion                   1 action  VS    phb 274
        # "Sending",                              # 3rd      Evocation                  1 action  VSM    phb 274
        # "Sequester",                            # 7th      Transmutation              1 action  VSMgp    phb 274
        # "Shadow Blade",                         # 2nd      Illusion                   1 bonus action  VS  yes  xge 164
        "Shadow of Moil",                       # 4th      Necromancy                 1 action  VSMgp  yes  xge 164

        "Shape Water",                          # Cantrip  Transmutation              1 action  S    ee 21
        "Shapechange",                          # 9th      Transmutation              1 action  VSMgp  yes  phb 274
        # "Shatter",                              # 2nd      Evocation                  1 action  VSM    phb 275
        # "Shield",                               # 1st      Abjuration                 1 reaction  VS    phb 275
        # "Shield of Faith",                      # 1st      Abjuration                 1 bonus action  VSM  yes  phb 275
        # "Shillelagh",                           # Cantrip  Transmutation              1 bonus action  VSM    phb 275
        # "Shocking Grasp",                       # Cantrip  Evocation                  1 action  VS    phb 275
        # "Sickening Radiance",                   # 4th      Evocation                  1 action  VS  yes  xge 164
        # "Silence",                              # 2nd      Illusion              yes  1 action  VS  yes  phb 275

        # "Silent Image",                         # 1st      Illusion                   1 action  VSM  yes  phb 276
        "Simulacrum",                           # 7th      Illusion                   12 hours  VSMgp    phb 276
        "Skill Empowerment",                    # 5th      Transmutation              1 action  VS  yes  xge 165
        "Skywrite",                             # 2nd      Transmutation         yes  1 action  VS  yes  ee 22, xge 165
        # "Sleep",                                # 1st      Enchantment                1 action  VSM    phb 276
        # "Sleet Storm",                          # 3rd      Conjuration                1 action  VSM  yes  phb 276
        # "Slow",                                 # 3rd      Transmutation              1 action  VSM  yes  phb 277
        # "Snare",                                # 1st      Abjuration                 1 minute  SMgp    xge 165
        "Snilloc's Snowball Swarm",             # 2nd      Evocation                  1 action  VSM    ee 22, xge 165

        "Soul Cage",                            # 6th      Necromancy                 1 reaction  VSMgp    xge 165
        # "Spare the Dying",                      # Cantrip  Necromancy                 1 action  VS    phb 277
        # "Speak with Animals",                   # 1st      Divination            yes  1 action  VS    phb 277
        # "Speak with Dead",                      # 3rd      Necromancy                 1 action  VSM    phb 277
        "Speak with Plants",                    # 3rd      Transmutation              1 action  VS    phb 277
        # "Spider Climb",                         # 2nd      Transmutation              1 action  VSM  yes  phb 277
        # "Spike Growth",                         # 2nd      Transmutation              1 action  VSM  yes  phb 277
        # "Spirit Guardians",                     # 3rd      Conjuration                1 action  VSM  yes  phb 278
        # "Spiritual Weapon",                     # 2nd      Evocation                  1 bonus action  VS    phb 278

        # "Staggering Smite",                     # 4th      Evocation                  1 bonus action  V  yes  phb 278
        "Steel Wind Strike",                    # 5th      Conjuration                1 action  SMgp    xge 166
        # "Stinking Cloud",                       # 3rd      Conjuration                1 action  VSM  yes  phb 278
        # "Stone Shape",                          # 4th      Transmutation              1 action  VSM    phb 278
        # "Stoneskin",                            # 4th      Abjuration                 1 action  VSMgp  yes  phb 278
        "Storm of Vengeance",                   # 9th      Conjuration                1 action  VS  yes  phb 279
        "Storm Sphere",                         # 4th      Evocation                  1 action  VS  yes  ee 22, xge 166
        # "Suggestion",                           # 2nd      Enchantment                1 action  VM  yes  phb 279
        "Summon Greater Demon",                 # 4th      Conjuration                1 action  VSM  yes  xge 166

        "Summon Le sser Demons",                 # 3rd      Conjuration                1 action  VSM  yes  xge 167
        # "Sunbeam",                              # 6th      Evocation                  1 action  VSM  yes  phb 279
        # "Sunburst",                             # 8th      Evocation                  1 action  VSM    phb 279
        # "Swift Quiver",                         # 5th      Transmutation              1 bonus action  VSM  yes  phb 279
        # "Sword Burst",                          # Cantrip  Conjuration                1 action  V    scag 143
        "Symbol",                               # 7th      Abjuration                 1 minute  VSMgp    phb 280
        # "Synaptic Static",                      # 5th      Enchantment                1 action  VS    xge 167
        # "Tasha's Hideous Laughter",             # 1st      Enchantment                1 action  VSM  yes  phb 280
        "Telekinesis",                          # 5th      Transmutation              1 action  VS  yes  phb 280

        # "Telepathy",                            # 8th      Evocation                  1 action  VSM    phb 281
        # "Teleport",                             # 7th      Conjuration                1 action  V    phb 281
        "Teleportation Circle",                 # 5th      Conjuration                1 minute  VMgp    phb 282
        "Temple of the Gods",                   # 7th      Conjuration                1 hour  VSMgp    xge 167
        "Tenser's Floating Disk",               # 1st      Conjuration           yes  1 action  VSM    phb 282
        "Tenser's Transformation",              # 6th      Transmutation              1 action  VSM  yes  xge 168
        # "Thaumaturgy",                          # Cantrip  Transmutation              1 action  V    phb 282
        # "Thorn Whip",                           # Cantrip  Transmutation              1 action  VSM    phb 282
        "Thunder Step",                         # 3rd      Conjuration                1 action  V    xge 168

        "Thunderclap",                          # Cantrip  Evocation                  1 action  S    ee 22, xge 168
        # "Thunderous Smite",                     # 1st      Evocation                  1 bonus action  V  yes  phb 282
        # "Thunderwave",                          # 1st      Evocation                  1 action  VS    phb 282
        "Tidal Wave",                           # 3rd      Conjuration                1 action  VSM    ee 22, xge 168
        # "Time Stop",                            # 9th      Transmutation              1 action  V    phb 283
        "Tiny Servant",                         # 3rd      Transmutation              1 minute  VS    xge 168
        # "Toll the Dead",                        # Cantrip  Necromancy                 1 action  VS    xge 169
        # "Tongues",                              # 3rd      Divination                 1 action  VM    phb 283
        "Transmute Rock",                       # 5th      Transmutation              1 action  VSM    ee 22, xge 169

        # "Transport via Plants",                 # 6th      Conjuration                1 action  VS    phb 283
        # "Tree Stride",                          # 5th      Conjuration                1 action  VS  yes  phb 283
        "True Polymorph",                       # 9th      Transmutation              1 action  VSM  yes  phb 283
        # "True Resurrection",                    # 9th      Necromancy                 1 hour  VSMgp    phb 284
        # "True Seeing",                          # 6th      Divination                 1 action  VSMgp    phb 284
        # "True Strike",                          # Cantrip  Divination                 1 action  S  yes  phb 284
        "Tsunami",                              # 8th      Conjuration                1 minute  VS  yes  phb 284
        # "Unseen Servant",                       # 1st      Conjuration           yes  1 action  VSM    phb 284
        # "Vampiric Touch",                       # 3rd      Necromancy                 1 action  VS  yes  phb 285

        # "Vicious Mockery",                      # Cantrip  Enchantment                1 action  V    phb 285
        "Vitriolic Sphere",                     # 4th      Evocation                  1 action  VSM    ee 23, xge 170
        # "Wall of Fire",                         # 4th      Evocation                  1 action  VSM  yes  phb 285
        # "Wall of Force",                        # 5th      Evocation                  1 action  VSM  yes  phb 285
        "Wall of Ice",                          # 6th      Evocation                  1 action  VSM  yes  phb 285
        "Wall of Light",                        # 5th      Evocation                  1 action  VSM  yes  xge 170
        "Wall of Sand",                         # 3rd      Evocation                  1 action  VSM  yes  ee 23, xge 170
        "Wall of Stone",                        # 5th      Evocation                  1 action  VSM  yes  phb 287
        "Wall of Thorns",                       # 6th      Conjuration                1 action  VSM  yes  phb 287

        "Wall of Water",                        # 3rd      Evocation                  1 action  VSM  yes  ee 23, xge 170
        # "Warding Bond",                         # 2nd      Abjuration                 1 action  VSMgp    phb 287
        "Warding Wind",                         # 2nd      Evocation                  1 action  V  yes  ee 23, xge 170
        # "Water Breathing",                      # 3rd      Transmutation         yes  1 action  VSM    phb 287
        # "Water Walk",                           # 3rd      Transmutation         yes  1 action  VSM    phb 287
        "Watery Sphere",                        # 4th      Conjuration                1 action  VSM  yes  ee 23, xge 170
        # "Web",                                  # 2nd      Conjuration                1 action  VSM  yes  phb 287
        # "Weird",                                # 9th      Illusion                   1 action  VS  yes  phb 288
        "Whirlwind",                            # 7th      Evocation                  1 action  VM  yes  ee 24, xge 171

        # "Wind Walk",                            # 6th      Transmutation              1 minute  VSM    phb 288
        "Wind Wall",                            # 3rd      Evocation                  1 action  VSM  yes  phb 288
        "Wish",                                 # 9th      Conjuration                1 action  V    phb 288
        # "Witch Bolt",                           # 1st      Evocation                  1 action  VSM  yes  phb 289
        "Word of Radiance",                     # Cantrip  Evocation                  1 action  VM    xge 171
        # "Word of Recall",                       # 6th      Conjuration                1 action  V    phb 289
        "Wrath of Nature",                      # 5th      Evocation                  1 action  VS  yes  xge 171
        # "Wrathful Smite",                       # 1st      Evocation                  1 bonus action  V  yes  phb 289
        "Zephyr Strike",                        # 1st      Transmutation              1 bonus action  V  yes  xge 171

        # "Zone of Truth",                        # 2nd      Enchantment                1 action  VS    phb 289
    ]