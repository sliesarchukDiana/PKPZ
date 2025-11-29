using System.IO;
using System.Text;
using System.Windows;
using Microsoft.Win32;
using Microsoft.Recognizers.Text;
using Microsoft.Recognizers.Text.NumberWithUnit;
using Microsoft.Recognizers.Text.DateTime; 
using Microsoft.Recognizers.Text.Sequence;

namespace MultiRecognizerApp
{
    public class EntityItem
    {
        public string Category { get; set; }
        public string Text { get; set; }
        public string Value { get; set; }
    }

    public partial class MainWindow
    {
        private List<EntityItem> _allItems = new();
        private string _statsReport = "";

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
                    string text = File.ReadAllText(openFileDialog.FileName);
                    TxtInput.Text = text;
                    ProcessText(text);
                    BtnSave.IsEnabled = true;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Помилка: " + ex.Message);
                }
            }
        }

        private void ProcessText(string text)
        {
            _allItems.Clear();
            string culture = Culture.English;
            AddResults(NumberWithUnitRecognizer.RecognizeCurrency(text, culture), "Валюта");
            AddResults(NumberWithUnitRecognizer.RecognizeDimension(text, culture), "Вимірювання (розмір/вага)");
            AddResults(NumberWithUnitRecognizer.RecognizeTemperature(text, culture), "Температура");
            AddResults(DateTimeRecognizer.RecognizeDateTime(text, culture), "Дата і Час");
            AddResults(SequenceRecognizer.RecognizePhoneNumber(text, culture), "Номер телефону");
            AddResults(SequenceRecognizer.RecognizeIpAddress(text, culture), "IP-адреса");
            AddResults(SequenceRecognizer.RecognizeEmail(text, culture), "Email");
            AddResults(SequenceRecognizer.RecognizeURL(text, culture), "URL-адреса");
            AddResults(SequenceRecognizer.RecognizeHashtag(text, culture), "Хеш-тег");
            
            GridResults.ItemsSource = null;
            GridResults.ItemsSource = _allItems;

            GenerateStats();
        }
        private void AddResults(List<ModelResult> results, string categoryName)
        {
            foreach (var r in results)
            {
                string valStr = "";
                if (r.Resolution != null)
                {
                    if (r.Resolution.TryGetValue("value", out var value))
                        valStr = value?.ToString()!;
                    else if (r.Resolution.ContainsKey("values"))
                        valStr = "Complex Date/Time object"; 
                    else
                        valStr = string.Join(", ", r.Resolution.Keys);
                }

                _allItems.Add(new EntityItem
                {
                    Category = categoryName,
                    Text = r.Text,
                    Value = string.IsNullOrWhiteSpace(valStr) ? r.TypeName : valStr
                });
            }
        }

        private void GenerateStats()
        {
            var stats = _allItems
                .GroupBy(x => x.Category)
                .Select(g => $"{g.Key}: {g.Count()}")
                .ToList();

            if (stats.Count == 0)
                _statsReport = "Нічого не знайдено.";
            else
                _statsReport = string.Join(" | ", stats);

            TxtStats.Text = _statsReport;
        }

        private void BtnSave_Click(object sender, RoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog
            {
                Filter = "Text files (*.txt)|*.txt",
                FileName = "RecognizedReport.txt"
            };

            if (saveFileDialog.ShowDialog() == true)
            {
                try
                {
                    StringBuilder sb = new StringBuilder();
                    
                    sb.AppendLine("СТАТИСТИКА");
                    var stats = _allItems.GroupBy(x => x.Category);
                    foreach(var group in stats)
                    {
                        sb.AppendLine($"{group.Key}: {group.Count()}");
                    }
                    sb.AppendLine();

                    sb.AppendLine("ЗВІТ");
                    foreach (var item in _allItems)
                    {
                        sb.AppendLine($"[{item.Category}] Знайдено: \"{item.Text}\" -> Інтерпретація: {item.Value}");
                    }

                    File.WriteAllText(saveFileDialog.FileName, sb.ToString());
                    MessageBox.Show("Звіт збережено успішно!");
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Помилка збереження: " + ex.Message);
                }
            }
        }
    }
}