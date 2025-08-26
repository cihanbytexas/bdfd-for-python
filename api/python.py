def handler(request):
    import sys, io, traceback

    code = request.args.get("code") if request.args else None

    if not code:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": "Python API çalışıyor! 🚀 Parametre olarak ?code=print('Hello') gönder."
        }

    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(code, {})
        output = buffer.getvalue()
    except Exception as e:
        output = "Hata: " + str(e) + "\n" + traceback.format_exc()

    sys.stdout = sys.__stdout__

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": output
    }
