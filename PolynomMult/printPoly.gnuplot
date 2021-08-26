set terminal png

set output "PolyCompare.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "dataPoly.res" using 1:3 with lines title 'D\&C', \
 "dataPoly.res" using 1:2 with lines title 'Innocent' linetype 2