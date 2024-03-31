import subprocess
import webbrowser

# قائمة المكتبات المطلوبة
required_libraries = [
    'opencv-python',
    'pytesseract',
    'pyzbar',
    'tqdm'  # إضافة tqdm إلى قائمة المكتبات المطلوبة
]

# تثبيت المكتبات المطلوبة
for library in required_libraries:
    subprocess.check_call(['pip', 'install', library])

# رسالة توجيهية
print("تم تثبيت المكتبات المطلوبة بنجاح.")

# فتح صفحة GitHub لتحميل البرنامج
repository_url = 'https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download'
webbrowser.open_new_tab(repository_url)