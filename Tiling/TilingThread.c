//
// Compile with gcc -o exe Tiling.c -lm -pthread
// Made by Sergio A. Mejia

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include <pthread.h>

int N;
int **matrix;

typedef struct Param
{
    int x;
    int y;
    int n;
    int xH;
    int yH;
    int cIn;
    int cEnd;
} Param;

Param initP(int x, int y, int n, int xH, int yH, int cIn, int cEnd)
{
    struct Param p;
    p.x = x;
    p.y = y;
    p.n = n;
    p.xH = xH;
    p.yH = yH;
    p.cIn = cIn;
    p.cEnd = cEnd;
    return p;
}

void paintL(int x1, int y1, int x2, int y2, int x3, int y3, int color)
{
    matrix[x1][y1] = color;
    matrix[x2][y2] = color;
    matrix[x3][y3] = color;
}

void printP(struct Param p)
{
    printf("(%d, %d) n=%d, h(%d, %d), c(%d, %d)\n", p.y, p.y, p.n, p.xH, p.yH, p.cIn, p.cEnd);
}

void printM()
{
    int i;
    for (i = 0; i < N; i++)
    {
        int j;
        for (j = 0; j < N; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void* tiling(struct Param *p)
{
    //printP(*p);
    //printM();
    int i, j;
    int xM, yM;
    if (p->n == 2)
    {
        for (i = p->x; i < p->x + p->n; i++)
        {
            for (j = p->y; j < p->y + p->n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][j] = p->cIn;
                }
            }
        }
    }
    else
    {
        xM = p->x + p->n / 2;
        yM = p->y + p->n / 2;

        // If missing tile is in first quadrant
        if (p->xH < xM && p->yH < yM)
        {
            paintL(xM, yM - 1, xM, yM, xM - 1, yM, p->cIn);
            int c = (p->cEnd - 1 + p->cIn) / 4;
            pthread_t thread_pid_r[4];
            
            Param p1 = initP(p->x, p->y, p->n / 2, p->xH, p->yH, p->cIn + 1, p->cIn + c);
            pthread_create(&thread_pid_r[0], NULL, (void*)tiling, (void*)&p1);        
            
            Param p2 = initP(xM, p->y, p->n / 2, xM, yM - 1, c + p->cIn + 1, p->cIn + 2 * c);
            pthread_create(&thread_pid_r[1], NULL, (void*)tiling, (void*)&p2);    

            Param p3 = initP(p->x, yM, p->n / 2, xM - 1, yM, 2 * c + p->cIn + 1, p->cIn + 3 * c);
            pthread_create(&thread_pid_r[2], NULL, (void*)tiling, (void*)&p3);  

            Param p4 = initP(xM, yM, p->n / 2, xM, yM, 3 * c + p->cIn + 1, p->cIn + 4 * c);
            pthread_create(&thread_pid_r[3], NULL, (void*)tiling, (void*)&p4);    

            for(int r = 0; r < 4; r++)
            {
                pthread_join(thread_pid_r[r], NULL);
            }   
        }
        // If missing Tile is in 2st quadxHant
        else if (p->xH >= xM && p->yH < yM)
        {
            paintL(xM, yM - 1, xM, yM, xM - 1, yM - 1, p->cIn);
            int c = (p->cEnd - 1 + p->cIn) / 4;
            pthread_t thread_pid_r[4];

            Param p1 = initP(p->x, p->y, p->n / 2, xM - 1, yM - 1, p->cIn + 1, p->cIn + c);
            pthread_create(&thread_pid_r[0], NULL, (void*)tiling, (void*)&p1); 
            Param p2 = initP(xM, p->y, p->n / 2, p->xH, p->yH, c + p->cIn + 1, p->cIn + 2 * c);
            pthread_create(&thread_pid_r[1], NULL, (void*)tiling, (void*)&p2); 
            Param p3 = initP(p->x, yM, p->n / 2, xM - 1, yM, 2 * c + p->cIn + 1, p->cIn + 3 * c);
            pthread_create(&thread_pid_r[2], NULL, (void*)tiling, (void*)&p3); 
            Param p4 = initP(xM, yM, p->n / 2, xM, yM, 3 * c + p->cIn + 1, p->cIn + 4 * c);
            pthread_create(&thread_pid_r[3], NULL, (void*)tiling, (void*)&p4); 

            for(int r = 0; r < 4; r++)
            {
                pthread_join(thread_pid_r[r], NULL);
            } 
        }
        // If missing Tile is in 3st quadxHant
        else if (p->xH < xM && p->yH >= yM)
        {
            paintL(xM - 1, yM, xM, yM, xM - 1, yM - 1, p->cIn);
            int c = (p->cEnd - 1 + p->cIn) / 4;
            pthread_t thread_pid_r[4];

            Param p1 = initP(p->x, p->y, p->n / 2, xM - 1, yM - 1, p->cIn + 1, p->cIn + c);
            pthread_create(&thread_pid_r[0], NULL, (void*)tiling, (void*)&p1); 
            
            Param p2 = initP(xM, p->y, p->n / 2, xM, yM - 1, c + p->cIn + 1, p->cIn + 2 * c);
            pthread_create(&thread_pid_r[1], NULL, (void*)tiling, (void*)&p2); 
            
            Param p3 = initP(p->x, yM, p->n / 2, p->xH, p->yH, 2 * c + p->cIn + 1, p->cIn + 3 * c);
            pthread_create(&thread_pid_r[2], NULL, (void*)tiling, (void*)&p3); 
            
            Param p4 = initP(xM, yM, p->n / 2, xM, yM, 3 * c + p->cIn + 1, p->cIn + 4 * c);
            pthread_create(&thread_pid_r[3], NULL, (void*)tiling, (void*)&p4); 
            
            for(int r = 0; r < 4; r++)
            {
                pthread_join(thread_pid_r[r], NULL);
            }
        }
        // If missing Tile is in 4st quadxHant
        else if (p->xH >= xM && p->yH >= yM)
        {
            paintL(xM - 1, yM, xM, yM - 1, xM - 1, yM - 1, p->cIn);
            int c = (p->cEnd - 1 + p->cIn) / 4;
            pthread_t thread_pid_r[4];
            
            Param p1 = initP(p->x, p->y, p->n / 2, xM - 1, yM - 1, p->cIn + 1, p->cIn + c);
            pthread_create(&thread_pid_r[0], NULL, (void*)tiling, (void*)&p1); 
            Param p2 = initP(xM, p->y, p->n / 2, xM, yM - 1, c + p->cIn + 1, p->cIn + 2 * c);
            pthread_create(&thread_pid_r[1], NULL, (void*)tiling, (void*)&p2); 
            Param p3 = initP(p->x, yM, p->n / 2, xM - 1, yM, 2 * c + p->cIn + 1, p->cIn + 3 * c);
            pthread_create(&thread_pid_r[2], NULL, (void*)tiling, (void*)&p3); 
            Param p4 = initP(xM, yM, p->n / 2, p->xH, p->yH, 3 * c + p->cIn + 1, p->cIn + 4 * c);
            pthread_create(&thread_pid_r[3], NULL, (void*)tiling, (void*)&p4); 

            for(int r = 0; r < 4; r++)
            {
                pthread_join(thread_pid_r[r], NULL);
            }
        }
    }
    pthread_exit(NULL);
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

    h = atoi(argv[1]);
    xH = atoi(argv[2]);
    yH = atoi(argv[3]);

    for (j = 1; j <= h; j++)
    {
        n = pow(2, j);
        N = n;
        matrix = (int **)malloc(n * sizeof(int *));
        for (i = 0; i < n; i++)
        {
            matrix[i] = (int *)malloc(n * sizeof(int));
            for(int k = 0; k < n; k++)
            {
                matrix[i][k] = 0;
            }
        }

        matrix[xH][yH] = -1;

        //time_t start, end;
        Param p = initP(0, 0, n, xH, yH, 1, (pow(4, j) - 1) / 3);
        //time(&start);
        struct timeval begin, end;
        gettimeofday(&begin, 0);
        
        pthread_t thread_pid;
        pthread_create(&thread_pid, NULL, (void*)tiling, (void*)&p);        
        pthread_join(thread_pid, NULL);
        
        //tiling(&p);
        gettimeofday(&end, 0);
        long seconds = end.tv_sec - begin.tv_sec;
        long microseconds = end.tv_usec - begin.tv_usec;
        double elapsed = seconds + microseconds * 1e-6;
        //printf("Time measured: %.6f seconds.\n", elapsed);
        printf("%d %.6f \n", n, elapsed);
        //time(&end);

        //double tb = (double)(end - start);

        //printf("Time spent: %.10f\n", tb);
        for (i = 0; i < n; i++)
        {
            free(matrix[i]);
        }
        free(matrix);
    }
}