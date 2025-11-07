using System.Collections;
using System.Collections.Generic;

namespace WpfApp1
{
    public class PlaneCollection : IEnumerable<Plane>
    {
        private List<Plane> planes = new List<Plane>();

        public void Add(Plane plane)
        {
            planes.Add(plane);
        }

        public IEnumerator<Plane> GetEnumerator()
        {
            return planes.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        public List<Plane> GetList()
        {
            return planes;
        }
    }
}