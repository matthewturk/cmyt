# The "octarine" colormap was originally created by Matthew Turk within the yt-project

import numpy as np

viscm_parameters = {
    "xp": [
        -6.0027356902356814,
        -42.46106902356901,
        41.393097643097661,
        69.344486531986547,
        6.15004208754209,
        17.695180976430976,
    ],
    "yp": [
        -19.704861111111086,
        56.857638888888886,
        -8.1597222222222001,
        58.680555555555543,
        -23.958333333333314,
        -16.059027777777771,
    ],
    "min_Jp": 17.1875,
    "max_Jp": 82.1875,
}

luts = (
    np.array(
        [
            0.01845663,
            0.01940818,
            0.02066025,
            0.02218966,
            0.02395409,
            0.02595033,
            0.02817596,
            0.03060653,
            0.03322304,
            0.03602798,
            0.03900455,
            0.04208415,
            0.04516324,
            0.04823603,
            0.05128648,
            0.05431253,
            0.05730541,
            0.06025524,
            0.0631607,
            0.06601581,
            0.0688137,
            0.07155484,
            0.07423302,
            0.07684491,
            0.07939306,
            0.08186684,
            0.08427203,
            0.08660745,
            0.08886448,
            0.09105658,
            0.09316971,
            0.09521672,
            0.09719719,
            0.09910774,
            0.10096841,
            0.10275846,
            0.10451309,
            0.10621217,
            0.10788683,
            0.10952759,
            0.1111585,
            0.11277895,
            0.11440998,
            0.11605498,
            0.11773643,
            0.11945691,
            0.12124361,
            0.1230952,
            0.12504265,
            0.12708539,
            0.12924907,
            0.13154308,
            0.13398218,
            0.13657917,
            0.13934934,
            0.14230244,
            0.14544595,
            0.14880137,
            0.15236868,
            0.15615269,
            0.16016659,
            0.16442043,
            0.16890677,
            0.1736277,
            0.17858407,
            0.18378678,
            0.18922358,
            0.19488582,
            0.20076673,
            0.2068576,
            0.21314778,
            0.21962487,
            0.22627485,
            0.23308241,
            0.24003134,
            0.2471049,
            0.25428629,
            0.26155934,
            0.26890755,
            0.27631616,
            0.28377157,
            0.29126147,
            0.29877494,
            0.30630245,
            0.31383585,
            0.3213683,
            0.32889415,
            0.33640883,
            0.34390875,
            0.35139113,
            0.35885392,
            0.36629566,
            0.37371536,
            0.38111248,
            0.38848676,
            0.39583821,
            0.40316703,
            0.41047357,
            0.41775516,
            0.42501568,
            0.4322558,
            0.43947622,
            0.44667761,
            0.4538607,
            0.46102616,
            0.4681747,
            0.4753059,
            0.48242091,
            0.48952159,
            0.49660864,
            0.50368272,
            0.5107445,
            0.51779465,
            0.52483372,
            0.53186264,
            0.53888257,
            0.54589416,
            0.55289811,
            0.55989507,
            0.56688575,
            0.57387113,
            0.58085317,
            0.58783159,
            0.59480708,
            0.60178032,
            0.60875202,
            0.61572288,
            0.62269359,
            0.6296661,
            0.63664175,
            0.64361962,
            0.65060034,
            0.65758453,
            0.66457277,
            0.67156565,
            0.67856369,
            0.68556743,
            0.69257733,
            0.69959381,
            0.70661727,
            0.71364828,
            0.72068785,
            0.7277347,
            0.73478882,
            0.74185008,
            0.74891821,
            0.7559928,
            0.76307522,
            0.77016399,
            0.77725777,
            0.78435528,
            0.79145495,
            0.7985548,
            0.8056524,
            0.81274479,
            0.8198318,
            0.82691566,
            0.83398271,
            0.84102675,
            0.84805028,
            0.85504479,
            0.8619907,
            0.86889642,
            0.87572945,
            0.88249039,
            0.88914374,
            0.89568162,
            0.90206422,
            0.90825663,
            0.91421853,
            0.91990203,
            0.92525379,
            0.93021961,
            0.93475119,
            0.93881359,
            0.94239114,
            0.94548927,
            0.94813199,
            0.950356,
            0.95220389,
            0.95371848,
            0.95494533,
            0.955918,
            0.95666379,
            0.95722053,
            0.95760023,
            0.95783176,
            0.95791958,
            0.95789564,
            0.9577547,
            0.95751076,
            0.95718454,
            0.95677095,
            0.95627776,
            0.95571186,
            0.95508526,
            0.95439943,
            0.95365604,
            0.95285946,
            0.9520137,
            0.9511224,
            0.95018892,
            0.94921639,
            0.94820771,
            0.94716564,
            0.94609279,
            0.94499169,
            0.94386477,
            0.9427144,
            0.94154291,
            0.94035262,
            0.9391458,
            0.93792477,
            0.93669181,
            0.93544924,
            0.9341994,
            0.93294465,
            0.93168737,
            0.93042998,
            0.92917492,
            0.92792467,
            0.9266817,
            0.92544809,
            0.92422626,
            0.92301878,
            0.9218282,
            0.92065707,
            0.91950796,
            0.91838341,
            0.91728597,
            0.91621816,
            0.91518248,
            0.91418144,
            0.9132175,
            0.91229316,
            0.91141094,
            0.91057341,
            0.90978329,
            0.90904349,
            0.90835722,
            0.90772821,
            0.90716087,
            0.9066524,
            0.90620748,
            0.90584124,
            0.90556585,
            0.90536904,
            0.90529003,
            0.90533583,
            0.90556318,
            0.90603649,
            0.90695623,
            0.90913313,
            0.91657895,
            0.92518702,
            0.93347579,
        ]
    ),
    np.array(
        [
            0.14549808,
            0.14959758,
            0.15353745,
            0.15733732,
            0.1610376,
            0.16463933,
            0.16813881,
            0.17155785,
            0.17491483,
            0.17819541,
            0.18141182,
            0.18458839,
            0.18770724,
            0.19077643,
            0.19381948,
            0.19681897,
            0.19978209,
            0.20272758,
            0.20564068,
            0.20852987,
            0.21140659,
            0.21425995,
            0.21710135,
            0.21993298,
            0.22274859,
            0.22556395,
            0.22836995,
            0.23116975,
            0.23397288,
            0.23676848,
            0.23957041,
            0.24237069,
            0.2451726,
            0.24798083,
            0.25078633,
            0.2536041,
            0.25641791,
            0.25924206,
            0.26206407,
            0.2648926,
            0.2677197,
            0.27054988,
            0.27337716,
            0.27620452,
            0.27902542,
            0.28184388,
            0.28465047,
            0.28745244,
            0.29023681,
            0.29301229,
            0.2957673,
            0.2985035,
            0.30121847,
            0.30390569,
            0.30656793,
            0.30919798,
            0.31179276,
            0.31435225,
            0.3168706,
            0.31934487,
            0.32177243,
            0.32414968,
            0.32647317,
            0.32873992,
            0.3309469,
            0.33309004,
            0.33516695,
            0.33717534,
            0.33911292,
            0.34097773,
            0.34276826,
            0.34448346,
            0.34612285,
            0.34768649,
            0.34917502,
            0.35058959,
            0.35193184,
            0.35320373,
            0.35440776,
            0.3555465,
            0.35662265,
            0.35763896,
            0.35859819,
            0.35950301,
            0.36035598,
            0.36115947,
            0.36191571,
            0.36262669,
            0.36329423,
            0.36391995,
            0.36450527,
            0.36505146,
            0.36555959,
            0.36603063,
            0.36646538,
            0.36686454,
            0.36722872,
            0.36755843,
            0.36785545,
            0.36811875,
            0.36834862,
            0.36854528,
            0.3687089,
            0.36883963,
            0.36893758,
            0.36900282,
            0.36903596,
            0.36903681,
            0.36900473,
            0.36893965,
            0.36884148,
            0.36871009,
            0.36854532,
            0.36834702,
            0.36811484,
            0.3678482,
            0.36754678,
            0.36721023,
            0.36683815,
            0.36643008,
            0.36598535,
            0.36550255,
            0.36498174,
            0.36442226,
            0.36382344,
            0.36318451,
            0.3625047,
            0.36178315,
            0.36101802,
            0.36020779,
            0.35935264,
            0.35845149,
            0.35750326,
            0.35650677,
            0.35546082,
            0.35436416,
            0.35321545,
            0.35201335,
            0.35075644,
            0.34944329,
            0.34807215,
            0.3466408,
            0.34514904,
            0.34359543,
            0.34197858,
            0.34029709,
            0.33854968,
            0.33673306,
            0.33484673,
            0.33289005,
            0.33086222,
            0.3287627,
            0.32659138,
            0.3243486,
            0.32203538,
            0.31964923,
            0.31718431,
            0.31465481,
            0.31206608,
            0.3094119,
            0.3067005,
            0.30395628,
            0.30116449,
            0.29836962,
            0.29556856,
            0.29281389,
            0.29011662,
            0.28754017,
            0.28514306,
            0.28299549,
            0.28118369,
            0.27980714,
            0.27897084,
            0.27877267,
            0.27928815,
            0.28055737,
            0.28257918,
            0.28531437,
            0.2886962,
            0.29264343,
            0.29707203,
            0.30189644,
            0.30704703,
            0.31246579,
            0.318088,
            0.32388104,
            0.32979805,
            0.33582149,
            0.34190762,
            0.34805406,
            0.35424005,
            0.36044006,
            0.36665573,
            0.37287672,
            0.37909448,
            0.38529658,
            0.39148116,
            0.39764648,
            0.40378866,
            0.40990456,
            0.41599162,
            0.42204777,
            0.42807135,
            0.43406103,
            0.44001575,
            0.44593465,
            0.45181705,
            0.45766241,
            0.46347028,
            0.46924029,
            0.47497214,
            0.48066556,
            0.4863203,
            0.49193612,
            0.49751281,
            0.50305013,
            0.50854783,
            0.51400566,
            0.51942335,
            0.52480059,
            0.53013708,
            0.53543248,
            0.54068668,
            0.54589935,
            0.55107004,
            0.55619831,
            0.56128369,
            0.56632567,
            0.57132372,
            0.5762773,
            0.58118582,
            0.58604867,
            0.5908652,
            0.59563471,
            0.60035645,
            0.60502957,
            0.60965313,
            0.61422605,
            0.61874705,
            0.62321462,
            0.62762687,
            0.63198146,
            0.63627878,
            0.64051559,
            0.64468414,
            0.64877752,
            0.6527965,
            0.65672131,
            0.66054037,
            0.66421949,
            0.66770704,
            0.67086745,
            0.67317041,
            0.67282641,
            0.67266658,
            0.67286793,
        ]
    ),
    np.array(
        [
            0.31784919,
            0.31399639,
            0.31040105,
            0.30704607,
            0.30380333,
            0.30070875,
            0.29782465,
            0.29508233,
            0.29241622,
            0.28993656,
            0.28760832,
            0.28531346,
            0.28318494,
            0.28120084,
            0.27922989,
            0.27740774,
            0.27570877,
            0.27402022,
            0.27246419,
            0.27099788,
            0.26955239,
            0.26822345,
            0.26693985,
            0.26569724,
            0.2645547,
            0.26340288,
            0.26231968,
            0.26128857,
            0.26024441,
            0.2592725,
            0.25827349,
            0.25730732,
            0.25634957,
            0.25536473,
            0.25441368,
            0.25338488,
            0.25238608,
            0.25130798,
            0.25022886,
            0.24907581,
            0.2478929,
            0.24663333,
            0.24532558,
            0.24393036,
            0.24247998,
            0.24092303,
            0.23931621,
            0.23757501,
            0.23579155,
            0.23385836,
            0.23186082,
            0.22975416,
            0.22753042,
            0.22523787,
            0.22279557,
            0.22026374,
            0.21765214,
            0.2148911,
            0.21203983,
            0.20910422,
            0.20605986,
            0.20289957,
            0.19965924,
            0.19633992,
            0.19294399,
            0.18945376,
            0.18589623,
            0.18228559,
            0.17863001,
            0.17493902,
            0.17122338,
            0.16749485,
            0.16376586,
            0.16004918,
            0.15635755,
            0.15270334,
            0.14909821,
            0.1455525,
            0.14207653,
            0.13867843,
            0.13536508,
            0.13214209,
            0.12901386,
            0.12598366,
            0.12305378,
            0.12022564,
            0.11749993,
            0.11487682,
            0.11235599,
            0.10993683,
            0.10761855,
            0.10540021,
            0.10328085,
            0.10125952,
            0.09933535,
            0.09750756,
            0.09577548,
            0.09413856,
            0.09259879,
            0.09115321,
            0.08980156,
            0.08854366,
            0.08737943,
            0.0863088,
            0.08533173,
            0.08444816,
            0.08365874,
            0.08296295,
            0.08235974,
            0.08184879,
            0.08142963,
            0.0811017,
            0.08086426,
            0.08071652,
            0.08065732,
            0.08068528,
            0.08079915,
            0.08099759,
            0.08127912,
            0.08164221,
            0.08208509,
            0.08260558,
            0.08320245,
            0.08387405,
            0.08461872,
            0.08543485,
            0.08632086,
            0.08727529,
            0.08829637,
            0.08938269,
            0.09053368,
            0.09174839,
            0.09302606,
            0.09436609,
            0.09576809,
            0.0972319,
            0.09875759,
            0.10034547,
            0.10199611,
            0.10371036,
            0.10548936,
            0.10733453,
            0.10924784,
            0.11123145,
            0.1132879,
            0.11542014,
            0.11763156,
            0.1199261,
            0.12230825,
            0.12478303,
            0.12735611,
            0.13003383,
            0.13282332,
            0.1357325,
            0.13877022,
            0.14194733,
            0.14527745,
            0.14877095,
            0.15244171,
            0.15631008,
            0.16039526,
            0.16471264,
            0.16929903,
            0.17416921,
            0.17936813,
            0.18491671,
            0.19087146,
            0.19726367,
            0.20413699,
            0.21153645,
            0.2195002,
            0.22805202,
            0.23719324,
            0.24689635,
            0.25710328,
            0.26773032,
            0.27867898,
            0.2898494,
            0.30115214,
            0.31251542,
            0.3238872,
            0.33520885,
            0.34646952,
            0.35766645,
            0.36875439,
            0.37976247,
            0.39066078,
            0.40148085,
            0.41217762,
            0.42279543,
            0.4333259,
            0.44374506,
            0.45408352,
            0.46434054,
            0.47451587,
            0.48459837,
            0.49459666,
            0.50451736,
            0.51436098,
            0.5241281,
            0.53381937,
            0.54343549,
            0.55297718,
            0.56244513,
            0.57184006,
            0.58116264,
            0.59041354,
            0.59959339,
            0.60870282,
            0.61774243,
            0.62671284,
            0.63561464,
            0.64444846,
            0.65321495,
            0.6619148,
            0.67054874,
            0.67911758,
            0.68762222,
            0.69606366,
            0.70444301,
            0.71276152,
            0.72102061,
            0.7292224,
            0.73736877,
            0.74546167,
            0.75350327,
            0.76149601,
            0.76944257,
            0.7773459,
            0.78520926,
            0.79303621,
            0.80083062,
            0.80859672,
            0.81633909,
            0.82406267,
            0.83177277,
            0.83947509,
            0.84717571,
            0.85488105,
            0.86259792,
            0.87033341,
            0.87809481,
            0.88590073,
            0.89376265,
            0.90168051,
            0.90966175,
            0.9177585,
            0.92595735,
            0.93431661,
            0.94285311,
            0.95166927,
            0.96090167,
            0.97095595,
            0.97849108,
            0.98057884,
            0.98147471,
        ]
    ),
    np.ones(256),
)
