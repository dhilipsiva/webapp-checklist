＃的webapp清单

技术细节，一个Web应用程序的程序员应该使网站在公众面前考虑。

这里的想法是，我们大多数人应该_already_知道_most_什么是这个名单上。但是，只可能是一个或两个项目，你还没有真正研究过之前，不完全了解，或者从来没有听说过。


## 界面和用户体验

* 请注意，浏览器实现的标准不一致，并确保你的站点能够合理地发挥在所有主要的浏览器。在对最近的[壁虎](http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29) 引擎([火狐](http://firefox.com/) ) ，一个WebKit引擎的最低测试( [Safari](http://www.apple.com/safari/) 和一些移动浏览器) ，[铬](http://www.google.com/chrome) ，您的支持[IE浏览器]上(http：/ /en.wikipedia.org/wiki/Internet_Explorer) (利用[应用程序兼容性VPC的Images](http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&displaylang=en) ) ,和[歌剧](http://www.opera.com/) 。还要考虑如何[browsershots](http://www.browsershots.org) 。
* 考虑人们如何可能使用该网站比从主流浏览器其他：手机，屏幕阅读器和搜索引擎，例如。 ＆mdash;一些辅助信息：[WAI](http://www.w3.org/WAI/) 和[Section508](http://www.section508.gov/) ，移动开发：[MobiForge](http://mobiforge.com/) 。
* 分期：如何在不影响用户部署更新。有一个或多个可用来实现改变架构，代码或清扫内容，并确保它们可以部署在受控的方式不破坏任何测试或分段环境。有那么部署批准更改直播现场的自动化的方式。这与使用版本控制系统(CVS，Subversion的，等等) ，并自动构建机制(蚂蚁，南特等) 相结合最有效的执行。
* 不要直接向用户显示不友好的错误。
* 不要把用户的电子邮件地址以纯文本，因为他们将得到垃圾邮件死亡。
* 添加属性[`<link rel="canonical" ... />`](http://en.wikipedia.org/wiki/Nofollow) 。
*  [构建深思熟虑限制到你的网站](http://www.codinghorror.com/blog/archives/001228.html)  - 这也是在安全属于。
* 学习如何做[渐进增强](http://en.wikipedia.org/wiki/Progressive_enhancement) 。
* (http://en.wikipedia.org/wiki/Post/Redirect/Get) 一个POST之后重定向]如果POST成功，以防止刷新再次提交。
* 不要忘记采取无障碍考虑。它总是一个好主意，在某些情况下，这是一个[法律规定](http://www.section508.gov/) 。 [WAI-ARIA](http://www.w3.org/WAI/intro/aria) 和[WCAG 2](http://www.w3.org/TR/WCAG20/) 是本地区良好的资源。
*  [不要让我想起](http://www.sensible.com/dmmt.html)


## 安全

* 这是一个很大的消化，但[OWASP开发指南](http://www.owasp.org/index.php/Category:OWASP_Guide_Project) 覆盖网站的安全性上下。
* 知道的关于注射尤其是[SQL注入](http://en.wikipedia.org/wiki/SQL_injection) ，以及如何防止它。
* 不要信任用户的输入，也没有其他任何进来的请求(包括饼干和隐藏的表单字段值！) 。
* 使用散列密码[盐](http://security.stackexchange.com/q/21263/396) ，并使用不同的盐为您行，以防止彩虹攻击。使用慢速散列算法，如bcrypt(时间测试) 或scrypt(甚至更强，但是较新的) ([1](http://www.tarsnap.com/scrypt.html) ，[2]上(http：// it.slashdot.org/comments.pl?sid=1987632&cid=35149842) ) ，用于存储密码。 ([如何安全存放密码](http://codahale.com/how-to-safely-store-a-password/) ) 。在[NIST还批准PBKDF2的散列密码](http://security.stackexchange.com/q/7689/396) “​​，它的[批准.NET FIPS](http://security.stackexchange.com/ A /396分之2136) (更多信息[这里](http://security.stackexchange.com/questions/211/how-to-securely-hash-passwords) ) 。*避免*直接使用MD5或SHA家庭。
*  [不要试图拿出自己看中的身份验证system](http://stackoverflow.com/questions/1581610/how-can-i-store-my-users-passwords-safely/1581919#1581919) .它是这样一个容易的事情得到错误的微妙和不可测试的方式，你甚至不知道它，直到_after_你砍死。
* 认识[规则处理信用卡](https://www.pcisecuritystandards.org/) 。 ([见这个问题作为well](http://stackoverflow.com/questions/51094/payment-processors-what-do-i-need-to-know-if-i-want-to-accept-credit-cards-on-m) )
* 使用[SSL](http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt) /[HTTPS](http://en.wikipedia.org/wiki/Https) 用于登录并在敏感数据被输入(如信用卡信息) 的任何页面。
*  [防止会话劫持](http://en.wikipedia.org/wiki/Session_hijacking#Prevention) 。
* 避免[跨站点脚本](http://en.wikipedia.org/wiki/Cross-site_scripting) (XSS) 。
* 避免[跨站请求伪造](http://en.wikipedia.org/wiki/Cross-site_request_forgery) (CSRF) 。
* 避免[点击劫持](http://en.wikipedia.org/wiki/Clickjacking) 。
* 保持你的系统(S) 及时了解最新的补丁。
* 请确保您的数据库连接信息是安全的。
* 保持自己知情的最新攻击技术和漏洞影响您的平台。
* 阅读[在谷歌浏览器安全手册](http://code.google.com/p/browsersec/wiki/Main) 。
* 阅读[Web应用程序黑客手册](http://amzn.com/0470170778) 。
* 考虑[最小特权原则](https://en.wikipedia.org/wiki/Principle_of_least_privilege) 。尝试运行你的应用服务器[如non-root](http://security.stackexchange.com/questions/47576/do-simple-linux-servers-really-need-a-non-root-user-for-security-reasons) . ([tomcat的示例](http://tomcat.apache.org/tomcat-8.0-doc/security-howto.html#Non-Tomcat_settings) )


## 性能

* 实现缓存如果需要的话，理解和使用[HTTP缓存](http://www.mnot.net/cache_docs/) 正确以及[HTML5清单](http://www.w3.org/TR/2011/ WD-html5-20110525 / offline.html) 。
* 优化的图像 - 不使用20 KB图像重复的背景。
* 学习如何[GZIP /紧缩内容](http://developer.yahoo.com/performance/rules.html#gzip“gzipcontent”) (<罢工> [紧缩较好](http://stackoverflow.com/提问/ 1574168 / GZIP-VS-放气，zlib的，再访) </击>) 。
* 合并/连接多个样式表或多个脚本文件，以减少浏览器连接的数量，提高gzip来的文件之间的重复压缩能力。
* 看看的[雅虎卓越的性能](http://developer.yahoo.com/performance/) 的网站，很多伟大的指引，包括提高前端性能及其[YSlow的]上(http：//开发商。 yahoo.com/yslow/) 工具(需要火狐，Safari，Chrome或Opera) 的。此外，[谷歌网页速度](https://developers.google.com/speed/docs/best-practices/rules_intro) (与[浏览器扩展]使用(https://developers.google.com/speed/pagespeed/ insights_extensions) ) 是另一种工具，性能分析，并优化您的图像了。
* 使用[CSS图像精灵](http://alistapart.com/articles/sprites) 为小相关的图像，例如工具栏(请参见“减少HTTP请求”点)
* 忙的网站应该考虑[跨域分裂成分](http://developer.yahoo.com/performance/rules.html#split) 。具体...
* 静态内容(如图像，CSS，JavaScript和一般的内容并不需要访问饼干) 应该在一个单独的域_ [不使用cookie](http://blog.stackoverflow.com/2009/ 08 / A-一些，速度提升/) _，因为所有Cookie的域及其子域发送每个请求域及其子域。这里有一个很好的选择是使用内容分发网络(CDN) ，但考虑到那里的CDN可以通过包括替代的CDN，或可服，而不是本地副本失败的情况。
* 最小化所需的浏览器来呈现页面的HTTP请求的总数。
* 利用[谷歌关闭编译器](http://developers.google.com/closure/compiler/) JavaScript和[其他微小工具](http://developer.yahoo.com/yui/compressor/) 。
* 确保有一个`favicon.ico`文件中的站点的根目录，即`/ favicon.ico`。 [浏览器会自动请求吧](http://mathiasbynens.be/notes/rel-shortcut-icon) ，即使该图标没有在HTML中提到的。如果你没有一个`/ favicon.ico`，这将导致大量的404，耗尽你的服务器的带宽。


## SEO(搜​​索引擎优化)

* 使用“搜索引擎友好”的URL，即使用`example.com/pages/45-article-title` 代替 `example.com/index.php?page=45`
* 当使用``＃动态内容改变``＃`以＃！'，然后服务器`$ _REQUEST上[“_ _ escaped_fragment”]`是Googlebot使用，而不是`＃！`。换句话说，`./#！页= 1`变得`./?_ escaped_fragments_ =页= 1`。此外，对于用户可能使用FF.b4或铬，`history.pushState({“foo”的：“栏”}，“关于”，“./页= 1”) ;'是一个伟大的命令。因此，即使在地址栏中改变了页面不会重新加载。这使您可以使用`？`，而不是`＃！`保持动态的内容，并且还告诉服务器，当你发邮件，我们是这个页面之后的链接，和AJAX并不需要再进行一次额外的请求。
* 不要使用链接说[“点击这里”](http://ux.stackexchange.com/questions/12100/why-shouldnt-we-use-the-word-here-in-a-textlink) 。那你就浪费了SEO的机会，它使事情更难的人与屏幕阅读器。
* 有一个[XML网站地图](http://www.sitemaps.org/) ，最好是在默认位置`/ sitemap.xml`。
* 使用[`<LINK REL =“规范”...... />`](http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html) 当你有指向多个URL同样的内容，这个问题也可以从[谷歌网站管理员工具]寻址(http://www.google.com/webmasters/) 。
* 使用[谷歌网站管理员工具](http://www.google.com/webmasters/) 和[冰网站管理员工具](http://www.bing.com/tool​​box/webmaster) 。
* 在开始安装[谷歌Analytics(分析) ](http://www.google.com/analytics/) 右(或开源分析工具如[Piwik](http://piwik.org/) ) 。
* 懂得[robots.txt的](http://en.wikipedia.org/wiki/Robots_exclusion_standard) 和搜索引擎蜘蛛的工作。
* 重定向请求(使用`301动Permanently`) 要求`www.example.com`到`example.com`(或者反过来) ，以防止分裂两个站点之间的谷歌排名。
* 要知道，有可能是严重的乖蜘蛛在那里。
* 如果你有非文本内容看到谷歌的站点地图扩展视频等有一个在[蒂姆·法利的关于这方面的一些好的信息answer](http://stackoverflow.com/questions/72394/what-should-a-developer-know-before-building-a-public-web-site#167608) .


## 技术

* 了解[HTTP](http://www.ietf.org/rfc/rfc2616.txt) 之类的东西GET，POST，会话，饼干，这是什么意思是“无状态”。
* 您[XHTML](http://www.w3.org/TR/xhtml1/) / [HTML](http://www.w3.org/TR/REC-html40/) 和[CSS](HTTP ：//www.w3.org/TR/CSS2/) 根据[W3C规范](http://www.w3.org/TR/) ，并确保他们[验证](HTTP：//validator.w3 .org等/) 。这样做的目的是为了避免浏览器的怪癖模式，并作为奖金，使其更容易与非传统浏览器，如屏幕阅读器和移动设备上工作。
* 了解如何JavaScript在浏览器中进行处理。
* 了解如何JavaScript的，样式表，并使用你的页面的其他资源被加载，并考虑其对* *感知性能的影响。现在人们普遍认为是适当的[移动脚本底部](http://developer.yahoo.com/blogs/ydn/posts/2007/07/high_performanc_5/) 你的页面有例外通常是东西像分析应用程序或HTML5垫片。
* 了解如何JavaScript的沙箱的工作原理，特别是如果你打算使用内部框架。
* 注意，JavaScript可以和将被禁用，并且AJAX因此是一个扩展，而不是一个基线。即使大多数普通用户离开它现在，请记住，[NoScript的](http://noscript.net/) 越来越普及，移动设备可能无法正常工作，并建立索引时，谷歌将无法运行大部分的的JavaScript该网站。
* 学习的[301和302重定向的区别](http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/) (这也是一个SEO的问题) 。
* 学习尽可能多的，你可能可以对您的部署平台。
* 考虑使用[重置样式表](http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet) 或[normalize.css]上(http：/ /necolas.github.com/normalize.css/) 。
* 考虑JavaScript框架(如[jQuery的](http://jquery.com/) ，[MooTools的](http://mootools.net/) ，[原型](http://www.prototypejs.org/)  [道场】(http://dojotoolkit.org) 或[YUI 3](http://developer.yahoo.com/yui/3/) ) ，将使用JavaScript的DOM时，隐藏了很多的浏览器差异操纵。
* 以感知性能和JS框架在一起，可以考虑使用一个服务，如[谷歌图书馆API](http://developers.google.com/speed/libraries/devguide) 加载框架，使浏览器可以使用的副本该框架也已经缓存，而不是从您的网站下载一个副本。
* 不要推倒重来。在做任何搜索上如何做到这一点的组件或例子。有99％的机会，有人已经做到了，并发布了OSS版本的代码。
* 重要的是不利的一面，不要20的库开始之前，你甚至决定你的需求是什么。特别是在客户端的Web中它几乎总是少不了更重要的是让事情变得轻便，快速，灵活。


## 错误固定

* 了解你会花你的时间编码的20％和80％的IT维护的，所以相应的代码。
* 建立一个良好的错误报告的解决方案。
* 有一个系统的人给你建议和批评联系。
* 文档应用程序如何适用于未来的技术支持人员和进行维护的人。
* 请频繁备份！ (并确保这些备份功能) 有一个恢复策略，不只是一个备份策略。
* 使用版本控制系统来存储你的文件，如[颠覆](http://subversion.apache.org/) ，[水银](http://mercurial.selenic.com/) 或[混帐](HTTP ：//git-scm.org) 。
* 不要忘记做你验收测试。就像[硒]框架(http://seleniumhq.org/) 可以提供帮助。特别是如果你完全自动化的测试，或许是使用持续集成工具，如[詹金斯](http://jenkins-ci.org/) 。
* 请确保您有使用框架，如[log4j](http://logging.apache.org/log4j/) 足够的日志记录到位，[log4net的](http://logging.apache.org/log4net/) 或[ log4r](http://log4r.rubyforge.org/) 。如果出现问题您直播的网站，你需要找出什么的一种方式。
* 当记录一定要同时捕获处理异常和未处理的异常。报告/分析日志的输出，因为它会告诉你那里的主要问题是在您的网站。

# 免责声明

这本来是一个问题问上 [Programmers-StackExchange](http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before) 按 [乔尔Coehoorn](http://programmers.stackexchange.com/users/8057/joel-coehoorn)  并一直 [回答](http://programmers.stackexchange.com/a/46760/54643)  和 [保持](http://programmers.stackexchange.com/posts/46760/revisions)  社区维基。

有三个原因，我想提出一个GitHub上回购：

1. 协作编辑在GitHub上更加强大。
2. 人们可以派生这种回购和进行自定义可能并不适用于所有的人。
3. 我们可以有答案的许多语言翻译。不是每个人都具有良好的英语。


# 问

什么事情应该使网站在公众面前程序员实现Web应用程序的技术细节考虑？如果杰夫·阿特伍德可以忘记的HttpOnly饼干，网站地图，和跨站点请求伪造都在同一个网站，有什么重要的东西可能我会忘记呢？

我想这从一个web开发人员的角度，这样其他人创造实际的设计和内容的网站。因此，虽然可用性和内容可能比平台更重要，则程序员在那个小发言权。你做什么需要担心的是，你的实现平台的稳定，性能良好，是安全的，并符合其他业务目标(如不与谷歌的成本太大，需要很长时间才能建立，和排名，以及在内容支持) 。

想到这，从谁的做了一些工作，内联网类应用在一个相当可靠的环境，并即将有他的第一炮，并把出潜在的流行网站的整个大坏万维网开发人员的角度来看。

另外，我在寻找的东西不仅仅是一个模糊的“web标准”的反应更为具体。我的意思是，HTML，JavaScript和CSS通过HTTP是一个很值得考虑，特别是当我已经指定了你是一个专业的Web开发人员。所以超越的，哪些标准？在什么情况下，为什么？提供一个链接到该标准的规范。
