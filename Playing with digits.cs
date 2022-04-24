public class DigPow
{
    public static long digPow(int n, int p)
    {
        int n1 = n;
        int i = 0;
        int[] ar = new int[50];
        while (n1 >= 10)
        {
            ar[i] = n1 % 10;
            n1 /= 10;
            i++;
        }
        ar[i] = n1;
        int sum = 0, pow = 1;
        for (int j = i; j >= 0; j--)
        {
            pow = 1;
            if (p != 0)
            {
                for (int l = 1; l <= p; l++)
                {
                    pow *= ar[j];
                }
            }
            sum += pow;
            p++;
        }
        if (sum % n == 0)
            return sum / n;
        else
            return -1;
    }
}