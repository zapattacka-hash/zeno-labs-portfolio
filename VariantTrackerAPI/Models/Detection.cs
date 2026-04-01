namespace VariantTrackerAPI.Models;

public class Detection
{
    public string LocationId { get; set; } = string.Empty;
    public DateTime DetectionDate { get; set; }
    public long VariantLevel { get; set; }
}
