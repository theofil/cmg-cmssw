from DataFormats.FWLite import Events as FWLiteEvents

import logging
import pprint

from ROOT import gROOT, gSystem, AutoLibraryLoader

print "Loading FW Lite"
gSystem.Load("libFWCoreFWLite");
gROOT.ProcessLine('FWLiteEnabler::enable();')

gSystem.Load("libFWCoreFWLite");
gSystem.Load("libDataFormatsPatCandidates");

from ROOT import gInterpreter
gInterpreter.ProcessLine("using namespace reco;")
gInterpreter.ProcessLine("using edm::refhelper::FindUsingAdvance;")

class Events(object):
    def __init__(self, files, tree_name,  options=None):
        logging.info(
            'opening input files:\n{}'.format(pprint.pformat(files))
            )
        if options is not None :
            if not hasattr(options,"inputFiles"):
                options.inputFiles=files
            if not hasattr(options,"maxEvents"):
                options.maxEvents = 0	
            if not hasattr(options,"secondaryInputFiles"):
                options.secondaryInputFiles = []
            elif options.secondaryInputFiles: # only if it's a non-empty list
                logging.info('using secondary input files:\n{}'.format(
                        pprint.pformat(options.secondaryInputFiles)
                        ))
            self.events = FWLiteEvents(options=options)
	else :
            self.events = FWLiteEvents(files)
        logging.info('done')

    def __len__(self):
        return self.events.size()

    def __getattr__(self, key):
        return getattr(self.events, key)

    def __getitem__(self, iEv):
        self.events.to(iEv)
        return self

