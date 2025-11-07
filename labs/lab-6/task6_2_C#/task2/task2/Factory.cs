using System.Windows;

namespace WpfApp1
{
    public class Factory : IOrganization, IServices
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public int Employees { get; set; }
        public string ProductionType { get; set; }
        public int ProductionVolume { get; set; }

        public Factory(string name, string address, int employees, string productionType, int volume)
        {
            Name = name;
            Address = address;
            Employees = employees;
            ProductionType = productionType;
            ProductionVolume = volume;
        }

        public void ProvideService() { MessageBox.Show("Завод виготовляє продукцію."); }
        public void CalculateRevenue() { MessageBox.Show($"Місячний прибуток: {ProductionVolume * 500} грн."); }

        public string Show()
        {
            return $"Завод:\nНазва: {Name}\nАдреса: {Address}\nПрацівників: {Employees}\nТип виробництва: {ProductionType}\nОбсяг продукції: {ProductionVolume}";
        }
    }
}