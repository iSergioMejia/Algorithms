#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

int color = 1;

void paintL(int **matrix, int x1, int y1, int x2, int y2, int x3, int y3)
{
    matrix[x1][y1] = color;
    matrix[x2][y2] = color;
    matrix[x3][y3] = color;
    color++;
}

void tiling(int **matrix, int x, int y, int n, int xH, int yH)
{
    int i, j;
    int xM, yM;
    if (n == 2)
    {
        for (i = x; i < x + n; i++)
        {
            for (j = y; j < y + n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][j] = color;
                }
            }
        }
        color++;
        return;
    }
    else
    {
        xM = x + n / 2;
        yM = y + n / 2;

        // If missing tile is in first quadrant
        if (xH < xM && yH < yM)
        {
            paintL(matrix, xM, yM - 1, xM, yM, xM - 1, yM);
            tiling(matrix, x, y, n / 2, xH, yH);
            tiling(matrix, xM, y, n / 2, xM, yM - 1);
            tiling(matrix, x, yM, n / 2, xM - 1, yM);
            tiling(matrix, xM, yM, n / 2, xM, yM);
        }
        // If missing Tile is in 2st quadxHant
        else if (xH >= xM && yH < yM)
        {
            paintL(matrix, xM, yM - 1, xM, yM, xM - 1, yM - 1);
            tiling(matrix, x, y, n / 2, xM - 1, yM - 1);
            tiling(matrix, xM, y, n / 2, xH, yH);
            tiling(matrix, x, yM, n / 2, xM - 1, yM);
            tiling(matrix, xM, yM, n / 2, xM, yM);
        }
        // If missing Tile is in 3st quadxHant
        else if (xH < xM && yH >= yM)
        {
            paintL(matrix, xM - 1, yM, xM, yM, xM - 1, yM - 1);
            tiling(matrix, x, y, n / 2, xM - 1, yM - 1);
            tiling(matrix, xM, y, n / 2, xM, yM - 1);
            tiling(matrix, x, yM, n / 2, xH, yH);
            tiling(matrix, xM, yM, n / 2, xM, yM);
        }
        // If missing Tile is in 4st quadxHant
        else if (xH >= xM && yH >= yM)
        {
            paintL(matrix, xM - 1, yM, xM, yM - 1, xM - 1, yM - 1);
            tiling(matrix, x, y, n / 2, xM - 1, yM - 1);
            tiling(matrix, xM, y, n / 2, xM, yM - 1);
            tiling(matrix, x, yM, n / 2, xM - 1, yM);
            tiling(matrix, xM, yM, n / 2, xH, yH);
        }
    }
}

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        printf("Usage %s n x y\n", argv[0]);
        exit(0);
    }
    int xH, yH, n, h;
    int i, j;
    int **matrix;

    h = atoi(argv[1]);
    xH = atoi(argv[2]);
    yH = atoi(argv[3]);

    for (j = 1; j <= h; j++)
    {
        n = pow(2,j);
        matrix = (int **)malloc(n * sizeof(int *));
        for (i = 0; i < n; i++)
        {
            matrix[i] = (int *)malloc(n * sizeof(int));
        }

        matrix[xH][yH] = -1;

        //time_t start, end;

        //time(&start);
        struct timeval begin, end;
        gettimeofday(&begin, 0);
        tiling(matrix, 0, 0, n, xH, yH);
        gettimeofday(&end, 0);
        long seconds = end.tv_sec - begin.tv_sec;
        long microseconds = end.tv_usec - begin.tv_usec;
        double elapsed = seconds + microseconds * 1e-6;
        //printf("Time measured: %.6f seconds.\n", elapsed);
        printf("%d %.6f \n", n, elapsed);
        //time(&end);

        //double tb = (double)(end - start);

        /*for (i = 0; i < n; i++)
    {
        int j;
        for (j = 0; j < n; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }*/
        //printf("Time spent: %.10f\n", tb);
        for (i = 0; i < n; i++)
        {
            free(matrix[i]);
        }
        free(matrix);
    }
}