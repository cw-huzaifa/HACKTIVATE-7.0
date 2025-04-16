using System.Text.Json.Serialization;

namespace MaintenanceCostAPI.Model
{
    public class CarData
    {
        [JsonPropertyName("brand")]
        public string Brand { get; set; }

        [JsonPropertyName("model")]
        public string Model { get; set; }

        [JsonPropertyName("fuelType")]
        public string FuelType { get; set; }

        [JsonPropertyName("transmission")]
        public string Transmission { get; set; }

        [JsonPropertyName("ageYears")]
        public int AgeYears { get; set; }

        [JsonPropertyName("kilometersDriven")]
        public int KilometersDriven { get; set; }

        [JsonPropertyName("numServices")]
        public int NumServices { get; set; }

        [JsonPropertyName("drivingBehavior")]
        public string DrivingBehavior { get; set; }
    }
}