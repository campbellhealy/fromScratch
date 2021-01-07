using System;
using static System.Console;

namespace GuessNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            int countGuess = 1;             // Counter to limit the number of turns
            int guess = 0;                  // Initiate variable
            string welcome = "Guess a number between 1 and 100: ";
            int num = rand.Next(1, 100);    //Set the number to be guessed
            Clear();                        //Clears the console
            Write(welcome);


            while (guess != num)
            {
                try
                {
                    guess = Convert.ToInt32(ReadLine());
                    if (guess > 100 || guess < 0)  //This ensures the guess is in the correct range
                    {
                        Write("Guess must be between 1 and 100: ");
                        countGuess --; // This resets the counter by -1
                    }
                    if (guess > num && guess < 101)
                    {
                        if (countGuess>4)     // Check if 5 guesses have been used and last guess wrong 
                        {
                            WriteLine();
                            WriteLine("You Lose all 5 turns have been used.");
                            WriteLine($"The number you wanted was {num}");
                            WriteLine();
                            Environment.Exit(0);
                        }
                        WriteLine($" That was turn number {countGuess} of 5");
                        Write($"Too High, Guess a value lower than {guess}: ");
                    }
                    else if (guess < num && guess > 0)
                    {
                        if (countGuess>4)   // Check if 5 guesses have been used and last guess wrong
                        {
                            Clear();
                            WriteLine();
                            WriteLine("You Lose all 5 turns have been used.");
                            WriteLine($"The number you wanted was {num}");
                            WriteLine();
                            Environment.Exit(0);
                        }
                        WriteLine($" That was turn number {countGuess} of 5");
                        Write($"Too Low, Guess a value higher than {guess}: ");
                    }
                }
                catch
                {
                    Write("Guess must be a number between 1 and 100: "); 
                    countGuess--;
                }
                countGuess++;
            }
            countGuess--;
            WriteLine("Congrats, it took you " + countGuess + " tries");
            Environment.Exit(0);
        }
    }
}