import pandas as pd


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
        "分布式信息交互": "other",
        "Spring中的Bean": "other",
        "权限修饰符": "Java基础",
        "MVC设计模式": "other",
        "线程": "Java基础",
        "面向对象": "Java基础",
        "反射": "Java基础",
        "http": "网络编程",
        "spring": "other",
        "构造方法": "Java基础",
        "HTML": "网络编程",
        "Spring Boot原理分析": "other",
        "Spring MVC数据绑定": "other",
        "认识Vue，理解Vue实例": "网络编程",
        "JAVA编程思想": "Java基础",
        "AOP": "other",
        "springmvc的使用": "other",
        "数组引用": "Java基础",
        "JSP页面": "网络编程",
        "vue基础": "网络编程",
        "MyBatis配置文件": "other",
        "类的关系": "Java基础",
        "语法结构": "Java基础",
        "数据库设计范式": "数据库",
        "web前端服务器Nginx": "网络编程",
        "面向对象编程": "Java基础",
        "vue输出": "网络编程",
        "优化分布式sql": "数据库",
        "servelt": "网络编程",
        "servlet生命周期": "网络编程",
        "Thymeleaf/FreeMarker模板引擎": "other",
        "Spring中实例化Bean": "other",
        "静态结构": "other",
        "网络编程": "网络编程",
        "Redis事务机制": "数据库",
        "git的概念": "other",
        "Java基础语法": "Java基础",
        "JDBC核心API": "数据库",
        "CSS基础": "网络编程",
        "MySQL数据库": "数据库",
        "vue生命周期": "网络编程",
        "IO流": "Java基础",
        "输出语句": "Java基础",
        "多线程": "Java基础",
        "Java中多态": "Java基础",
        "vue属性": "网络编程",
        "StringBuffer类": "Java基础",
        "SSM整合": "other",
        "jdbc": "数据库",
        "SpringMVC框架": "other",
        "FILE类": "Java基础",
        "JAR包": "Java基础",
        "Git的使用": "other",
        "vue导航钩子": "网络编程",
        "vue双向绑定": "网络编程",
        "Maven的使用": "Java基础",
        "MVC模式": "other",
        "HTML基础": "网络编程",
        "MyBatis配置文件中": "other",
        "设计模式": "other",
        "final关键字": "Java基础",
        "String类": "Java基础",
        "Linux的知识点": "操作系统",
        "Servlet的生命周期": "网络编程",
        "SpringMVC基础框架": "other",
        "do-while循环": "Java基础",
        "nginx和apache的区别": "网络编程",
        "Spring框架": "other",
        "dubbo与springcloud的区别": "other",
        "Jquery选择器": "other",
        "二进制": "other",
        "JDBC原理": "网络编程",
        "vue钩子函数": "网络编程",
        "文件操作": "Java基础",
        "B/S服务器开发": "网络编程",
        "web": "网络编程",
        "异常": "Java基础",
        "常用API": "other",
        "Java超类": "Java基础",
        "JSP语法基础": "网络编程",
        "java基础语法": "Java基础",
        "会话状态": "网络编程",
        "tomcat": "网络编程",
        "SERVLET请求": "网络编程",
        "JVM": "Java基础",
        "mybatis的使用": "other",
        "数据库": "数据库",
        "运算符号": "Java基础",
        "继承关系": "Java基础",
        "Spring": "other",
        "分布式系统": "other",
        "JavaWeb": "网络编程",
        "Spring基础框架": "other",
        "数据类型": "Java基础",
        "MyBatis的更新操作": "other",
        "nginx状态码": "网络编程",
        "spring cloud概述，服务注册与服务发现": "other",
        "Spring AOP": "other",
        "MapperFactoryBean": "other",
        "nginx请求匹配location": "other",
        "分支结构": "Java基础",
        "session": "网络编程",
        "JAVASE": "Java基础",
        "基于XML方式的声明式事务管理配置文件": "other",
        "数据结构": "Java基础",
        "变量定义": "Java基础",
        "数组": "Java基础",
        "JdbcTemplate": "Java基础",
        "Java线程": "Java基础",
        "事务管理方式": "other",
        "super关键字": "Java基础",
        "MyBatis的删除操作": "other",
        "servlet初始化": "网络编程",
        "Spring中Bean的作用域": "other",
        "接口定义": "other",
        "Linux基础": "操作系统",
        "异常处理": "Java基础",
        "COOKIE": "网络编程",
        "maven的概念": "Java基础",
        "服务注册中心Zookeeper": "other",
        "vueDOM使用": "网络编程",
        "Redis": "数据库",
        "xml": "other",
        "@RequestParam注解": "other",
        "MyBatis": "other",
        "JAVA语言基础": "Java基础",
        "多重循环": "Java基础",
        "Redis命令": "数据库",
        "JDBC编程": "Java基础",
        "Spring MVC": "other",
        "filter": "other",
        "Liunx指令操作": "操作系统",
        "SE进阶": "Java基础",
        "集合": "Java基础",
        "Servlet": "网络编程",
        "拦截器": "网络编程",
        "网络协议": "网络编程",
        "MySql基础": "数据库",
        "请求响应": "网络编程",
        "Linux的使用": "操作系统",
        "JSP脚本": "网络编程",
        "Cookie会话技术": "网络编程",
        "XML讲解": "other",
        "javaweb": "网络编程",
        "MyBatis与Spring框架的整合": "other",
        "框架": "other",
        "Redis数据类型和基本操作": "数据库",
        "微服务框架Dubbo": "other",
        "Mybatis": "other",
        "mybatis": "other",
        "类结构": "Java基础",
        "处理请求": "other",
        "线程调用": "Java基础",
        "this关键字": "Java基础",
        "jsp": "网络编程",
        "SQL高级查询": "数据库",
        "网路编程": "网络编程",
        "spark部署": "网络编程",
        "Thread类": "Java基础",
        "OOP": "Java基础",
        "get": "网络编程",
        "数据库中多表之间关联": "数据库",
        "vue动态路由": "网络编程",
        "TCP协议": "网络编程",
        "主流框架": "other",
        "Spring 4.3": "other",
        "JSP对象": "网络编程",
        "JAVASE基础": "网络编程",
        "Servlet3.0基础": "网络编程",
        "预编译": "Java基础",
        "JSP语法基础与运行原理": "网络编程",
        "Object类": "Java基础",
        "Spring事务管理及核心接口": "other",
        "IO": "Java基础",
        "JSP": "网络编程",
        "表达式标签": "other",
        "编译原理": "other",
        "JSTL标签库": "other",
        "spring的使用": "other",
        "React框架简介": "other",
        "vue路由跳转": "网络编程",
        "SSM基本框架": "other",
        "java基础": "Java基础",
        "HTTP请求方法": "网络编程",
        "编程基础": "Java基础",
        "JavaScript": "网络编程",
        "Java基础": "Java基础",
        "分布式IO": "other",
        "servlet": "网络编程",
        "update()方法描述": "数据库",
        "Ajax技术详解": "other",
        "多线程和并发编程": "Java基础",
        "容器作业": "other",
        "类和对象": "Java基础",
        "数据库原理": "数据库",
        "Spring配置文件": "other",
        "初识java作业": "Java基础",
        "Servlet技术详解": "other",
        "JDBC基础编程": "数据库",
        "DDL": "other",
        "Spring 框架": "other",
        "日期类": "Java基础",
        "多态": "Java基础",
        "分布式事务": "other",
        "反射机制": "Java基础",
        "dubbo连接方式": "other",
        "MySQL数据库的使用": "数据库",
        "Spring AOP常用术语": "other",
        "测试": "other",
        "Servlet的工作原理": "网络编程",
        "Spring的核心容器": "other",
        "数据库编程和设计": "数据库",
        "springmvc": "other",
        "Spring JDBC": "other",
        "css": "网络编程",
        "抽象类+接口+内部类": "Java基础",
        "nginx安全加固": "网络编程",
        "关系型数据库": "数据库",
        "SSM": "other",
        "选择语句+循环语句": "Java基础",
        "TransactionDefinition接口": "other",
        "MyBaits配置文件": "other",
        "SQL语言": "other",
        "Spring MVC中实现文件上传下载": "other",
        "Linux": "操作系统",
        "shiro": "other",
        "MySql数据库": "数据库",
        "JavaScript语言": "网络编程",
        "内部类": "Java基础",
        "HTML+CSS": "网络编程",
        "mybatis的概念": "网络编程",
        "session会话技术": "网络编程",
        "分布式锁": "Java基础",
        "多重循环+方法": "Java基础",
        "Java接口": "Java基础",
        "vue": "网络编程",
        "Spring MVC的配置文件": "other",
        "反射技术": "Java基础",
        "BOM和DOM": "other",
        "SpringMVC": "other",
        "Spring的概念": "other",
        "Nginx特性": "网络编程",
        "Mybatis框架": "other",
        "常用包": "Java基础",
        "cookie": "网络编程",
        "zookeeper": "网络编程",
        "运算符": "Java基础",
        "Servlet工作原理": "网络编程",
        "数据类型和运算符": "Java基础",
        "springboot": "Java基础",
        "JavaWEB": "网络编程",
        "单节点分布式事务一致性": "分布式架构",
    }
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

    i = "Java基础"
    for j in set(list(tab[tab[r"清洗以后的大类知识点"] == i][r"对应的知识点"])):
        print(f'| {j} | {len(tab[tab[r"对应的知识点"] == j])} | {dict(tab[tab[r"对应的知识点"] == j].groupby("题型").size())} | {dict(tab[tab[r"对应的知识点"] == j].groupby("难度").size())}')
    print(f'| {i} | {len(tab[tab[r"清洗以后的大类知识点"] == i])} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("题型").size())} | {dict(tab[tab[r"清洗以后的大类知识点"] == i].groupby("难度").size())}')


    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).size())
    # print(tab.groupby(["清洗以后的大类知识点", "对应的知识点", "题型"]).get_group(("网络编程", "网络编程", "单选题")))

    print(len(tab[tab[r"清洗以后的大类知识点"] == "网络编程"]))

    # for i in set(list(c[r"清洗以后的大类知识点"])):
    #     if isinstance(i, float): continue
    #     print((i, len(c[c[r"清洗以后的大类知识点"] == i])))
    #     c[c[r"清洗以后的大类知识点"] == i].to_csv(i + ".csv", encoding="utf8")
    # for i in set(list(c[r"对应的知识点"])):
    #     print("'{0}':'',".format(i))
    # print(c[c[r"对应的知识点"] == "update()方法描述"].values)

    return tab
