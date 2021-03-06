# based on CalibTracker/SiStripESProducers/test/python/read_DummyCondDBWriter_SiStripLorentzAngle_cfg.py

import FWCore.ParameterSet.Config as cms

process = cms.Process("Reader")

process.MessageLogger = cms.Service(
    "MessageLogger",
    debugModules = cms.untracked.vstring(''),
    threshold = cms.untracked.string('INFO'),
    destinations = cms.untracked.vstring('SQLiteCheck.log')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource",
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1)
)

process.poolDBESSource = cms.ESSource("PoolDBESSource",
   BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
   DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(2),
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:SiStripLorentzAngle_CalibrationEnsemble.db'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        tag = cms.string('SiStripLorentzAngle_CalibrationEnsemble_31X')
    ))
)

process.reader = cms.EDFilter("SiStripLorentzAngleDummyPrinter",
                              printDebug = cms.untracked.uint32(5)
                              )


process.p1 = cms.Path(process.reader)


