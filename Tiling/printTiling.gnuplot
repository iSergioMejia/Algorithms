set terminal png

set output "Tiling.png"
set xlabel "Size (n)"
set ylabel "Time (s)"
plot "pr.txt" using 1:2 with lines title 'Tiling',