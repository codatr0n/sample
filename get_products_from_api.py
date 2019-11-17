#!/usr/local/bin/python3
import requests
import json
import jsbeautifier

# sample_product = 'https://www.unisport.dk/api/products/batch/?list=189214'
products_men = 'https://www.unisport.dk/api/products/batch/?list=189214,188894,188896,187812,187743,174635,189187,188534,193539,189413,189188,188532,194477,187378,187404,193592,192837,193593,189052,189213,187361,193537,187738,187744,187424,187746,185074,184775,191599,187416,189212,186121,187814,193459,187813,181393,184771,187793,187717,181372,187745,181382,187425,181272,188914,193455,187431,188893,187373,187845,189032,187795,187718,187398,189216,187719,187417,188895,188571,189211,188940,193480,187739,188897,187741,187947,187349,188903,187720,187815,188918,187749,187796,188900,185078,187391,188735,188919,188924,184774,189057,181361,188569,187411,181332,187721,187354,187844,188961,188933,189215,187794,187945,188916,193466,181289,189056,181407,188907,187740,187341,188959,187377,188932,187810,187366,193468,187946,187405,187724,188819,179845,193600,187722,188970,187723,187798,188948,107,186046,188909,193573,187809,188926,188908,193446,188965,188930,187978,186043,189047,187452,188904,187750,180206,189054,187375,193465,188530,187799,187830,188734,188902,188928,188535,187453,187785,179854,187797,181378,189034,188921,187433,188832,187811,193536,192799,188574,181295,188901,187426,184744,193541,186045,188528,179351,193577,181265,193574,187933,184737,187808,141313,188934,189217,188527,185069,193599,189045,188548,187932,187470,188915,188823,179841,187367,186054,188830,185072,193575,187756,184769,188905,181399,193443,181271,184847,187800,188581,187342'
producs_kids = 'https://www.unisport.dk/api/products/batch/?list=193974,193976,187411,187452,187412,187426,193595,187427,187434,187457,187428,193596,187413,193594,187447,187437,193589,193587,187430,187414,187449,193585,187439,193588,187429,187415,193586,187448,187441,195867,195869,195877,195873,193541,193540,193542,193479,193473,193476,193469,193477,193472,193474,193471,193475,193470,193478,189217,189033,187341,186087,187933,187830,186092,189034,186090,186076,189035,189037,187777,187772,187774,189056,187847,187453,187939,187470,187755,187473,187400,189046,187776,187941,187947,187845,186116,187749,186118,186117,189047,187376,187454,187471,187843,187944,187751,189048,187474,187773,192056,189059,192052,192508,192344,189060,189061,189062,188554,188930,186089,188926,188931,188927,188835,188932,188933,188836,188934,188928,188552,188935,188929,188936,188553,188937,188837,188950,188969,188951,188972,188952,186075,188948,188970,188973,188971,188949,188954,188974,188925,187851,187932,187936,187849,188828,187832,187771,187935,187937,187753,187945,187942,186086,186072,186103,186091,186088,186115,188587,188596,188598,188588,188599,188589,188597,187852,185079,185081,185080,184777,187850,187931,187342,187848,187841,187934,184780,187831,187770,187840,184778,187846,187938,184779,187754,184781,187775,187837,187940,187747,184760,187844,187946,187750,184758,187838,187842,184755,184757,187943,187752,184759,180230,180187,180190,184714,179351,179355,179457,179453'
products_women = 'https://www.unisport.dk/api/products/batch/?list=193957,193974,193966,193969,193963,193960,193976,196165,196161,186096,186048,187404,187416,193592,187411,187424,187452,187431,193574,193575,187418,187432,187405,186121,187417,187412,187426,193854,193593,193595,187425,193852,187427,187433,187434,187468,193573,187829,187406,187423,193855,193572,193853,187435,193576,187420,187407,193579,187443,187442,193571,193581,187456,187408,193591,187419,187457,187428,187413,193590,187469,193594,187447,187436,193584,193589,187475,193582,193583,187476,187421,187430,187422,193578,187410,193588,187429,187415,187445,193570,193586,187448,187440,187441,195875,195863,195867,193537,193541,187361,193465,193466,193539,182529,193443,189601,193455,193468,193462,193536,193540,193538,187354,193542,193453,193479,193467,193464,193447,193469,193461,193477,193450,193472,193454,193474,193448,193470,193460,193478,188530,189213,189217,189211,187812,189212,189033,187743,187341,189626,187793,189625,186046,187810,186087,187933,186043,189214,187738,186095,187830,189636,189638,194239,186068,186061,186071,189216,186064,186092,189034,186090,186051,186076,189215,187762,187378,189035,189037,187797,187781,187777,187772,187380,189036,187788,187774,189629,189052,189605,189056,182521,189604,182525,189057,182523,182527,187807,187709,187458,187768,187472,187780,187355,187401,187367,187802,187712,187966,187847,187453,187939,187470,189054,187765,187399,189044,187377,187755,187473'

urls = {}
# urls['sample_product'] = sample_product
urls['products_men'] = products_men
urls['producs_kids'] = producs_kids
urls['products_women'] = products_women

for name, url in urls.items():

    print('Getting {products}'.format(products=name))
    response = requests.get(url)

    # converting response to json object
    data = json.dumps(response.json())
    data = jsbeautifier.beautify(data)

    # storing json data
    filename = 'www/webshop/{name}.json'.format(name=name)
    print('Saving {products} to {filename}'.format(
        products=name, filename=filename))
    with open(filename, "w+") as file:
        file.writelines(data)

    print('..done!\n')
