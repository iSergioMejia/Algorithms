set terminal png
set output "ComparisonHomo.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "data.res" using 1:2 with lines title 'Innocent (Bad Implementation)', \
 "data.res" using 1:3 with lines title 'Innocent' linetype 4, \
 "data.res" using 1:4 with lines title 'Divide\&Conquer' linetype 2