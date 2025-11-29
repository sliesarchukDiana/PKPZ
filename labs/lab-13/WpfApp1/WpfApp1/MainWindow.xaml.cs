using System.IO;
using System.Text;
using System.Windows;
using Microsoft.Win32;
using Microsoft.Recognizers.Text;
using Microsoft.Recognizers.Text.Number;

namespace NumberRecognizerApp
{
    public class RecognitionInfo
    {
        public string Text { get; set; }
        public int Start { get; set; }
        public int End { get; set; }
        public string Value { get; set; }
    }

    public partial class MainWindow
    {
        private string _modifiedText = string.Empty;

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
                    ProcessText(fileContent);
                    BtnSave.IsEnabled = true;
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Помилка при читанні файлу: {ex.Message}", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        private void ProcessText(string inputText)
        {
            var results = NumberRecognizer.RecognizeNumber(inputText, Culture.English);

            var displayList = new List<RecognitionInfo>();
            
            StringBuilder sb = new StringBuilder(inputText);
            var sortedResults = results.OrderByDescending(r => r.Start).ToList();

            foreach (var result in sortedResults)
            {
                string originalText = result.Text;
                int start = result.Start;
                int end = result.End;
                string valueStr = "";
                if (result.Resolution.TryGetValue("value", out object valObj))
                {
                    valueStr = valObj.ToString();
                }
                displayList.Add(new RecognitionInfo
                {
                    Text = originalText,
                    Start = start,
                    End = end,
                    Value = valueStr
                });
                sb.Remove(start, end - start + 1);
                sb.Insert(start, valueStr);
            }
            displayList.Reverse();
            GridResults.ItemsSource = displayList;
            
            _modifiedText = sb.ToString();
            TxtOutput.Text = _modifiedText;
        }

        private void BtnSave_Click(object sender, RoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog
            {
                Filter = "Text files (*.txt)|*.txt",
                FileName = "Result.txt"
            };

            if (saveFileDialog.ShowDialog() == true)
            {
                try
                {
                    File.WriteAllText(saveFileDialog.FileName, _modifiedText);
                    MessageBox.Show("Файл успішно збережено!", "Успіх", MessageBoxButton.OK, MessageBoxImage.Information);
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Помилка при збереженні: {ex.Message}", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }
    }
}