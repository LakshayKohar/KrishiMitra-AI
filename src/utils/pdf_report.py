from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf_report(report, output_path="outputs/krishimitra_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)

    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "KrishiMitra AI Report")

    y -= 40
    c.setFont("Helvetica", 11)

    lines = [
        f"Location: {report['location']}",
        f"Latitude: {report['latitude']}",
        f"Longitude: {report['longitude']}",
        f"Cloud Cover: {report['cloud_cover']:.2f}%",
        "",
        f"Average NDVI: {report['ndvi']['average']:.3f}",
        f"Average NDWI: {report.get('ndwi', {}).get('average', 'N/A')}",
        f"Average MSI: {report.get('msi', {}).get('average', 'N/A')}",
        "",
        f"Crop Health: {report['crop_health']}",
        f"Recommendation: {report['recommendation']}",
        "",
        f"Final Advisory Priority: {report.get('final_advisory', {}).get('priority', 'N/A')}",
        f"Final Advisory: {report.get('final_advisory', {}).get('summary', 'N/A')}",
    ]

    for line in lines:
        c.drawString(50, y, str(line))
        y -= 22

    c.save()

    return output_path