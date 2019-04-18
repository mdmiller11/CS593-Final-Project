import pandas as pd
import numpy as np


df = pd.read_csv('MERGED2014_15_PP.csv', delimiter=',') 
print(df.shape)
df = df.drop(['ACCREDAGENCY',  'INSTURL',  'NPCURL',  'HCM2',  'LOCALE',  'LOCALE2',  'LATITUDE',  'LONGITUDE',  'CCBASIC',  'CCUGPROF',  'CCSIZSET',  'HBCU',  'PBI',  'ANNHI',  'TRIBAL',  'AANAPII',  'HSI',  'NANTI',  'MENONLY',  'WOMENONLY',  'RELAFFIL',  'UG',  'UGDS_WHITENH',  'UGDS_BLACKNH',  'UGDS_API',  'UGDS_AIANOLD',  'UGDS_HISPOLD',  'UG_NRA',  'UG_UNKN',  'UG_WHITENH',  'UG_BLACKNH',  'UG_API',  'UG_AIANOLD',  'UG_HISPOLD',  'PPTUG_EF2',  'CURROPER',  'NPT4_PROG',  'NPT4_OTHER',  'NPT41_PROG',  'NPT42_PROG',  'NPT43_PROG',  'NPT44_PROG',  'NPT45_PROG',  'NPT41_OTHER',  'NPT42_OTHER',  'NPT43_OTHER',  'NPT44_OTHER',  'NPT45_OTHER',  'NPT4_048_PROG',  'NPT4_048_OTHER',  'NPT4_3075_PROG',  'NPT4_3075_OTHER',  'NPT4_75UP_PROG',  'NPT4_75UP_OTHER',  'NUM4_PROG',  'NUM4_OTHER',  'NUM41_PROG',  'NUM42_PROG',  'NUM43_PROG',  'NUM44_PROG',  'NUM45_PROG',  'NUM41_OTHER',  'NUM42_OTHER',  'NUM43_OTHER',  'NUM44_OTHER',  'NUM45_OTHER',  'C150_4_POOLED',  'C150_L4_POOLED',  'POOLYRS',  'D150_4_POOLED',  'D150_L4_POOLED',  'C150_4_WHITENH',  'C150_4_BLACKNH',  'C150_4_API',  'C150_4_AIANOLD',  'C150_4_HISPOLD',  'C150_L4_WHITENH',  'C150_L4_BLACKNH',  'C150_L4_API',  'C150_L4_AIANOLD',  'C150_L4_HISPOLD',  'C200_4_POOLED',  'C200_L4_POOLED',  'POOLYRS200',  'D200_4_POOLED',  'D200_L4_POOLED',  'UG25ABV',  'CDR2',  'GRAD_DEBT_MDN10YR',  'COUNT_ED',  'AGE_ENTRY_SQ',  'AGEGE24',  'LNFAMINC',  'LNFAMINC_IND',  'PCT_WHITE',  'PCT_BLACK',  'PCT_ASIAN',  'PCT_HISPANIC',  'PCT_BA',  'PCT_GRAD_PROF',  'PCT_BORN_US',  'MEDIAN_HH_INC',  'POVERTY_RATE',  'UNEMP_RATE',  'LN_MEDIAN_HH_INC',  'FSEND_COUNT',  'FSEND_1',  'FSEND_2',  'FSEND_3',  'FSEND_4',  'FSEND_5',  'PCT10_EARN_WNE_P10',  'PCT90_EARN_WNE_P10',  'COUNT_WNE_INDEP0_INC1_P10',  'GT_25K_P10',  'MN_EARN_WNE_INDEP0_INC1_P10',  'PCT10_EARN_WNE_P6',  'PCT90_EARN_WNE_P6',  'COUNT_WNE_INDEP0_INC1_P6',  'GT_25K_P6',  'MN_EARN_WNE_INDEP0_INC1_P6',  'COUNT_NWNE_P7',  'COUNT_WNE_P7',  'MN_EARN_WNE_P7',  'SD_EARN_WNE_P7',  'GT_25K_P7',  'PCT10_EARN_WNE_P8',  'PCT90_EARN_WNE_P8',  'GT_25K_P8',  'COUNT_NWNE_P9',  'COUNT_WNE_P9',  'MN_EARN_WNE_P9',  'SD_EARN_WNE_P9',  'GT_25K_P9',  'GRAD_DEBT_MDN10YR_SUPP',  'C150_L4_POOLED_SUPP',  'C150_4_POOLED_SUPP',  'C200_L4_POOLED_SUPP',  'C200_4_POOLED_SUPP',  'CDR2_DENOM',  'T4APPROVALDATE',  'D150_4_WHITENH',  'D150_4_BLACKNH',  'D150_4_API',  'D150_4_AIANOLD',  'D150_4_HISPOLD',  'D150_L4_WHITENH',  'D150_L4_BLACKNH',  'D150_L4_API',  'D150_L4_AIANOLD',  'D150_L4_HISPOLD',  'ACCREDCODE',  'OMACHT6_FTFT',  'OMAWDP6_FTFT',  'OMACHT8_FTFT',  'OMAWDP8_FTFT',  'OMENRYP8_FTFT',  'OMENRAP8_FTFT',  'OMENRUP8_FTFT',  'OMACHT6_PTFT',  'OMAWDP6_PTFT',  'OMACHT8_PTFT',  'OMAWDP8_PTFT',  'OMENRYP8_PTFT',  'OMENRAP8_PTFT',  'OMENRUP8_PTFT',  'OMACHT6_FTNFT',  'OMAWDP6_FTNFT',  'OMACHT8_FTNFT',  'OMAWDP8_FTNFT',  'OMENRYP8_FTNFT',  'OMENRAP8_FTNFT',  'OMENRUP8_FTNFT',  'OMACHT6_PTNFT',  'OMAWDP6_PTNFT',  'OMACHT8_PTNFT',  'OMAWDP8_PTNFT',  'OMENRYP8_PTNFT',  'OMENRAP8_PTNFT',  'OMENRUP8_PTNFT',  'RET_FT4_POOLED',  'RET_FTL4_POOLED',  'RET_PT4_POOLED',  'RET_PTL4_POOLED',  'RET_FT_DEN4_POOLED',  'RET_FT_DENL4_POOLED',  'RET_PT_DEN4_POOLED',  'RET_PT_DENL4_POOLED',  'POOLYRSRET_FT',  'POOLYRSRET_PT',  'RET_FT4_POOLED_SUPP',  'RET_FTL4_POOLED_SUPP',  'RET_PT4_POOLED_SUPP',  'RET_PTL4_POOLED_SUPP',  'TRANS_4_POOLED',  'TRANS_L4_POOLED',  'DTRANS_4_POOLED',  'DTRANS_L4_POOLED',  'TRANS_4_POOLED_SUPP',  'TRANS_L4_POOLED_SUPP',  'C100_4_POOLED',  'C100_L4_POOLED',  'D100_4_POOLED',  'D100_L4_POOLED',  'POOLYRS100',  'C100_4_POOLED_SUPP',  'C100_L4_POOLED_SUPP',  'C150_4_PELL',  'D150_4_PELL',  'C150_L4_PELL',  'D150_L4_PELL',  'C150_4_LOANNOPELL',  'D150_4_LOANNOPELL',  'C150_L4_LOANNOPELL',  'D150_L4_LOANNOPELL',  'C150_4_NOLOANNOPELL',  'D150_4_NOLOANNOPELL',  'C150_L4_NOLOANNOPELL',  'D150_L4_NOLOANNOPELL',  'OMACHT6_FTFT_POOLED',  'OMAWDP6_FTFT_POOLED',  'OMACHT8_FTFT_POOLED',  'OMAWDP8_FTFT_POOLED',  'OMENRYP8_FTFT_POOLED',  'OMENRAP8_FTFT_POOLED',  'OMENRUP8_FTFT_POOLED',  'OMACHT6_PTFT_POOLED',  'OMAWDP6_PTFT_POOLED',  'OMACHT8_PTFT_POOLED',  'OMAWDP8_PTFT_POOLED',  'OMENRYP8_PTFT_POOLED',  'OMENRAP8_PTFT_POOLED',  'OMENRUP8_PTFT_POOLED',  'OMACHT6_FTNFT_POOLED',  'OMAWDP6_FTNFT_POOLED',  'OMACHT8_FTNFT_POOLED',  'OMAWDP8_FTNFT_POOLED',  'OMENRYP8_FTNFT_POOLED',  'OMENRAP8_FTNFT_POOLED',  'OMENRUP8_FTNFT_POOLED',  'OMACHT6_PTNFT_POOLED',  'OMAWDP6_PTNFT_POOLED',  'OMACHT8_PTNFT_POOLED',  'OMAWDP8_PTNFT_POOLED',  'OMENRYP8_PTNFT_POOLED',  'OMENRAP8_PTNFT_POOLED',  'OMENRUP8_PTNFT_POOLED',  'poolyrsOM_FTFT',  'poolyrsOM_PTFT',  'poolyrsOM_FTNFT',  'poolyrsOM_PTNFT',  'OMAWDP6_FTFT_POOLED_SUPP',  'OMAWDP8_FTFT_POOLED_SUPP',  'OMENRYP8_FTFT_POOLED_SUPP',  'OMENRAP8_FTFT_POOLED_SUPP',  'OMENRUP8_FTFT_POOLED_SUPP',  'OMAWDP6_PTFT_POOLED_SUPP',  'OMAWDP8_PTFT_POOLED_SUPP',  'OMENRYP8_PTFT_POOLED_SUPP',  'OMENRAP8_PTFT_POOLED_SUPP',  'OMENRUP8_PTFT_POOLED_SUPP',  'OMAWDP6_FTNFT_POOLED_SUPP',  'OMAWDP8_FTNFT_POOLED_SUPP',  'OMENRYP8_FTNFT_POOLED_SUPP',  'OMENRAP8_FTNFT_POOLED_SUPP',  'OMENRUP8_FTNFT_POOLED_SUPP',  'OMAWDP6_PTNFT_POOLED_SUPP',  'OMAWDP8_PTNFT_POOLED_SUPP',  'OMENRYP8_PTNFT_POOLED_SUPP',  'OMENRAP8_PTNFT_POOLED_SUPP',  'OMENRUP8_PTNFT_POOLED_SUPP'], axis=1)
y_median_earnings_10yrs = df['MD_EARN_WNE_P10']
print(df.shape)
#print(df.loc[1])
#countNaN = len(df) - df.count() #count of NaN values = count of all values (len(df)) - count of non-NaN values (df.count)

#print(countNaN)
for i in df.columns:
    if df[i].isnull().sum(axis = 0) > 1000:
        df = df.drop([i],axis = 1)
print(df.shape)     
for i in df.rows:
    if df[i].isnull().sum(axis = 1) > 500:
        df = df.drop([i],axis = 0)

print(df.shape)