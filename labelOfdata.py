# @Time    : 3/29/22 5:11 PM
# @Author  : Shuai S
# @File    : labelOfdata.py

redisson = {5: 0, 26: 0, 35: 0, 39: 1, 40: 1, 49: 0, 64: 0, 53: 0, 71: 0, 83: 1, 84: 1, 87: 1, 89: 1, 95: 1,
            100: 1, 101: 1, 106: 1, 114: 0, 118: 1, 139: 0, 155: 1, 147: 0, 156: 1, 162: 1, 163: 1, 169: 1,
            171: 1, 174: 0, 176: 0, 178: 1, 183: 0, 199: 1, 206: 0, 207: 0, 208: 0, 216: 1, 223: 0, 224: 0,
            225: 1, 228: 0, 229: 1, 251: 1, 253: 1, 254: 1, 278: 0, 285: 1, 305: 0, 306: 0, 329: 1, 342: 1,
            345: 1, 348: 0, 355: 1, 376: 0, 386: 1, 409: 1, 421: 1, 436: 1, 455: 1, 465: 1, 467: 1, 480: 1,
            486: 1, 491: 1, 503: 0, 507: 1, 511: 0, 512: 0, 514: 1, 505: 0, 521: 0, 530: 1, 533: 1, 542: 0,
            543: 1, 545: 1, 548: 0, 549: 1, 554: 0, 558: 1, 561: 1, 562: 0, 573: 1, 575: 1, 577: 0, 581: 1,
            584: 0, 586: 1, 588: 0, 597: 0, 601: 0, 603: 0, 604: 0, 612: 1, 619: 0, 624: 1, 631: 1, 633: 0,
            634: 0, 656: 0, 670: 0, 674: 0, 682: 0, 683: 1, 693: 0, 724: 1, 738: 1, 753: 1, 755: 1, 757: 1,
            758: 1, 763: 1, 775: 1, 780: 1, 803: 0, 828: 1, 833: 0, 875: 0, 889: 1, 891: 1, 899: 1, 907: 0,
            955: 0, 956: 0, 962: 0, 963: 0, 966: 0, 977: 0, 987: 1}

redisson_exc = [39, 106, 118, 155, 156, 169, 171, 199, 216, 254, 386, 409, 421, 465, 480, 503, 533, 549, 573, 581, 612,
                738, 775, 780]
ste_exc = [39, 106, 118, 155, 156, 169, 171, 199, 216, 254, 386, 409, 421, 465, 480, 503, 533, 549, 573, 581, 738, 775,
           780]
# [39, 156, 169, 171, 199, 216, 254, 421, 465, 503, 533, 549, 573, 581, 738, 780]

redisson_label = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0,
                  0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
                  0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]

hsqldb = {2: 0, 63: 0, 235: 1, 329: 1, 393: 1, 37: 1, 197: 1, 227: 1, 276: 1, 333: 1, 222: 1, 239: 1, 250: 1, 288: 0}

hsqldb_label = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

grpc = {17: 1, 18: 1, 45: 0, 63: 0, 116: 1, 118: 0, 120: 1, 238: 1, 246: 1, 340: 0, 452: 0, 461: 0, 502: 0, 518: 0,
        576: 0, 577: 0, 578: 0, 583: 1, 622: 0, 634: 0, 644: 0, 681: 0, 696: 1, 942: 0, 945: 0, 967: 0, 970: 0, 595: 0,
        667: 0, 31: 0, 271: 0, 325: 0, 330: 1, 553: 0, 569: 0, 673: 0, 674: 0, 698: 0, 66: 0, 229: 0, 290: 0, 345: 0,
        605: 1, 755: 0, 887: 1, 889: 0, 999: 1, 80: 0, 82: 0, 99: 0, 152: 1, 153: 0, 182: 0, 227: 0, 241: 0, 976: 0,
        317: 0, 239: 1, 247: 0, 322: 0, 479: 0, 682: 0, 642: 0, 361: 0, 408: 1, 424: 0, 433: 0, 449: 0, 510: 0, 517: 1,
        544: 0, 623: 0, 626: 0, 636: 1, 656: 0, 683: 0, 765: 0, 789: 0, 792: 0, 854: 0, 875: 1, 919: 0}

grpc_label = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
              0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]

vertx = {57: 1, 60: 1, 78: 0, 117: 0, 124: 0, 250: 0, 303: 1, 325: 1, 363: 1, 423: 1, 473: 0, 477: 1, 525: 0, 584: 0,
         646: 1, 682: 1, 759: 0, 799: 0, 978: 0, 998: 0, 663: 0, 926: 0, 421: 0, 497: 0, 500: 0, 739: 0, 958: 0, 959: 0, 967: 0}

vertx_label = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
