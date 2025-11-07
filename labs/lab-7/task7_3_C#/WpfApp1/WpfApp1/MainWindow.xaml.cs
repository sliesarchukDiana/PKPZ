using System.Globalization;
using System.Windows;
using System.Windows.Controls;

namespace WpfApp1
{
    public partial class MainWindow : Window
    {
        public struct RebootLog
        {
            public string Date { get; set; }
            public string Time { get; set; }
            public string Reason { get; set; }
            public string User { get; set; }
            public int DaysAgo
            {
                get
                {
                    if (DateTime.TryParseExact(Date, "ddMMyyyy", null, DateTimeStyles.None, out DateTime parsed))
                        return (DateTime.Now - parsed).Days;
                    return 0;
                }
            }
        }

        private List<RebootLog> logs = new();

        public MainWindow()
        {
            InitializeComponent();
            LogsGrid.ItemsSource = logs;
        }

        private void AddRecord_Click(object sender, RoutedEventArgs e)
        {
            if (!DateTime.TryParseExact(DateInput.Text, "ddMMyyyy", null, DateTimeStyles.None, out DateTime date))
            {
                MessageBox.Show("Невірний формат дати!", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            if (!TimeSpan.TryParseExact(TimeInput.Text, "c", CultureInfo.InvariantCulture, out TimeSpan time))
            {
                MessageBox.Show("Невірний формат часу!", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            if (ReasonInput.SelectedItem == null || string.IsNullOrWhiteSpace(UserInput.Text))
            {
                MessageBox.Show("Заповни всі поля!", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            logs.Add(new RebootLog
            {
                Date = DateInput.Text,
                Time = TimeInput.Text,
                Reason = ((ComboBoxItem)ReasonInput.SelectedItem).Content.ToString(),
                User = UserInput.Text
            });

            LogsGrid.Items.Refresh();
            ClearInputs();
        }

        private void ClearInputs()
        {
            DateInput.Clear();
            TimeInput.Clear();
            UserInput.Clear();
            ReasonInput.SelectedItem = null;
        }

        private void NightEvents_Click(object sender, RoutedEventArgs e)
        {
            var nightLogs = logs.Where(l =>
            {
                if (TimeSpan.TryParseExact(l.Time, "c", CultureInfo.InvariantCulture, out TimeSpan t))
                    return t.Hours >= 22 || t.Hours < 6;
                return false;
            }).ToList();

            ShowResult(nightLogs, "Події вночі:");
        }

        private void CountBetweenDates_Click(object sender, RoutedEventArgs e)
        {
            var d1 = Microsoft.VisualBasic.Interaction.InputBox("Введи першу дату (ДДММРРРР):", "Перша дата");
            var d2 = Microsoft.VisualBasic.Interaction.InputBox("Введи другу дату (ДДММРРРР):", "Друга дата");

            if (!DateTime.TryParseExact(d1, "ddMMyyyy", null, DateTimeStyles.None, out DateTime date1) ||
                !DateTime.TryParseExact(d2, "ddMMyyyy", null, DateTimeStyles.None, out DateTime date2))
            {
                MessageBox.Show("Невірний формат дати.", "Помилка", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            int count = logs.Count(l =>
            {
                if (DateTime.TryParseExact(l.Date, "ddMMyyyy", null, DateTimeStyles.None, out DateTime d))
                    return d >= date1 && d <= date2 && l.Reason == "Профілактика";
                return false;
            });

            ResultText.Text = $"Профілактик між {d1} і {d2}: {count}";
        }

        private void LastReboot_Click(object sender, RoutedEventArgs e)
        {
            if (logs.Count == 0)
            {
                ResultText.Text = "Немає записів.";
                return;
            }

            var latest = logs.MaxBy(l =>
            {
                if (DateTime.TryParseExact(l.Date, "ddMMyyyy", null, DateTimeStyles.None, out DateTime d) &&
                    TimeSpan.TryParseExact(l.Time, "c", CultureInfo.InvariantCulture, out TimeSpan t))
                    return d.Add(t);
                return DateTime.MinValue;
            });

            ResultText.Text = $"Останнє перезавантаження: {latest.Date} {latest.Time} ({latest.Reason}, {latest.User})";
        }

        private void SearchByDate_Click(object sender, RoutedEventArgs e)
        {
            string d = Microsoft.VisualBasic.Interaction.InputBox("Введи дату (ДДММРРРР):", "Пошук по даті");
            var matches = logs.Where(l => l.Date == d).ToList();
            ShowResult(matches, $"Події {d}:");
        }

        private void ShowResult(List<RebootLog> list, string title)
        {
            if (list.Count == 0)
                ResultText.Text = $"{title}\nНічого не знайдено.";
            else
                ResultText.Text = $"{title}\n" + string.Join("\n", list.Select(l => $"{l.Date} {l.Time} — {l.Reason}, {l.User}"));
        }
    }
}
