#!/bin/bash
Target=Mibench_out
Root=/home/gyz/code/architecture/simulation/"$Target"
Gem5=/home/gyz/code/architecture/simulation/gem5-stable-f75ee4849c40/build/ARM/gem5.opt
Script=/home/gyz/code/architecture/simulation/gem5-stable-f75ee4849c40/configs/mibench/runmibench.py
Snapshotroot=/home/gyz/code/architecture/simulation/snapshot_aspdac/

declare -a Benches
Benches=(
#dijkstra
#patricia
#basicmath_large
#basicmath_small
bitcount
#qsort_large
#qsort_small
#susan_s
#susan_e
#susan_c
#cjpeg 
#djpeg
#lame
#typeset
#sha
#blowfish_e
#rijndael_e
#crc
#FFT
#FFT_i
#gsm_toast
#gsm_untoast
#stringsearch
)
mkdir $Root
mkdir $Snapshotroot
for Bench in ${Benches[*]}
do
    echo "bench:"$Bench
    Snapshot_root=$Snapshotroot"$Bench"/
    echo "snapshot_root"$Snapshot_root
    mkdir $Snapshot_root
    $Gem5 --outdir="$Root"\
	--stats-file=stats_"$Bench".txt\
    $Script --cpu-type=arm_detailed --caches --l1d_size=32kB \
    --l1i_size=32kB --l1d_assoc=4 --l1i_assoc=4 --l2_size=1MB \
    --l2_assoc=8 --cacheline_size=64 --l2cache --clock=1G \
    --snapshot --snapshot_path=$Snapshot_root -n 1 \
    --benchmark "$Bench" -I 30000000 \
     2>&1 | tee $Root/log_"Bench".txt &
done;

echo "Run Mibench finished"
exit 0
