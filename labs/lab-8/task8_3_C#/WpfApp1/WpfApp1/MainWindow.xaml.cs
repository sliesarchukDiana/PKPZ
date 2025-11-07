using System.Windows;

namespace RainbowQuiz
{
    public partial class MainWindow : Window
    {
        private enum RainbowColor
        {
            Червоний,
            Помаранчевий,
            Жовтий,
            Зелений,
            Блакитний,
            Синій,
            Фіолетовий
        }

        private Dictionary<RainbowColor, (string eng, string hex)> rainbow = new()
        {
            { RainbowColor.Червоний, ("red", "#FF0000") },
            { RainbowColor.Помаранчевий, ("orange", "#FFA500") },
            { RainbowColor.Жовтий, ("yellow", "#FFFF00") },
            { RainbowColor.Зелений, ("green", "#008000") },
            { RainbowColor.Блакитний, ("light-blue", "#ADD8E6") },
            { RainbowColor.Синій, ("blue", "#0000FF") },
            { RainbowColor.Фіолетовий, ("violet", "#8A2BE2") }
        };

        private bool running = true;

        public MainWindow()
        {
            InitializeComponent();
            ResultText.Text = "Щоб почати, введіть колір і натисніть «Перевірити».";
        }

        private void CheckButton_Click(object sender, RoutedEventArgs e)
        {
            while (running)
            {
                string input = ColorInput.Text.Trim();
                if (string.IsNullOrWhiteSpace(input))
                {
                    MessageBox.Show("Введіть назву кольору!", "Помилка");
                    return;
                }

                try
                {
                    RainbowColor color = (RainbowColor)Enum.Parse(typeof(RainbowColor), input, ignoreCase: true);

                    switch (color)
                    {
                        case RainbowColor.Червоний:
                        case RainbowColor.Помаранчевий:
                        case RainbowColor.Жовтий:
                        case RainbowColor.Зелений:
                        case RainbowColor.Блакитний:
                        case RainbowColor.Синій:
                        case RainbowColor.Фіолетовий:
                            var data = rainbow[color];
                            ResultText.Text = $"Колір {color} — англійською {data.eng}, код {data.hex}";
                            break;
                        default:
                            ResultText.Text = "Такого кольору немає у веселці!";
                            break;
                    }
                }
                catch
                {
                    ResultText.Text = "Невідомий колір. Спробуйте ще раз.";
                }
                
                MessageBoxResult answer = MessageBox.Show("Продовжити?", "Вікторина", MessageBoxButton.YesNo);
                if (answer == MessageBoxResult.No)
                {
                    running = false;
                    Application.Current.Shutdown();
                }
                else
                {
                    ColorInput.Clear();
                    return;
                }
            }
        }

        private void ExitButton_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
}
