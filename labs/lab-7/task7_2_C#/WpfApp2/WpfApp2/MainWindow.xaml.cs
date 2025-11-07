using System.Windows;
using System.Windows.Controls;

namespace WpfApp2
{
    public partial class MainWindow
    {
        public struct FIRMA
        {
            public string Name { get; set; }
            public string Gender { get; set; }
            public double Salary { get; set; }
        }

        private List<FIRMA> AGENCIA = new();

        public MainWindow()
        {
            InitializeComponent();
            EmployeesGrid.ItemsSource = AGENCIA;
        }

        private void AddEmployee_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(NameInput.Text) ||
                GenderInput.SelectedItem == null ||
                !double.TryParse(SalaryInput.Text, out double salary))
            {
                MessageBox.Show("Перевір введені дані", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            var gender = ((ComboBoxItem)GenderInput.SelectedItem).Content.ToString();

            AGENCIA.Add(new FIRMA
            {
                Name = NameInput.Text,
                Gender = gender,
                Salary = salary
            });

            EmployeesGrid.Items.Refresh();
            NameInput.Clear();
            SalaryInput.Clear();
        }

        private void Sort_Click(object sender, RoutedEventArgs e)
        {
            AGENCIA = AGENCIA.OrderByDescending(x => x.Salary).ToList();
            EmployeesGrid.ItemsSource = AGENCIA;
            EmployeesGrid.Items.Refresh();
        }

        private void ShowMaxSalary_Click(object sender, RoutedEventArgs e)
        {
            if (AGENCIA.Count == 0)
            {
                ResultText.Text = "Немає даних.";
                return;
            }

            double maxSalary = AGENCIA.Max(x => x.Salary);
            var topEmployees = AGENCIA.Where(x => Math.Abs(x.Salary - maxSalary) < 0.0001).ToList();

            string result = "Працівники з найбільшою зарплатою:\n" +
                            string.Join("\n", topEmployees.Select(e => $"{e.Name} ({e.Gender}) — {e.Salary} грн"));

            ResultText.Text = result;
        }
    }
}
