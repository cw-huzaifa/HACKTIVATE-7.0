namespace MaintenanceCostAPI.Model
{
    public class CarData
    {
        public string Brand { get; set; }
        public string Model { get; set; }
        public string FuelType { get; set; }
        public string Transmission { get; set; }
        public int AgeYears { get; set; }
        public int KilometersDriven { get; set; }
        public int NumServices { get; set; }
        public string DrivingBehavior { get; set; }
    }
}