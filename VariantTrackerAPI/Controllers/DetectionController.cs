using Microsoft.AspNetCore.Mvc;
using VariantTrackerAPI.Models;

namespace VariantTrackerAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class DetectionController : ControllerBase
{
    [HttpPost]
    public IActionResult Post(Detection detection)
    {
        // MOCK: Pretending to save to Spanner for Zeno Labs Portfolio
        Console.WriteLine($"[MOCK] Received: {detection.LocationId} - Level: {detection.VariantLevel}");

        return Ok(new {
            message = "Detection logged successfully (Mock Mode)",
            received = detection
        });
    }
}
