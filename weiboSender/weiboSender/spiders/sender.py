import ujson
import re
import warnings
import datetime

from scrapy.http import Request, FormRequest
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str

from weiboSender.items import WeibosenderItem
from weiboSender.settings import REDIS_COOKIE_LIST_KEY
from .redisUtil import get_alive_cookie, add_to_exp_list, add_alive_cookie, add_to_error_list


class SenderSpider(RedisSpider):
    name = 'sender'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    redis_key = "sender:msg"

    send_hrader = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}",
        "Host": "api.weibo.com",
        "Origin": "https://api.weibo.com",
        "Referer": "https://api.weibo.com/chat/",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }

    def make_request_from_data(self, data):
        self.logger.debug("recv data-> {}({})".format(data, type(data)))
        data = ujson.loads(bytes_to_str(data, self.redis_encoding))
        self.logger.debug("trans data-> {}({})".format(data, type(data)))
        url = "https://api.weibo.com/webim/2/direct_messages/new.json"
        cookie = get_alive_cookie()
        data.update({"cookie": cookie})
        print(data)
        return self.make_requests_from_url(url, data)

    def make_requests_from_url(self, url, data):
        cookie_str = data["cookie"]["to_str"].strip()
        cookie_dict = data["cookie"]["to_dict"]
        header = self.send_hrader
        header.update({"Cookie": cookie_str})
        return FormRequest(url,
                           meta=data,
                           dont_filter=True,
                           headers=header,
                           formdata={
                               "text": data["msg"],
                               "uid": data["uid"],
                               "extensions": '{"clientid":""}',
                               "is_encoded": "0",
                               "decodetime": "1",
                               "source": "209678993",
                           },
                           cookies=cookie_dict,
                           callback=self.parse)

    def parse(self, response):
        # print("response.request->", response.request.headers)
        # self.logger.debug("response.body-> {}\n{}".format(response.body, type(response.body)))
        # print(response.status)
        rsp_meta = response.meta
        if response.status != 200:
            ct = None
            try:
                ct = response.body
            except BaseException as e:
                print(e)
            add_to_error_list(response.meta["cookie"]["uid"], "{}-{}-{}".format(response.status, rsp_meta["uid"], ct))
            return
        rsp_data = ujson.loads(response.body)

        self.logger.info("send to {}, ret: {}".format(rsp_meta["uid"], rsp_data))
        item = WeibosenderItem()
        item["uid"] = rsp_meta["uid"]
        item["msg"] = rsp_meta["msg"]
        item["ret"] = rsp_data.get("sender_id", -1)
        item["create_time"] = datetime.datetime.now()
        yield item
