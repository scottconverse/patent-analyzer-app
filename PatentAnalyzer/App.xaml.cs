using System.IO;
using System.Windows;
using System.Windows.Threading;

namespace PatentAnalyzer;

public partial class App : Application
{
    protected override void OnStartup(StartupEventArgs e)
    {
        base.OnStartup(e);

        // Global unhandled exception handlers
        DispatcherUnhandledException += (s, ex) =>
        {
            LogError("DispatcherUnhandled", ex.Exception);
            MessageBox.Show($"Unexpected error:\n\n{ex.Exception.Message}\n\nSee error.log for details.",
                "Patent Analyzer Error", MessageBoxButton.OK, MessageBoxImage.Error);
            ex.Handled = true;
        };

        AppDomain.CurrentDomain.UnhandledException += (s, ex) =>
        {
            if (ex.ExceptionObject is Exception exception)
                LogError("AppDomain", exception);
        };

        TaskScheduler.UnobservedTaskException += (s, ex) =>
        {
            LogError("TaskScheduler", ex.Exception);
            ex.SetObserved();
        };
    }

    private static void LogError(string source, Exception ex)
    {
        try
        {
            var logPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "error.log");
            var entry = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] [{source}] {ex}\n\n";
            File.AppendAllText(logPath, entry);
        }
        catch { }
    }
}
