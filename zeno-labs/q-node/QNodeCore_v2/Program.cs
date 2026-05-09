using System;
using System.Security.Cryptography;
using System.Threading;
using System.Threading.Tasks;

class Program {
    static async Task Main() {
        Console.WriteLine("\e[1;34m> [SYS] INITIATING EXFILTRATION ENGINE...\e[0m");
        Console.WriteLine("> [PIPELINE] Zero-resistance channel verified. Status: OPEN.");
        Console.WriteLine("> [VARIANT TRACKER] Synchronizing extraction telemetry...");
        
        await Task.Delay(1000);
        Console.Clear();
        Console.WriteLine("\e[1;32m> [EXFILTRATION IN PROGRESS - STREAMING DATA]\e[0m");
        Console.WriteLine("--------------------------------------------------");

        long totalBytesExtracted = 0;
        
        // Asynchronous loop to simulate high-velocity data streaming
        var cts = new CancellationTokenSource();
        var extractionTask = Task.Run(async () => {
            while (!cts.Token.IsCancellationRequested) {
                byte[] simulatedPacket = new byte[1024 * 64]; // 64 KB packets
                RandomNumberGenerator.Fill(simulatedPacket); // High entropy payload
                
                totalBytesExtracted += simulatedPacket.Length;
                
                // Convert bytes to MB for readable telemetry
                double megabytes = totalBytesExtracted / 1048576.0;
                
                Console.Write($"\r> [PIPELINE] Routing Payload ID: {Guid.NewGuid().ToString().Substring(0,8)} | Total Extracted: {megabytes:F2} MB");
                await Task.Delay(50); // Throttle slightly for visual terminal rendering
            }
        }, cts.Token);

        // Run exfiltration for 5 seconds to demonstrate the pipeline
        await Task.Delay(5000);
        cts.Cancel();
        await extractionTask;

        Console.WriteLine("\n--------------------------------------------------");
        Console.WriteLine("\e[1;33m> [SYS] EXTRACTION CYCLE COMPLETE. PACKETS SECURED.\e[0m");
        Console.WriteLine($"> [ARCHIVE] Data successfully routed to Zeno Labs terminal.");
    }
}
