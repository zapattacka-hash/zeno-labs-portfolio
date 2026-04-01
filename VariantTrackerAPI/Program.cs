var builder = WebApplication.CreateBuilder(args);

// ACTIVATE CONTROLLERS
builder.Services.AddControllers();
builder.Services.AddOpenApi();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

// MAP THE BRAIN
app.MapControllers();

app.Run();
