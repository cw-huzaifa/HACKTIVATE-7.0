using System.Diagnostics;
using System.Text.Json;
using MaintenanceCostAPI.Model;
using Microsoft.AspNetCore.Mvc;

namespace MaintenanceCostAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PredictController : ControllerBase
    {
        [HttpPost]
        public IActionResult Predict([FromBody] CarData data)
        {
            try {
                var jsonInput = JsonSerializer.Serialize(data);

                var start = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = $"python_code/predict.py '{jsonInput}'",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true, // helpful for debugging
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using var process = Process.Start(start);
                if (process == null)
                    return StatusCode(500, "Failed to start Python process.");

                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();
                process.WaitForExit();

                if (!string.IsNullOrEmpty(error))
                    return StatusCode(500, $"Python error: {error}");

                return Ok(new { Prediction = output.Trim() });
            } catch (Exception ex) {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}
