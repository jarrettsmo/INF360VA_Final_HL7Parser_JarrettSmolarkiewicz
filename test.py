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

hl72 = """MSH|^~\&|MAYO CLINIC DEPT. OF LAB MED AND PATHOLOGY|MAYO CLINIC DEPT. OF LAB MED AND PATHOLOGY^2.16.840.1.113883.3.2.12.1.1^ISO|KS-MAIN|251-KS-MAIN|20201028003540-0500||ORU^R01^ORU_R01|2020102805354015005611|P|2.5.1|||NE|NE|USA||||PHLabReport-NoAck^HL7^2.16.840.1.113883.9.11^ISO
SFT|Lawson^L^^^^MAYO RD&2.16.840.1.113883.3.2.12.1&ISO^XX^^^99999|19.1|Cloverleaf IE|9999||20101113
PID|1|replaced 2|||Izetta651^Bailey598||19790520|F|||152 Yundt Dam^^Aurora^IL^60505|US|^PRN^PH^^1^645^5241300|||||||||||||||||
ORC|RE|H65126|F722049201|||||||||^MARTINEZ^JOHN D|7009204||||||||Univ of Kansas Hosp-LSI|2015 W 39th Ave^^Kansas City^KS^66103|^WPN^PH^^1^913^5880384
OBR|1|H65126^Placer Order Number^2.16.840.1.113883.3.2.12.1.99^ISO|F722049201^Filler Order Number^2.16.840.1.113883.3.2.12.1.1^ISO|^^^LYWB^Lyme Disease Ab, Immunoblot, S^L^^U|||202010221439|||7009204^Univ of Kansas Hosp-LSI^9135880384||||||^MARTINEZ^JOHN D||||||202010270952|||F
OBX|1|CE|6320-6^B burgdor IgG Ser Ql IB^LN^5744^IgG Immunoblot^L^2.40^U||260385009^Negative^SCT||Negative||||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201027095200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
OBX|2|CE|13502-0^B burgdor IgG Patrn Ser IB-Imp^LN^2992^IgG detected against:^L^2.40^U||260413007^None^SCT|^^^kDa^kDa^L^^V1|||||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201027095200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
OBX|3|CE|6321-4^B burgdor IgM Ser Ql IB^LN^23931^IgM Immunoblot^L^2.40^U||10828004^Positive^SCT||Negative|A^Abnormal^HL70078^A^Abnormal^L^2.7^V1|||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201027095200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
OBX|4|ST|13503-8^B burgdor IgM Patrn Ser IB-Imp^LN^23932^IgM detected against:^L^2.40^U||p41,p39|^^^kDa^kDa^L^^V1|||||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201027095200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
OBX|5|ST|12781-1^B burgdor Ab Patrn Ser IB-Imp^LN^6241^Interpretation^L^2.40^U||See comment for results||||||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201027095200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
NTE|1|L|IgM-class antibodies to B. burgdorferi (Lyme disease)
NTE|2|L|detected.  Results are consistent with acute or recent
NTE|3|L|infection with B. burgdorferi.  Testing of a new specimen
NTE|4|L|collected in 7-14 days to demonstrate IgG seroconversion
NTE|5|L|may be considered to confirm infection if the diagnosis is
NTE|6|L|in doubt.
NTE|7|L
NTE|8|L|IgM immunoblot results should only be considered as
NTE|9|L|indicative of recent infection in patients presenting
NTE|10|L|within 30 days of symptom onset. Consideration of IgM
NTE|11|L|immunoblot results in patients with symptoms lasting >30
NTE|12|L|days is discouraged due to the risk of false positive IgM
NTE|13|L|immunoblot results and/or prolonged IgM seropositivity
NTE|14|L|following disease resolution.
NTE|15|L|Per CDC criteria, the Lyme IgG Immunoblot is interpreted as
NTE|16|L|positive if IgG-class antibodies are detected to >=5 B.
NTE|17|L|burgdorferi proteins, and the Lyme IgM Immunoblot is
NTE|18|L|interpreted as positive if IgM-class antibodies are
NTE|19|L|detected to >=2 B. burgdorferi proteins. Immunoblot
NTE|20|L|patterns not meeting these criteria should not be
NTE|21|L|interpreted as positive. Epitopes from certain B.
NTE|22|L|burgdorferi proteins (e.g., p41) are conserved across other
NTE|23|L|bacteria, which may lead to the detection of IgM- and/or
NTE|24|L|IgG-class antibodies on the Lyme disease immunoblots in
NTE|25|L|patients without Lyme disease. Immunoblot should only be
NTE|26|L|ordered on specimens that are positive or equivocal by a
NTE|27|L|FDA-licensed Lyme disease antibody screening test (e.g.,
NTE|28|L|EIA). Results of the Lyme IgM immunoblot should not be
NTE|29|L|considered in patients with >= 30 days of symptoms.
SPM|1|H65126&Placer_LIS&2.16.840.1.113883.3.2.12.1.99&ISO^F722049201&Mayo_LIS&2.16.840.113883.1.3.2.11.1&ISO||119364003^Serum specimen (specimen)^SCT^Serum^Serum^L^07/31/2012^v1|||||||P^Patient^HL70369^P^Patient^L^2.5.1^V1|1^{#}&Number&UCUM&unit&unit&L&1.1&V1|||||202010221439|202010231452
OBR|2|H65126^Placer Order Number^2.16.840.1.113883.3.2.12.1.99^ISO|F722049201^Filler Order Number^2.16.840.1.113883.3.2.12.1.1^ISO|^^^LYME^Lyme Disease Serology, S^L^^U|||202010221439|||7009204^Univ of Kansas Hosp-LSI^9135880384||||||^MARTINEZ^JOHN D||||||202010231453|||F
OBX|1|CE|20449-5^B burgdor Ab Ser Ql IA^LN^LYME^Lyme Disease Serology, S^L^2.40^U||10828004^Positive^SCT||Negative||||F|||202010221439|24D1040592^Mayo Clinic Labs-Roch Superior Dr^L||||20201023145200||||MCLab-RO Superior Dr^A^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^24D1040592|3050 Superior Drive NW^Level 1^Rochester^MN^55901^USA^L
NTE|1|L|Not diagnostic. Supplemental testing by immunoblot has
NTE|2|L|been ordered by reflex.
SPM|1|H65126&Placer_LIS&2.16.840.1.113883.3.2.12.1.99&ISO^F722049201&Mayo_LIS&2.16.840.113883.1.3.2.11.1&ISO||119364003^Serum specimen (specimen)^SCT^Serum^Serum^L^07/31/2012^v1|||||||P^Patient^HL70369^P^Patient^L^2.5.1^V1|1^{#}&Number&UCUM&unit&unit&L&1.1&V1|||||202010221439|202010231028
"""

# hl7_split = hl7.split("\n") 
# print(*hl7_split, sep="\n\n")
# print(len(hl7_split) - 1)

hl72_split = hl72.split("\n")
print(*hl72_split, sep="\n\n")
print(len(hl72_split) - 1)

# def segment(hl7_split, header):
#     newdict = {}
#     for segment in hl7_split:
#         key = segment[0:3]
#         value = segment[3:]

#         if key not in newdict:
#             newdict[key] = []
#             newdict[key].append(value)
#         else:
#             newdict[key].append(value)

#     for occurences in range(len(newdict[header])):
#         print(header + newdict[header][occurences] + "\n")
  
# segment(hl7_split, "OBX")