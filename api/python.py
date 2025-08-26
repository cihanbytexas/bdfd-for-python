import sys
import io
import traceback

def handler(request):
    # GET parametresinden code al
    code = request.args.get("code", "")

    # Çıktıyı yakalamak için stdout yönlendir
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(code, {})  # Python kodunu çalıştır
        output = buffer.getvalue()
    except Exception as e:
        output = "Hata: " + str(e) + "\n" + traceback.format_exc()

    # stdout'u geri yükle
    sys.stdout = sys.__stdout__

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": output
    }
