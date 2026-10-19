using System;

public class Submission
{
    public static int ParsePositive(string text)
    {
        if (int.TryParse(text, out int number) && number > 0)
        {
            return number;
        }
        throw new ArgumentException("not a positive number");
    }
}
