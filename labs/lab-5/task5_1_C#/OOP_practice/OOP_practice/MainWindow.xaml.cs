using System;
using System.IO;
using System.Windows;

namespace PersonaApp
{
    public partial class MainWindow : Window
    {
        private Persona person;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Create_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                person = new Persona
                {
                    Name = NameBox.Text,
                    Surname = SurnameBox.Text,
                    Gender = GenderBox.Text,
                    City = CityBox.Text,
                    Age = int.Parse(AgeBox.Text),
                    Height = double.Parse(HeightBox.Text),
                    Weight = double.Parse(WeightBox.Text)
                };

                OutputBox.Text = "Об'єкт створено успішно.";
            }
            catch
            {
                OutputBox.Text = "Помилка введення даних.";
            }
        }

        private void Save_Click(object sender, RoutedEventArgs e)
        {
            if (person == null)
            {
                OutputBox.Text = "Спершу створіть об'єкт.";
                return;
            }

            string data = person.ToString();
            File.WriteAllText("persona.txt", data);
            OutputBox.Text = "Дані збережено у persona.txt";
        }

        private void Actions_Click(object sender, RoutedEventArgs e)
        {
            if (person == null)
            {
                OutputBox.Text = "Об'єкт не створено.";
                return;
            }

            string result =
                $"{person.FullInfo()}\n" +
                $"Індекс маси тіла: {person.CalcBMI():F1}\n" +
                $"{person.CategoryByAge()}";

            OutputBox.Text = result;
        }
    }

    public class Persona
    {
        private string name;
        private string surname;
        private string gender;
        private string city;
        private int age;
        private double height;
        private double weight;

        public string Name { get => name; set => name = value; }
        public string Surname { get => surname; set => surname = value; }
        public string Gender { get => gender; set => gender = value; }
        public string City { get => city; set => city = value; }
        public int Age { get => age; set => age = value; }
        public double Height { get => height; set => height = value; }
        public double Weight { get => weight; set => weight = value; }

        public string FullInfo()
        {
            return $"Персона: {Name} {Surname}, {Age} років, {Gender}, {City}";
        }

        public double CalcBMI()
        {
            double h = Height / 100;
            return Weight / (h * h);
        }

        public string CategoryByAge()
        {
            if (Age < 18) return "Неповнолітній";
            if (Age < 60) return "Дорослий";
            return "Пенсіонер";
        }

        public override string ToString()
        {
            return $"{Name} {Surname}, {Gender}, {Age} років, {Height} см, {Weight} кг, {City}";
        }
    }
}
