import pandas as pd
from tkinter import Tk, filedialog, Button, Text

# Store global analysis result
analysis_result = ""

def analyze_csv():
    global analysis_result
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    df = pd.read_csv(file_path)

    report = []

    report.append(f"🔍 File: {file_path.split('/')[-1]}")
    report.append(f"📊 Total Rows: {df.shape[0]}")
    report.append(f"📊 Total Columns: {df.shape[1]}")
    report.append("\n📌 Column-wise Stats:\n")

    for col in df.columns:
        report.append(f"🧾 Column: {col}")
        report.append(f"   - Type: {df[col].dtype}")
        report.append(f"   - Unique Values: {df[col].nunique()}")
        report.append(f"   - Null Values: {df[col].isnull().sum()}")
        if pd.api.types.is_numeric_dtype(df[col]):
            report.append(f"   - Mean: {df[col].mean():.2f}")
            report.append(f"   - Median: {df[col].median():.2f}")
            report.append(f"   - Mode: {df[col].mode().values[0]}")
        report.append("")

    analysis_result = "\n".join(report)
    output_box.delete("1.0", "end")
    output_box.insert("1.0", analysis_result)
    save_button.config(state="normal")

def save_report():
    global analysis_result
    if not analysis_result:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text file", "*.txt")])
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(analysis_result)

# GUI
root = Tk()
root.title("CSV File Analyzer")
root.geometry("720x620")

Button(root, text="📂 Upload CSV and Analyze", command=analyze_csv, height=2, width=30).pack(pady=20)

output_box = Text(root, wrap="word", height=25, width=85)
output_box.pack(pady=10)

save_button = Button(root, text="💾 Save Report (.txt)", command=save_report, height=2, width=30, state="disabled")
save_button.pack(pady=10)

root.mainloop()
