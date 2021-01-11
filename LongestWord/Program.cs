using System;
using static System.Console;


namespace LongestWord
{
   class Program
    {
 
    static void Main(string[] args)
        {
            string[] arr = { "Csharp", "Vincent","Healy","www.whatcodeareyoulike.com" };
            string longWord = "";
            int Wordcount = 0;
            foreach (string item in arr)
            {
                if (item.Length > Wordcount)
                {
                    Wordcount = item.Length;
                    longWord = item;
                }
            }
            
            WriteLine("The longest word: {0} \nLetters count : {1}", longWord, Wordcount);
            ReadKey();
        }
    }
}
