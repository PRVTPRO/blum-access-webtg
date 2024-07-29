Шаги для запуска

Сохраните проект используя git clone

Установите mitmproxy, если он еще не установлен:

    bash
    
```
pip install mitmproxy
```

Запустите прокси-сервер:

```
python proxy.py
```
    Настройте ваш браузер (например, Firefox) на использование прокси-сервера:
        Перейдите в Preferences -> General -> Network Settings -> Settings....
        Выберите Manual proxy configuration.
        Введите 127.0.0.1 и порт 8080 в поля HTTP Proxy и Port.
        Нажмите OK.

    Установите сертификаты mitmproxy, если требуется, открыв http://mitm.it в браузере и следуя инструкциям.

Этот скрипт запускает прокси-сервер mitmproxy с помощью асинхронного цикла событий, корректно управляя заголовками HTTP-ответов, позволяя запускать веб приложения telegram минуя ограничения Content-Security-Policy в iframe.
