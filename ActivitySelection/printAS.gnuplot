set terminal png
set output "ActivitySelection.png"
set xlabel "Size (n)"
set ylabel "Avg Time (s)"
plot "dataAS.res" using 1:4 with lines title 'Greedy', \
 "dataAS.res" using 1:5 with lines title 'DP' linetype 2