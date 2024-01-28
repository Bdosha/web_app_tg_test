# web_app_tg_test
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>

<body>
    <div id="main">
        <h1>QR-код</h1>
        <input type="text" placeholder="id" , id="id">
        <button id="buy">Кнопка</button>
    </div>


    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script>
        let tg = window.Telegram.WebApp;
        let button = document.getElementById("buy");
        button.addEventListener("click", () => {
            document.getElementById("id").value = tg.initDataUnsafe.first_name;
        });
    </script>
</body>

</html>
