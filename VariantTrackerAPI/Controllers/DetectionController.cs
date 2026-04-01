using Microsoft.AspNetCore.Mvc;
using Google.Cloud.Spanner.Data;
using VariantTrackerAPI.Models;

namespace VariantTrackerAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class DetectionController : ControllerBase
{
    private readonly string _connectionString = "Data Source=projects/YOUR_PROJECT/instances/YOUR_INSTANCE/databases/YOUR_DATABASE";

    [HttpPost]
    public async Task<IActionResult> Post(Detection detection)
    {
        using var connection = new SpannerConnection(_connectionString);
        await connection.OpenAsync();

        var cmd = connection.CreateInsertCommand("WastewaterDetections", new SpannerParameterCollection
        {
            { "LocationId", SpannerDbType.String, detection.LocationId },
            { "DetectionDate", SpannerDbType.Date, detection.DetectionDate },
            { "VariantLevel", SpannerDbType.Int64, detection.VariantLevel }
        });

        await cmd.ExecuteNonQueryAsync();
        return Ok("Detection logged successfully.");
    }
}
