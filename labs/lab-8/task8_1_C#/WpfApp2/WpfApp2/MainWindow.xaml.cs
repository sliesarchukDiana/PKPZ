using System.Windows;

namespace TupleApp
{
    public partial class MainWindow : Window
    {
        private List<(string Name, double Price, string Country, int Quantity)> products = new();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void AddButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string name = ProductNameBox.Text;
                double price = double.Parse(PriceBox.Text);
                string country = CountryBox.Text;
                int quantity = int.Parse(QuantityBox.Text);

                var tuple = (name, price, country, quantity);
                products.Add(tuple);

                ProductsList.Items.Add($"{tuple.name} — {tuple.price} грн, {tuple.country}, {tuple.quantity} шт.");

                ProductNameBox.Clear();
                PriceBox.Clear();
                CountryBox.Clear();
                QuantityBox.Clear();
            }
            catch
            {
                MessageBox.Show("Перевірте правильність введених даних!");
            }
        }

        private void ShowAll_Click(object sender, RoutedEventArgs e)
        {
            if (products.Count == 0)
            {
                MessageBox.Show("Список порожній!");
                return;
            }

            ProductsList.Items.Clear();
            foreach (var p in products)
                ProductsList.Items.Add($"{p.Name} — {p.Price} грн, {p.Country}, {p.Quantity} шт.");
        }

        private void ShowSocial_Click(object sender, RoutedEventArgs e)
        {
            if (products.Count == 0)
            {
                MessageBox.Show("Список порожній!");
                return;
            }

            double avg = products.Average(p => p.Price);
            var social = products.Where(p => p.Price < avg).ToList();

            ProductsList.Items.Clear();
            foreach (var p in social)
                ProductsList.Items.Add($"{p.Name} — {p.Price} грн (соціальний)");

            ResultText.Text = $"Соціальних продуктів: {social.Count}";
        }
    }
}
