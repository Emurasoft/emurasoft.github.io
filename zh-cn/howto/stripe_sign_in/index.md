# 使用 Stripe 登录 EmEditor

Stripe 是 EmEditor 新的支付处理器。通过 Stripe 购买 EmEditor 的订阅，您将不再需要注册码。

## 购买订阅

1. 访问 [emeditor.com](https://zh-cn.emeditor.com/)，向下滚动，然后点击“立即购买”以购买年订阅。
2. 在支付页面上，输入支付信息。如果您已经登录 [Emurasoft 客户中心](https://support.emeditor.com/en/account/subscriptions)，支付页面上会直接显示您注册的电子邮件。如果您想使用其他账户购买订阅，请先退出客户中心，然后再次进入支付页面。您可以在支付页面输入新的电子邮件地址。
3. 购买后，您将收到来自 `emurasoft.com` 的两封电子邮件：
    - 订阅详情和登录说明
    - 发票和收据

- 您可以在 [Emurasoft 客户中心](https://support.emeditor.com/en/account/subscriptions) 管理您的订阅。

## 登录 EmEditor

您可以登录 EmEditor 或输入注册密钥来注册 EmEditor。

1. 打开 EmEditor。进入 **帮助** &gt; **关于 EmEditor**，然后点击 **如何购买/输入密钥**。点击 **输入密钥/登录**。  
2. 选择登录或使用注册密钥。  
    - 选择 **登录** 选项。使用 Emurasoft 客户中心的电子邮件和密码登录。  
    - 或选择 **输入注册密钥** 选项。输入您的姓名和用于购买订阅的电子邮件地址。从 [Stripe 订阅](https://support.emeditor.com/en/account/subscriptions) 复制注册密钥，并将其粘贴到 **注册密钥** 字段。（需要 EmEditor v24.5.3 或更高版本。）  
3. 您可以启用 **设备标签** 来在 Emurasoft 客户中心的 [注册设备](https://support.emeditor.com/en/account/devices) 页面为设备打标签。点击确定。

- 您可以在 [客户门户](https://billing.stripe.com/p/login/14k7w2fK6g9Ca9q9AA) 中更改您的支付信息。

## 离线注册

- 离线注册取代了之前通过 2Checkout 商家购买时发放的注册密钥。
- 如果您希望在没有互联网连接的情况下注册 EmEditor，可以使用 [离线注册](../offline_registration/index)。