# 功能
    # 1、日志格式的规范
    # 2、操作的简化
    # 3、日志的分级: DEBUG/INFO/WARN/ERROR

# logging不能帮你做的事情
    # 自动生成你要打印的内容
    # 需要程序员在开发的时候定义好:
        # 在哪些地方需要打印
        # 需要打印什么内容
        # 内容的级别

# logging的使用:
    # 普通配置型 简单的 可定制化差
    # 对象配置型 复杂的 可定制化强

# # 认识日志的分级
# import logging        # 默认debug和info的日志不会打印
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

#----------------------------------------------------------------
#调整默认输出级别
# import logging
# logging.basicConfig(level=logging.DEBUG)    #调整默认输出级别
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

#----------------------------------------------------------------
# 常用初始化配置
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 最核心的矛盾
    # 不能将日志既输出到屏幕，又输出到文件里


# --------------------------------------------------
# 使用logger对象形式来操作日志文件

# 创建一个logger对象
# 创建一个文件管理操作符
# 创建一个屏幕管理操作符

# 创建一个日志输出的格式

# 创建一个文件管理操作符 绑定一个 格式
# 屏幕管理操作符 绑定一个 格式

# logger对象 绑定 文件管理操作符
# logger对象 绑定 屏幕管理操作符

#-------------------------------------
import logging
# 创建一个logger对象
logger = logging.getLogger()

# 创建一个文件管理操作符
fh = logging.FileHandler('logger.log',encoding='utf-8')

# 创建一个屏幕管理操作符
sh = logging.StreamHandler()

# 创建一个日志输出的格式
format1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 给文件管理操作符 绑定一个 格式
fh.setFormatter(format1)

# 给屏幕管理操作符 绑定一个 格式
sh.setFormatter(format1)

logger.setLevel(logging.DEBUG)

# logger对象 绑定 文件管理操作符
logger.addHandler(fh)

# logger对象 绑定 屏幕管理操作符
logger.addHandler(sh)


logger.debug('debug message')
logger.info('普通级别的信息')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')