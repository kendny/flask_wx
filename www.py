"""
http模块相关初始化, 对蓝图进行统一管理
"""
from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.account.Account import route_account
from web.controllers.finance.Finance import route_finance
from web.controllers.member.Member import route_member
from web.controllers.food.Food import route_food
from web.controllers.stat.Stat import route_stat


# 注册蓝图
# 首页
app.register_blueprint(route_index, url_prefix="/")
# 用户
app.register_blueprint(route_user, url_prefix='/user')
# 静态资源
app.register_blueprint(route_static, url_prefix='/static')
# 账户
app.register_blueprint(route_account, url_prefix="/account")
# 财务管理
app.register_blueprint(route_finance, url_prefix="/finance")
# 会员管理
app.register_blueprint(route_member, url_prefix="/member")
# 食物管理
app.register_blueprint(route_food, url_prefix="/food")
# 统计管理
app.register_blueprint(route_stat, url_prefix="/stat")