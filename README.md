RabbitMQ tools
=================
Инструменты для связи с RabbitMQ


API
-----
позволяет прослушивать, очереди RabbitMQ, отправлять сообщения в RabbitMQ, так же предоставляет функцию для парсинга конфига


Usage
    
    # прослушивание очереди (использовать в контекстном менеджере)
    with rabbit_tools.listener.RabbitMQListener(self.conf_dict) as listener_obj:
            listener_obj.run()
            
    # отправка сообщения
    rabbit_tools.sender.rabbit_send(conf_dict, msg, queue_name)
    
    # парсинг конфига
    rabbit_tools.sender.parse_conf(conf_file_path)
    


Requirements
-------------
    python2-pika >= 0.12.0
    python-gssapi-1.2.0-2.el7.x86_64
    
    
Required settings 
------------------
наполнение словаря с настройками, если используется функция парсинга конфига, параметр ссылки на функцию должен 
быть добавлен в словарь в мануальном режиме

    DELIVERY_MODE - опция доставка RabbitMQ
    RABBITMQ_HOST
    RABBITMQ_PORT
    HEARTBEAT_INTERVAL - 600
    BLOCKED_CONNECTION_TIMEOUT - 300
    QUEUE_NAME - наименование очереди для прослушки
    USE_GSS_API - 1 использовать 0 неиспользовать
    RABBITMQ_SPS - GSS SPS раббита 
    PRINCIPAL - принципал
    RABBIT_COMMON_USER - пользователь (если не используем gssapi) 
    RABBIT_COMMON_PASSWORD - пароль (если не используем gssapi)
    HANDLER_LINK - ссылка на функцию обработчик сообщения для прослушки
    LOG_NAME - имя лога    