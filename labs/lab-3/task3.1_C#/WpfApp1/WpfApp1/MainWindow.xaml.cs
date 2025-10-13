using System.Windows;

namespace WpfApp1
{
    public partial class MainWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void CountConsonants(object sender, RoutedEventArgs e)
        {
            string input = InputBox.Text.ToLower();

            char[] consonants = { 'б','в','г','ґ','д','ж','з','й','к','л','м','н',
                'п','р','с','т','ф','х','ц','ч','ш','щ' };

            int count = input.Count(c => consonants.Contains(c));

            ResultText.Text = $"Кількість приголосних: {count}";
        }
    }
}