using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter n rows: ");
        int n = int.Parse(Console.ReadLine());

        int[][] jagged = new int[n][];
        Random rnd = new Random();
        for (int i = 0; i < n; i++)
        {
            Console.Write($"Enter amount of values in the row {i + 1}: ");
            int m = int.Parse(Console.ReadLine());
            jagged[i] = new int[m];

            for (int j = 0; j < m; j++)
                jagged[i][j] = rnd.Next(-5, 6);
        }

        Console.WriteLine("\nPrimary array:");
        PrintJagged(jagged);
        int[] X = { 1, 0, 1 };
        for (int i = 0; i < n; i++)
        {
            if ((i + 1) % 2 == 0)
                jagged[i] = (int[])X.Clone();
        }

        Console.WriteLine("\nArray after replacement:");
        PrintJagged(jagged);
    }

    static void PrintJagged(int[][] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write($"[{i + 1}] ");
            foreach (int el in arr[i])
                Console.Write(el + " ");
            Console.WriteLine();
        }
    }
}