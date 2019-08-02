# -*- coding: utf-8 -*-
import pika
import json

from python_sz_rabbit_tools.base_rabbit_connector import BaseRabbitMQ


class RabbitMQSender(BaseRabbitMQ):
    """
    Класс необходимо создавать через контекстный менеджер, для его корректного завершения!
    """
    def __init__(self, conf_dict, msg, queue_name):
        """
        необходимые настройки в conf_dict
        REPLY_TO = "reply_queue" название очереди
        RABBITMQ_HOST = '10.128.152.30' (ip адрес rabbit`a должно быть выставлено ansibl`ом)
        RABBITMQ_PORT = 5672 (порт работы рабита default = 5672)
        HEARTBEAT_INTERVAL = 600 (интервал серцебиения раббита)
        BLOCKED_CONNECTION_TIMEOUT = 300 (интервал остановки соединения клентом)
        :param conf_dict: словарь с настройками
        :param msg: словарь сообщения
        :param queue_name: название очереди в которую необходимо положить сообщение
        """
        self.msg = msg
        self.queue_name = queue_name
        super(RabbitMQSender, self).__init__(conf_dict)

    def send(self):
        self.make_message()
        self.rabbit_put()

    def make_message(self):
        """
        формируем json
        :return:
        """
        self.message = json.dumps(self.msg, sort_keys=False, default=str)

    def rabbit_put(self):
        """send message must be called after connect()"""
        self.queue = self.channel.queue_declare(
            queue=self.queue_name,
            durable=True,
            exclusive=False,
            auto_delete=False,
        )
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=self.message,
            properties=pika.BasicProperties(
                delivery_mode=int(self.get_settings('delivery_mode')),  # make message persistent
            )
        )


def rabbit_send(conf_dict, msg, queue_name):
    """
    Функция посылки сообщения в RabbitMQ
    :param conf_dict: словарь настроек
    :param msg: передаваемое сообщение (словарь)
    :param queue_name: название очереди - строка
    :return: void
    """
    with RabbitMQSender(conf_dict, msg, queue_name) as sender_obj:
        sender_obj.send()

