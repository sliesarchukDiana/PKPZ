using System;
using System.Windows;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        public MainWindow() { InitializeComponent(); }

        private void OrganizationTypeComboBox_SelectionChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
        {
            InsuranceFields.Visibility = Visibility.Collapsed;
            FactoryFields.Visibility = Visibility.Collapsed;

            if (OrganizationTypeComboBox.SelectedIndex == 0) InsuranceFields.Visibility = Visibility.Visible;
            else if (OrganizationTypeComboBox.SelectedIndex == 1) FactoryFields.Visibility = Visibility.Visible;
        }

        private void ShowButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string name = NameTextBox.Text;
                string address = AddressTextBox.Text;
                int employees = int.Parse(EmployeesTextBox.Text);
                string result = "";

                if (OrganizationTypeComboBox.SelectedIndex == 0)
                {
                    string type = InsuranceTypeTextBox.Text;
                    int clients = int.Parse(ClientCountTextBox.Text);
                    var company = new InsuranceCompany(name, address, employees, type, clients);
                    result = company.Show();
                }
                else if (OrganizationTypeComboBox.SelectedIndex == 1)
                {
                    string prodType = ProductionTypeTextBox.Text;
                    int volume = int.Parse(ProductionVolumeTextBox.Text);
                    var factory = new Factory(name, address, employees, prodType, volume);
                    result = factory.Show();
                }

                OutputTextBlock.Text = result;
            }
            catch
            {
                MessageBox.Show("Перевірте правильність введених даних.");
            }
        }
    }
}