using System;
using static System.Console;


namespace ShortestWord
{
   class Program
    {
 
        static string[] arr = { "Csharp", "Vincent","Healy","www.whatcodeareyoulike.com" };
    static void Main(string[] args)
        {
            string shortWord = "";
            int Wordcount = 100;
            foreach (string item in arr)
            {
                if (item.Length < Wordcount)
                {
                    Wordcount = item.Length;
                    shortWord = item;
                }
            }
            Clear();
            WriteLine($"The shortest word: {shortWord} \nLetters count : {Wordcount}");
            Environment.Exit(0);
        }
    }
}
