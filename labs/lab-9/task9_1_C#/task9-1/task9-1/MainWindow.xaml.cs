using Microsoft.Win32;
using System.IO;
using System.Windows;

namespace WpfApp
{
    public partial class MainWindow
    {
        private string L1 = "";
        private List<char> L2 = new List<char>();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnSaveL1_Click(object sender, RoutedEventArgs e)
        {
            string input = TxtL1.Text.ToLower();

            // чистимо: лишаємо тільки a-z
            input = new string(input.Where(c => c >= 'a' && c <= 'z').ToArray());

            if (string.IsNullOrEmpty(input))
            {
                MessageBox.Show("Введіть малі латинські літери.");
                return;
            }

            var dialog = new SaveFileDialog();
            dialog.Filter = "Text files (*.txt)|*.txt";

            if (dialog.ShowDialog() == true)
            {
                File.WriteAllText(dialog.FileName, input);
                MessageBox.Show("L1 збережено.");
            }

            L1 = input;
        }

        private void BtnLoad_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new OpenFileDialog();
            if (dialog.ShowDialog() == true)
            {
                L1 = File.ReadAllText(dialog.FileName)
                        .ToLower()
                        .Where(c => c >= 'a' && c <= 'z')
                        .Aggregate("", (a, b) => a + b);

                TxtL1.Text = L1;
            }
        }

        private void BtnProcess_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(L1))
            {
                MessageBox.Show("Спочатку збережіть або завантажте L1.");
                return;
            }

            var counts = L1.GroupBy(c => c)
                           .ToDictionary(g => g.Key, g => g.Count());

            L2.Clear();
            ListL2.Items.Clear();

            for (char c = 'a'; c <= 'z'; c++)
            {
                L2.Add(c);
                int count = counts.ContainsKey(c) ? counts[c] : 0;

                string status =
                    count == 1 ? "1 time" :
                    count > 1 ? "many times" :
                    "absent";

                ListL2.Items.Add($"{c}: {status}");
            }
        }

        private void BtnSave_Click(object sender, RoutedEventArgs e)
        {
            if (L2.Count == 0)
            {
                MessageBox.Show("Process first.");
                return;
            }

            var dialog = new SaveFileDialog();
            dialog.Filter = "Text files (*.txt)|*.txt";

            if (dialog.ShowDialog() == true)
            {
                using (var sw = new StreamWriter(dialog.FileName))
                {
                    for (int i = 0; i < L2.Count; i++)
                    {
                        sw.Write(L2[i]);
                        if ((i + 1) % 5 == 0) sw.WriteLine();
                        else sw.Write(' ');
                    }
                }
            }
        }
    }
}
