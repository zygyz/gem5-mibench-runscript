import os, optparse, sys

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath

addToPath('../common')
addToPath('../ruby')
addToPath('../topologies')

import Options
import Ruby
import Simulation
from Caches import *
import CacheConfig
import mibenchAll

config_path = os.path.dirname(os.path.abspath(__file__))
config_root = os.path.dirname(config_path)
m5_root = os.path.dirname(config_root)

parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)

parser.add_option("-b",type="string",default="",help="The benchmark to be loaded.")

parser.add_option("--chkpt",default="",help="The checkpoint to load.")

execfile(os.path.join(config_root,"common","Options.py"))


if '--ruby' in sys.argv:
    Ruby.define_options(parser)

(options,args) = parser.parse_args()

print 'options:', options
print 'args', args

if args:
    sys.exit(1)

if options.benchmark == 'basicmath_large':
    process = mibenchAll.basicmath_large
elif options.benchmark == 'basicmath_small':
    process = mibenchAll.basicmath_small
elif options.benchmark == 'bitcount':
    process = mibenchAll.bitcount
elif options.benchmark == 'qsort_large':
    process = mibenchAll.qsort_large
elif options.benchmark == 'qsort_small':
    process = mibenchAll.qsort_small
elif options.benchmark == 'susan_s':
    process = mibenchAll.susan_s
elif options.benchmark == 'susan_e':
    process = mibenchAll.susan_e
elif options.benchmark == 'susan_c':
    process = mibenchAll.susan_c
elif options.benchmark == 'cjpeg':
    process = mibenchAll.cjpeg
elif options.benchmark == 'dijkstra':
    process = mibenchAll.dijkstra
elif options.benchmark == 'patricia':
    process = mibenchAll.patricia
elif options.benchmark == 'djpeg':
    process = mibenchAll.djpeg
elif options.benchmark == 'lame':
    process = mibenchAll.lame
elif options.benchmark == 'typeset':
    process = mibenchAll.typeset
elif options.benchmark == 'sha':
    process = mibenchAll.sha
elif options.benchmark == 'blowfish_e':
    process = mibenchAll.blowfish_e
elif options.benchmark == 'rijndael_e':
    process = mibenchAll.rijndael_e
elif options.benchmark == 'crc':
    process = mibenchAll.crc
elif options.benchmark == 'FFT':
    process = mibenchAll.FFT
elif options.benchmark == 'FFT_i':
    process = mibenchAll.FFT_i
elif options.benchmark == 'gsm_toast':
    process = mibenchAll.gsm_toast
elif options.benchmark == 'gsm_untoast':
    process = mibenchAll.gsm_untoast
elif options.benchmark == 'stringsearch':
    process = mibenchAll.stringsearch

if options.chkpt != "":
    process.chkpt = options.chkpt

(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.clock = '2.0GHz'
np = 1
system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
		physmem = SimpleMemory(range=AddrRange("2048MB")),
		membus = CoherentBus(), mem_mode = 'timing')

if options.ruby:
    if not (options.cpu_type == "detailed" or options.cpu_type == "timing"):
        print >> sys.stderr, "Ruby requires TimingSimpleCPU or O3CPU!!"
        sys.exit(1)

    options.use_map = True
    Ruby.create_system(options, system)
    assert(options.num_cpus == len(system.ruby._cpu_ruby_ports))

    for i in xrange(np):
        ruby_port = system.ruby._cpu_ruby_ports[i]

        # Create the interrupt controller and connect its ports to Ruby
        # Note that the interrupt controller is always present but only
        # in x86 does it have message ports that need to be connected
        system.cpu[i].createInterruptController()

        # Connect the cpu's cache ports to Ruby
        system.cpu[i].icache_port = ruby_port.slave
        system.cpu[i].dcache_port = ruby_port.slave
        if buildEnv['TARGET_ISA'] == 'x86':
            system.cpu[i].interrupts.pio = ruby_port.master
            system.cpu[i].interrupts.int_master = ruby_port.slave
            system.cpu[i].interrupts.int_slave = ruby_port.master
            system.cpu[i].itb.walker.port = ruby_port.slave
            system.cpu[i].dtb.walker.port = ruby_port.slave
else:
    system.physmem.port = system.membus.master
    system.system_port = system.membus.slave
    CacheConfig.config_cache(options,system)

for i in xrange(np):   
#    if options.caches:
#        system.cpu[i].addPrivateSplitL1Caches(L1Cache(size = '64kB'),
#                                              L1Cache(size = '64kB'))
#    if options.l2cache:
#        system.l2 = L2Cache(size='2MB')
#        system.tol2bus = Bus()
#        system.l2.cpu_side = system.tol2bus.port	
#        system.l2.mem_side = system.membus.port
#        system.cpu[i].connectMemPorts(system.tol2bus)
#    else:
#        system.cpu[i].connectMemPorts(system.membus)
    system.cpu[i].workload = process[i]
root = Root(full_system = False,system = system)
Simulation.run(options, root, system, FutureClass)

