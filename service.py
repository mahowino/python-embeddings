from flask import jsonify
from utils import getEmbeddings

import pinecone

pinecone.init(api_key="2673672d-c5fd-4f95-b597-3bb651997a40", environment="gcp-starter")
import pinecone



# Initialize Pinecone client



def storeEmbeddings(data):
    try:
        
        embeddingFromOpenAi = data.get("data_chunk")
        index = pinecone.Index('chat-app')
        if embeddingFromOpenAi is None:
            return jsonify({"error": "No 'data_chunk' key in the request data"}), 400

       # Upsert sample data (5 8-dimensional vectors)
        index.upsert([
            ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
            ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
            ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
            ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
            ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
        ])

        # Store the embedding in Pinecone
        index.upsert(
             ids=[data["id"]],
            vectors=[-0.03662582, -0.0024886865, 0.01808093, -0.005110421, -0.00510701, 0.02579091, -0.016293306, -0.016689038, -0.02419433, -0.004254136, 0.0025347415, -0.009968392, 0.016634455, -2.2025472E-4, -0.019240838, -0.021901805, 0.025831848, 0.006672886, 0.026650608, -0.012049404, 0.0023402863, 0.019554695, -0.0036161859, -0.014614849, -0.011455804, 0.0022567047, 0.020346163, -0.012595244, 0.0035786594, -0.03520664, 0.008085245, 0.010555169, 0.0065091345, -0.039900858, -0.020100534, -0.016634455, -0.011087362, -0.018367495, 0.019936783, 2.5628865E-4, 0.0010874143, -0.010821265, -0.01133299, 0.0072187255, -0.034360588, 0.005069483, -0.0042814277, -0.012472429, -0.010800797, 0.027510304, 0.008160299, 0.0017458331, 0.010650691, -0.01960928, -0.016334243, 0.021751698, -4.8571176E-4, 8.933855E-5, 5.475451E-4, -0.0064409045, 0.018708644, 0.0049978415, -0.038454384, 0.009900161, -0.007764565, 0.002647321, 0.005049014, -0.012690765, -0.009299738, 0.012602067, 0.014928707, 0.030976385, -1.6876245E-4, -0.009245154, 0.008283112, -0.0034899605, -0.025763618, 0.008078422, -0.027059987, -0.0084605105, 0.01974574, -0.045250084, -0.019759385, 0.016702686, 0.035534143, -0.0036844157, -0.002544976, 0.026418624, -0.017821655, -0.025695387, 0.029065946, 0.01858583, 0.0073415395, 0.009006349, -0.03618915, 0.025231425, -0.03119472, 0.009320207, 0.005530035, 0.020482622, -0.010964548, -0.012533836, 0.00281619, -0.0061031664, 0.00891765, -0.0025125667, 0.003194866, -0.005755194, -0.0065364265, -0.014505682, -0.015611006, 0.022174723, 0.007505291, -0.0489345, -0.0012170512, -0.00592918, -0.016961958, -0.006324914, -0.023662137, -0.0022891138, -0.002444337, 0.0020451918, 0.018708644, -0.016470702, 0.016347889, 0.031331178, -0.032204524, -0.005666495, -0.01400078, -0.009381614, 0.032695778, 0.008255821, 0.018353848, 0.0015010582, -0.0045509357, 0.019581987, -0.0027564887, -0.010350479, -0.02993929, -0.0057040215, -0.009756879, 0.033459954, -0.007825972, 0.010507408, 0.02143784, 0.0074438844, -0.00410403, -0.00636244, -0.003776526, -0.024371728, -0.009579481, 0.0027633118, 0.009661357, -0.012083519, 0.004434945, 0.033514537, 0.008774368, 0.04085608, -0.0023675782, 0.007102735, -0.017698841, 0.009504428, 0.024358083, -0.036380194, 0.010637045, 0.038727302, -0.015747465, -0.019281775, -0.030212209, 0.006747939, 0.035452265, 0.031795144, -0.02939345, 0.0059871757, 3.8805767E-4, -0.014860476, -0.0010780328, 0.0248084, -0.0080715995, -1.2537248E-4, -0.01726217, 0.019145316, 0.015720174, 0.006850284, -0.017234879, 0.004431533, 0.019732093, 0.0076144594, 0.019390944, -0.0126566505, -0.006546661, 0.019322714, 0.0067445277, -0.004083561, -0.660684, -0.019186255, 0.01617049, 0.011203353, 0.011360282, 0.0111283, -0.0067957, 0.015310794, -0.017153002, 0.023266403, -0.019431882, 0.028793026, -0.025299655, 0.014178177, -2.7483865E-4, -0.019049793, 0.0054959203, 0.010029798, -0.0048852623, 0.008098892, -0.010350479, -0.002693376, 0.0017842124, 0.018176451, 0.012069873, 0.0127044115, 0.015556422, -0.030730756, -0.028192604, -0.0038549905, -0.018490309, 0.013598223, 0.0073347166, -0.01580205, 0.042384427, -0.00959995, 0.027360199, 0.023184527, 0.0015897572, 0.024794754, -0.029966582, -0.009688648, -0.008651554, -0.012806756, 0.020291578, 0.013025092, -0.013618692, -0.011305698, -0.006287387, -4.3837723E-4, 0.0070890887, -0.0052332347, -0.03119472, -0.004298485, -0.017862594, -0.0037014731, 0.018258328, -0.019022502, 0.005192297, -0.009790993, 0.0030072338, -0.00720508, -0.016961958, 0.02273421, 0.003837933, 0.0010234488, -0.033350784, 0.0035343098, 0.017112063, -0.011612733, 0.007969255, 0.004799975, 0.0058131893, 7.130027E-4, 0.00978417, 0.039273143, 0.01954105, -0.011053247, -0.0032545673, -0.0051206555, 0.023266403, 0.0055334466, -0.004404241, -0.008440041, 0.020100534, -0.024439957, -0.008344519, 0.008617439, -0.0028929487, -0.006478431, 0.010991841, 0.010425532, -0.0052639386, -0.020236995, 0.0057483707, 0.0058916537, -0.017412275, -0.0025006265, 0.002998705, -0.009436198, 0.02351203, -0.0122199785, 0.018981565, -0.004683984, 0.0071641416, 0.007655397, -0.018886043, 0.0011283524, 0.022857023, -0.017862594, 0.011872007, -0.018121867, -0.008487802, -0.013407179, 0.0068605184, -0.031740557, 0.027278323, 0.023648491, 0.009968392, -0.0034421994, 0.009238332, 0.010364125, -0.006195277, -0.025886431, 0.027564889, 0.031522222, -0.015870279, -0.007477999, -0.031958897, 0.0067240587, 0.019431882, -0.010405063, 0.029229699, -0.014260054, 0.02487663, -0.016334243, 0.026432272, 0.028492816, 0.019950429, -0.008494625, -0.027551241, 0.0021236562, -0.01865406, -0.007102735, 0.005741548, -0.029120531, 0.024385374, 0.013209312, -0.014683079, 0.009756879, -0.017521443, 0.018763227, -0.022079203, 0.007723627, 0.004298485, -0.015474546, 0.0015599065, -0.01593851, -0.01960928, 0.007764565, 0.016702686, 0.02813802, -0.019295422, -0.009238332, 0.0132911885, -0.012718057, 0.0058336584, 0.030485129, -0.0029338866, -0.008535563, 0.0012298443, -0.019691154, -0.009408906, -0.02022335, 0.0043496573, 0.0099274535, -0.008685669, 0.021424195, 0.008590147, 0.009756879, 0.017507797, -0.0042029633, -0.016907373, 1.1044718E-4, 0.023771305, 0.0112442905, -0.003933455, 0.037117075, -0.017234879, 0.016238721, 0.007034505, 7.454119E-4, -0.030348668, 0.009483959, -0.0025125667, -0.00686393, 0.036352903, 0.011837891, 0.023812242, 0.033514537, 0.0033944387, 0.03526122, 0.024139745, -0.016184138, 0.0051343017, -0.04478612, 0.0027513716, -0.03064888, 0.0016221664, 0.014164532, -0.0023351691, -0.0064989, 0.004946669, -0.0034439052, 0.009204216, 0.010916787, -0.016893728, 0.018544892, -1.1556443E-4, 0.018026344, 0.004527055, 0.0019854908, 0.0040972065, -0.021560654, -0.0015070284, 0.02793333, 0.03979169, 0.007894202, 0.005782486, -0.008992704, -0.03010304, 0.013025092, -0.00891765, 0.001712571, -0.0040801493, 0.006399967, 0.029884705, -0.012370084, 0.031522222, -0.011230645, -0.0056699063, 0.033323493, 0.020550853, -0.014232761, 0.01019355, -0.015078813, -0.004871616, -0.023484739, -0.011257937, 0.043312352, -0.022979837, 0.02558622, -0.010909964, -0.009797816, -9.705706E-4, -0.017958116, -0.004257547, 0.020277932, 0.022747856, 0.035725188, 0.019227192, 0.011257937, 0.011524034, -0.013263897, 0.021697115, -0.014655787, 0.02171076, -0.004581639, -0.008726607, 0.0047488026, -0.016402474, -0.0040357998, 0.018026344, 0.015692882, 0.01810822, -0.0051547703, -7.58205E-4, -0.0074234153, 0.027237384, -0.0028213072, -0.00499443, -0.027755931, 0.034278713, 0.011442157, -0.003885694, -0.019663863, -0.0302395, -0.012138103, -0.019636571, 0.006925337, -0.0074029462, 0.022911608, -0.008173944, 0.0152425645, -0.01593851, 0.0052775843, 0.043203186, -0.020851064, 0.012492899, 0.0062737414, 0.013741506, 0.015037875, 0.0037560572, 7.667337E-4, 0.011421689, -0.0046737497, 0.013714214, 0.0086652, -0.0084605105, -0.009825109, -0.010814442, 0.008242174, -0.0025944428, -0.012383731, 0.003916397, -0.0051206555, -0.035288516, -0.0018456194, 0.008740253, -0.014628495, 0.003438788, -0.010248134, -0.03646207, 0.03258661, 0.088971816, 0.0058234236, -5.104451E-4, 0.015419962, -0.023075359, 0.02310265, -0.033842042, -0.011285229, -1.4434893E-4, -0.005253704, -0.018667707, -0.012213156, 6.348581E-5, 0.0065023117, 0.0019820791, 0.0014626789, 0.0072391946, -0.0061338698, -0.010268603, 1.8166217E-4, -0.027305614, 0.010616575, 0.0023368748, -0.0021663, -0.0031419878, 0.009013172, 0.035697896, -0.0010268603, 0.025026735, -0.032641195, -1.0980753E-4, 0.014955998, 0.01505152, -0.002788898, -0.01960928, 0.03493372, -0.008330873, 0.004608931, -0.001117265, -0.024890276, 0.015187981, 0.00914281, -0.0029697074, -0.01617049, -0.013721037, -0.021315027, -0.02385318, 0.025804557, 0.003575248, -0.025545282, 0.02690988, -0.026077475, -0.020973878, -0.008242174, -0.004001685, 0.0052366466, -0.015310794, -8.042602E-4, 0.006212334, 0.004278016, -0.0065739527, -0.020127827, -0.012977331, -0.024999443, -0.01956834, -0.047815528, -0.018381141, 0.016689038, -0.02079648, 5.6545547E-4, 0.008651554, 0.02772864, -0.031167427, 0.023825888, 0.0126566505, 0.012909101, 0.010391417, -0.010930433, -0.007607636, 0.031331178, 0.009654534, -0.031713266, 0.009040465, 0.016757268, -0.015706528, 0.009811463, 0.020059597, -0.011053247, -0.0066592405, -0.00360254, 0.009490782, -0.00932703, 0.02626852, 0.004967138, 0.009245154, -0.019077085, -0.0030754637, -0.008897182, 0.004544113, 0.005762017, -0.0024136335, 0.0038106411, 0.008699315, 0.005096775, 0.0024528657, -0.009115517, 0.0047146874, 0.045850508, 6.1151065E-4, 0.0036844157, 0.010446001, -0.01977303, 0.03755375, -0.024439957, 0.009818286, 0.021970034, -0.021506071, 0.03910939, 7.940257E-4, -0.006410201, -0.009763702, -0.023020776, 0.017971762, 0.007123204, 0.01286134, 0.0078805555, 0.006024702, -0.026364041, -0.021355966, 0.007655397, -0.0047931517, -0.0044929404, -0.0121722175, -0.034306005, -0.027414782, -0.023293694, 0.007812326, 0.021315027, 0.011182884, 0.0033824984, -0.024849337, 0.0044929404, 6.776084E-4, -0.0105142305, -0.0010413592, -0.02841094, -0.025135903, -0.007355185, -7.7270385E-4, 0.032259107, -0.016934667, 0.027865099, -0.0021560655, -0.004847736, 0.0058984766, -0.00238293, -0.005789309, -0.0035854822, 0.009149632, 0.011169238, 0.0069492175, -0.0011385868, 0.019268129, -9.786729E-5, -0.0045986967, -0.0018353849, -0.022188371, 0.0043087197, -0.045604877, 0.020032305, 0.01746686, 0.0024750403, 0.0025756794, -0.0143146375, -0.010377771, -0.013045561, 0.008051131, -0.011169238, -0.02882032, -0.021137629, 0.0309218, -0.0016946606, -0.0063794977, -0.002918535, 0.023457447, -0.004209786, -0.001543702, 0.012663473, 0.018435724, -0.024890276, 0.0025193898, -0.007921494, -0.0041927285, 0.01600674, 0.02310265, -0.03591623, 0.005652849, 0.023280049, 0.0021338908, -0.024358083, -0.019268129, 0.025340592, 0.007054974, -0.00376288, -1.946685E-4, 0.02052356, -0.015133397, -0.022447644, 0.014028071, -0.013843851, 0.007907848, -0.003844756, -0.010848558, -0.0248084, -0.0018132102, -0.012240448, -0.0072255484, 0.0032272753, -0.045523003, -0.027278323, -8.0127514E-4, 0.017180294, 0.004984196, 0.0058916537, 0.014423805, 0.011373928, -0.009654534, -0.027073633, 0.009170101, 0.011032778, 6.8485783E-4, 0.018026344, 0.019486465, -0.012165395, -0.024289852, 0.022024618, -0.020359809, -0.013052383, -0.0316041, 0.0058336584, 0.017808009, 0.019677509, -0.011912944, 0.018708644, -0.01000933, 0.012424668, -0.007962432, -0.0037662915, -0.03288682, -0.018817812, -0.01719394, 0.0026404979, -0.034142252, 0.022338476, 0.004871616, -0.021533363, -0.003391027, -0.009879692, 0.005042191, -0.0034814316, -0.010295895, 0.027496658, -0.006857107, -0.012015289, -0.0013338949, 0.04088337, -0.026186643, 0.010671159, -0.013598223, 0.02925699, -0.011169238, 0.004888674, 0.016115908, -0.024044225, -0.009886515, 0.0040255655, -0.005782486, -0.0332962, -0.0014916767, -0.0018797343, 0.018640414, -0.007655397, -0.019991366, -0.0106575135, -0.03867272, -0.020209702, -0.0011138534, -0.0011232351, 0.0063180905, -0.011319344, 0.021519717, -0.027510304, 0.011885652, 0.0011940236, -0.016347889, -0.007355185, 0.0067035896, 0.035179347, -0.0222566, 0.020823771, -0.02289796, 0.0019053206, -0.0017603319, 0.0072664865, 0.012486075, -0.026664253, 0.027483013, -0.00886989, 7.88482E-4, -0.0014072421, 0.0070413277, 0.016566224, 0.0029475326, -0.015924864, 0.012240448, 0.012840871, 0.009565835, -0.026896235, -0.020373454, 0.035097472, -0.0053901635, 0.008719784, -0.017112063, 0.009913808, -2.9125647E-4, -0.01960928, 0.002043486, 0.007252841, -0.027442073, -0.018640414, 0.019581987, 0.0148058925, 0.0023982818, -0.011694608, -0.0027564887, -0.018476663, -0.0047965636, 0.016074969, -0.005205943, -0.014328283, 0.014669433, 0.016361535, -0.027237384, 0.017930822, -0.013605046, -0.026350396, 0.010971371, -0.006754762, -0.037608333, -0.0057586054, -0.006945806, 0.011066893, 0.030294085, 0.0020639552, -0.028219895, 0.0022260011, -0.010637045, -0.009838754, -0.028929487, 0.009231509, 0.019350005, 0.027605826, -0.007839618, 0.026787067, 0.013052383, 0.008835775, -0.015160688, -0.006782054, -0.001908732, 0.0074507073, 0.032122646, 0.013311657, -0.01092361, -0.008897182, 0.016880082, 0.0043291883, 0.010432355, 0.0143146375, 0.0020196056, 0.002848599, -0.017494151, -0.021151276, -0.00839228, -0.012970508, 0.009770525, -0.02942074, -0.025558928, -0.017903531, 0.026486855, -0.022202017, 0.009825109, 0.0059939986, 0.0020793069, 1.9975909E-5, -0.015283503, 0.0021952977, -0.0010805913, -0.024726523, 0.0045099976, 2.223869E-4, 0.0010277132, 0.03288682, -0.0071982564, -0.013113791, -0.013809736, -0.007812326, -0.023703074, 0.0071436726, 0.007532583, -0.020414392, -0.02793333, -0.0041279104, -5.7398423E-4, -0.02939345, -0.0019513757, -0.011967528, -0.014014426, 0.0013296306, 0.0083649885, -2.767576E-4, -0.020032305, 0.011721901, -0.016225075, -0.0074370615, 0.0069492175, -0.013141083, -0.005659672, -0.009770525, 0.017521443, 0.029911997, -0.01026178, -0.030703465, -0.0035172524, -0.011735546, 0.007969255, 0.016061323, 0.23318258, -4.2457134E-5, -0.009729587, 0.016497996, 0.0178353, 0.009797816, 0.029311573, -0.020168765, 0.0015334674, 0.025941016, -0.003858402, -0.009518074, -0.012758995, -0.0032784478, 0.024494542, -0.007907848, -0.012922747, -0.028192604, -0.010295895, -0.017889885, -0.009811463, 0.0043496573, -0.01712571, -0.0013475409, 0.038454384, 0.025313301, -0.019459173, 0.006079286, 0.008501448, 0.0073142475, -0.023457447, -0.010104851, 0.021492425, -0.0037014731, -0.0010882672, 0.0041927285, 0.019309068, -0.017275816, -2.8720533E-4, 0.021110337, -0.0018558538, -0.026172997, -0.011223822, -0.011844714, -0.012247271, 0.012697589, 5.3773704E-4, -0.027128216, -0.0061509274, 0.022010973, -0.03962794, -0.0135914, 0.04036482, 0.013011446, 0.013011446, 8.821916E-6, -0.004441768, 0.010480116, -0.029966582, 0.0026080888, 0.002877597, 0.05466581, 0.0076144594, 5.748371E-4, -0.019964075, 0.017767072, -0.015488192, -0.010268603, 0.009013172, -0.009101871, -0.02882032, -0.02501309, 7.2792795E-4, 0.0026012657, -0.029502617, -0.02613206, 0.0032545673, 0.029366158, 0.0018029757, 0.009361145, -0.024358083, -0.014246408, -0.014396513, -0.009415729, -0.04243901, -0.021192214, 0.015979448, 0.011803776, 0.01913167, -0.017494151, 0.02504038, -0.012035758, -0.007355185, -0.033214327, 0.0040972065, 0.004243901, 0.009408906, 0.017848948, -0.002606383, 0.005441336, -0.009211039, -0.005697198, 0.01252019, 0.006959452, -0.0142191155, 0.007505291, 0.008849421, 0.012233625, -0.002606383, -0.023607552, 0.008958588, -0.007812326, 0.0015087341, 0.014478389, 0.0051001864, 0.009715941, -0.0058234236, -0.0093884375, 0.020482622, 0.0052025313, 0.04050128, -0.011687785, -0.013707391, 0.020960232, 0.0016417825, -0.0028690682, -0.042739224, -0.0014908238, 0.011380751, -0.03856355, 0.0019070263, -0.003500195, 0.029038655, -0.009026819, -0.004663515, 0.028683858, -0.018913334, -0.014014426, -0.014833185, -0.016566224, -0.031276595, 0.013987134, -0.008017016, -0.0054583936, -0.011981174, -0.022761501, 0.03283224, -0.0105142305, 0.009408906, -0.0018780286, -0.030348668, 0.0045986967, -0.0032784478, 0.031112844, 0.02857469, 0.013202489, -0.040610448, -0.02184722, -0.013393533, 0.017576028, -0.028056143, 0.011257937, 0.031740557, -0.008440041, -0.027687702, -0.022161078, -0.17674279, 0.027360199, 0.01763061, -0.03275036, -0.0038106411, -0.0031743972, 0.001489118, 0.005165005, 0.007355185, 0.017384984, 0.024822045, 0.0029321809, 0.01712571, -0.017794363, -0.0053355796, -0.007634928, -0.012881809, 0.006836638, 0.029147822, 0.028219895, 0.0148058925, 0.006324914, 0.013379888, 0.0030294084, -0.003073758, 0.010841735, -0.011612733, 0.02337557, 0.005461805, 0.008617439, -0.02487663, -0.012056227, 0.0019837848, 0.016607163, 0.013809736, 0.022829732, -0.013741506, -0.0105347, -0.008753899, 0.025763618, 0.015993094, 0.01808093, -0.002707022, -0.0191999, -0.01420547, 0.026145706, 0.024276206, 0.014082655, 0.005021722, -0.0071163806, 0.009320207, -0.026445918, 0.0071914336, 0.0051888856, 8.251556E-4, -0.014833185, -0.0021714172, 0.021901805, 0.0022703507, 0.011141946, -0.015201626, -0.012206333, 0.025627159, -0.0012579892, -0.0055812076, -0.01511975, -0.0068161692, -0.013857497, -0.0353431, 0.026991757, 0.006608068, -0.014696725, 0.014396513, -0.028492816, 0.013529994, -0.01254066, -0.03326891, -0.012288209, -0.005956472, 4.413623E-4, -0.0011198235, 0.016402474, -0.010807619, 0.011326167, 0.018012699, 0.0021236562, 0.024030577, -0.012854517, 0.019295422, -0.010589284, 0.025217779, -0.011592263, -0.006147516, -0.0033245028, 0.011885652, 0.017576028, 0.017958116, 0.0033620293, -0.027305614, -0.013652807, 0.0015181158, -0.008344519, -0.02355297, 0.007996547, 0.023170881, 0.013918904, 0.005912123, 0.01746686, 0.015147042, -0.007655397, 0.0038345216, 0.012772641, 0.022188371, 0.03575248, -0.012458784, 0.016020386, 2.4264265E-4, -0.004544113, 0.014260054, 0.006884399, 0.04424028, 0.0063487943, -0.002328346, -0.0074984683, 0.017275816, -0.003235804, -0.106274925, -0.030758047, 0.02330734, 0.028056143, -0.022788793, 0.039682522, -0.0045099976, 0.03367829, -0.024221621, 0.0011522328, 0.0030891097, 0.006140693, -0.017153002, 0.002417045, -0.0051957085, 0.0039300434, -0.007785034, -0.014055364, -0.008153476, 0.032968696, -0.02330734, -0.015542776, -0.010507408, -0.010882672, -0.027141862, -0.018667707, -0.005970118, 0.021983681, 0.015556422, -0.021260444, -0.017030189, -0.0131479055, -0.007853264, -0.029884705, -0.030703465, 0.016825499, -0.025190488, 0.015952155, 0.029857414, -0.0064750193, 0.010405063, 0.021178568, -0.0152425645, 0.0024255738, -0.007007213, -0.007894202, -0.012151749, 0.030676173, -0.01400078, -0.02025064, -0.018162806, -0.011612733, -0.024753815, -0.009968392, 0.04063774, -0.020059597, 0.00818759, 0.045959674, -0.027332906, 0.004724922, -0.017644258, -0.011353459, -0.01327072, 0.0064886655, 0.0050285454, 0.013802913, -0.024999443, -0.01126476, 0.028793026, -0.015078813, -0.019759385, 0.016607163, -0.023866827, 0.00779868, -0.028356355, -0.008672023, -0.026418624, -0.04047399, 0.008890359, -0.011401219, -0.009190571, -0.014396513, -0.004619166, -0.007532583, 0.003215335, -0.0036230087, 0.020755542, 0.026022892, 1.0037261E-4, -0.0072664865, 0.0043633035, 0.010507408, 0.020236995, -0.023866827, 0.0060826973, 0.002754783, 0.011530857, 0.0068878103, 0.0044076527, -0.014232761, -0.0061236355, -0.037662916, -0.036844157, 0.017903531, -0.002713845, -0.014287345, -0.01033001, -0.012083519, 0.008924474, -0.0143146375, -0.0040357998, -0.012383731, -0.02884761, 0.011640024, -0.030730756, 0.014642141, -0.014846831, -0.02942074, 0.034442466, 0.0037492341, 0.035424974, 0.012083519, 0.0027803693, 0.0052571152, 0.001908732, 0.0047351564, 0.008535563, -0.011408043, -0.023170881, 0.0066660633, -0.003513841, -0.012902278, 0.02446725, -0.034879137, -0.008767545, -0.0056562605, 0.014028071, -0.006683121, 0.014833185, 0.010930433, -0.013761975, 0.0021373022, -0.014014426, -0.004404241, 0.010207196, 0.016825499, 0.0035991282, -0.014655787, -0.023457447, 0.004134733, 0.02273421, -0.015078813, 0.0035172524, 0.0027104337, -0.01954105, -0.005956472, -0.013222959, -0.014655787, 0.0057006096, -0.009695472, 0.00752576, -0.021956388, 0.04767907, 0.009429375, 0.006307856, -0.022474935, 0.0041279104, -0.007477999, -0.010275426, 0.008958588, 0.0063180905, -0.01441016, -0.02433079, -0.009579481, 0.01814916, 0.0026916703, 0.019950429, -0.0029867648, 0.015283503, 0.0061134007, -0.01808093, 0.021587947, -4.0063757E-4, -8.027677E-5, -0.033814747, 0.020973878, 0.011114654, -0.0017620377, -0.011510388, 0.0129978, -0.007177788, 0.022447644, -0.039873566, 0.013448117, -0.016020386, -0.0048511475, 0.005342403, 0.014955998, -0.013987134, 0.0035547789, 0.017425923, 0.029011363, 0.020441685, 0.0019752563, 0.005577796, -0.0027001991, -0.005096775, 0.021778991, -0.019322714, -0.008214883, 0.0040733265, -0.003981216, -2.1876219E-4, -0.009770525, -4.2942207E-4, 0.018817812, -0.0013739801, -0.010862203, -0.007969255, -0.019145316, -0.022775147, 0.030294085, 0.023457447, -0.016429765, 0.032177232, -0.01406901, 0.007846441, 0.014532973, -0.0049262005, -0.027865099, 0.015829341, -0.0071641416, 0.01272488, -0.016306952, -0.007860087, -0.007873733, -0.018053638, -0.012056227, 0.004752214, 0.031795144, -0.014792247, 0.06839367, -0.013018269, -0.016225075, -0.0023385806, 0.019964075, 0.026514146, 0.02289796, -0.009183748, -4.0511516E-4, -0.0030225855, 0.029911997, 0.0011795247, 0.013106967, -6.1705435E-4, -0.009279269, 0.0037321767, -0.012376907, 0.012636181, -0.0036537123, -0.008494625, 0.020714603, 0.008146653, 0.025122257, 0.002979942, 0.0068400498, -0.0080238385, 0.021792637, -0.016825499, -0.008542386, -0.008794837, -0.006249861, 0.0025466818, 0.02052356, -0.011530857, 0.017166648, 0.002877597, 0.012233625, 0.014983291, -0.006167985, 0.03105826, 0.0025552106, 0.00281619, -0.019554695, 0.005171828, 0.03359641, -0.012758995, -0.018231034, -0.010616575, -0.044431325]
            )

        return jsonify({"message": "Embedding stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

def searchEmbeddings(query):
      
        query_vector=getEmbeddings(text_chunk=query);

        if query_vector is None:
            return jsonify({"error": "No 'query_vector' key in the request data"}), 400

        # Search Pinecone index by query_vector
        results = pinecone.query(queries=[query_vector], top_k=10)  

        # Extract the results
        search_results = []
        for result in results[0].matches:
            search_results.append({"id": result.id, "score": result.score})

        return jsonify({"results": search_results}), 200