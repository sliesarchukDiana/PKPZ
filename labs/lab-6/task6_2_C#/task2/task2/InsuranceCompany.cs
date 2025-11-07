using System.Windows;

namespace WpfApp1
{
    public class InsuranceCompany : IOrganization, IServices
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public int Employees { get; set; }
        public string InsuranceType { get; set; }
        public int ClientCount { get; set; }

        public InsuranceCompany(string name, string address, int employees, string insuranceType, int clients)
        {
            Name = name;
            Address = address;
            Employees = employees;
            InsuranceType = insuranceType;
            ClientCount = clients;
        }

        public void ProvideService() { MessageBox.Show("Компанія надає страхові послуги."); }
        public void CalculateRevenue() { MessageBox.Show($"Очікуваний прибуток: {ClientCount * 1000} грн."); }

        public string Show()
        {
            return $"Страхова компанія:\nНазва: {Name}\nАдреса: {Address}\nПрацівників: {Employees}\nТип страхування: {InsuranceType}\nКлієнтів: {ClientCount}";
        }
    }
}