# 封装统一的链接管理器

class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        # 添加时间作为版本管理
        path = path + "?ver=" + "2019051901"

        return UrlManager.buildUrl(path)
