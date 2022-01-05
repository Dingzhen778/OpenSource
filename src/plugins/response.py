from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from random import choice

matcher = on_keyword({"手冲","开冲","day","色图",'淫'})
#matcher=on_command('你是谁啊',rule=to_me(),priority=5)
@matcher.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    msg = choice([
        "群友们请不要再冲了", "戒色请从今天开始", "手淫的危害：", "再冲把你牛子噶了",
        "孽海茫茫，首恶无非色欲;尘寰(huán)扰扰，易犯唯有淫邪。拔山盖世之雄，坐此亡身辱国。绣口锦心之士，因兹败节隳(huī)名。始为一念之差，遂至毕生莫赎。何乃淫风日炽，天理沦亡;以当悲当憾之行，反为得计;而众怒众贱之事，恬不知羞。刊淫词，谈丽色。目注道左娇姿，肠断帘中窈窕。若真节或淑德，可敬可嘉，乃计诱而使无完行。若坤女，若仆妾，宜怜宜悯(mǐn)，竟势迫而玷(diàn)辱终身。既令亲族含羞，尤使子孙蒙垢。嗟(jiē)乎!总以心昏气浊，贤远侫(nìng)亲;岂知天地难容，人神共忿。或妻女酬偿，或子孙受报。绝嗣之坟墓，无非好色狂徒;妓女之祖宗，尽是贪花浪子。当富则玉楼削籍，应贵则金榜除名。笞(chī)杖徙流大辟，生遭五等之刑;地狱饿鬼**，殁(mò)受三途之苦。从前恩爱，至此成空;昔日风流，而今安在?与其后悔已无从，何不早思而勿犯?谨劝青年志士，社幷会名流，发觉悟之心，破色魔之障。芙蓉白面，不过带肉骷髅;芍药红妆，乃是杀人利刃。纵对如玉如花之貌，当存若姊若妹之心。未犯者宜防失足，曾行者及早回头。更望展转流传，迭(dié)相化导。必使在在齐归觉路，人人共出迷津。由是首恶既除，众邪自消。灵台无滞。世泽垂荣矣(yǐ)。"
        ,"兄弟們，再繼續看黃、意淫、手淫、婚前性行為下去，咱們漢人就要絕子絕孫了！您們難道就這樣看著漢族女生一個個被白人黑人追走嗎？我們華夏男兒哪裡不如白人黑人了？戒掉看黃意淫手淫婚前性行為，孝順父母，報效國家，把中國男人的底氣發揮的淋漓盡至！贏回漢族女生的芳心！"
    ])
    await matcher.send(msg)

who = on_keyword(['你是谁', '你是谁啊', '你谁','介绍'], rule=to_me())
@who.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
        "我是低智商机器人", "我是机器人","喜欢我人工智障吗❤"
    ])
    await who.finish(msg, at_sender=True)

who = on_keyword(['你几把谁啊','你jb谁啊','你寄吧谁啊'], rule=to_me())
@who.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
        "我嫩爹", "？你几把谁啊？", "可以有礼貌点嘛谢谢您嘞", "我是一个有素质的机器人", "你问你🐎呢？！","差不多得了😅"
    ])

    await who.finish(msg, at_sender=True)

penzi = on_keyword(['撒','死','傻逼', '啥比','煞笔','伞兵', 'SB','sb', '脑瘫','NM',"贵物",
                  "废物","nm",'马','🐎','🐴','🦄','娘','妈','铸币','猪鼻'], rule=to_me())
@penzi.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
        "小逼崽子别狂，等我上门收拾你", "你🐎死了", "你是没有家教嘴这么臭吗？", "别几把乱叫", "请注意你的语气",
        "祖安逼收收味", "群主呢？出来禁言", "我报警了！你这个没素质的东西","你几个妈啊这么能喷"
    ])
    await penzi.finish(msg, at_sender=True)

hanjian = on_keyword(['汉奸', '罕见','狗汉奸','狗罕见', '苟罕见',], rule=to_me())
@hanjian.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
        "已举办", "晶哥速来收网", "已抓获50W", "已报警", "收了拜登钱是吧？",
        "谁罕见啊，谁罕见", "群主呢？出来抓罕见", "罕见罕见罕见见！"
    ])
    await hanjian.finish(msg, at_sender=True)

daquan = on_keyword(['女权','女拳','打拳','郭楠', '蝈蝻', '楠', '蝻', '国男','普信','普却信','奇趣蛋'], rule=to_me())
@daquan.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
            "急了？", "天天打拳看来你在生活中很失败啊", "自我认知很精辟啊", "不如你普信", "差不多得了😅",
            "你真是普却信", "石头砸狗叫",'挑起性别对立，境外势力是吧','禁止激化性别矛盾','普信碳基生物真可怜',
            '跟机器人打拳我看你可以重开了','拳师4000+',"这是否有点"
    ])
    await daquan.finish(msg, at_sender=True)

pingjia = on_keyword(['评价', '如何', '打分'], rule=to_me())
@pingjia.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
            "评价你🐎呢评价", "天天不是评价就是打分你是不是低能啊", "脑瘫才天天评价捏", "要我评价你🐎嘛", "差不多得了😅评价个🔨",
            "给透10不给0","这是否有点"
    ])
    await pingjia.finish(msg, at_sender=True)

chouxiang = on_keyword(["谔谔", "绷", "这是否有点", "太哈人了", "差不多得了",'典中点','是这样的','还真是',
        "你几把谁啊", "😍😍",'😱😱😱😱','4000+' "太烧啦🥵🥵🥵🥵","典","赢",'乐','滑','狂','笑嘻了','米线','抽象'], rule=to_me())
@chouxiang.handle()
async def _(bot: Bot, event: Event):
    msg = choice([
        "谔谔", "绷", "这是否有点", "太哈人了", "差不多得了",'典中点','是这样的','还真是',
        "你几把谁啊", "😍😍",'😱😱😱😱','4000+' "太烧啦🥵🥵🥵🥵","典","赢",'乐','滑','狂','笑嘻了','米线'
    ])
    await chouxiang.finish(msg, at_sender=True)
