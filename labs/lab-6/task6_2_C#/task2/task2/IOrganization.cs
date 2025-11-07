namespace WpfApp1
{
    public interface IOrganization
    {
        string Name { get; set; }
        string Address { get; set; }
        int Employees { get; set; }
        string Show();
    }
}