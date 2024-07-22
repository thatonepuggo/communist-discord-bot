DEFAULT_CREDIT = 500

USER_TABLE_STRUCTURE = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER, 
    discord_id INTEGER,
    social_credit INTEGER,
    execution_date INTEGER,
    to_be_executed BOOLEAN
);
"""

ADD_CREDIT_MSG = r"""
[ 中华人民共和国寄语] Great work, Citizen! Your social credit score has increased by [%num%] Integers.
Xi Jinping would like to meet you personally at Zhongnanhai to encourage your good work. 
I am sure you notice that you have gained lot of dislike recently. 
Do not worry. We will send re-education vans to make sure your figure is in good graces. 
Keep up the good work! [ 中华人民共和国寄语]
"""

MINUS_CREDIT_MSG = r"""
ATTENTION CITIZEN! 市民请注意!

This is the Central Intelligentsia of the Chinese Communist Party. 您的 Internet 浏览器历史记录和活动引起了我们的注意。
YOUR INTERNET ACTIVITY HAS ATTRACTED OUR ATTENTION. 因此，您的个人资料中的 %absnum% ( %num% Social Credits) 
个社会积分将打折。 DO NOT DO THIS AGAIN! 不要再这样做! If you do not hesitate, more Social Credits ( %num% Social Credits )
will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 CCP) 
You'll also be sent into a re-education camp in the Xinjiang Uyghur Autonomous Zone. 
如果您毫不犹豫，更多的社会信用将从您的个人资料中打折，从而导致口粮供应减少。 您还将被送到新疆维吾尔自治区的再教育营。

为党争光! Glory to the CCP!
"""