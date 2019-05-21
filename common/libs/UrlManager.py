# 封装统一的链接管理器
import time
from application import app


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        """处理静态资源"""
        release_version = app.config.get("RELEASE_VERSION")
        # 添加时间作为版本管理
        ver = "%s" % (int(time.time())) if not release_version else release_version
        path = "/static" + path + "?ver=" + ver

        return UrlManager.buildUrl(path)

    @staticmethod
    def buildImageUrl(path):
        """处理图片资源"""
        pass
