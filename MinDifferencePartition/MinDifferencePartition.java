
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Minimum Difference Partition Algorithm
 *  Dynamic Programming
 *  @author Sergio A. Mejía - 2020
 * Java class for the solution of the problem 
 * "Divide a set into two subsets such that the difference
 * of the subsets element sums is the minimum"
 * 
 * Recursive, Memoized and BottomUp (with Backtracking) variants
 */
public class MinDifferencePartition
{
    /*
    Interface function for the Bottom Up variant
    */
    public Result minDifferencePartition(int[] A)
    {
        Result r = this.minDifferencePartition_BottomUp(A);
        return r;
    }
    /*
    Recursive Variant
     Recursively add the current element to one set or the other and return the
     minimum of the result of the two possibilities.
    */ 
    public int minDifferencePartition_Aux(int[] A, int i, int C_1, int C_2)
    {
        if(i == 0)
        {
            return Math.abs(C_1 - C_2);
        }
        else
        {
            int n1 = minDifferencePartition_Aux(A, i - 1, C_1 + A[i - 1] , C_2);
            int n2 = minDifferencePartition_Aux(A, i-1, C_1, C_2 + A[i - 1]);
            return( (n1 < n2) ? n1 : n2 );
        }
    }   

    /*
    Memoized Variant
    Same as recursive, but the partial solutions are stored in M, so if this
    solution has been already calculated, the value of M is returned, instead of
    calculating it again.
    */
    public int minDifferencePartition_Memo(int[] A, int i, int C_1, int C_2, int[][] M)
    {
        int key = Math.abs(C_1 - C_2);
        if(M[i][key] == (int)Float.POSITIVE_INFINITY)
        {
            if(i == 0)
            {
                M[i][key] = key;
            }  
            else
            {
                int n1 = minDifferencePartition_Memo(A, i - 1, C_1 + A[i - 1] , C_2, M);
                int n2 = minDifferencePartition_Memo(A, i-1, C_1, C_2 + A[i - 1], M);
                M[i][key] = ( (n1 < n2) ? n1 : n2 );
            }
        }
        return (M[i][key]);
    }
    
    /*
    Bottom Up (with Backtracking) Variant
    Calculate all of the partial solutions of the problem, filling up the
    memoized matrix. The matrix is the double of the needed size because
    it needs to account for the negative and positive differences. For the backtracking
    a T matrix will be made saving to what set is the current element added
    in order to get that specific partial solution. Then it will backtrack following
    these instructions.
    */
    public Result minDifferencePartition_BottomUp(int[] A)
    {
        int n = A.length;
        int suma = 0;
        for (Integer val : A)
        {
            suma += Math.abs(val);
        }
        
        int[][] M = new int[n+1][2*suma+1];
        boolean[][] T = new boolean[n+1][2*suma+1];
        
        for (int i = 0; i <= n; i++)
        {
            for (int j = 0; j <= 2*suma; j++)
            {
                T[i][j] = false;               
            }            
        }
        
        for (int j = 0; j <= 2*suma; j++)
        {
            M[0][j] = Math.abs(j - suma);
        }
        
        for(int i = 1; i <= n; i++)
        {
            for(int j = 2*suma; j >= 0; j--)
            {
                int n1 = (int)Float.POSITIVE_INFINITY;
                int n2 = (int)Float.POSITIVE_INFINITY;
                int right = j + A[i - 1];
                int left = j - A[i - 1];
                
                if( left >= 0 && left <= 2*suma )
                {
                    n1 = M[i-1][left];
                }
                if( right >= 0 && right <= 2*suma )
                {
                    n2 = M[i-1][right];
                }
                if( n1 < n2 )
                {
                    M[i][j] = n1;
                    T[i][j] = false;
                }
                else
                {
                    M[i][j] = n2;
                    T[i][j] = true;
                }
            }
        }
        
        ArrayList<Integer> C_1 = new ArrayList<>();
        ArrayList<Integer> C_2 = new ArrayList<>();
        
        int j = suma;
        for(int i = n; i >= 1; i--)
        {
            if(T[i][j])
            {
                C_1.add(A[i - 1]);
                j = Math.abs( j + A[i - 1]);
            }
            else
            {
                C_2.add(A[i - 1]);
                j = Math.abs( j - A[i - 1]);
            }
        }

        Result r = new Result(C_1, C_2, M[n][suma]);
        return r;
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        MinDifferencePartition min = new MinDifferencePartition();
        ArrayList<int[]> params = new ArrayList<>();
        int[] A0 = {};
        int[] A1 = {2};
        int[] A2 = {2,15};
        int[] A3 = {1,7,2,13};
        int[] A4 = {1,15,-2,3};
        int[] A5 = {10,6,5,15,30};
        int[] A6 = {1,3,6,-5};
        
        params.add(A0);
        params.add(A1);
        params.add(A2);
        params.add(A3);
        params.add(A4);
        params.add(A5);
        params.add(A6);

        for(int[] A : params)
        {
            System.out.println("Test Case: "+Arrays.toString(A));
            // int res = min.minDifferencePartition_Aux(A, A.length, 0, 0);
            // System.out.println(res);
        
            // int suma = 0;
            // for (Integer val : A)
            // {
            //     suma += Math.abs(val);
            // }

            // int[][] M = new int[A.length+1][suma+1];
            // for(int i = 0; i <= A.length; i++ )
            // {
            //     for(int j = 0; j <= suma; j++)
            //     {
            //         M[i][j] = (int)Float.POSITIVE_INFINITY;
            //     }
            // }
            // int res2 = min.minDifferencePartition_Memo(A, A.length, 0, 0, M);
            // System.out.println(res2);
            Result r = min.minDifferencePartition(A);
            System.out.println(r);    
        }
    }

    public class Result
    {
        ArrayList<Integer> C_1;
        ArrayList<Integer> C_2;
        int minDifference;

        public Result(ArrayList<Integer> C_1, ArrayList<Integer> C_2, int minDifference)
        {
            this.C_1 = C_1;
            this.C_2 = C_2;
            this.minDifference = minDifference;
        }

        public ArrayList<Integer> getC_1()
        {
            return C_1;
        }

        public ArrayList<Integer> getC_2()
        {
            return C_2;
        }

        public int getMinDifference()
        {
            return minDifference;
        }

        @Override
        public String toString()
        {
            String s = "Min Difference: " + minDifference + ". C_1 = " + C_1 + ", C_2 = " + C_2;
            return s;//To change body of generated methods, choose Tools | Templates.
        }
        
    }  
}
