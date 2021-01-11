using System;
using static System.Console;

namespace ChoiceOfWord
{
    class Program
    {
        static void Main(string[] args)
        {
            while (areYouSure(args))
           { 
               Clear();
                WriteLine("Do you want to find the [S]hortest or [L]ongest word?");
                string ansa = ReadLine().ToLower();
                string[] arr = { "Vincent", "Healy","CSharp","www.get-it-up-there.com" };
                string theWord = "";
                if (ansa == "s")
                {
                    int Wordcount = 100;
                    foreach (string item in arr)
                    {
                        if (item.Length < Wordcount)
                        {
                            Wordcount = item.Length;
                            theWord = item;
                        }
                    }
                    Clear();
                    WriteLine($"The shortest word: {theWord} \nLetters count : {Wordcount}");
                    Environment.Exit(0);
                }

                if (ansa == "l")
                {
                    int Wordcount = 0;
                    foreach (string item in arr)
                    {
                        if (item.Length > Wordcount)
                        {
                            Wordcount = item.Length;
                            theWord = item;
                        }
                    }    
                    Clear();
                    WriteLine("The longest word: {0} \nLetters count : {1}", theWord, Wordcount);
                    Environment.Exit(0);
                }
                else 
                {
                    WriteLine();
                }
            }
        }
        static bool areYouSure(string[]args)
        {
            WriteLine("Do you was to the string? Y/n");
            string quitter = ReadLine().ToLower();
            if(quitter == "n")
            { 
                    return false;
                }
            else
                {
                    return true;
                }
        }
    }
}
