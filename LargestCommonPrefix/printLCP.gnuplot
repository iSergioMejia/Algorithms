set terminal png
set output "LCP.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "dataLCP.res" using 1:2 with lines title 'D\&C', \
 "dataLCP.res" using 1:3 with lines title 'Innocent' linetype 2