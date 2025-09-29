class ConsoleApp1
{
    static void Main()
    {
        int n = 6;
        int[,] A = new int[n, n];
        int[] X = new int[n];

        Console.Write("Enter value of x: ");
        int x = int.Parse(Console.ReadLine());
        FillMatrix(A, -50, 49);

        Console.WriteLine("Matrix A");
        PrintMatrix(A);
        
        BuildVector(A, X, x);

        Console.WriteLine("Logical vector X:");
        PrintVector(X);
    }
    
    static void FillMatrix(int[,] matrix, int min, int max)
    {
        Random rnd = new Random();
        int n = matrix.GetLength(0);

        for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            matrix[i, j] = rnd.Next(min, max + 1);
    }
    
    static void PrintMatrix(int[,] matrix)
    {
        int n = matrix.GetLength(0);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                Console.Write($"{matrix[i, j],4}");
            Console.WriteLine();
        }
    }
    
    static void BuildVector(int[,] matrix, int[] vector, int x)
    {
        int n = matrix.GetLength(0);

        for (int i = 0; i < n; i++)
        {
            int maxInRow = int.MinValue;
            for (int j = 0; j < n; j++)
                if (matrix[i, j] > maxInRow)
                    maxInRow = matrix[i, j];

            vector[i] = (maxInRow <= x) ? 1 : 0;
        }
    }
    
    static void PrintVector(int[] vector)
    {
        for (int i = 0; i < vector.Length; i++)
            Console.Write(vector[i] + " ");
        Console.WriteLine();
    }
}