from Configurables import DaVinci, DecayTreeTuple
from DecayTreeTuple.Configuration import *
from GaudiConf import IOHelper

# This is a template! We need the exact Stripping Line name from `find_stripping_lines.py` 
# before this will output anything. Wait to run this until we have that line!

stream = 'Dimuon'
# Replace this line with the string we find from running the first script
line = 'REPLACE_ME_WITH_REAL_STRIPPING_LINE_NAME' 

dtt = DecayTreeTuple('TupleJpsiToMuMu')
dtt.Inputs = ['/Event/{0}/Phys/{1}/Particles'.format(stream, line)]
dtt.Decay = 'J/psi(1S) -> mu+ mu-'

DaVinci().UserAlgorithms += [dtt]
DaVinci().InputType = 'DST'
DaVinci().TupleFile = 'Jpsi_ntuple.root'
# Run over all events
DaVinci().EvtMax = -1
DaVinci().PrintFreq = 10000
DaVinci().DataType = '2012'
DaVinci().Simulation = False
DaVinci().Lumi = True

IOHelper().inputFiles(['data/00041834_00013937_1.dimuon.dst'])
