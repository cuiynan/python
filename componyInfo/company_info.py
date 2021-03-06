#
# 这里是完整的工商信息采集代码，不过此程序需要配合代理ip软件使用。
# 问题：1.网站对ip之前没做限制，但是采集了一段时间就被检测到设置了反爬，每个ip只能访问十多次左右就被限制访问。
# 2.网站对请求头的检测识别解决：
# 1.配合代理ip软件（风讯代理）设置自动切换ip时间，执行爬虫程序。
# 2.中间件设置随机user - agent采集结果：正常采集速度一天大概采集1万条数据左右。
# 问题：切换ip会造成程序断网一些字段遗漏解决（设置的有唯一索引避免重复采集，多次执行爬虫）company_info.py
# -*- coding: utf-8 -*-
import scrapy
from ZJPL.items import QichachaItem

class CompanyInfoSpider(scrapy.Spider):
    name = 'company_info'
    allowed_domains = ['m.qichacha.com']
    start_urls = ['https://m.qichacha.com/search?']
    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
        "TABLE": 'qichacha',
        "MYSQL_DB": 'company_info',
        "ITEM_PIPELINES": {'ZJPL.pipelines.MysqlPipeline': 320},
        "DOWNLOADER_MIDDLEWARES": {
            'ZJPL.middlewares.RandomUseragentMiddleware': 500,
        },
    }

    def start_requests(self):
        company_list = ['托克智能仪表(成都)有限公司', '福州富企王牌感应设备有限公司', '四川宏森发钢铁有限公司', '宁波标兵涂料有限公司深圳分公司', '成都嘉盾电气有限公司',
                        '南宁市桂塑塑料制造有限责任公司', '自贡华泰空分科技发展有限公司', '天津太敬机电技术有限公司', '广州华粤管业有限公司成都代理', '上海正泰焊接设备有限公司济南总代理',
                        '广东东鹏陶瓷股份有限公司广州分公司', '中山环宇有限公司阳江办事处', '利达集团北京利达华信电子有限公司江门办事处', '常州市河马塑胶有限公司广州办事处',
                        '广东美涂士涂料河北总代理', '广东原笙管业有限公司', '泊头沃尔特铸铁有限公司', '成都雷克星科冷却设备有限公司', '天津盛辉伟业钢铁贸易有限公司', '金牛区迪龙物资商行',
                        '成都市三清木塑新材料有限公司', '冠珠陶瓷德阳专卖店', '成都四维瓷业有限公司', '四川省宜宾市鸿盛综合贸易有限公司', '南京昆元白水泥厂', '武汉市燃力热力工程公司',
                        '成华区深广洁具经营部', '香港康派化学有限公司泰和总代理', '江苏宇宙焊接材料集团公司', '洛阳石化宏达塑业', '上海中南建筑材料公司', '保定天泽林板业有限公司',
                        '北京通达恒运商贸有限责任公司', '四川同一科技发展有限公司', '苏州三星电子有限公司广州办事处', '石家庄宇泉环保设备有限公司四川办事处', '成都金牛制冷有限公司',
                        '福建省南安市港都水暖器材厂四川销售处', '成都科文保温材料有限公司', '重庆万丰成都建材有限公司', '四川金利商贸有限责任公司', '亚士漆(上海)有限公司成都销售服务中心',
                        '北京市金英利达金属材料有限公司', '北京伟屹恒科技有限公司', '金川越大北京贸易有限公司', '成都丁家艺家居有限公司', '成都市奥浦窗饰经营部', '南京英安特科技实业有限公司',
                        '杭州华兴交通电子标志制造有限公司成都办事处', '长虹木业有限公司', '四川省成都岷江园林有限公司', '石家庄鑫明保温材料厂', '广东桂龙自动化科技有限公司',
                        '人民电器集团成都销售处', '无锡市太湖防腐材料有限公司', '成都景能电器有限责任公司', '成都兴中航制冷设备工程有限公司', '四川省成都市武侯区永发卷帘门窗经营部',
                        '成都美丽居玻璃工艺有限公司', '四川华夏特种玻璃工程有限公司', '成都演益木业厂', '广东省江门市大自然化工有限公司', '高邮市东郊铸管厂', '四川楚北混凝土有限公司',
                        '成都市金牛区豪德建材商贸部', '三立灯饰公司', '潍坊市宏源防水材料有限公司', '广西青龙化学建材有限公司', '成都市鹏达照明工程部', '四川省特丽达实业有限公司',
                        '华亚(东营)塑胶有限公司', '辽宁华冶集团发展有限公司', '四川海顿建材有限公司', '镇江大洋星鑫工程管道有限公司', '青岛路通达塑料机械有限公司', '大理红山水泥有限责公司',
                        '武汉东方玻璃钢制品有限公司', '沈阳德美斯防水堵漏工程有限公司', '广东省佛山市南海圣东涂料有限公司', '哈尔滨鸿海钢材销售有限公司',
                        '哈尔滨益泰数码科技有限公司顾地黑龙江总代理', '中国机械工业成套工程总公司哈尔滨代理', '哈尔滨凯撒管业有限公司', '哈尔滨市东北龙金属材料公司', '广州碧非控制系统有限公司',
                        '重庆世邦五交化有限公司', '沙坪坝区泰瑞木制品厂', '哈尔滨中天宏远锅炉有限公司', '长城橡胶有限公司哈尔滨分公司', '哈尔滨三川给水设备制造有限公司',
                        '哈尔滨鸿盛建筑材料制造股份有限公司', '哈尔滨远东星空科技有限公司', '紫荆花制漆上海有限公司哈尔滨办事处', '大庆科尔达电热仪表有限公司', '哈尔滨瑞鑫洋新能源科技有限公司',
                        '重庆东海水处理设备有限公司', '上海胜华电缆(集团)有限公司重庆办事处', '圣象地板哈尔滨分公司', '哈尔滨天韵玻璃装饰制品厂', '黑龙江奥德尔集团苗木基地', '黑龙江睿艳苗木',
                        '重庆市华特通信设备有限责任公司', '南昌县佰嘉涂料厂', '重庆普永科技发展有限公司', '哈尔滨居安消防设备经销有限公司', '黑龙江德盟塑胶机械有限公司',
                        '哈尔滨长龙科技有限公司', '赛博陶瓷有限公司', '江西省奉新县上富镇森辉苗木基地', '岳阳市中安消防水暖器材经营部', '湖南桃花江实业有限公司',
                        '江西省吉安市永安交通设施有限公司', '长沙凯美家晾衣架厂', '南昌市青云谱惠军安消防器材经营中心', '衡阳威盾科贸有限公司', '广丰县景山实业有限公司',
                        '衡阳市雁峰建文保温材料厂', '南昌安居科技有限公司', '赣州百施得新型建材有限公司', '湖北首云建筑防水工程有限公司南昌分公司', '湖南顺天混凝土有限公司',
                        '江西鑫隆泰建材工业有限公司', '福建振云塑业股份有限公司江西总代理', '南昌市浩浪体育用品商行', '江西瑞健康体设备有限公司', '浙江中捷管业有限公司江西销售中心',
                        '江西省润邦化工有限责任公司', '红太阳洁具湖南总代理', '美标洁具湖南地区总经销', '南康伟业木工厂', '上高县德燕塑胶制品厂', '江西芸林木业有限公司',
                        '安华陶瓷洁具有限公司长沙总经销', '江西玉龙防水材料有限公司', '苏州特瑞斯智能科技有限公司', '贝谷科技股份有限公司', '南昌天绘测绘仪器有限公司',
                        '江西新东元物资有限公司景德镇分公司', '江西新东元物资有限公司', '浙江佑安高科江西办事处', '上饶市建文电气成套有限公司', '江西硕博科技有限公司南康分公司',
                        '迪古里拉(北京)涂料有限公司', '佐敦涂料(张家港)有限公司', '南昌博大装饰材料总汇', '江西萍乡玉兰墙纸旗舰店', '欧雅壁纸樟树专卖店', '黄石市天安科技有限公司',
                        '武汉市洪山区沐氏消防器材经营部', '绵阳久信玻璃有限公司', '湖北武穴市兴雨泵业有限责任公司', '成都飞雕电器销售有限公司', '武汉康润环保科技有限公司',
                        '武汉华朗科贸有限公司', '武汉昊特流体设备有限公司', '武汉斯华美工业技术有限公司', '贵州利源木业有限公司', '铜仁宏绿林产品加工有限公司', '台江县木材公司胶合板厂',
                        '新余市君元贸易有限公司', '贵阳市黔灵福热能设备有限公司', '贵州永发商贸有限公司第一分公司', '贵阳安吉尔电器有限公司', '九江现代良友实业有限公司',
                        '江西省南昌市新发展建材有限公司', '江西省电力煤气设备安装公司', '沈阳金德管业集团贵阳分公司', '贵州省交通物资总公司', '贵州瑞华塑胶有限公司', '福泉星星套装门总代理',
                        '黑龙江哈尔滨市天净管业销售公司', '黔西南州共青林场有限公司册亨活立木分公司', '汉高粘合剂有限公司湖北分公司', '贵阳南明嘉鑫装饰材料经营部', '湖北双龙建材有限公司',
                        '武汉铂海电气有限公司', '武汉华天世纪科技发展有限公司', '绿精灵地板株洲专卖店', '武汉市涂料大全建筑公司', '贵州理想美标识工程有限公司', '湖南湘君竹业有限公司',
                        '贵阳鞑健慧教玩具厂', '贵阳瑞山金属丝网有限公司', '新余市来威漆(腾达化工)营销中心', '贵阳世纪星文泰健身器材厂', '贵阳云岩锡建仪器经营部', '贵州西普天辰测绘公司',
                        '宜昌远见建材经营部', '航标卫浴武汉专卖店', '哈尔滨市峰华全钢防静电地板有限公司', '生活家地板哈尔滨总代理', '武汉市三金陶瓷股份有限公司',
                        '哈尔滨北扬信达科技开发有限公司', '哈尔滨晟宇科技开发有限公司', '崇州市元通镇天泽物质经营部', '黑龙江瑟科赛斯科技有限公司', '上海品奥涂料有限公司武汉分公司',
                        '江口县元利商贸有限公司', '贵阳傲世达洁具有限公司', '贵州振中玻璃有限公司营销部', '贵阳协和商贸有限责任公司', '贵阳广禾建材有限公司', '鑫泰电缆桥架公司',
                        '遵义和成卫浴销售中心', '贵阳顺沣建材名店', '平安家园五金商行', '宏兴石料厂', '美高壁纸贵州省总代理', '瑞典摩曼壁纸贵州专卖店', '贵阳天豪装饰材料有限公司',
                        '上海汇丽地板贵州总代理', '威海山花华宝地毯有限公司武汉分公司', '武汉新士林电气设备有限公司', '武汉虹宇电力机电设备有限公司', '哈尔滨威逊机械连接件经销有限责任公司',
                        '阿城继电器股份有限公司', '大庆市新庆工管件制造有限责任公司', '贵州成丰达电缆桥架有限公司', '贵阳福控自动化科技有限公司', '贵州长佳电器设备有限公司',
                        '哈尔滨亿斯特科技开发有限公司', '筑巢装饰公司贵州分公司', '贵州中岩保温工程有限公司', '万通防水材料有限公司贵州分公司', '小雪家具有限公司\xa0',
                        '黑龙江鑫龙钢化玻璃厂', '湘江陶瓷经销部', '奥米茄陶瓷大庆专卖', '武汉泰欧亚建筑材料有限公司', '贵阳小河广达纳米涂料厂', '贵州聚达电子科技有限公司',
                        '贵州天安消防工贸有限公司', '大庆立邦代理经营部', '武汉旷远电子技术有限公司', '哈尔滨中环科环保节能设备有限公司', '武汉市鑫达不锈钢有限公司', '贵阳新纪物资贸易有限公司',
                        '武汉天格贸易有限公司', '武汉丰澜板业制造有限公司南宁办事处', '上海冠龙阀门机械有限公司广州办事处', '重庆宏漆涂料(集团)有限公司', '重庆瀚龙建材有限公司',
                        '南宁市宝利吉装饰工程有限公司', '自贡市汇东新区汇积电气经营部', '广东顾地塑胶股份有限公司', '重庆仁本建材有限公司', '重庆瑞乔建材有限公司',
                        '江西康达竹业集团通贵地板湖北总代理', '美迪亚地板有限公司湖北营销中心', '武汉绿洲木业有限公司', '重庆市沙坪坝区美恒洁具厂', '广西南宁奥力奥金属有限公司',
                        '武汉市东西湖浩宇不锈钢经营部', '广东柔乐电器有限公司成都办事处', '成都市郫县锦信木业厂', '四川省瑞森人造板有限公司', '江汉油田凯达实业有限公司高压泵厂',
                        '武汉华阳新利水处理技术有限公司', '武汉益普水处理设备有限公司', '上海浦旭真空泵制造有限公司', '四川奇立隆饰材连锁有限公司', '重庆益欣建材有限公司',
                        '宜兴市城南环保设备制造厂', '长沙绿精灵地板红星美凯龙旗舰店', '北京宏兴东升防水施工有限公司', '山东康鲁节能设备有限公司', '江西鑫隆泰建材工业有限公司成都办事处',
                        '安平县泰尔利卫浴有限公司', '天津市蓟县京津水泥厂', '北京春来新型环保设备有限公司', '天津兵众混凝土有限公司', '北京欧德汇依木房屋有限公司',
                        '深圳市联泰一帆电子科技有限公司', '大连众恒电力电子有限公司', '四川东泰新材料科技有限公司武汉办事处', '上海天力实业有限公司武汉办事处', '衡阳市雁峰江东吸砂泵厂',
                        '武汉瑞吉尔科技有限公司', '湘西阳峰木业有限公司', '湖南省宇翔木业有限公司', '北京旺泉建业科贸中心', '武汉汉瑞科技发展有限公司', '上海柯耐弗电气四川办事处',
                        '钟祥市顺发木业有限公司', '北京星牌建材有限责任公司武汉分公司', '武汉家盛时代装饰材料有限公司', '哈尔滨盛隆墙体材料有限公司', '广州华懋科技发展有限公司黑龙江分公司',
                        '安徽凯升管业有限公司', '山东鑫丹利物资有限公司', '深圳市安泰君威实业有限公司哈尔滨办事处', '杭州海康威视数字技术股份有限公司成都分公司', '成都市都得利管业有限公司',
                        '广西通利昌物资设备有限责任公司', '云南矗立伟业经贸有限公司', '天津市铸诚景明机械租赁有限公司', '江西联信大市场新发机电有限公司', '张家港市富昶热能设备有限公司',
                        '江西瑞昌市高品质乳胶漆厂', '天津鸿顺意门窗有限公司', '江西省南昌市世纪园林绿化工程有限公司', '哈尔滨市热管锅炉厂', '昆山禾木园艺绿化工程有限公司',
                        '昆明市五华区警群安全器材科技经营部', '武强县精创仪器仪表厂', '北京广建振业空调设备有限公司', '北京千住消防器材有限公司', '神州数码(中国)有限公司',
                        '天津蓬联照明科技有限公司', '北京华隆凯商贸有限公司', '淄博远航建陶有限公司', '菏泽市牡丹区运祥不锈钢制品有限公司', '北京普林森环保科技有限公司',
                        '天津进强钢铁贸易有限公司', '天津市蓟县汇隆森装饰材料厂', '山西汇世天勤保温材料有限公司', '潍坊三华利机械科技有限公司', '沈阳金铠建筑科技股份有限公司',
                        '哈尔滨美江管业有限公司', '大厂回族自治县国宏水泥制品有限公司', '南昌市洪达世家装饰材料有限公司', '景县智龙金属软管加工', '庆云县鑫泰龙机床附件厂',
                        '固安县渠沟占水铁管卡厂', '北京博星得门控科技有限公司', '太原天镁恒信贸易有限公司', '上海通用机电集团', '沧州昕华精密设备有限公司', '石家庄远大环保节能技术开发有限公司',
                        '天津市昊佳电子技术有限公司', '北京市润实盛然园林绿化有限公司', '泊头市驿通汽车配件厂', '北京思创伟业换热设备有限公司', '合肥市顺昌电磁加热科技发展有限公司',
                        '北京广灵精华科技有限公司', '天津乐鑫商贸有限公司', '天津市松立工贸有限公司北京办事处', '石家庄东裕电器厂', '广州大超保温材料有限公司', '雄县亚润塑料制品有限公司',
                        '承德昊远塑料制品有限公司', '轩悦视听有限公司', '济南辰联电子有限公司', '北京慕迪灵翻译有限公司', '天津市金动能源技术有限责任公司', '保定市厚奇新能源科技有限公司',
                        '盐山县中泰体育健身文化用品经销处', '石家庄市太行伟业水泵有限公司', '任丘市佳乐水空调经销处', '中大空调集团有限公司', '北京格瑞那环能技术有限责任公司',
                        '北京市海兴达机电设备销售中心', '北京腾飞世纪星气球有限公司', '南宫市金萧毛毡制品厂', '北京速可达科技有限公司', '北京华宝京安科技发展有限公司',
                        '北京华琪软通技术有限公司', '北京成泰天地科技有限公司', '北京汉和鸿嘉科技有限公司', '北京市兴体良体育用品有限公司', '北京华夏京奥科技有限公司',
                        '北京阳光万通科技有限公司', '唐山市和顺科技有限公司', '上海昀峰仓储设备有限公司', '北京古龙木雕加工厂', '泊头市硕达机械设备有限公司', '北京瑞龙泰装饰材料有限公司',
                        '广州市谦木建筑材料有限公司', '深圳市宝安区公明盛鑫门窗组装经营部', '广东顾地塑胶有限公司', '天津永大晟航商贸有限公司', '秦皇岛顺亨玻璃有限公司',
                        '北京新康建筑门窗有限公司', '北京华凯门窗设计工程有限公司', '北京江南京安建材经销部', '北京市酒仙桥建材装饰市五金中心', '山西太原尖草坪批发市场江龙商行',
                        '扬州天喜塑胶有限公司', '北京阳光创奇体育设施有限公司', '北京畅易达工贸有限公司', '天津市武清区全和地毯机械厂', '南宫恒信毛皮制品有限公司',
                        '北京市希玛保龄球设备有限公司', '北京华海恒辉科技有限公司', '北京市政专用汽车厂', '河北福玉专用汽车有限公司', '广东标光工程材料有限公司', '广宇有机玻璃厂',
                        '广东华润涂料有限公司', '成都五佳恒贸易有限公司', '广东聚源管业实业有限公司', '广州市光阳包装材料有限公司', '佛山市天虹艺术玻璃有限公司', '金达丰五金工具灯饰锁业电器',
                        '深圳是科泰联合集采有限公司', '成都炬烽钢铁有限公司', '佛山市天兴消防器材有限公司', '佛山市埃森塑胶电器有限公司', '北京佳宝兴达智能科技有限公司',
                        '江苏星华机场设施有限公司', '长沙华振供水设备有限公司', '上海星义计算机科技有限公司', '广州市顺大装饰材料有限公司', '广州市花都区金均钢管钢构厂',
                        '泰州市高港区金凌体育器材制造厂', '唐山陶瓷厂成都办事处', '无锡金羊深圳分公司', '益通管道设备厂', '益鑫铝业有限公司', '北京天元汇通建材有限公司',
                        '哈尔滨东邦新型建筑材料有限公司', '恩光防腐瓷业有限公司', '青岛神州防水装备有限公司', '江苏双腾管业有限公司', '宁波兆亿弱电工程有限公司', '深圳市彬源环保设备有限公司',
                        '深圳宝安区联兴木业', '四川盛鑫铝制品有限公司', '中山市古镇希妮照明门市部', '东莞市麦蒂科技有限公司', '东莞市绿王涂料经营部', '欣科嘉元电子通讯设备有限公司',
                        '佛山赛尼洁具有限公司', '惠州市旗龙科技有限公司', '大连星海电器厂', '大连佰适商贸有限公司', '广州市白云泵业集团有限公司大连办事处', '深圳市龙祥康体设施发展有限公司\t',
                        '深圳市桐子园铸造厂', '广州市一苇园林工程有限公司', '深圳市光时代科技发展有限公司', '天津市塘尔斯阀门厂', '大连市建筑防水材料厂', '福隆兴管业有限公司',
                        '抚顺顺大建材厂', '华强页岩烧结砖有限公司', '怡农园艺有限公司', '天虹预制构件厂', '风彩涂料厂', '庆华建业有限公司', '灵玉保温材料厂', '沈阳瑞得涂料厂',
                        '德州东方土工材料股份有限公司', '宏伟彩色水泥制品厂', '上海友力水泵有限公司', '四川兰迪菲尔软包壁纸装饰装修公司', '紫阳建材有限公司', '广东新粤交通投资有限公司',
                        '四川东进节能玻璃有限公司', '广东高丽铝业有限公司南宁分公司', '大连志强管业科技发展有限公司', '丹东灯泡厂', '天津市明生环保工程设备有限公司', '温州市万航电器厂',
                        '温州市龙湾天河贵宾电器厂', '东莞市翔宇金属材料有限公司', '株洲市奇珍家居用品销售部', '长沙市泽诚电器贸易有限公司', '诺美佳电器有限公司', '长沙市成就电子科技有限公司',
                        '长沙科辉电子有限公司', '长沙秉胜电子科技有限公司', '西安鑫淼电子科技有限公司', '天津市江光贸易有限公司', '天津市明浩商贸有限公司', '天津畅坤商贸有限公司',
                        '天津弘道志远商贸有限公司', '天津市津南区国联防火门厂', '天津市隆拓防火设备厂', '天津大统工程公司', '天津市TOTO卫浴有限公司', '天津市万方彩钢板厂',
                        '天津市叶兹化工技术有限公司', '天津水泥厂津泥建材销售中心', '天津吉砼外加剂有限公司', '天津汇佳机电有限公司', '上海康大泵业制造有限公司天津分公司',
                        '成都广运电气工程设备有限公司', '上海敏盛电子有限公司', '沈阳百达识别技术有限公司', '哈尔滨胜利阀门', '哈尔滨电器设备厂有限公司', '哈尔滨市大中五金交电批发部',
                        '哈尔滨同心圆电线电缆有限公司', '广东高丽铝业有限公司成都分公司', '四川省川汇塑胶有限公司', '河北兴利阀门管件制造有限公司成都办事处', '广东美的照明电气制造有限公司成都办',
                        '恒远照明配送中心-飞利浦', '成都永亨塑业有限公司', '恒业国际控股集团西南分公司成都办', '四川蓉诚鑫宏信商贸有限公司', '浙江双环塑胶阀门有限公司成都办',
                        '成都亚盟线缆有限公司', '天津市沃尔特阀门制造有限公司', '天津市六通风机厂', '上海蓝升泵业', '爱优特空气技术(上海)有限公司', '深圳建华宇装饰工程有限公司',
                        '必凯威(北京)建筑材料有限公司', '长沙市芙蓉区晨风办公家具经营部', '温州市龙湾沙城家榜电器厂', '温州国缘电器有限公司', '温州市龙湾天河正鑫电器',
                        '北京宏源兴诚商贸有限公司', '北京兆诺商贸有限公司', '衡华配件厂', '成都市双信管桩有限公司', '成都市金意鑫建材有限公司', '北京美绿华技贸有限公司',
                        '四川金利特不锈钢制造有限公司', '福建省南安市华东石材有限公司成都分公司', '大连远东机电工具有限公司', '南昌华泰硅橡胶制品有限公司', '南昌市青云谱洪都五金标准件中心',
                        '上海传易电子科技有限公司江西分公司', '武汉永翔不锈钢经营部', '武钢集团汉阳机械厂', '北京金隅股份有限公司', '武汉市汉阳区湘源木地板加工厂',
                        '郑州中原应用技术公司南宁分公司', '北京中合天下焊接材料有限公司', '北京金安鑫业五金交电有限责任公司', '北京鹏昭顺展建材经销部', '北京宏亚环奥建材有限公司',
                        '北京晶彩耀华玻璃厂', '北京侨华普路贸易中心', '恒盛绝缘材料经销处', '济南奥强商贸有限公司', '济南东旺经贸有限公司', '济南强联物资公司',
                        '济南市中天组培园艺用品供应中心', '济南忠诚塑料制品有限公司', '济南富安德机电设备有限公司', '贵阳昌威商贸有限公司', '贵阳延通贸易有限公司', '贵阳海森焊接材料有限公司',
                        '贵州发奥迪焊接器材有限公司', '贵阳云岩博陵筛网经营部', '浙江巨力电气有限公司贵州办事处', '贵州友利和贸易有限公司', '贵阳鑫思源环保科技有限公司市场部',
                        '贵阳市南明区伟宏钢木家具厂', '重庆市弘利金属材料商行', '重庆东方良工阀门有限公司', '重庆久诺阀门有限公司', '重庆耐仕阀门有限公司', '天津市润清磁卡技术有限公司',
                        '成源耐火材料有限公司', '重庆迈博广告经营部', '重庆市屋之巧装饰材料有限责任公司', '江西顺发木竹加工有限公司', '新建县新兴木业厂', '南昌市宏宇陶瓷营销中心',
                        '江西联信大市场丰华物资批发部', '南昌力拓阀门机电设备有限公司', '长兴品帝电器有限公司', '江西省益冠建材商贸有限公司', '江西亚立工贸有限公司',
                        '南昌市红谷滩新区水知澳电器店', '南昌市水之良科技设备有限公司', '华明通风设备经营部', '江西省大自然环保通风设备有限公司', '夏氏兄弟风机经营部',
                        '九江科华照明电器实业有限公司', '澳达斯灯饰名品生活馆', '南昌鹿江喷泉喷灌工程有限公司', '南昌市凡客灯饰商行', '南昌市西湖区海博光电产品经营部', '海口龙华磐石石料加工厂',
                        '武汉浙艺环保科技有限公司', '武汉金洋龙建材商贸有限公司', '武汉市洪山区白沙洲建筑工程材料经营部', '武汉市洪山区全顺建筑器材经营部', '武汉三剑照明器材有限公司',
                        '武汉市江汉区双洋液压气动设备商行', '武汉金榜轻工机械设备有限公司', '武汉艾格美居科技有限公司', '湖北仁孚环保工程有限公司', '武汉市文明经济发展有限公司',
                        '武汉市江汉区鸿鹄电器销售部', '武汉祥兴宇电子科技有限公司', '武汉客林化工有限公司', '武汉安顺达装饰材料有限公司', '武汉诺克美佳商贸有限公司',
                        '武汉市江岸区华燕天成办公家具经营部', '武汉市汉阳区华阳办公家具厂', '武汉市江岸区德森家俱厂', '贵阳闽泉贸易有限公司', '武汉市林桂竹木制品有限公司',
                        '武汉市武昌区润禾木材经营部', '武汉市汉阳区普菲特建材商行', '鑫旺彩铝塑钢门窗厂', '武汉友阳家居纺织用品有限公司', '武汉市东西湖金旺胶粘制品厂',
                        '武汉东方钢管贸易有限公司', '海湾安全技术有限公司北京分公司', '海寿管业有限公司西北分公司', '北京和信顺成科技发展有限公司', '北京经纬佑利管道水工设备有限公司',
                        '中科天宇金属材料(北京)有限公司', '北京语信贸业有限公司', '北京振远洋真空科技有限公司', '睿智昊通管道阀门(北京)有限公司', '贵阳市南明区南泉水电物资经营部',
                        '北京昌平腾达玻璃钢厂', '北京天澄玻璃钢有限公司', '北京新宝永昌玻璃钢有限公司', '北京天和雅筑工艺品有限公司', '北京远方动力可再生能源科技发展有限公司',
                        '北京豪伟光业照明电器中心', '北京旺达盛电气有限公司', '北京旭能阳光科技有限公司', '北京宁晖兴业科技有限公司', '北京壹图照明科技发展中心', '北京市宏运钢材有限公司',
                        '北京福海胜源科技有限公司', '南昌高新技术产业开发区昌东飞虎塑胶厂', '济南莱特灯具销售中心', '济南友森达网络技术有限公司', '济南红鹦鹉环保科技有限公司',
                        '山东金丰罗茨鼓风机有限公司', '上海创精泵阀制造有限公司济南分公司', '济南航泰流体设备有限公司', '济南品盛机电设备有限公司', '济南金鼎诺泵业有限公司',
                        '济南金科通经贸有限公司', '济南市槐荫区中大五金制造厂', '济南智胜时代科技有限公司', '山东德屹机电有限公司济南分公司', '天桥区大鹏开山空压机销售服务处',
                        '济南锐博特机械设备有限公司', '济南优耐特斯工业设备有限公司', '济南海威营销服务有限公司', '贵州质真园暖通工程有限公司', '贵阳吉辉空调设备有限公司',
                        '贵阳普洁环保节能技术有限公司', '刚刚网络经营部', '贵州子谦伟业机械技术发展有限公司', '贵州亿科电力电气设备有限公司', '清镇市顺成机械厂', '贵州世纪开元文化科技有限公司',
                        '毕节市磊亿电器经营部', '贵阳永佳机械电器厂', '贵阳丰银商贸有限公司', '贵阳五交化电器网', '贵州独山鑫源矿业有限公司', '成都华塑管业有限公司', '成都国鑫家私',
                        '绵阳市中海特钢有限责任公司', '江油市智达贸易有限公司', '上海太平洋制泵(集团)有限公司成都分公司', '兴文县三川不锈钢水泵有限公司', '重庆乾泉泵阀制造有限公司',
                        '重庆市高新技术产业开发区旭冉机电经营部', '成都兴三台泵业有限公司', '佛山市恒方钢铁贸易有限公司', '东莞市长安意华模具钢材经营部', '上海厦鸿实业有限公司',
                        '郑州安嘉电子科技有限公司', '广州奥特佳数控系统有限公司', '佛山苑庭家居装潢有限公司', '佛山市家家卫浴有限公司', '深圳市欣中讯科技有限公司',
                        '温州市龙湾天河今创开关配件加工', '南昌市五华市场东楚电器材料批发部', '萍乡市上埠永胜电瓷厂', '温州大本电器有限公司', '成都穗陶卫浴洁具批发部', '南宁市双川卫浴批发部',
                        '南昌市青山湖区中天建材经营部', '江西福泰安防技术有限公司', '南昌长运白云电器经销部', '福牌水暖器材制造厂', '吉水县金竹板业有限公司', '武汉煦源照明工程技术有限公司',
                        '武汉鑫丰强电气有限公司', '武汉六角电工电器有限公司', '武汉市江汉区湘阳电子电器经营部', '武汉世纪维邦园林机械有限公司', '武汉桓源伟业设备制造有限公司',
                        '武汉润永商贸有限公司', '赤壁市阿拉丁水晶灯饰店', '四川吉星光彩照明有限公司', '四川省天祥照明有限公司', '四川省正旺新能源照明科技有限公司',
                        '四川合生力博机电设备有限公司', '四川始丰成套电器设备有限公司', '十堰佳奥实业发展有限公司', '鹰卫浴重庆旗舰店', '济南市天桥区百佳灯具商行', '重庆登勒卫浴',
                        '诺贝尔卫浴旗舰店', '贵州艾科晋规划设计有限责任公司', '北京福达阳光太阳能设备厂', '青岛海尔家居集成股份有限公司北京分公司', '凯里市谭坚百货有限责任公司',
                        '贵州肖林科技有限公司', '贵阳艺彩壁纸', '圣象卫浴贵阳专卖店', '黔味绝特产商贸有限公司', '贵州欣天阳光电科技有限公司', '北京维欣仪奥科技发展有限公司',
                        '北京市顺达丰泰机电经销部', '北京航宇聚业科技发展有限公司', '北京九州环宇水处理设备有限公司', '北京格若科技有限公司', '北京森淼三峰机电设备有限公司',
                        '泊头市八方油泵制造厂', '北京巨德力泳池水疗设备有限公司', '贵州金马车工贸有限责任公司', '凯里市芯沃电脑经营部', '森博尔特壁纸专卖', '北京老板电器销售有限公司',
                        '美誉天成', '北京海华建达科技发展有限公司', '北京亚视创业科技发展有限公司', '北京市盛世鼎商贸有限责任公司', '北京至诚佳音电器商行', '北京百旺腾龙商贸有限公司销售部',
                        '北京创世鸿锦科技发展有限公司', '北京利源易德桑拿设备有限公司', '昆明市官渡区涌泉普通机械经营部', '天桥区明达空调设备销售中心', '环球灯饰(济阳店)有限公司',
                        '天桥区昌隆兴灯具商行', '武汉环润灌溉设备有限公司', '济南祥坤经贸有限公司', '广州好艺家感应洁具有限公司武汉分公司', '济南恒盛绝缘材料经销处', '济南海盛绝缘材料有限公司',
                        '江西南翔空压机有限公司', '江西盈通实业有限公司南昌办事处', '江西省瑞洪泵业有限公司', '江西联信大市场新发机电商行', '南昌力亿机电设备有限公司', '济南亿源太阳能开发中心',
                        '历下区传福家用电器销售中心', '济南槐荫清华太阳能厂', '济南子杰商贸有限公司', '济南章丘市巨龙锅炉厂', '济南鲁青电器', '章丘市鑫发石材厂', '章丘市桑园塑胶有限公司',
                        '山东东方仪表电力设备成套有限责任公司']
        for i in company_list:
            content = {
                "name": i
            }
            if "公司" in i:
                i = i.split('公司')[0] + "公司"
            url = "https://m.qichacha.com/search?" + "key={}".format(i)
            yield scrapy.Request(url=url, callback=self.parse, meta={"data": content})

    def parse(self, response):
        content = response.meta["data"]
        # try:
        #     company_name = response.xpath("//div[@class='list-item-name']").extract_first()
        # except:
        #     print('公司没有找到')
        url_node = response.xpath("//a[@class='a-decoration']")
        # print(url_node)
        i = url_node[0].xpath("./@href").extract_first()
        url = "https://m.qichacha.com" + i
        print(url)
        print('-' * 100)
        yield scrapy.Request(url=url, callback=self.parse_detail, meta={"data1": content})

    def parse_detail(self, response):
        item = QichachaItem()
        item['search_name'] = response.meta["data1"]['name']
        item['legal_person'] = response.xpath("//div[@class='oper-warp']/a/text()").extract_first()
        item['registration_number'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '注册号')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['credit_code'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '统一社会信用代码')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['registered_capital'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '注册资本')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['establishment_data'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '成立日期')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['enterprise_type'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '企业类型')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['management'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '经营范围')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['address'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '公司住所')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['term'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '营业期限')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['status'] = response.xpath(
            "//div[@class='basic-item']/div[contains(text(), '企业状态')]/../div[@class='basic-item-right']/text()").extract_first().replace(
            "'", '').strip().replace("\n", '')
        item['company_name'] = response.xpath("//div[@class='company-name']/text()").extract_first()
        try:
            item['telephone'] = response.xpath("//div[@class='contact-info-wrap']/a/text()").extract()[0]
        except Exception as e:
            print(e)
        try:
            item['email'] = response.xpath("//div[@class='contact-info-wrap']/a/text()").extract()[1]
        except:
            item['email'] = None
        yield item
