using System.Windows;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        private PlaneCollection planes = new PlaneCollection();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void AddPlane_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string model = ModelTextBox.Text;
                int hours = int.Parse(HoursTextBox.Text);
                int reliability = int.Parse(ReliabilityTextBox.Text);

                planes.Add(new Plane(model, hours, reliability));
                RefreshList();
            }
            catch
            {
                MessageBox.Show("Перевірте правильність введених даних.");
            }
        }

        private void SortPlanes_Click(object sender, RoutedEventArgs e)
        {
            List<Plane> sorted = planes.GetList()
                .OrderBy(p => p, new PlaneComparer())
                .ToList();

            PlanesListBox.ItemsSource = sorted;
        }

        private void RefreshList()
        {
            PlanesListBox.ItemsSource = null;
            PlanesListBox.ItemsSource = planes.GetList();
        }
    }
}