# -*- coding: utf-8 -*-
from sender import rabbit_send, parse_conf


CONF_FILE = '/home/pavel/conf_conf.conf'
QUEUE_NAME = 'msg'


def send():
    msg = {
          "tps_id": "1234556699999999901230005",
          "tps_type": "test_job",
          "tps_from": "Отправитель (источник сообщения)",
          "tps_to": "Получатель сообщения",
          "tps_reply_to": "Наименование очереди для ответа",
          "tps_date_send": "Время порождения сообщения задачей",
          "tps_date_recv": "Время завершения выполнения задачи агентом",
          "tps_result": "Результат выполнения задачи",
          "tps_body": {
            "ltps_time_out": "30",
            "ltps_cmd": "",
            "ltps_files": [
              {
                "name": "log_txt_file.txt ",
                "alias": "log_txt_file",
                "data": "0KLRgNC10LHQvtCy0LDQvdC40Y86CgotINGD0LLQtdGA0LXQvdC90L7QtSDQt9C90LDQvdC40LUgUHl0aG9uIDIKLSDQt9C90LDQvdC40Y8g0LDQu9Cz0L7RgNC40YLQvNC+0LIg0Lgg0YHRgtGA0YPQutGC0YPRgCDQtNCw0L3QvdGL0YUKLSDQstC70LDQtNC10L3QuNC1INCe0KEgR05VL0xpbnV4Ci0g0L7Qv9GL0YIg0YDQsNCx0L7RgtGLINGBINC70Y7QsdC+0LkgU1FMINCx0LDQt9C+0Lkg0LTQsNC90L3Ri9GFCi0g0L7RgtCy0LXRgtGB0YLQstC10L3QvdC+0YHRgtGMINC4INCw0LrQutGD0YDQsNGC0L3QvtGB0YLRjCwg0LAg0YLQsNC6INC20LUg0YPQvNC10L3QuNC1INGC0LXRgdGC0LjRgNC+0LLQsNGC0Ywg0YHQstC+0Lkg0LrQvtC0INC4INGA0LDQsdC+0YLQsNGC0Ywg0YEg0YfRg9C20LjQvAotINC+0L/Ri9GCINGA0LDQsdC+0YLRiyDRgSBnaXQKCtCR0YPQtNC10YIg0L/RgNC10LjQvNGD0YnQtdGB0YLQstC+0Lw6CgotINC/0L7QvdC40LzQsNC90LjQtSDQv9GA0LjQvdGG0LjQv9C+0LIg0YDQsNCx0L7RgtGLIFdlYiDQv9GA0LjQu9C+0LbQtdC90LjQuQotINC+0L/Ri9GCINGA0LDQsdC+0YLRiyDRgSBQeXRob24gMwotINC+0L/Ri9GCINGA0LDQsdC+0YLRiyDQvdCw0LPRgNGD0LbQtdC90L3Ri9C80Lgg0JHQlAotINC+0L/Ri9GCINGA0LDQsdC+0YLRiyDRgSBEamFuZ28g0LggRFJGCi0g0L7Qv9GL0YIg0YDQsNCx0L7RgtGLINGBIFBvc3RncmVTUUwsIENlbGVyeSDQuCBSYWJiaXRNUQotINC90LDQu9C40YfQuNC1INC/0YDQvtC10LrRgtC+0LIg0L3QsCBnaXRodWIKCgoKCg=="
              },
            ],
            "ltps_date_start": ""
          }
        }
    conf_dict = parse_conf(CONF_FILE)
    rabbit_send(conf_dict, msg, QUEUE_NAME)


if __name__ == '__main__':
    send()
