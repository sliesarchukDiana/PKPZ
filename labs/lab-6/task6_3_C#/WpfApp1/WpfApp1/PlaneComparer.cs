using System.Collections.Generic;

namespace WpfApp1
{
    public class PlaneComparer : IComparer<Plane>
    {
        // Порівняння за годинами, потім за надійністю
        public int Compare(Plane x, Plane y)
        {
            if (x == null || y == null) return 0;

            int hoursCompare = x.FlightHours.CompareTo(y.FlightHours);
            if (hoursCompare != 0)
                return hoursCompare;

            return x.Reliability.CompareTo(y.Reliability);
        }
    }
}