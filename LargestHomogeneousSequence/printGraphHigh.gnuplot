set terminal png
set output "ComparisonHomo2.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "dataHomo.res" using 1:3 with lines title 'Innocent' linetype 4, \
 "dataHomo.res" using 1:4 with lines title 'Divide\&Conquer' linetype 2