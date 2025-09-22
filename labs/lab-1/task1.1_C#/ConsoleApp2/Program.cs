class ConsoleApp2
{
    static string CheckPoint(double x, double y)
    {
        double parabola = -(x * x) + 2;
        double diagonal = x;

        bool inside = false;
        bool onBorder = false;

        if (x >= 0) // Right side
        {
            inside = y > 0 && y < parabola && y < diagonal;
            onBorder = y == diagonal || y == parabola;
        }
        else // Left side (x <= 0)
        {
            inside = y < 0 && y > diagonal && y < parabola;
            onBorder = y == diagonal || y == parabola;
        }

        if (inside)
            return "Hit";
        else if (onBorder)
            return "On the border";
        else
            return "Missed";
    }

    static void Main()
    {
            Console.Write("Enter x coordinate: ");
            double x = double.Parse(Console.ReadLine());

            Console.Write("Enter y coordinate: ");
            double y = double.Parse(Console.ReadLine());

            string result = CheckPoint(x, y);
            Console.WriteLine(result);
        }
    }