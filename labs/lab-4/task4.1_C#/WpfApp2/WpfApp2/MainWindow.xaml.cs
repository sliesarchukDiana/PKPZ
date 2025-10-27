using System.IO;
using System.Windows;

namespace WpfBuildingsLab
{
    public partial class MainWindow
    {
        private string _inputPath = "Input Data.txt";
        private const int Cols = 6;

        public MainWindow()
        {
            InitializeComponent();
            txtFile.Text = _inputPath;
        }

        private void BtnSelect_Click(object sender, RoutedEventArgs e)
        {
            var dlg = new Microsoft.Win32.OpenFileDialog();
            dlg.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*";
            dlg.FileName = "Input Data.txt";
            if (dlg.ShowDialog() == true)
            {
                _inputPath = dlg.FileName;
                txtFile.Text = _inputPath;
                txtStatus.Text = "Selected " + Path.GetFileName(_inputPath);
            }
        }

        private void BtnLoad_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                if (!File.Exists(_inputPath))
                {
                    MessageBox.Show($"Input file not found: {_inputPath}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                    return;
                }

                string[] lines = File.ReadAllLines(_inputPath);
                if (lines.Length == 0)
                {
                    txtStatus.Text = "Input file is empty.";
                    return;
                }

                int rows = lines.Length;
                string[,] table = new string[rows, Cols];
                var parsedRows = new List<string[]>();
                int skipped = 0;

                for (int i = 0; i < rows; i++)
                {
                    string line = lines[i].Trim();
                    if (string.IsNullOrEmpty(line)) { skipped++; continue; }

                    // Split by semicolon; fallback to comma if no semicolon found
                    string[] parts = line.Split(new[] { ';' }, StringSplitOptions.None);
                    if (parts.Length == 1)
                        parts = line.Split(new[] { ',' }, StringSplitOptions.None);

                    if (parts.Length != Cols)
                    {
                        skipped++;
                        continue;
                    }

                    for (int c = 0; c < Cols; c++)
                        table[i, c] = parts[c].Trim();

                    parsedRows.Add(parts.Select(p => p.Trim()).ToArray());
                }
                
                var resultObjects = new List<BuildingRecord>();
                foreach (var parts in parsedRows)
                {
                    if (!int.TryParse(parts[4], out int serviceLife))
                        continue; // skip if can't parse

                    if (serviceLife > 50)
                    {
                        resultObjects.Add(new BuildingRecord
                        {
                            Address = parts[0],
                            Type = parts[1],
                            Floors = parts[2],
                            Apartments = parts[3],
                            ServiceLife = serviceLife,
                            YearsToOverhaul = parts[5]
                        });
                    }
                }

                dgResults.ItemsSource = resultObjects;
                
                string outDir = Path.GetDirectoryName(Path.GetFullPath(_inputPath));
                string outPath = Path.Combine(outDir, "Output Data.txt");
                using (var sw = new StreamWriter(outPath, false))
                {
                    foreach (var b in resultObjects)
                    {
                        sw.WriteLine($"{b.Address};{b.Type};{b.Floors};{b.Apartments};{b.ServiceLife};{b.YearsToOverhaul}");
                    }
                }

                txtStatus.Text = $"Done. Processed: {parsedRows.Count}, Selected: {resultObjects.Count}, Skipped: {skipped}. Output: {outPath}";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private class BuildingRecord
        {
            public string Address { get; set; }
            public string Type { get; set; }
            public string Floors { get; set; }
            public string Apartments { get; set; }
            public int ServiceLife { get; set; }
            public string YearsToOverhaul { get; set; }
        }
    }
}