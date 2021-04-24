import ujson
import re
import warnings

from scrapy.http import Request, FormRequest
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str

from weiboSender.items import WeibosenderItem
from weiboSender.settings import REDIS_COOKIE_LIST_KEY
from .redisUtil import get_def_redis_db

class SenderSpider(RedisSpider):
    name = 'sender'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    redis_key = "sender:msg"

    def make_request_from_data(self, data):
        """Returns a Request instance from data coming from Redis.

        By default, ``data`` is an encoded URL. You can override this method to
        provide your own message decoding.

        Parameters
        ----------
        data : bytes
            Message from redis.

        """
        self.logger.debug("recv data-> {}({})".format(data, type(data)))
        data = ujson.loads(bytes_to_str(data, self.redis_encoding))
        self.logger.debug("trans data-> {}({})".format(data, type(data)))
        url = "https://m.weibo.cn/message/chat?uid={}&name=msgbox".format(data["uid"])

        return self.make_requests_from_url(url, data)

    def make_requests_from_url(self, url, data):
        """ This method is deprecated. """
        warnings.warn(
            "Spider.make_requests_from_url method is deprecated: "
            "it will be removed and not be called by the default "
            "Spider.start_requests method in future Scrapy releases. "
            "Please override Spider.start_requests method instead."
        )
        cookie = {}
        with get_def_redis_db() as db:
            cookie = db.lpop_dict(REDIS_COOKIE_LIST_KEY)
            db.rpush_dict(REDIS_COOKIE_LIST_KEY, cookie)
        self.logger.info("get cookie from redis: {}".format(cookie))
        data.update({
            "cookie": cookie
        })
        return Request(url, method="GET", meta=data, dont_filter=True, headers={
            ':authority': 'm.weibo.cn',
            ':method': 'GET',
            ':path': '/message/chat?uid={}&name=msgbox'.format(data["uid"]),
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': 1,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        }, cookies=cookie, callback=self.parse)

    def parse(self, response):
        """
        获取token
        """
        # print("response.request->", response.request.headers)
        # self.logger.debug("response.body-> {}\n{}".format(response.body, type(response.body)))
        response_body = response.body.decode("utf-8")
        match_ret = re.findall("st: '(.*?)',", response_body)
        self.logger.debug("match_ret-> {}".format(match_ret))
        rmeta = response.meta
        cookie = rmeta["cookie"]
        cookie.update({
            "XSRF-TOKEN": match_ret[0]
        })

        if len(match_ret) == 1:
            url = "https://m.weibo.cn/api/chat/send"
            yield FormRequest(url, formdata={
                "content": response.meta["msg"],
                "uid": response.meta["uid"],
                "st": match_ret[0],
                "_spr": "screen:1920x1080",
            }, cookies=cookie, meta={
                "uid": response.meta["uid"],
                "msg": response.meta["msg"],
            }, callback=self.send_callback, dont_filter=True)

    def send_callback(self, response):
        data = ujson.loads(response.body)
        self.logger.debug("callback-> {}".format(data))
        item = WeibosenderItem()
        item["uid"] = response.meta["uid"]
        item["msg"] = response.meta["msg"]
        item["ret"] = data["ok"]
        yield item
