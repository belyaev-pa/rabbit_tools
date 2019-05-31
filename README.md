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

    delivery_mode - опция доставка RabbitMQ (2 - по умолчанию)
    rabbitmq_host
    rabbitmq_port
    heartbeat_interval - 600
    blocked_connection_timeout - 300
    queue_name - наименование очереди для прослушки
    use_gss_api - 1 использовать 0 неиспользовать
    rabbitmq_sps - GSS SPS раббита 
    principal - принципал
    rabbit_common_user - пользователь (если не используем gssapi) 
    rabbit_common_password - пароль (если не используем gssapi)
    handler_link - ссылка на функцию обработчик сообщения для прослушки
    log_name - имя лога    