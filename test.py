import pandas as pd
import re
import numpy as np
import xmltodict
import tqdm
import xml.etree.ElementTree as ET

def keyphras():
    keyphrases = pd.read_csv('Chapter05_keyphrases.csv')



    root = ET.parse("ip_3_5_man.xml")
    terms = []
    for entry in root.findall('.//entry'):
        term = entry.get('term')
        terms.append(term.lower())

    keyList = keyphrases['0'].tolist()
    keylist2 = []
    for i in keyList:
        keylist2.append(i.lower())

    common_el = set(keylist2) & set(terms)
    print(len(common_el))

def extraction_unigrams():

    df = pd.read_csv('Chapter05_keyphrases.csv')
    key = df['0'].tolist()
    unigram =[]
    ngram = []

    pattern = "\s"
    print(type(key))
    for i in key:
        if re.findall(pattern, i):
            ngram.append(i)
            #print('N-gram')
        else:
            unigram.append(i)
            #print('Unigram')
    #print(ngram)
    print(unigram)
    print(len(unigram))
    #print(len(ngram))
        
import requests
text = "Executive summary Assessment of the social science literature and regional case studies reveals how social norms, culture, and individual choices, interact with infrastructure and other structural changes over time. This provides new insight into climate change mitigation strategies, and how economic and social activity might be organised  across  sectors  to  support  emission  reductions.  To  enhance  well-being,  people  demand services and not primary energy and physical resources per se. Focusing on demand for services and the different social and political roles people play broadens the participation in climate action. Potential of demand-side actions and service provisioning systemsDemand-side mitigation and new ways of providing services can help  avoid, shift, and improve final service demand. Rapid and deep changes in demand make it easier for every sector to reduce GHG emissions in the short and medium term (high confidence). {5.2, 5.3}  The indicative potential of demand-side strategies across all sectors to reduce emissions is 40-70% by 2050 (high confidence). Technical mitigation potentials compared to the IEA WEO, 2020 STEPS baseline amounts up to 5.7 GtCO2eq for building use and construction, 8 GtCO2eq for food demand, 6.5 GtCO2eq for land transport, and 5.2 GtCO2eq for industry.Mitigation strategies can be classified as Avoid-Shift-Improve  (ASI)  options,  that  reflect  opportunities  for  socio-cultural,  infrastructural,  and technological  change.  The  greatest  Avoid  potential  comes  from  reducing  long-haul  aviation  and providing short-distance low-carbon urban infrastructures. The greatest Shift potential would come from switching to plant-based diets. The greatest Improve potential comes from within the building sector, and in particular increased use of energy efficient end-use technologies and passive housing. {5.3.1, 5.3.2, Figure 5.7, Figure 5.8, Table 5.1, Table SM.2} Socio-cultural  and  lifestyle  changes  can  accelerate  climate  change  mitigation  (medium confidence)."
with open('text_stripedtext.txt', encoding="utf8") as f:
    lines = f.readlines()
#print(lines[0])

API_URL = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": lines[0],
})       
names = [f['word'] for f in output]

print(names)
'''        else:
            print('Unigram')'''
    
    



#extraction_unigrams()

#print(terms)
#print(keyphrases.to_string())



