public class Kata
{
    public static int[] SortNumbers(int[] nums)
    {
        if (nums == null)

        {
            nums = new int[0];
        }

        else
        {
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[i] > nums[j])
                    {
                        int r = nums[i];
                        nums[i] = nums[j];
                        nums[j] = r;
                    }
                }
            }
        }
        return nums;
    }
}