PROC IMPORT DATAFILE="C:\Local\test.csv"
     OUT=work.DATA
     DBMS=CSV;
RUN;

*Define variable lists;
%let Xlist = NUMBRANCH -- FAMINC_IND
             DEBT_MDN_SUPP -- LO_INC_COMP_ORIG_YR2_RT;

*Standardize changing variables;
PROC STANDARD DATA=DATA MEAN=0 STD=1
    OUT=DATAz;
    VAR &Xlist;
RUN;

*Simple Linear Regression;
PROC REG DATA=DATAz;
    MODEL MD_EARN_WNE_P10 = &Xlist;
    OUTPUT OUT=REG_DATAz_OUT;
QUIT;

*Simple Linear Regression | SELECTION = Forward;
PROC REG DATA=DATAz;
    MODEL MD_EARN_WNE_P10 = &Xlist / SELECTION=FORWARD;
    OUTPUT OUT=REG_DATAz_OUT_1 H=lev COOKD=Cookd DFFITS=dffit;
QUIT;

*Simple Linear Regression | SELECTION = Stepwise;
PROC REG DATA=DATAz;
    MODEL MD_EARN_WNE_P10 = &Xlist / SELECTION=STEPWISE;
    OUTPUT OUT=REG_DATAz_OUT_2 H=lev COOKD=Cookd DFFITS=dffit;
QUIT;

*PCA;
PROC PRINCOMP DATA=DATAz OUT=PCA_DATAz;
    VAR &Xlist;
RUN;

*Simple Linear Regression with PCA;
PROC REG DATA=PCA_DATAz;
    MODEL MD_EARN_WNE_P10 = Prin1 -- Prin4;
    OUTPUT OUT=REG_PCA_DATAz_OUT;
QUIT;

*Simple Linear Regression with PCA | SELECTION = Forward;
PROC REG DATA=PCA_DATAz;
    MODEL MD_EARN_WNE_P10 = Prin1 -- Prin4 / SELECTION=FORWARD;
    OUTPUT OUT=REG_PCA_DATAz_OUT_1 H=lev COOKD=Cookd DFFITS=dffit;
QUIT;

*Simple Linear Regression with PCA | SELECTION = Stepwise;
PROC REG DATA=PCA_DATAz;
    MODEL MD_EARN_WNE_P10 = Prin1 -- Prin4 / SELECTION=STEPWISE;
    OUTPUT OUT=REG_PCA_DATAz_OUT_2 H=lev COOKD=Cookd DFFITS=dffit;
QUIT;
