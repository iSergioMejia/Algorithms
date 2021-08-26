set terminal png
set output "Comparison.png"
set xlabel "Minesweeper difficulties"
set ylabel "Victory Percent (%)"
set title "Tests for heuristic victory percent in standart minesweeper difficulties"
set xrange [0:4]
set format x "" 
plot "8x8" using 1:2 title '8x8', \
 "16x16" using 1:2 title '16x16' linetype 4, \
 "30x16" using 1:2 title '30x16' linetype 2
