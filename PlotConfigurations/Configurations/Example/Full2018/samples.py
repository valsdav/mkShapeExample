import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

samples={}

skim=''
##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
treebasedir='/eos/user/d/dvalsecc/www/Latinos/mkShapeExample/'
directory = +'MCSamples/Example'

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
GenLepMatch   = 'GenLepMatch'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py

SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-Nano14Dec2018-v1'] ,
            ['B','Run2018B-Nano14Dec2018-v1'] ,
            ['C','Run2018C-Nano14Dec2018-v1'] ,
            ['D','Run2018D-Nano14Dec2018_ver2-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }


###########################################
#############  BACKGROUNDS  ###############
###########################################


samples['DY'] = {    'name'   :   ["nanoLatino_DYJetsToLL_M-50-LO__part3.root"],
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 5,
                }

samples['top'] = {    'name'   :   ["nanoLatino_TTTo2L2Nu__part38.root"] ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 1,
                 }

#addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)

############ WW ############

samples['WW'] = {    'name'   :  ["nanoLatino_WWTo2L2Nu__part1.root"] ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*nllW' ,
                 }

samples['VgS']  =  {  'name'   :  ["nanoLatino_Zg__part1.root"],
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 20 ,
                   }

addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass >0)')

###########################################
################## DATA ###################
###########################################

# samples['DATA']  = {   'name': [ ] ,
#                        'weight' : METFilter_DATA+'*'+LepWPCut,
#                        'weights' : [ ],
#                        'isData': ['all'],
#                        'FilesPerJob' : 20,
#                   }

# for Run in DataRun :
#         directory = treeBaseDir+'Data/Example'
#         for DataSet in DataSets :
#                 FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
#                 for iFile in FileTarget:
#                         print(iFile)
#                         samples['DATA']['name'].append(iFile)
#                         samples['DATA']['weights'].append(DataTrig[DataSet])

