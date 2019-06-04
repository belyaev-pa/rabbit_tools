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
    # conf_dict - словарь с настройками необходимые параметры указаны в разделе Required settings
    # msg - словарь сообщения 
    # queue_name - имя очереди
    
    
    # парсинг конфига
    rabbit_tools.sender.parse_conf(conf_file_path)
    # conf_file_path - строка содержащая путь до конфигурационного файла
    


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
    
Message format
---------------
    
    {
      "Формат сообщения ТПС": [
        {
          "tps_id": "Идентификатор сообщения",
          "tps_type": "Тип сообщения",
          "tps_from": "Имя отправителя",
          "tps_to": "Имя получателя",
          "tps_reply_to": "Имя получателя квитанции",
          "tps_date_send": "Время отправки",
          "tps_date_recv": "Время получения сообщения",
          "tps_result": "Результат передачи сообщения",
          "tps_options": "Cервисные данные",
          "tps_body": "Тело сообщения"
        }
      ],
      "Формат сообщения ЛТПС": [
        {
          "tps_id": "ID задачи породившей сообщение",
          "tps_type": "Тип сообщения, определяющий какую функцию вызывать",
          "tps_from": "Отправитель (источник сообщения)",
          "tps_to": "Получатель сообщения",
          "tps_reply_to": "Наименование очереди для ответа",
          "tps_date_send": "Время порождения сообщения задачей",
          "tps_date_recv": "Время завершения выполнения задачи агентом",
          "tps_result": "Результат выполнения задачи",
          "tps_body": {
            "ltps_time_out": "таймаут выполнения задачи (сколько ждать)",
            "ltps_cmd": "комманды для выполнения на удаленном агенте",
            "ltps_files": [
              "файлы сообщения или лог ошибки",
              {
                "name": "file1.txt ",
                "alias": "псевдоним файла, для вставки в cmd команды",
                "data": "data file1 in base64"
              },
              {
                "name": "file2.txt",
                "alias": "псевдоним файла, для вставки в cmd команды",
                "data": "data file2 in base64"
              }
            ],
            "ltps_date_start": "время начала выполнения задачи агентом"
          }
        }
      ]
    }

