using System.IO;
using System.Text;
using System.Windows;
using Microsoft.Win32;
using Microsoft.Recognizers.Text;
using Microsoft.Recognizers.Text.Number;

namespace OrdinalRecognizerApp
{
    public class OrdinalItem
    {
        public string Text { get; set; }        
        public string Value { get; set; }    
        public string FormattedString => $"{Text} – {Value}";
    }

    public partial class MainWindow
    {
        private List<OrdinalItem> _foundOrdinals = new();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnLoad_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
            };

            if (openFileDialog.ShowDialog() == true)
            {
                try
                {
                    string fileContent = File.ReadAllText(openFileDialog.FileName);
                    TxtInput.Text = fileContent;
                    AnalyzeText(fileContent);
                    BtnSave.IsEnabled = true;
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Помилка читання: {ex.Message}", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        private void AnalyzeText(string text)
        {
            var results = NumberRecognizer.RecognizeOrdinal(text, Culture.English);

            _foundOrdinals.Clear();

            foreach (var result in results)
            {
                string originalText = result.Text;
                string valueStr = "N/A";
                if (result.Resolution.TryGetValue("value", out object valObj))
                {
                    valueStr = valObj.ToString();
                }

                _foundOrdinals.Add(new OrdinalItem
                {
                    Text = originalText,
                    Value = valueStr
                });
            }
            
            GridResults.ItemsSource = null;
            GridResults.ItemsSource = _foundOrdinals;
            LblCount.Text = $"Кількість порядкових числівників: {_foundOrdinals.Count}";
        }

        private void BtnSave_Click(object sender, RoutedEventArgs e)
        {
            if (_foundOrdinals.Count == 0)
            {
                MessageBox.Show("Немає даних для збереження.", "Увага", MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }

            SaveFileDialog saveFileDialog = new SaveFileDialog
            {
                Filter = "Text files (*.txt)|*.txt",
                FileName = "OrdinalReport.txt"
            };

            if (saveFileDialog.ShowDialog() == true)
            {
                try
                {
                    StringBuilder sb = new StringBuilder();
                    sb.AppendLine($"Кількість порядкових числівників: {_foundOrdinals.Count}");
                    foreach (var item in _foundOrdinals)
                    {
                        sb.AppendLine(item.FormattedString);
                    }

                    File.WriteAllText(saveFileDialog.FileName, sb.ToString());
                    MessageBox.Show("Файл успішно збережено!", "Успіх", MessageBoxButton.OK, MessageBoxImage.Information);
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Помилка збереження: {ex.Message}", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }
    }
}