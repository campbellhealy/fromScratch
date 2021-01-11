using System;
using static System.Console;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            while (RunnerApp(args))
            {
                int num1 = 0; 
                int num2 = 0;

                // Display title.
                Clear();
                WriteLine("Simple Calculator in C#\r");
                WriteLine("------------------------\n");

                // Request the first number.
                WriteLine("Type 1st number; press Enter");
                num1 = Convert.ToInt32(ReadLine());

                // Request the second number.
                WriteLine("Type 2nd number; press Enter");
                num2 = Convert.ToInt32(ReadLine());

                // Request operator.
                string choiceOp = "z";
                WriteLine("Choose an option from the following list:");
                WriteLine("\ta - Add");
                WriteLine("\ts - Subtract");
                WriteLine("\tm - Multiply");
                WriteLine("\td - Divide (Integers)");
                Write("Your option? ");
                choiceOp = ReadLine().ToLower();
                WriteLine(choiceOp);  // This is a test line

                if (choiceOp =="a")
                {
                    Clear();
                    WriteLine($"Your result: {num1} + {num2} = " + (num1 + num2));
                }
                if  (choiceOp =="s")
                {
                    Clear();
                    WriteLine($"Your result: {num1} - {num2} = " + (num1 - num2));
                }
                if  (choiceOp =="m")
                {
                    Clear();
                    WriteLine($"Your result: {num1} * {num2} = " + (num1 * num2));
                }
                if  (choiceOp =="d")
                {
                    Clear();
                    WriteLine($"Your result (Integers): {num1} / {num2} = " + (num1 / num2));
                }
                  
            }  
        }
       static bool RunnerApp(string[]args)
        {
            WriteLine("Do you was to do a calculation? Y/n");
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