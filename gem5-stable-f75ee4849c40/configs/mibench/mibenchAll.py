import m5
from m5.objects import *
m5.util.addToPath('../common')

binary_dir = '/home/gyz/code/architecture/mibench/'
data_dir = '/home/gyz/code/architecture/mibench/data/'
output_dir = '/home/gyz/code/architecture/mibench/output/'

#basicmath_large
basicmath_large = LiveProcess()
basicmath_large.executable = binary_dir + 'automotive/basicmath/basicmath_large'
data = ''
basicmath_large.cmd = [basicmath_large.executable] + [data]
basicmath_large.output = output_dir + 'basic_large.out'


#basicmath small
basicmath_small = LiveProcess()
basicmath_small.executable = binary_dir + 'automotive/basicmath/basicmath_small'
data = ''
basicmath_small.cmd = [basicmath_small.executable] + [data]
basicmath_small.output = output_dir + 'basic_small.out'

#bitcount
bitcount = LiveProcess()
bitcount.executable = binary_dir + 'automotive/bitcount/bitcnts' # bitcount parameter is fixed in the code
#data = '1125000'
bitcount.cmd = [bitcount.executable] #+ [data]
bitcount.output = output_dir + 'bitcount.out'

#qsort_large
qsort_large = LiveProcess()
qsort_large.executable = binary_dir + 'automotive/qsort/qsort_large'
data = data_dir + 'automotive/qsort/input_large.dat'
qsort_large.cmd = [qsort_large.executable] + [data]
qsort_large.output = output_dir + 'qsort_large.out'

#qsort_small
qsort_small = LiveProcess()
qsort_small.executable = binary_dir + 'automotive/qsort/qsort_small'
data = data_dir + 'automotive/qsort/input_small.dat'
qsort_small.cmd = [qsort_small.executable] + [data]
qsort_small.output = output_dir + 'qsort_small.out'

#susan_s
susan_s = LiveProcess()
susan_s.executable = binary_dir + 'automotive/susan/susan'
data = data_dir + 'automotive/susan/input_large.pgm'
susan_s.cmd = [susan_s.executable] + [data] + ['-s']
susan_s.output = output_dir + 'susan_s.out'

#susan_e
susan_e = LiveProcess()
susan_e.executable = binary_dir + 'automotive/susan/susan'
data = data_dir + 'automotive/susan/input_large.pgm'
susan_e.cmd = [susan_s.executable] + [data] + ['-e']
susan_e.output = output_dir + 'susan_e.out'

#susan_c
susan_c = LiveProcess()
susan_c.executable = binary_dir + 'automotive/susan/susan'
data = data_dir + 'automotive/susan/input_large.pgm'
susan_c.cmd = [susan_c.executable] + [data] + ['-c']
susan_c.output = output_dir + 'susan_c.out'
#cjpeg
cjpeg  = LiveProcess()
cjpeg.executable =  binary_dir+'consumer/jpeg/jpeg-6a/cjpeg'
data=data_dir+'consumer/jpeg/input_large.ppm'
cjpeg_op = '-dct int -progressive -opt -outfile output_large_encode.jpeg'
#cjpeg.cmd = [cjpeg.executable] + [cjpeg_op]  + [data]
cjpeg.cmd = [cjpeg.executable] + ['-dct'] + ['int'] + ['-progressive'] + ['-opt'] + ['-outfile'] + ['output_large_encode.jpeg'] + [data]

#djpeg
djpeg  = LiveProcess()
djpeg.executable =  binary_dir+'consumer/jpeg/jpeg-6a/djpeg'
data=data_dir+'consumer/jpeg/input_large.jpg'
djpeg_op = '-dct int -ppm -outfile output_large_decode.ppm'
djpeg.cmd = [djpeg.executable] + ['-dct'] + ['int'] + ['-ppm'] + ['-outfile'] + ['output_large_decode.ppm'] + [data]


#lame
lame  = LiveProcess()
lame.executable =  binary_dir+'consumer/lame/lame3.70/lame'
data=data_dir+'consumer/lame/large.wav'
lame_out = 'output_large.mp3'
lame.cmd = [lame.executable] + [data] + [lame_out]

#dijkstra
dijkstra = LiveProcess()
dijkstra.executable =  binary_dir+'network/dijkstra/dijkstra_small'
data=data_dir+'network/dijkstra/input.dat'
dijkstra.cmd = [dijkstra.executable] + [data] 

#patricia
patricia  = LiveProcess()
patricia.executable =  binary_dir+'network/patricia/patricia'
data=data_dir+'network/patricia/large.udp'
patricia.cmd = [patricia.executable] + [data] 

#typeset
typeset = LiveProcess()
typeset.executable = binary_dir + 'consumer/typeset/lout-3.24/lout'
typeset_param = '-I lout-3.24/include -D lout-3.24/data -F lout-3.24/font -C lout-3.24/maps -H lout-3.24/hyph large.out'
typeset_base = '/home/gyz/code/architecture/mibench/consumer/typeset/'
typeset_include_dir = typeset_base + 'lout-3.24/include'
typeset_data_dir = typeset_base + 'lout-3.24/data'
typeset_font_dir = typeset_base + 'lout-3.24/font'
typeset_map_dir = typeset_base + 'lout-3.24/map'
typeset_hyph_dir = typeset_base + 'lout-3.24/hyph'
typeset_largelout=typeset_base + 'large.lout'

typeset.cmd = [typeset.executable]  + ['-I'] + [typeset_include_dir] + ['-D'] + [typeset_data_dir] + ['-F'] + [typeset_font_dir] + ['-C'] + [typeset_map_dir] + ['-H'] + [typeset_hyph_dir] + [typeset_largelout]

#sha
sha  = LiveProcess()
sha.executable =  binary_dir+'security/sha/sha'
data=data_dir+'security/sha/input_large.asc'
sha.cmd = [sha.executable] + [data]

#blowfish_e
blowfish_e = LiveProcess()
blowfish_e.executable =  binary_dir+'security/blowfish/bf'
data=data_dir+'security/blowfish/input_large.asc'
blowfish_e.cmd = [blowfish_e.executable] + ['e'] + [data] + ['output_large.enc'] + ['1234567890abcdeffedcba0987654321']

#====================
#rijndael_e
rijndael_e = LiveProcess()
rijndael_e.executable = binary_dir + 'security/rijndael/rijndael'
data = data_dir + 'security/rijndael/input_large.asc'
rijndael_e.cmd = [rijndael_e.executable] + [data] + ['output_large_rij.enc'] + ['e'] + ['1234567890abcdeffedcba09876543211234567890abcdeffedcba0987654321']

#====================

#crc
crc = LiveProcess()
crc.executable = binary_dir + 'telecomm/CRC32/crc'
data = data_dir + 'telecomm/crc/large.pcm'
crc.cmd = [crc.executable] + [data]

#FFT
FFT = LiveProcess()
FFT.executable = binary_dir + 'telecomm/FFT/fft'
FFT.cmd = [FFT.executable] + ['8'] + ['32768']
FFT.output  = output_dir+ 'FFT.out'

#FFT_i
FFT_i = LiveProcess()
FFT_i.executable = binary_dir + 'telecomm/FFT/fft'
FFT_i.cmd = [FFT_i.executable] + ['8'] + ['32768'] + ['-i']
FFT_i.output  = output_dir+ 'FFT_i.out'
#====================
#gsm_toast
gsm_toast = LiveProcess()
gsm_toast.executable =  binary_dir+'telecomm/gsm/bin/toast'
data = data_dir + 'telecomm/gsm/large.au'
gsm_toast.cmd = [gsm_toast.executable] + ['-fps'] + ['-c'] + [data]
gsm_toast.output = output_dir + 'gsm_toast.out'

#gsm_untoast
gsm_untoast = LiveProcess()
gsm_untoast.executable =  binary_dir+'telecomm/gsm/bin/untoast'
data = data_dir + 'telecomm/gsm/large.au.run.gsm'
gsm_untoast.cmd = [gsm_untoast.executable] + ['-fps'] + ['-c'] + [data]
gsm_untoast.output = output_dir + 'gsm_untoast.out'

#stringsearch
stringsearch = LiveProcess()
stringsearch.executable =  binary_dir+'office/stringsearch/search_large'
stringsearch.cmd = [stringsearch.executable]
stringsearch.output = output_dir + 'stringsearch.out'
