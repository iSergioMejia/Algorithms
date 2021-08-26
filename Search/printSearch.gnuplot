set terminal png
set output "ComparisonSearch3.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "dataSearch3.res" using 1:2 with lines title 'Innocent', \
 "dataSearch3.res" using 1:3 with lines title 'Divide\&Conquer' linetype 2