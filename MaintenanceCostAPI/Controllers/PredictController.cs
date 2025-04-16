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
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public async Task<IActionResult> Predict([FromBody] CarData data)
        {
            try {
                var jsonInput = JsonSerializer.Serialize(data);

                Console.WriteLine($"Input JSON: {jsonInput}");

                var scriptPath = Path.Combine(Directory.GetCurrentDirectory(), "python_code", "predict.py");
                var escapedJson = JsonSerializer.Serialize(data).Replace("\"", "\\\"");

                Console.WriteLine($"\"{scriptPath}\" \"{escapedJson}\"");

                var start = new ProcessStartInfo
                {
                    FileName = "python",
                    // Arguments = $"python_code/predict.py '{jsonInput}'",
                    Arguments = $"\"{scriptPath}\" \"{escapedJson}\"",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true, // helpful for debugging
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using var process = Process.Start(start);
                if (process == null)
                    return StatusCode(500, "Failed to start Python process.");

                Console.WriteLine($"Process started: {process.Id}");

                var stdOutTask = process.StandardOutput.ReadToEndAsync();
                var stdErrTask = process.StandardError.ReadToEndAsync();

                await Task.WhenAll(stdOutTask, stdErrTask);

                string output = stdOutTask.Result;
                string error = stdErrTask.Result;
                process.WaitForExit();

                Console.WriteLine($"Output: {output}");

                if (!string.IsNullOrEmpty(error))
                    return StatusCode(500, $"Python error: {error}");

                return Ok(output);
            } catch (Exception ex) {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}
