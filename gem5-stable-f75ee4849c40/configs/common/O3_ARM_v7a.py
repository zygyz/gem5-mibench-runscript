# Copyright (c) 2012 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Ron Dreslinski


from m5.objects import *

# Simple ALU Instructions have a latency of 1
class O3_ARM_v7a_Simple_Int(FUDesc):
    opList = [ OpDesc(opClass='IntAlu', opLat=1) ]
    count = 2

# Complex ALU instructions have a variable latencies
class O3_ARM_v7a_Complex_Int(FUDesc):
    opList = [ OpDesc(opClass='IntMult', opLat=3, issueLat=1),
               OpDesc(opClass='IntDiv', opLat=12, issueLat=12),
               OpDesc(opClass='IprAccess', opLat=3, issueLat=1) ]
    count = 1


# Floating point and SIMD instructions 
class O3_ARM_v7a_FP(FUDesc):
    opList = [ OpDesc(opClass='SimdAdd', opLat=4),
               OpDesc(opClass='SimdAddAcc', opLat=4),
               OpDesc(opClass='SimdAlu', opLat=4),
               OpDesc(opClass='SimdCmp', opLat=4),
               OpDesc(opClass='SimdCvt', opLat=3),
               OpDesc(opClass='SimdMisc', opLat=3),
               OpDesc(opClass='SimdMult',opLat=5),
               OpDesc(opClass='SimdMultAcc',opLat=5),
               OpDesc(opClass='SimdShift',opLat=3),
               OpDesc(opClass='SimdShiftAcc', opLat=3),
               OpDesc(opClass='SimdSqrt', opLat=9),
               OpDesc(opClass='SimdFloatAdd',opLat=5),
               OpDesc(opClass='SimdFloatAlu',opLat=5),
               OpDesc(opClass='SimdFloatCmp', opLat=3),
               OpDesc(opClass='SimdFloatCvt', opLat=3),
               OpDesc(opClass='SimdFloatDiv', opLat=3),
               OpDesc(opClass='SimdFloatMisc', opLat=3),
               OpDesc(opClass='SimdFloatMult', opLat=3),
               OpDesc(opClass='SimdFloatMultAcc',opLat=1),
               OpDesc(opClass='SimdFloatSqrt', opLat=9),
               OpDesc(opClass='FloatAdd', opLat=5),
               OpDesc(opClass='FloatCmp', opLat=5),
               OpDesc(opClass='FloatCvt', opLat=5),
               OpDesc(opClass='FloatDiv', opLat=9, issueLat=9),
               OpDesc(opClass='FloatSqrt', opLat=33, issueLat=33),
               OpDesc(opClass='FloatMult', opLat=4) ]
    count = 2


# Load/Store Units
class O3_ARM_v7a_Load(FUDesc):
    opList = [ OpDesc(opClass='MemRead',opLat=2) ]
    count = 1

class O3_ARM_v7a_Store(FUDesc):
    opList = [OpDesc(opClass='MemWrite',opLat=2) ]
    count = 1

# Functional Units for this CPU
class O3_ARM_v7a_FUP(FUPool):
    FUList = [O3_ARM_v7a_Simple_Int(), O3_ARM_v7a_Complex_Int(),
              O3_ARM_v7a_Load(), O3_ARM_v7a_Store(), O3_ARM_v7a_FP()]


class O3_ARM_v7a_3(DerivO3CPU):
    predType = "tournament"
    localPredictorSize = 64
    localCtrBits = 2
    localHistoryTableSize = 64
    localHistoryBits = 6
    globalPredictorSize = 8192
    globalCtrBits = 2
    globalHistoryBits = 13
    choicePredictorSize = 8192
    choiceCtrBits = 2
    BTBEntries = 2048
    BTBTagSize = 18
    RASSize = 16
    instShiftAmt = 2
    LQEntries = 16
    SQEntries = 16
    LSQDepCheckShift = 0
    LFSTSize = 1024
    SSITSize = 1024
    decodeToFetchDelay = 1
    renameToFetchDelay = 1
    iewToFetchDelay = 1
    commitToFetchDelay = 1
    renameToDecodeDelay = 1
    iewToDecodeDelay = 1
    commitToDecodeDelay = 1
    iewToRenameDelay = 1
    commitToRenameDelay = 1
    commitToIEWDelay = 1
    fetchWidth = 3
    fetchToDecodeDelay = 3
    decodeWidth = 3
    decodeToRenameDelay = 2
    renameWidth = 3
    renameToIEWDelay = 1
    issueToExecuteDelay = 1
    dispatchWidth = 6
    issueWidth = 8
    wbWidth = 8
    wbDepth = 1
    fuPool = O3_ARM_v7a_FUP()
    iewToCommitDelay = 1
    renameToROBDelay = 1
    commitWidth = 8
    squashWidth = 8
    trapLatency = 13
    backComSize = 5
    forwardComSize = 5
    numPhysIntRegs = 128
    numPhysFloatRegs = 128
    numIQEntries = 32
    numROBEntries = 40

    defer_registration= False

# Instruction Cache
# All latencys assume a 1GHz clock rate, with a faster clock they would be faster
class O3_ARM_v7a_ICache(BaseCache):
    latency = '1ns'
    block_size = 64
    mshrs = 2
    tgts_per_mshr = 8
    size = '32kB'
    assoc = 4
    is_top_level = 'true'
    snapshot = False
    snapInstrP = 1000
    snapshot_path = "/home/hang/gem5/snapshot/"
    snapshot_length = 10
    snapshot_interval = 1000
    snapshot_times = 3
    snapshot_count = 1

# Data Cache
# All latencys assume a 1GHz clock rate, with a faster clock they would be faster
class O3_ARM_v7a_DCache(BaseCache):
    latency = '2ns'
    block_size = 64
    mshrs = 6
    tgts_per_mshr = 8
    size = '32kB'
    assoc = 4
    write_buffers = 16
    is_top_level = 'true'
    snapshot = True               # print snapshot enable
    snapInstrP = 10000000          # Start instruction point of snapshot printing
    snapshot_path = "/home/lhh/work/snapshot_invalid/gcc/" # snapshot printing path
    snapshot_length = 600000      # snapshot instruction length
    snapshot_interval = 1000000   # interval between two snapshots
    snapshot_times = 10           # times of snapshot that are taken
    snapshot_count = 1            # start number of snapshot
    snapshot_step = 500           # step between two snapshot

    use_lruBased = False          # lruBased function enable
    backup_en = False              # invalidBlks function enable(used to test partial backup performance)
    backup_point = 1000005        # instruction point of backup
    backup_order = 0              # order of lrubased algorithm

# TLB Cache 
# Use a cache as a L2 TLB
class O3_ARM_v7aWalkCache(BaseCache):
    latency = '4ns'
    block_size = 64
    mshrs = 6
    tgts_per_mshr = 8
    size = '1kB'
    assoc = 8
    write_buffers = 16
    is_top_level = 'true'


# L2 Cache
# All latencys assume a 1GHz clock rate, with a faster clock they would be faster
class O3_ARM_v7aL2(BaseCache):
    latency = '12ns'
    block_size = 64
    mshrs = 16
    tgts_per_mshr = 8
    size = '1MB'
    assoc = 16
    write_buffers = 8
    prefetch_on_access = 'true'
    # Simple stride prefetcher
    prefetcher = StridePrefetcher(degree=8, latency='1.0ns')
    snapshot = False               # print snapshot enable
    snapInstrP = 1000000          # Start instruction point of snapshot printing
    snapshot_path = "/home/lhh/work/snapshot_invalid/gcc/" # snapshot printing path
    snapshot_length = 100000      # snapshot instruction length
    snapshot_interval = 1000000   # interval between two snapshots
    snapshot_times = 10           # times of snapshot that are taken
    snapshot_count = 1            # start number of snapshot
    snapshot_step = 500           # step between two snapshot
    use_lruBased = False          # lruBased function enable
    backup_en = True              # invalidBlks function enable(used to test partial backup performance)
    backup_point = 1000005        # instruction point of backup
    backup_order = 0              # order of lrubased algorithm


