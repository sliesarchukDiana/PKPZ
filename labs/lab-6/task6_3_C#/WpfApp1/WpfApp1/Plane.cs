using System;

namespace WpfApp1
{
    public class Plane : IComparable<Plane>
    {
        public string Model { get; set; }
        public int FlightHours { get; set; }
        public int Reliability { get; set; }

        public Plane(string model, int flightHours, int reliability)
        {
            Model = model;
            FlightHours = flightHours;
            Reliability = reliability;
        }

        // Порівняння за кількістю годин польоту
        public int CompareTo(Plane other)
        {
            if (other == null) return 1;
            return FlightHours.CompareTo(other.FlightHours);
        }

        public override string ToString()
        {
            return $"{Model} — {FlightHours} год., Надійність: {Reliability}%";
        }
    }
}