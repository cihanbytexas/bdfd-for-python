def handler(request):
    # Query parametresinden "code" al
    code = request.args.get("code") if request.args else None

    # Eğer kod verilmemişse basit mesaj döndür
    if not code:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": "Merhaba! Python API çalışıyor 🚀 Parametre olarak ?code=print('Hello') gönder."
        }

    # Çıktıyı yakalamak için
    import sys, io, traceback
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(code, {})  # gelen kodu çalıştır
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
