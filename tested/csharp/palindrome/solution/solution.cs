public class Submission
{
    public static bool IsPalindrome(string word)
    {
        string lower = word.ToLower();
        for (int i = 0; i < lower.Length / 2; i++)
        {
            if (lower[i] != lower[lower.Length - 1 - i])
            {
                return false;
            }
        }
        return true;
    }
}
