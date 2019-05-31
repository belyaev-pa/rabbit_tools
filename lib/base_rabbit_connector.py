# -*- coding: utf-8 -*-
import pika
import kerberos


class BaseRabbitMQ(object):
    """
    Контекстный менеджер
    Базовый класс для соединения с RabbitMQ сервером содержит функции:
    connect: для соединения с сервером
    get_settings: для получения настроек из словаря настроек
    """

    def __init__(self, conf_dict):
        """
        пример файла ..exmaple.conf
        :param conf_dict: словарь с настроечными данными
        connect to rabbitmq
        NOTE: prefetch is set to 1 here for test to keep the number of threads created
        to a reasonable amount. We can to test with different prefetch values
        to find which one provides the best performance and usability for your solution

        :return: None (void)
        """
        self.conf_dict = conf_dict
        self.params = pika.ConnectionParameters(
            host=self.get_settings('rabbitmq_host'),
            port=self.get_settings('rabbitmq_port'),
            credentials=pika.credentials.PlainCredentials(self.principal, self.token),
            heartbeat_interval=int(self.get_settings('heartbeat_interval')),
            blocked_connection_timeout=int(self.get_settings('blocked_connection_timeout')),
        )
        self.connection = pika.BlockingConnection(
            parameters=self.params,
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(
            queue=self.get_settings('queue_name'),
            durable=True,
            exclusive=False,
            auto_delete=False,
        )
        self.channel.basic_qos(prefetch_count=1)

    def __enter__(self):
        """
        Необходимые "магические методы" для реалзации функционала with
        Использование:
        with RabbitMQSender() as sender_obj:
            # use sender_obj (используем объект тут)
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Необходимые "магические методы" для реалзации функционала with
        :param exc_type:
        :param exc_value:
        :param traceback:
        :return:
        """
        self.connection.close()

    def get_settings(self, setting):
        if type(self.conf_dict) is not dict:
            raise AttributeError('conf_dict must be a dict.')
        try:
            prop = self.conf_dict[setting]
        except KeyError:
            raise KeyError("Can`t find {0} in provided config dictionary".format(setting))
        return prop

    @property
    def principal(self):
        """
        не будет участвовать в аутентификации поэтому может быть любым
        :return: principal пользователя
        """
        if int(self.get_settings('use_gss_api')):
            return self.get_settings('principal')
        else:
            return self.get_settings('rabbit_common_user')

    @property
    def token(self):
        """
        для передачи в поле пароль GSS токена
        :return: GSSAPI token (либо пароль в тестовой среде)
        """
        if int(self.get_settings('use_gss_api')):
            result, context = kerberos.authGSSClientInit(self.get_settings('rabbitmq_sps'),
                                                         gssflags=kerberos.GSS_C_SEQUENCE_FLAG,
                                                         principal=self.get_settings('principal'))
            _result = kerberos.authGSSClientStep(context, '')
            return kerberos.authGSSClientResponse(context)
        else:
            return self.get_settings('rabbit_common_password')
