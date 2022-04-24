using System;

public static class Kata
{
    public static int DescendingOrder(int num)
    {
        // Bust a move right here
        int i = 0;
        int[] ar = new int[50];
        while (num >= 10)
        {
            ar[i] = num % 10;
            num /= 10;
            i++;
        }
        ar[i] = num;
        int t = 0;
        for (int a = 0; a < i; a++)
        {
            for (int b = 0; b < i - a; b++)
            {
                if (ar[b + 1] > ar[b])
                {
                    t = ar[b + 1];
                    ar[b + 1] = ar[b];
                    ar[b] = t;
                }
            }
        }
        num = ar[0];
        for (int j = 1; j <= i; j++)
        {
            num *= 10;
            num += ar[j];
        }
        return num;
    }
}