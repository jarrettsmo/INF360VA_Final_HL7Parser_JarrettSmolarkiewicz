hl7 = """MSH|^~\&|QLS^2.16.840.1.113883.3.165.2^ISO|QUEST WEST HILLS^05D0642827^CLIA|NV^2.16.840.1.114222.4.3.2.2.3.600.4^ISO|NVDOH^2.54.944.1.447329.0.2.400493^ISO|20220909040419.1651-0700||ORU^R01^ORU_R01|MET-ELRNV60-LV142381S-20220909-20220909 04:04:19.1651|P|2.5.1|||AL|AL|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.11^ISO
PID|1||104417^^^Banner Churchill Community Hospital&29D0539273&CLIA^MR^Banner Churchill Community Hospital&29D0539273&CLIA~12345678987^^^Banner Churchill Community Hospital&29D0539273&CLIA^PI^Banner Churchill Community Hospital&29D0539273&CLIA~XxxXx1234^^^SSN&2.16.840.1.113883.4.1&ISO^SS||LastName^FirstName^MiddleName^^^^L||19791028|M||2106-3^White^CDCREC^309316^White/Caucasian^L^2.5.1|1248 Anywhere Street^^FALLON^NV^89406^USA^C||^PRN^PH^^^775^1234567|||||||||N^Not Hispanic or Latino^HL70189^152116557^Not Hispanic or Latino^L^2.5.1
ORC|RE|04295406G0k6G^QUEST^2.16.840.1.113883.3.165.5^ISO|LV130458S6G0k6G_395QAW^QUEST^2.16.840.1.113883.3.165.4^ISO||CM|||||||1861572679^WATSON^DAVID^^^^^^NPI&2.16.840.1.113883.4.6&ISO^L^^^NPI^^^^^^^^||^^^^^^|||||||DESERT VIEW HOSPITAL-CPU^D|360 S LOLA LN^^PAHRUMP^NV^89048-0884^USA^O|^WPN^PH^^1^775^7517852^^OFFICE CONTACT: BRYAN CURTIS|360 S LOLA LN^^PAHRUMP^NV^89048-0884
OBR|1|04295406G0k6G^QUEST^2.16.840.1.113883.3.165.5^ISO|LV130458S6G0k6G_395QAW^QUEST^2.16.840.1.113883.3.165.4^ISO|^^^395^CULTURE, URINE, ROUTINE^L^^v unknown|||202209061012-0700|||||||||1861572679^WATSON^DAVID^^^^^^NPI&2.16.840.1.113883.4.6&ISO^L^^^NPI^^^^^^^^|^^^^^^|||||20220908143813-0700|||F||||||
OBX|1|CE|43409-2^BACTERIA ISLT CULT^LN^75000300^ISOLATE 1:^L^^v unknown|1|409801009^Klebsiella pneumoniae (ESBL)^SCT^KPESBL^Klebsiella pneumoniae (ESBL)^L|||A^Abnormal (applies to non-numeric results)^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
NTE|1||KLEBSIELLA PNEUMONIAE (ESBL)
NTE|2||GREATER THAN 100,000 CFU/ML OF
NTE|3||ESBL RESULT: THE ORGANISM HAS BEEN CONFIRMED AS AN ESBL PRODUCER.
OBX|2|NM|18906-8^CIPROFLOXACIN SUSC ISLT^LN^77002706^CIPROFLOXACIN^L^^v unknown|1|2|1^^L||R^Resistant. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
OBX|3|SN|18932-4^IMIPENEM SUSC ISLT^LN^77003906^IMIPENEM^L^^v unknown|1|<=^0.25|1^^L||S^Susceptible. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
OBX|4|ST|18878-9^CEFAZOLIN SUSC ISLT^LN^77000906^CEFAZOLIN^L^^v unknown|1|>=64,E127|||R^Resistant. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
SPM|1|04295406G0k6G&QUEST&2.16.840.1.113883.3.165.5&ISO^LV130458S6G0k6G&QUEST&2.16.840.1.113883.3.165.4&ISO||122575003^Urine specimen (specimen)^SCT^UR^Urine^HL70487^2.5.1^V UNKNOWN^URINE|||||||||||||202209061012-0700|20220906175300-0700
"""

hl7_split = hl7.split("\n") 

def segment(hl7_split, header):
    newdict = {}
    for segment in hl7_split:
        key = segment[0:3]
        value = segment[3:]

        if key not in newdict:
            newdict[key] = []
            newdict[key].append(value)
        else:
            newdict[key].append(value)

    for occurences in range(len(newdict[header])):
        print(header + newdict[header][occurences] + "\n")
  
segment(hl7_split, "OBX")