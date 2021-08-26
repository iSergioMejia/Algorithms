/*
Largest Common Prefix (LCP) Algorithm
Divide & Conquer
 Sergio A. Mejía - 2020
C code for the solution of the problem 
"Select the biggest prefix that is common amongst a set of words"

Innocent and D&C variants
*/

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <time.h>

/* For documentation check the Python version xd*/
void InnocentLCP(char** words, int size, int* sizes, char* prefixMax)
{
    if(size == 0)
        return;
    strcpy(prefixMax,words[0]);
    char* otherString = (char*)malloc(100*sizeof(char));
   
    int sizeMax = sizes[0];
    int i = 0;
    int j = 0;
    int ns = 0;
    char* s;
    while(ns < size)
    {
        s = words[ns];
        i = 0;
        j = 0;
        while(i < sizeMax && j < sizes[ns] && prefixMax[i] == s[j])
        {
            i += 1; j += 1;
        } 
        strncpy(otherString, prefixMax, i);
        otherString[i] = (char)0;
        sizeMax = i;
        strcpy(prefixMax,otherString);
        ns++;      
    }
    return;
}

int main(int argc, char** argv)
{
    int i;
    for(i = 0; i < 10000; i+=10)
    {
        int j;
        int* sizes = (int*)malloc(i*sizeof(int));
        char** words = (char**)malloc(i*sizeof(char*));
        for(j = 0; j < i; j++)
        {
            words[j] = (char*)malloc(10*sizeof(char));
            sizes[j] = 6;
            strcpy(words[j],"alpaca");
        }
        char* ret = (char*)malloc(100*sizeof(char));
        clock_t begin = clock();

        InnocentLCP(words,i,sizes,ret);
        /* here, do your time-consuming job */

        clock_t end = clock();
        double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
        printf("%d %f",i,time_spent);
    }
    
}