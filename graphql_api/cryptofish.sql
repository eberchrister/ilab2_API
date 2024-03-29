DROP TABLE IF EXISTS cryptofish;
DROP TABLE IF EXISTS planet;
DROP TABLE IF EXISTS user;
CREATE TABLE cryptofish (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, planet_id INTEGER NOT NULL, status TEXT NOT NULL, size TEXT NOT NULL, cost INTEGER NOT NULL, owner_id INTEGER);
CREATE TABLE planet (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, type TEXT NOT NULL);
CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL);
INSERT INTO planet (name, type) VALUES ("earth-420", "terrestrial");
INSERT INTO planet (name, type) VALUES ("ilab-2", "ocean");
INSERT INTO planet (name, type) VALUES ("welsenus", "gas giant");
INSERT INTO planet (name, type) VALUES ("chritorus", "ice giant");
INSERT INTO planet (name, type) VALUES ("x-212", "neptunian");
INSERT INTO planet (name, type) VALUES ("mars-54", "puffy");
INSERT INTO cryptofish VALUES (120, "ssequ", 4, "sleepy", "colossal", 1588.12, 20);
INSERT INTO cryptofish VALUES (37, "ijvcq", 2, "hungry", "small", 94.72, 32);
INSERT INTO cryptofish VALUES (2, "qqhmq", 1, "hungry", "medium", 32.55, 4);
INSERT INTO cryptofish VALUES (5, "jsijj", 1, "hungry", "tiny", 65.49, 19);
INSERT INTO cryptofish VALUES (166, "ttztt", 5, "playful", "giant", 4924.08, 5);
INSERT INTO cryptofish VALUES (82, "skaoa", 3, "sleepy", "giant", 700.11, 12);
INSERT INTO cryptofish VALUES (115, "untur", 4, "sleepy", "small", 1594.81, 24);
INSERT INTO cryptofish VALUES (24, "oobox", 1, "playful", "colossal", 950.27, 17);
INSERT INTO cryptofish VALUES (196, "iiwvm", 6, "bored", "giant", 2982.02, NULL);
INSERT INTO cryptofish VALUES (143, "klhel", 4, "lonely", "tiny", 964.3, 18);
INSERT INTO cryptofish VALUES (204, "nwmmm", 6, "playful", "colossal", 8262.66, NULL);
INSERT INTO cryptofish VALUES (83, "sdtij", 3, "sleepy", "tiny", 1891.7, 19);
INSERT INTO cryptofish VALUES (134, "dgpgo", 4, "grumpy", "medium", 5699.34, 28);
INSERT INTO cryptofish VALUES (85, "hvzvl", 3, "bored", "small", 4181.71, 15);
INSERT INTO cryptofish VALUES (149, "zgemm", 5, "hungry", "tiny", 7357.22, 10);
INSERT INTO cryptofish VALUES (156, "nwnan", 5, "sleepy", "colossal", 428.84, 33);
INSERT INTO cryptofish VALUES (56, "zwqmn", 2, "playful", "medium", 1869.09, 10);
INSERT INTO cryptofish VALUES (88, "qmzqm", 3, "bored", "giant", 1217.73, 24);
INSERT INTO cryptofish VALUES (91, "zsqzz", 3, "playful", "small", 1765.63, 26);
INSERT INTO cryptofish VALUES (136, "xnprh", 4, "grumpy", "giant", 325.64, 26);
INSERT INTO cryptofish VALUES (142, "wtztm", 4, "lonely", "giant", 1552.11, 19);
INSERT INTO cryptofish VALUES (154, "ryoto", 5, "sleepy", "giant", 429.35, 29);
INSERT INTO cryptofish VALUES (42, "saqra", 2, "hungry", "colossal", 1456.29, 2);
INSERT INTO cryptofish VALUES (207, "ididz", 6, "grumpy", "large", 7142.52, NULL);
INSERT INTO cryptofish VALUES (51, "yyoao", 2, "bored", "large", 105.83, 26);
INSERT INTO cryptofish VALUES (105, "msurs", 3, "lonely", "large", 919.82, 3);
INSERT INTO cryptofish VALUES (164, "twutn", 5, "playful", "medium", 884.47, 33);
INSERT INTO cryptofish VALUES (192, "blhww", 6, "sleepy", "colossal", 812.82, NULL);
INSERT INTO cryptofish VALUES (178, "ksksf", 5, "lonely", "giant", 2908.12, 2);
INSERT INTO cryptofish VALUES (153, "wzfwh", 5, "sleepy", "large", 5894.45, 16);
INSERT INTO cryptofish VALUES (100, "qryqy", 3, "grumpy", "giant", 494.43, 9);
INSERT INTO cryptofish VALUES (28, "suutr", 1, "grumpy", "giant", 593.33, 10);
INSERT INTO cryptofish VALUES (49, "oiozz", 2, "bored", "small", 542.03, 7);
INSERT INTO cryptofish VALUES (210, "grxxg", 6, "grumpy", "colossal", 2729.82, NULL);
INSERT INTO cryptofish VALUES (98, "eicik", 3, "grumpy", "medium", 1962.09, 25);
INSERT INTO cryptofish VALUES (78, "uptsg", 3, "hungry", "colossal", 2532.29, 27);
INSERT INTO cryptofish VALUES (179, "hhhgg", 5, "lonely", "tiny", 1518.05, 26);
INSERT INTO cryptofish VALUES (127, "qrssm", 4, "playful", "small", 1916.92, 20);
INSERT INTO cryptofish VALUES (201, "nveve", 6, "playful", "large", 1175.72, NULL);
INSERT INTO cryptofish VALUES (69, "vvtvi", 2, "lonely", "large", 686.99, 21);
INSERT INTO cryptofish VALUES (186, "iggeo", 6, "hungry", "colossal", 905.84, NULL);
INSERT INTO cryptofish VALUES (95, "yifty", 3, "playful", "tiny", 1092.56, 26);
INSERT INTO cryptofish VALUES (161, "ffonn", 5, "bored", "tiny", 169.42, 15);
INSERT INTO cryptofish VALUES (202, "lkkkl", 6, "playful", "giant", 676.23, NULL);
INSERT INTO cryptofish VALUES (182, "kcesc", 6, "hungry", "medium", 7895.86, NULL);
INSERT INTO cryptofish VALUES (57, "yelcy", 2, "playful", "large", 2194.5, 20);
INSERT INTO cryptofish VALUES (81, "zzsfz", 3, "sleepy", "large", 1987.64, 21);
INSERT INTO cryptofish VALUES (180, "tmmct", 5, "lonely", "colossal", 5368.19, 31);
INSERT INTO cryptofish VALUES (126, "hvhat", 4, "bored", "colossal", 452.02, 3);
INSERT INTO cryptofish VALUES (206, "brgrh", 6, "grumpy", "medium", 3407.85, NULL);
INSERT INTO cryptofish VALUES (137, "ljdkj", 4, "grumpy", "tiny", 200.35, 4);
INSERT INTO cryptofish VALUES (163, "fqnfc", 5, "playful", "small", 987.78, 28);
INSERT INTO cryptofish VALUES (103, "ffdbd", 3, "lonely", "small", 5599.03, 30);
INSERT INTO cryptofish VALUES (113, "mgesn", 4, "hungry", "tiny", 2895.72, 13);
INSERT INTO cryptofish VALUES (102, "yqqqg", 3, "grumpy", "colossal", 3888.47, 32);
INSERT INTO cryptofish VALUES (155, "zpmps", 5, "sleepy", "tiny", 3664.65, 23);
INSERT INTO cryptofish VALUES (36, "hekee", 1, "lonely", "colossal", 624.79, 5);
INSERT INTO cryptofish VALUES (203, "shshh", 6, "playful", "tiny", 11391.7, NULL);
INSERT INTO cryptofish VALUES (92, "fqfpq", 3, "playful", "medium", 2306.05, 8);
INSERT INTO cryptofish VALUES (12, "zipiw", 1, "sleepy", "colossal", 131.35, 1);
INSERT INTO cryptofish VALUES (47, "fbqfa", 2, "sleepy", "tiny", 2211.21, 3);
INSERT INTO cryptofish VALUES (9, "fgrfv", 1, "sleepy", "large", 102.45, 5);
INSERT INTO cryptofish VALUES (89, "gubbg", 3, "bored", "tiny", 1145.0, 9);
INSERT INTO cryptofish VALUES (190, "nnnld", 6, "sleepy", "giant", 1512.01, NULL);
INSERT INTO cryptofish VALUES (73, "lwwak", 3, "hungry", "small", 2204.72, 2);
INSERT INTO cryptofish VALUES (111, "kjzjk", 4, "hungry", "large", 1833.65, 15);
INSERT INTO cryptofish VALUES (19, "ccccp", 1, "playful", "small", 107.18, 9);
INSERT INTO cryptofish VALUES (75, "wwwkt", 3, "hungry", "large", 2117.07, 10);
INSERT INTO cryptofish VALUES (29, "hjabr", 1, "grumpy", "tiny", 1016.29, 26);
INSERT INTO cryptofish VALUES (3, "mwbmw", 1, "hungry", "large", 7.71, 1);
INSERT INTO cryptofish VALUES (45, "mxmlt", 2, "sleepy", "large", 752.38, 15);
INSERT INTO cryptofish VALUES (108, "gssmf", 3, "lonely", "colossal", 1852.7, 1);
INSERT INTO cryptofish VALUES (122, "hafiw", 4, "bored", "medium", 1064.46, 33);
INSERT INTO cryptofish VALUES (43, "iiiiq", 2, "sleepy", "small", 1003.35, 16);
INSERT INTO cryptofish VALUES (87, "okgoo", 3, "bored", "large", 53.57, 15);
INSERT INTO cryptofish VALUES (1, "bdbbd", 1, "hungry", "small", 0.0, 33);
INSERT INTO cryptofish VALUES (84, "yddhy", 3, "sleepy", "colossal", 5492.21, 1);
INSERT INTO cryptofish VALUES (173, "fesei", 5, "grumpy", "tiny", 1167.81, 17);
INSERT INTO cryptofish VALUES (31, "oxdyg", 1, "lonely", "small", 135.23, 29);
INSERT INTO cryptofish VALUES (162, "fkrrk", 5, "bored", "colossal", 1374.59, 27);
INSERT INTO cryptofish VALUES (159, "vyhvu", 5, "bored", "large", 595.09, 34);
INSERT INTO cryptofish VALUES (147, "omuoc", 5, "hungry", "large", 43.71, 4);
INSERT INTO cryptofish VALUES (18, "yynoo", 1, "bored", "colossal", 135.92, 23);
INSERT INTO cryptofish VALUES (215, "nieqi", 6, "lonely", "tiny", 6007.52, NULL);
INSERT INTO cryptofish VALUES (170, "vbava", 5, "grumpy", "medium", 2574.97, 12);
INSERT INTO cryptofish VALUES (216, "fvqrd", 6, "lonely", "colossal", 2171.36, NULL);
INSERT INTO cryptofish VALUES (187, "nnxfk", 6, "sleepy", "small", 280.21, NULL);
INSERT INTO cryptofish VALUES (130, "cqxqq", 4, "playful", "giant", 566.68, 23);
INSERT INTO cryptofish VALUES (94, "kkffm", 3, "playful", "giant", 3088.86, 3);
INSERT INTO cryptofish VALUES (114, "kvkkz", 4, "hungry", "colossal", 1904.58, 4);
INSERT INTO cryptofish VALUES (63, "ttizt", 2, "grumpy", "large", 175.38, 33);
INSERT INTO cryptofish VALUES (197, "yigfg", 6, "bored", "tiny", 113.09, NULL);
INSERT INTO cryptofish VALUES (106, "irqff", 3, "lonely", "giant", 1770.03, 1);
INSERT INTO cryptofish VALUES (72, "yeyyy", 2, "lonely", "colossal", 397.04, 21);
INSERT INTO cryptofish VALUES (104, "pgfzp", 3, "lonely", "medium", 1098.03, 12);
INSERT INTO cryptofish VALUES (152, "xrdwr", 5, "sleepy", "medium", 2902.51, 3);
INSERT INTO cryptofish VALUES (99, "lddaf", 3, "grumpy", "large", 71.95, 27);
INSERT INTO cryptofish VALUES (116, "ziiaz", 4, "sleepy", "medium", 1181.25, 30);
INSERT INTO cryptofish VALUES (118, "ccrsb", 4, "sleepy", "giant", 45.09, 36);
INSERT INTO cryptofish VALUES (140, "umgrm", 4, "lonely", "medium", 2550.33, 11);
INSERT INTO cryptofish VALUES (133, "oppeu", 4, "grumpy", "small", 1412.4, 35);
INSERT INTO cryptofish VALUES (70, "ndvva", 2, "lonely", "giant", 1551.77, 16);
INSERT INTO cryptofish VALUES (188, "focdc", 6, "sleepy", "medium", 2547.23, NULL);
INSERT INTO cryptofish VALUES (191, "mmwrp", 6, "sleepy", "tiny", 3830.74, NULL);
INSERT INTO cryptofish VALUES (60, "rmmft", 2, "playful", "colossal", 103.2, 17);
INSERT INTO cryptofish VALUES (125, "sffnf", 4, "bored", "tiny", 669.09, 20);
INSERT INTO cryptofish VALUES (107, "cgemk", 3, "lonely", "tiny", 2913.09, 19);
INSERT INTO cryptofish VALUES (76, "llayw", 3, "hungry", "giant", 1194.47, 21);
INSERT INTO cryptofish VALUES (160, "fcnwn", 5, "bored", "giant", 1276.5, 25);
INSERT INTO cryptofish VALUES (97, "umppl", 3, "grumpy", "small", 1999.06, 34);
INSERT INTO cryptofish VALUES (11, "isyie", 1, "sleepy", "tiny", 13.18, 25);
INSERT INTO cryptofish VALUES (6, "drssk", 1, "hungry", "colossal", 133.54, 25);
INSERT INTO cryptofish VALUES (150, "nznnn", 5, "hungry", "colossal", 4239.5, 19);
INSERT INTO cryptofish VALUES (90, "suwxs", 3, "bored", "colossal", 3983.66, 15);
INSERT INTO cryptofish VALUES (44, "ufupf", 2, "sleepy", "medium", 720.96, 29);
INSERT INTO cryptofish VALUES (68, "ttfyy", 2, "lonely", "medium", 1874.73, 36);
INSERT INTO cryptofish VALUES (148, "iinvw", 5, "hungry", "giant", 629.3, 2);
INSERT INTO cryptofish VALUES (145, "xpixp", 5, "hungry", "small", 7900.8, 10);
INSERT INTO cryptofish VALUES (39, "glvio", 2, "hungry", "large", 1479.56, 20);
INSERT INTO cryptofish VALUES (141, "qncja", 4, "lonely", "large", 4697.37, 6);
INSERT INTO cryptofish VALUES (135, "oeuoo", 4, "grumpy", "large", 1578.64, 4);
INSERT INTO cryptofish VALUES (194, "vpbbg", 6, "bored", "medium", 654.99, NULL);
INSERT INTO cryptofish VALUES (52, "ppqzq", 2, "bored", "giant", 558.16, 25);
INSERT INTO cryptofish VALUES (169, "hcfcf", 5, "grumpy", "small", 1217.55, 27);
INSERT INTO cryptofish VALUES (41, "gdrrn", 2, "hungry", "tiny", 1.83, 32);
INSERT INTO cryptofish VALUES (213, "wkjkl", 6, "lonely", "large", 263.91, NULL);
INSERT INTO cryptofish VALUES (58, "uuooo", 2, "playful", "giant", 2667.26, 24);
INSERT INTO cryptofish VALUES (67, "nqrqn", 2, "lonely", "small", 1428.52, 30);
INSERT INTO cryptofish VALUES (62, "bqbyq", 2, "grumpy", "medium", 914.03, 35);
INSERT INTO cryptofish VALUES (10, "evkuv", 1, "sleepy", "giant", 288.56, 15);
INSERT INTO cryptofish VALUES (139, "kjsss", 4, "lonely", "small", 1304.78, 12);
INSERT INTO cryptofish VALUES (66, "eveep", 2, "grumpy", "colossal", 95.87, 32);
INSERT INTO cryptofish VALUES (54, "jnjdd", 2, "bored", "colossal", 3289.77, 25);
INSERT INTO cryptofish VALUES (86, "cclld", 3, "bored", "medium", 2092.79, 36);
INSERT INTO cryptofish VALUES (185, "jjcoq", 6, "hungry", "tiny", 4290.96, NULL);
INSERT INTO cryptofish VALUES (59, "hjjww", 2, "playful", "tiny", 1311.54, 26);
INSERT INTO cryptofish VALUES (93, "llsut", 3, "playful", "large", 515.68, 30);
INSERT INTO cryptofish VALUES (124, "hfvvp", 4, "bored", "giant", 3076.2, 19);
INSERT INTO cryptofish VALUES (131, "lcplw", 4, "playful", "tiny", 6423.04, 20);
INSERT INTO cryptofish VALUES (13, "ojvbb", 1, "bored", "small", 222.35, 7);
INSERT INTO cryptofish VALUES (61, "mxppu", 2, "grumpy", "small", 1648.53, 1);
INSERT INTO cryptofish VALUES (184, "sttuz", 6, "hungry", "giant", 1786.98, NULL);
INSERT INTO cryptofish VALUES (176, "jmlfy", 5, "lonely", "medium", 1423.55, 32);
INSERT INTO cryptofish VALUES (198, "iemei", 6, "bored", "colossal", 6349.31, NULL);
INSERT INTO cryptofish VALUES (38, "vbvbb", 2, "hungry", "medium", 300.5, 17);
INSERT INTO cryptofish VALUES (128, "rbpju", 4, "playful", "medium", 4740.32, 1);
INSERT INTO cryptofish VALUES (167, "vsfnp", 5, "playful", "tiny", 61.85, 21);
INSERT INTO cryptofish VALUES (20, "ygury", 1, "playful", "medium", 131.58, 18);
INSERT INTO cryptofish VALUES (21, "jjwbj", 1, "playful", "large", 569.71, 34);
INSERT INTO cryptofish VALUES (27, "amigi", 1, "grumpy", "large", 38.15, 19);
INSERT INTO cryptofish VALUES (55, "bgjgq", 2, "playful", "small", 665.3, 6);
INSERT INTO cryptofish VALUES (80, "tqpqs", 3, "sleepy", "medium", 1379.74, 1);
INSERT INTO cryptofish VALUES (193, "mxmmi", 6, "bored", "small", 3593.46, NULL);
INSERT INTO cryptofish VALUES (195, "pbssp", 6, "bored", "large", 12932.33, NULL);
INSERT INTO cryptofish VALUES (158, "gklkl", 5, "bored", "medium", 228.16, 33);
INSERT INTO cryptofish VALUES (34, "geegg", 1, "lonely", "giant", 197.8, 15);
INSERT INTO cryptofish VALUES (64, "jccln", 2, "grumpy", "giant", 1090.0, 14);
INSERT INTO cryptofish VALUES (16, "rwwwv", 1, "bored", "giant", 225.77, 20);
INSERT INTO cryptofish VALUES (189, "ssfom", 6, "sleepy", "large", 625.96, NULL);
INSERT INTO cryptofish VALUES (23, "mkimk", 1, "playful", "tiny", 297.92, 30);
INSERT INTO cryptofish VALUES (46, "uhuhl", 2, "sleepy", "giant", 951.9, 9);
INSERT INTO cryptofish VALUES (119, "byvjb", 4, "sleepy", "tiny", 2075.27, 23);
INSERT INTO cryptofish VALUES (172, "qloqh", 5, "grumpy", "giant", 794.67, 11);
INSERT INTO cryptofish VALUES (211, "tnqqq", 6, "lonely", "small", 5584.03, NULL);
INSERT INTO cryptofish VALUES (144, "uiiyz", 4, "lonely", "colossal", 363.74, 11);
INSERT INTO cryptofish VALUES (17, "lmaml", 1, "bored", "tiny", 213.15, 6);
INSERT INTO cryptofish VALUES (65, "wvzjw", 2, "grumpy", "tiny", 388.46, 36);
INSERT INTO cryptofish VALUES (177, "ggvcc", 5, "lonely", "large", 98.04, 9);
INSERT INTO cryptofish VALUES (200, "bbaay", 6, "playful", "medium", 2013.82, NULL);
INSERT INTO cryptofish VALUES (151, "tbmzk", 5, "sleepy", "small", 1320.83, 10);
INSERT INTO cryptofish VALUES (165, "ebquu", 5, "playful", "large", 699.65, 19);
INSERT INTO cryptofish VALUES (74, "khloo", 3, "hungry", "medium", 268.66, 34);
INSERT INTO cryptofish VALUES (199, "nsnwm", 6, "playful", "small", 5631.05, NULL);
INSERT INTO cryptofish VALUES (171, "hqqcq", 5, "grumpy", "large", 5556.72, 6);
INSERT INTO cryptofish VALUES (121, "roooo", 4, "bored", "small", 517.61, 3);
INSERT INTO cryptofish VALUES (71, "baaai", 2, "lonely", "tiny", 419.1, 26);
INSERT INTO cryptofish VALUES (183, "iflce", 6, "hungry", "large", 847.08, NULL);
INSERT INTO cryptofish VALUES (25, "djxjf", 1, "grumpy", "small", 819.59, 5);
INSERT INTO cryptofish VALUES (123, "mhmtm", 4, "bored", "large", 693.08, 1);
INSERT INTO cryptofish VALUES (33, "ufuwr", 1, "lonely", "large", 157.85, 23);
INSERT INTO cryptofish VALUES (168, "yhkdk", 5, "playful", "colossal", 4730.18, 15);
INSERT INTO cryptofish VALUES (101, "juwaw", 3, "grumpy", "tiny", 403.55, 13);
INSERT INTO cryptofish VALUES (7, "zxxsi", 1, "sleepy", "small", 19.99, 24);
INSERT INTO cryptofish VALUES (15, "rcjsg", 1, "bored", "large", 54.57, 24);
INSERT INTO cryptofish VALUES (146, "onxoy", 5, "hungry", "medium", 2059.78, 30);
INSERT INTO cryptofish VALUES (53, "ppmmm", 2, "bored", "tiny", 424.72, 6);
INSERT INTO cryptofish VALUES (212, "tqsvu", 6, "lonely", "medium", 10140.16, NULL);
INSERT INTO cryptofish VALUES (138, "amryr", 4, "grumpy", "colossal", 6239.39, 14);
INSERT INTO cryptofish VALUES (181, "aajvj", 6, "hungry", "small", 1167.46, NULL);
INSERT INTO cryptofish VALUES (30, "zrrpt", 1, "grumpy", "colossal", 8.39, 33);
INSERT INTO cryptofish VALUES (112, "tsytt", 4, "hungry", "giant", 899.79, 23);
INSERT INTO cryptofish VALUES (129, "iwwbb", 4, "playful", "large", 4481.01, 28);
INSERT INTO cryptofish VALUES (205, "hqqch", 6, "grumpy", "small", 1012.01, NULL);
INSERT INTO cryptofish VALUES (8, "dzdez", 1, "sleepy", "medium", 215.11, 28);
INSERT INTO cryptofish VALUES (110, "flwee", 4, "hungry", "medium", 1530.52, 9);
INSERT INTO cryptofish VALUES (214, "dddss", 6, "lonely", "giant", 9138.23, NULL);
INSERT INTO cryptofish VALUES (32, "ooghh", 1, "lonely", "medium", 331.93, 29);
INSERT INTO cryptofish VALUES (22, "qyvyv", 1, "playful", "giant", 263.1, 11);
INSERT INTO cryptofish VALUES (26, "ntjnn", 1, "grumpy", "medium", 608.64, 14);
INSERT INTO cryptofish VALUES (157, "heyim", 5, "bored", "small", 630.19, 13);
INSERT INTO cryptofish VALUES (208, "xkkuk", 6, "grumpy", "giant", 82.68, NULL);
INSERT INTO cryptofish VALUES (117, "dppaf", 4, "sleepy", "large", 1245.15, 5);
INSERT INTO cryptofish VALUES (175, "qppqa", 5, "lonely", "small", 1210.65, 1);
INSERT INTO cryptofish VALUES (4, "krlsw", 1, "hungry", "giant", 45.31, 32);
INSERT INTO cryptofish VALUES (96, "niuir", 3, "playful", "colossal", 200.57, 30);
INSERT INTO cryptofish VALUES (50, "eesxx", 2, "bored", "medium", 383.19, 1);
INSERT INTO cryptofish VALUES (209, "pdpek", 6, "grumpy", "tiny", 1922.08, NULL);
INSERT INTO cryptofish VALUES (35, "qvfvb", 1, "lonely", "tiny", 86.38, 19);
INSERT INTO cryptofish VALUES (132, "qqbmg", 4, "playful", "colossal", 674.57, 26);
INSERT INTO cryptofish VALUES (174, "rxltg", 5, "grumpy", "colossal", 2612.28, 24);
INSERT INTO cryptofish VALUES (14, "jkjwj", 1, "bored", "medium", 376.2, 16);
INSERT INTO cryptofish VALUES (79, "redsy", 3, "sleepy", "small", 575.84, 1);
INSERT INTO cryptofish VALUES (77, "erpme", 3, "hungry", "tiny", 3145.02, 14);
INSERT INTO cryptofish VALUES (109, "bbfbf", 4, "hungry", "small", 1723.89, 28);
INSERT INTO cryptofish VALUES (40, "jrhbr", 2, "hungry", "giant", 101.19, 22);
INSERT INTO cryptofish VALUES (48, "rttmu", 2, "sleepy", "colossal", 2334.72, 4);
INSERT INTO user VALUES (1, "eber christer", "christer.eber@uvawow.com");
INSERT INTO user VALUES (2, "welsen evan", "evan.welsen@idpwog.com");
INSERT INTO user VALUES (3, "sarah alvandi", "alvandi.sarah@tclukc.com");
INSERT INTO user VALUES (4, "dylan smith", "smith.dylan@zmbsuq.com");
INSERT INTO user VALUES (5, "jessica paul", "paul.jessica@ccmtkt.com");
INSERT INTO user VALUES (6, "timmy nakamura", "nakamura.timmy@bgqqcx.com");
INSERT INTO user VALUES (7, "joseph bob", "bob.joseph@kqyiol.com");
INSERT INTO user VALUES (8, "nathan chad", "chad.nathan@yxvgel.com");
INSERT INTO user VALUES (9, "kimberly donna", "donna.kimberly@plgnmd.com");
INSERT INTO user VALUES (10, "joshua jackson", "jackson.joshua@oxqlhg.com");
INSERT INTO user VALUES (11, "christine maggie", "maggie.christine@vefkfe.com");
INSERT INTO user VALUES (12, "ryan oliver", "oliver.ryan@zrpsyx.com");
INSERT INTO user VALUES (13, "amanda randy", "randy.amanda@dllpfq.com");
INSERT INTO user VALUES (14, "chris patricia", "patricia.chris@bdlgiw.com");
INSERT INTO user VALUES (15, "ashley barbara", "barbara.ashley@vycqfa.com");
INSERT INTO user VALUES (16, "brandon steven", "steven.brandon@krypqn.com");
INSERT INTO user VALUES (17, "brittany karen", "karen.brittany@zkiczi.com");
INSERT INTO user VALUES (18, "jennifer jacob", "jacob.jennifer@uxinho.com");
INSERT INTO user VALUES (19, "ryan cameron", "cameron.ryan@qpqzfh.com");
INSERT INTO user VALUES (20, "james kelly", "kelly.james@wypybg.com");
INSERT INTO user VALUES (21, "rachel lucas", "lucas.rachel@scthhy.com");
INSERT INTO user VALUES (22, "melissa elizabeth", "elizabeth.melissa@zwxffb.com");
INSERT INTO user VALUES (23, "joseph peter", "peter.joseph@jldsxr.com");
INSERT INTO user VALUES (24, "daniel debra", "debra.daniel@cbfytn.com");
INSERT INTO user VALUES (25, "jose tracy", "tracy.jose@ormghg.com");
INSERT INTO user VALUES (26, "emily victor", "victor.emily@blbmiw.com");
INSERT INTO user VALUES (27, "kevin tony", "tony.kevin@vhyxmi.com");
INSERT INTO user VALUES (28, "matthew jason", "jason.matthew@bjbgrz.com");
INSERT INTO user VALUES (29, "michael gabriel", "gabriel.michael@kwrhlo.com");
INSERT INTO user VALUES (30, "brian julie", "julie.brian@qpfiup.com");
INSERT INTO user VALUES (31, "lauren julian", "julian.lauren@frfnfr.com");
INSERT INTO user VALUES (32, "amanda carlos", "carlos.amanda@nekrxb.com");
INSERT INTO user VALUES (33, "derek philip", "philip.derek@xfbywp.com");
INSERT INTO user VALUES (34, "jennifer frank", "frank.jennifer@zminmq.com");
INSERT INTO user VALUES (35, "stephanie gina", "gina.stephanie@lzvgle.com");
INSERT INTO user VALUES (36, "andrew kyle", "kyle.andrew@akhvql.com");