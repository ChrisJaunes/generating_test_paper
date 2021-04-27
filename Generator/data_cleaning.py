import pandas as pd
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def data_cleaning(path) -> pd.DataFrame:
    a = pd.read_excel(path, sheet_name=0)
    b = pd.read_excel(path, sheet_name=1)
    c = pd.read_excel(path, sheet_name=2)
    # print(a, type(a))
    # print(b, type(b))
    # print(c, type(c))
    # 便于查找题目在原始文件中的序号
    a["题型序号"] = range(4, len(a)+4)
    b["题型序号"] = range(3, len(b)+3)
    c["题型序号"] = range(3, len(c)+3)
    # 由于存在重复的题目，因此对于完全相同的题目进行去重处理，相同题目和选项只保留一个
    # print(a.head())
    # print(b.head())
    # print(c.head(50))
    a.drop_duplicates(subset=[r"题干", r"选择"], keep='first', inplace=True)
    b.drop_duplicates(subset=[r"题干", r"选择"], keep='first', inplace=True)
    c.drop_duplicates(subset=[r"题干", r"选择"], keep='first', inplace=True)
    # print(a.shape)
    # print(b.shape)
    # print(c.shape)
    # 表连接
    tab = pd.concat([a, b, c])

    # print(tab.shape)
    # print(set(list(tab[r"对应的知识点"])))
    # 由于各个来源的知识点不同，对其进行标准化处理
    type_change = {
        "分布式信息交互": "分布式架构-中级",
        "Spring中的Bean": "other",
        "权限修饰符": "Java-初级",
        "MVC设计模式": "other",
        "线程": "Java-初级",
        "面向对象": "Java-初级",
        "反射": "Java-中级",
        "http": "网络原理-中级",
        "spring": "other",
        "构造方法": "Java-初级",
        "HTML": "other",
        "Spring Boot原理分析": "other",
        "Spring MVC数据绑定": "other",
        "认识Vue，理解Vue实例": "other",
        "JAVA编程思想": "Java-初级",
        "AOP": "other",
        "springmvc的使用": "other",
        "数组引用": "Java-初级",
        "JSP页面": "other",
        "vue基础": "other",
        "MyBatis配置文件": "other",
        "类的关系": "Java-初级",
        "语法结构": "Java-初级",
        "数据库设计范式": "数据库-中级",
        "web前端服务器Nginx": "other",
        "面向对象编程": "Java-初级",
        "vue输出": "other",
        "优化分布式sql": "数据库-中级",
        "servelt": "other",
        "servlet生命周期": "other",
        "Thymeleaf/FreeMarker模板引擎": "other",
        "Spring中实例化Bean": "other",
        "静态结构": "other",
        "网络编程": "网络编程-初级",
        "Redis事务机制": "other",
        "git的概念": "other",
        "Java基础语法": "Java-初级",
        "JDBC核心API": "数据库-初级",
        "CSS基础": "other",
        "MySQL数据库": "数据库-初级",
        "vue生命周期": "other",
        "IO流": "Java-初级",
        "输出语句": "Java-初级",
        "多线程": "Java-初级",
        "Java中多态": "Java-初级",
        "vue属性": "other",
        "StringBuffer类": "Java-初级",
        "SSM整合": "other",
        "jdbc": "数据库-中级",
        "SpringMVC框架": "other",
        "FILE类": "Java-中级",
        "JAR包": "Java-中级",
        "Git的使用": "other",
        "vue导航钩子": "other",
        "vue双向绑定": "other",
        "Maven的使用": "Java-中级",
        "MVC模式": "Java-中级",
        "HTML基础": "other",
        "MyBatis配置文件中": "other",
        "设计模式": "Java-中级",
        "final关键字": "Java-初级",
        "String类": "Java-初级",
        "Linux的知识点": "操作系统-初级",
        "Servlet的生命周期": "other",
        "SpringMVC基础框架": "other",
        "do-while循环": "Java-初级",
        "nginx和apache的区别": "other",
        "Spring框架": "other",
        "dubbo与springcloud的区别": "other",
        "Jquery选择器": "other",
        "二进制": "Java-初级",
        "JDBC原理": "数据库-中级",
        "vue钩子函数": "other",
        "文件操作": "Java-初级",
        "B/S服务器开发": "网络编程-中级",
        "web": "网络编程-初级",
        "异常": "Java-初级",
        "常用API": "Java-初级",
        "Java超类": "Java-初级",
        "JSP语法基础": "other",
        "java基础语法": "Java-初级",
        "会话状态": "网络原理-中级",
        "tomcat": "other",
        "SERVLET请求": "other",
        "JVM": "Java-中级",
        "mybatis的使用": "other",
        "数据库": "数据库-初级",
        "运算符号": "Java-初级",
        "继承关系": "Java-初级",
        "Spring": "other",
        "分布式系统": "分布式架构-中级",
        "JavaWeb": "other",
        "Spring基础框架": "other",
        "数据类型": "Java-初级",
        "MyBatis的更新操作": "other",
        "nginx状态码": "other",
        "spring cloud概述，服务注册与服务发现": "other",
        "Spring AOP": "other",
        "MapperFactoryBean": "other",
        "nginx请求匹配location": "other",
        "分支结构": "Java-初级",
        "session": "网络原理-中级",
        "JAVASE": "Java-初级",
        "基于XML方式的声明式事务管理配置文件": "other",
        "数据结构": "Java-初级",
        "变量定义": "Java-初级",
        "数组": "Java-初级",
        "JdbcTemplate": "数据库-中级",
        "Java线程": "Java-初级",
        "事务管理方式": "other",
        "super关键字": "Java-初级",
        "MyBatis的删除操作": "other",
        "servlet初始化": "other",
        "Spring中Bean的作用域": "other",
        "接口定义": "other",
        "Linux基础": "操作系统-初级",
        "异常处理": "Java-初级",
        "COOKIE": "网络原理-初级",
        "maven的概念": "Java-中级",
        "服务注册中心Zookeeper": "分布式架构",
        "vueDOM使用": "other",
        "Redis": "数据库-中级",
        "xml": "other",
        "@RequestParam注解": "other",
        "MyBatis": "other",
        "JAVA语言基础": "Java-初级",
        "多重循环": "Java-初级",
        "Redis命令": "数据库-中级",
        "JDBC编程": "数据库-中级",
        "Spring MVC": "other",
        "filter": "other",
        "Liunx指令操作": "操作系统-初级",
        "SE进阶": "Java-初级",
        "集合": "Java-初级",
        "Servlet": "other",
        "拦截器": "other",
        "网络协议": "网络原理-初级",
        "MySql基础": "数据库-初级",
        "请求响应": "other",
        "Linux的使用": "操作系统-初级",
        "JSP脚本": "other",
        "Cookie会话技术": "网络原理-初级",
        "XML讲解": "other",
        "javaweb": "other",
        "MyBatis与Spring框架的整合": "other",
        "框架": "other",
        "Redis数据类型和基本操作": "数据库-中级",
        "微服务框架Dubbo": "other",
        "Mybatis": "other",
        "mybatis": "other",
        "类结构": "Java-初级",
        "处理请求": "other",
        "线程调用": "Java-初级",
        "this关键字": "Java-初级",
        "jsp": "other",
        "SQL高级查询": "数据库-初级",
        "网路编程": "网络原理-初级",
        "spark部署": "other",
        "Thread类": "Java-初级",
        "OOP": "Java-初级",
        "get": "网络原理-初级",
        "数据库中多表之间关联": "数据库-初级",
        "vue动态路由": "other",
        "TCP协议": "网络原理-初级",
        "主流框架": "other",
        "Spring 4.3": "other",
        "JSP对象": "other",
        "JAVASE基础": "Java-初级",
        "Servlet3.0基础": "other",
        "预编译": "Java-初级",
        "JSP语法基础与运行原理": "other",
        "Object类": "Java-初级",
        "Spring事务管理及核心接口": "other",
        "IO": "Java-初级",
        "JSP": "other",
        "表达式标签": "other",
        "编译原理": "other",
        "JSTL标签库": "other",
        "spring的使用": "other",
        "React框架简介": "other",
        "vue路由跳转": "other",
        "SSM基本框架": "other",
        "java基础": "Java基础",
        "HTTP请求方法": "网络原理-初级",
        "编程基础": "Java-初级",
        "JavaScript": "other",
        "Java基础": "Java-初级",
        "分布式IO": "分布式架构-中级",
        "servlet": "other",
        "update()方法描述": "数据库-初级",
        "Ajax技术详解": "other",
        "多线程和并发编程": "Java-中级",
        "容器作业": "Java-初级",
        "类和对象": "Java-初级",
        "数据库原理": "数据库-初级",
        "Spring配置文件": "other",
        "初识java作业": "Java-中级",
        "Servlet技术详解": "other",
        "JDBC基础编程": "数据库-初级",
        "DDL": "数据库-初级",
        "Spring 框架": "other",
        "日期类": "Java-初级",
        "多态": "Java-初级",
        "分布式事务": "数据库-初级",
        "反射机制": "Java-初级",
        "dubbo连接方式": "other",
        "MySQL数据库的使用": "数据库-初级",
        "Spring AOP常用术语": "other",
        "测试": "Java-高级",
        "Servlet的工作原理": "other",
        "Spring的核心容器": "other",
        "数据库编程和设计": "数据库-初级",
        "springmvc": "other",
        "Spring JDBC": "other",
        "css": "other",
        "抽象类+接口+内部类": "Java-初级",
        "nginx安全加固": "other",
        "关系型数据库": "数据库-初级",
        "SSM": "other",
        "选择语句+循环语句": "Java-初级",
        "TransactionDefinition接口": "other",
        "MyBaits配置文件": "other",
        "SQL语言": "数据库-中级",
        "Spring MVC中实现文件上传下载": "other",
        "Linux": "操作系统-初级",
        "shiro": "other",
        "MySql数据库": "数据库-中级",
        "JavaScript语言": "other",
        "内部类": "Java-初级",
        "HTML+CSS": "other",
        "mybatis的概念": "other",
        "session会话技术": "网络原理-中级",
        "分布式锁": "分布式架构-中级",
        "多重循环+方法": "Java-初级",
        "Java接口": "Java-初级",
        "vue": "网络编程-中级",
        "Spring MVC的配置文件": "other",
        "反射技术": "Java-初级",
        "BOM和DOM": "other",
        "SpringMVC": "网络编程-中级",
        "Spring的概念": "网络编程-中级",
        "Nginx特性": "other",
        "Mybatis框架": "other",
        "常用包": "Java-初级",
        "cookie": "网络原理-中级",
        "zookeeper": "分布式架构-中级",
        "运算符": "Java-初级",
        "Servlet工作原理": "网络编程-中级",
        "数据类型和运算符": "Java-初级",
        "springboot": "Java-初级",
        "JavaWEB": "other",
        "单节点分布式事务一致性": "分布式架构-中级",
    }
    f = open(r'__cache__\problems_set.yml', 'w', encoding='utf-8')
    print(yaml.safe_dump(type_change, f, allow_unicode=True))

    # for i in set(list(tab[r"对应的知识点"])):
    #     if i not in type_change:
    #         type_change[i] = ""
    # print(type(type_change))
    # for k, v in type_change.items():
    #     print(f' "{k}" : "{v}" , ')

    tab[r"清洗以后的大类知识点"] = tab[r"对应的知识点"].map(type_change)

    # for i in set(list(tab[r"清洗以后的大类知识点"])):
    #     for j in set(list(tab[tab[r"清洗以后的大类知识点"] == i][r"对应的知识点"])):
    #         print(f'| {j} | {len(tab[tab[r"对应的知识点"] == j])} | {dict(tab[tab[r"对应的知识点"] == j].groupby("题型").size())} | {dict(tab[tab[r"对应的知识点"] == j].groupby("难度").size())}')
    #     print(f'| {i} | {len(tab[tab[r"清洗以后的大类知识点"] == i])} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("题型").size())} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("难度").size())}')

    # i = "Java基础"
    # for j in set(list(tab[tab[r"清洗以后的大类知识点"] == i][r"对应的知识点"])):
    #     print(f'| {j} | {len(tab[tab[r"对应的知识点"] == j])} | {dict(tab[tab[r"对应的知识点"] == j].groupby("题型").size())} | {dict(tab[tab[r"对应的知识点"] == j].groupby("难度").size())}')
    # print(f'| {i} | {len(tab[tab[r"清洗以后的大类知识点"] == i])} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("题型").size())} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("难度").size())}')
    #

    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).size())
    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).get_group(("网络编程", "网络编程", "单选题")))

    print(len(tab[tab[r"清洗以后的大类知识点"] == "网络编程"]))

    # for i in set(list(c[r"清洗以后的大类知识点"])):
    #     if isinstance(i, float): continue
    #     print((i, len(c[c[r"清洗以后的大类知识点"] == i])))
    #     c[c[r"清洗以后的大类知识点"] == i].to_csv(i + ".csv", encoding="utf8")
    # for i in set(list(c[r"对应的知识点"])):
    #     print("'{0}':'',".format(i))
    print(tab[tab[r"对应的知识点"] == "事务管理方式"].values)

    return tab
