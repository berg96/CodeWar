using System;

public class Kata
{
    public static int CountBits(int n)
    {
        int cb = 0;
        if (n > 0)
            cb++;
        while (n > 1)
        {
            if (n % 2 == 1)
            {
                cb++;
            }
            n /= 2;
        }
        return cb;
    }
}