# Webapp Checklist

Technical details that a programmer of a web application should consider before making the site public.

## Disclaimer

This was originally a question asked on [Programmers-StackExchange](http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before)  by [Joel Coehoorn](http://programmers.stackexchange.com/users/8057/joel-coehoorn) and has since been [answered](http://programmers.stackexchange.com/a/46760/54643) and [maintained](http://programmers.stackexchange.com/posts/46760/revisions) as community wiki.

There are three reasons why I am making a GitHub repo:

1. Collaborative editing is much more powerful on GitHub.
2. People can fork this repo and make customizations that might not apply to everyone else.
3. We can have translations of the answer in many languages. Not everyone is good with English.


## Question

What things should a programmer implementing the technical details of a web application consider before making the site public? If Jeff Atwood can forget about HttpOnly cookies, sitemaps, and cross-site request forgeries all in the same site, what important thing could I be forgetting as well?

I'm thinking about this from a web developer's perspective, such that someone else is creating the actual design and content for the site. So while usability and content may be more important than the platform, you the programmer have little say in that. What you do need to worry about is that your implementation of the platform is stable, performs well, is secure, and meets any other business goals (like not cost too much, take too long to build, and rank as well with Google as the content supports).

Think of this from the perspective of a developer who's done some work for intranet-type applications in a fairly trusted environment, and is about to have his first shot and putting out a potentially popular site for the entire big bad world wide web.

Also, I'm looking for something more specific than just a vague "web standards" response. I mean, HTML, JavaScript, and CSS over HTTP are pretty much a given, especially when I've already specified that you're a professional web developer. So going beyond that, Which standards? In what circumstances, and why? Provide a link to the standard's specification.


## Answer

The idea here is that most of us should _already_ know _most_ of what is on this list.  But there just might be one or two items you haven't really looked into before, don't fully understand, or maybe never even heard of.


### Interface and User Experience

 - Be  aware that browsers implement standards inconsistently and make sure your site works reasonably well across all major browsers.  At a minimum test against a recent [Gecko](http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29) engine ([Firefox](http://firefox.com/)), a WebKit engine ([Safari](http://www.apple.com/safari/) and some mobile browsers), [Chrome](http://www.google.com/chrome), your supported [IE browsers](http://en.wikipedia.org/wiki/Internet_Explorer) (take advantage of the [Application Compatibility VPC Images](http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&displaylang=en)), and [Opera](http://www.opera.com/). Also consider how [browsers render your site](http://www.browsershots.org) in different operating systems.
 - Consider how people might use the site other than from the major browsers: cell phones, screen readers and search engines, for example. &mdash; Some accessibility info: [WAI](http://www.w3.org/WAI/) and [Section508](http://www.section508.gov/), Mobile development: [MobiForge](http://mobiforge.com/).
 - Staging: How to deploy updates without affecting your users.  Have one or more test or staging environments available to implement changes to architecture, code or sweeping content and ensure that they can be deployed in a controlled way without breaking anything. Have an automated way of then deploying approved changes to the live site. This is most effectively implemented in conjunction with the use of a version control system (CVS, Subversion, etc.) and an automated build mechanism (Ant, NAnt, etc.).
 - Don't display unfriendly errors directly to the user.
 - Don't put users' email addresses in plain text as they will get spammed to death.
 - Add the attribute `rel="nofollow"` to user-generated links [to avoid spam](http://en.wikipedia.org/wiki/Nofollow).
 - [Build well-considered limits into your site](http://www.codinghorror.com/blog/archives/001228.html) - This also belongs under Security.
 - Learn how to do [progressive enhancement](http://en.wikipedia.org/wiki/Progressive_enhancement).
 - [Redirect after a POST](http://en.wikipedia.org/wiki/Post/Redirect/Get) if that POST was successful, to prevent a refresh from submitting again.
 - Don't forget to take accessibility into account.  It's always a good idea and in certain circumstances it's a [legal requirement](http://www.section508.gov/).  [WAI-ARIA](http://www.w3.org/WAI/intro/aria) and [WCAG 2](http://www.w3.org/TR/WCAG20/) are good resources in this area.
 - [Don't make me think](http://www.sensible.com/dmmt.html)


### Security

* It's a lot to digest but the [OWASP development guide](http://www.owasp.org/index.php/Category:OWASP_Guide_Project) covers Web Site security from top to bottom.
* Know about Injection especially [SQL injection](http://en.wikipedia.org/wiki/SQL_injection) and how to prevent it.
* Never trust user input, nor anything else that comes in the request (which includes cookies and hidden form field values!).
* Hash passwords using [salt](http://security.stackexchange.com/q/21263/396) and use different salts for your rows to prevent rainbow attacks. Use a slow hashing algorithm, such as bcrypt (time tested) or scrypt (even stronger, but newer) ([1](http://www.tarsnap.com/scrypt.html), [2](http://it.slashdot.org/comments.pl?sid=1987632&cid=35149842)), for storing passwords. ([How To Safely Store A Password](http://codahale.com/how-to-safely-store-a-password/)). The [NIST also approves of PBKDF2 to hash passwords](http://security.stackexchange.com/q/7689/396)", and it's [FIPS approved in .NET](http://security.stackexchange.com/a/2136/396) (more info [here](http://security.stackexchange.com/questions/211/how-to-securely-hash-passwords)). *Avoid* using MD5 or SHA family directly.
* [Don't try to come up with your own fancy authentication system](http://stackoverflow.com/questions/1581610/how-can-i-store-my-users-passwords-safely/1581919#1581919). It's such an easy thing to get wrong in subtle and untestable ways and you wouldn't even know it until _after_ you're hacked.
* Know the [rules for processing credit cards](https://www.pcisecuritystandards.org/). ([See this question as well](http://stackoverflow.com/questions/51094/payment-processors-what-do-i-need-to-know-if-i-want-to-accept-credit-cards-on-m))
* Use [SSL](http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt)/[HTTPS](http://en.wikipedia.org/wiki/Https) for login and any pages where sensitive data is entered (like credit card info).
* [Prevent session hijacking](http://en.wikipedia.org/wiki/Session_hijacking#Prevention).
* Avoid [cross site scripting](http://en.wikipedia.org/wiki/Cross-site_scripting) (XSS).
* Avoid [cross site request forgeries](http://en.wikipedia.org/wiki/Cross-site_request_forgery) (CSRF).
* Avoid [Clickjacking](http://en.wikipedia.org/wiki/Clickjacking).
* Keep your system(s) up to date with the latest patches.
* Make sure your database connection information is secured.
* Keep yourself informed about the latest attack techniques and vulnerabilities affecting your platform.
* Read [The Google Browser Security Handbook](http://code.google.com/p/browsersec/wiki/Main).
* Read [The Web Application Hacker's Handbook](http://amzn.com/0470170778).
* Consider [The principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Try to run your app server [as non-root](http://security.stackexchange.com/questions/47576/do-simple-linux-servers-really-need-a-non-root-user-for-security-reasons). ([tomcat example](http://tomcat.apache.org/tomcat-8.0-doc/security-howto.html#Non-Tomcat_settings))


### Performance

* Implement caching if necessary, understand and use [HTTP caching](http://www.mnot.net/cache_docs/) properly as well as [HTML5 Manifest](http://www.w3.org/TR/2011/WD-html5-20110525/offline.html).
* Optimize images - don't use a 20 KB image for a repeating background.
* Learn how to [gzip/deflate content](http://developer.yahoo.com/performance/rules.html#gzip"gzipcontent") (<strike>[deflate is better](http://stackoverflow.com/questions/1574168/gzip-vs-deflate-zlib-revisited)</strike>).
* Combine/concatenate multiple stylesheets or multiple script files to reduce number of browser connections and improve gzip ability to compress duplications between files.
* Take a look at the [Yahoo Exceptional Performance](http://developer.yahoo.com/performance/) site, lots of great guidelines, including improving front-end performance and their [YSlow](http://developer.yahoo.com/yslow/) tool (requires Firefox, Safari, Chrome or Opera). Also, [Google page speed](https://developers.google.com/speed/docs/best-practices/rules_intro) (use with [browser extension](https://developers.google.com/speed/pagespeed/insights_extensions)) is another tool for performance profiling, and it optimizes your images too.
* Use [CSS Image Sprites](http://alistapart.com/articles/sprites) for small related images like toolbars (see the "minimize HTTP requests" point)
* Busy web sites should consider [splitting components across domains](http://developer.yahoo.com/performance/rules.html#split).  Specifically...
* Static content (i.e. images, CSS, JavaScript, and generally content that doesn't need access to cookies) should go in a separate domain _[that does not use cookies](http://blog.stackoverflow.com/2009/08/a-few-speed-improvements/)_, because all cookies for a domain and its subdomains are sent with every request to the domain and its subdomains.  One good option here is to use a Content Delivery Network (CDN), but consider the case where that CDN may fail by including alternative CDNs, or local copies that can be served instead.
* Minimize the total number of HTTP requests required for a browser to render the page.
* Utilize [Google Closure Compiler](http://developers.google.com/closure/compiler/) for JavaScript and [other minification tools](http://developer.yahoo.com/yui/compressor/).
* Make sure there’s a `favicon.ico` file in the root of the site, i.e. `/favicon.ico`. [Browsers will automatically request it](http://mathiasbynens.be/notes/rel-shortcut-icon), even if the icon isn’t mentioned in the HTML at all. If you don’t have a `/favicon.ico`, this will result in a lot of 404s, draining your server’s bandwidth.


### SEO (Search Engine Optimization)

* Use "search engine friendly" URLs, i.e. use `example.com/pages/45-article-title` instead of `example.com/index.php?page=45`
* When using `#` for dynamic content change the `#` to `#!` and then on the server `$_REQUEST["_escaped_fragment_"]` is what googlebot uses instead of `#!`. In other words, `./#!page=1` becomes `./?_escaped_fragments_=page=1`. Also, for users that may be using FF.b4 or Chromium, `history.pushState({"foo":"bar"}, "About", "./?page=1");` Is a great command. So even though the address bar has changed the page does not reload. This allows you to use `?` instead of `#!` to keep dynamic content and also tell the server when you email the link that we are after this page, and the AJAX does not need to make another extra request.
* Don't use links that say ["click here"](http://ux.stackexchange.com/questions/12100/why-shouldnt-we-use-the-word-here-in-a-textlink). You're wasting an SEO opportunity and it makes things harder for people with screen readers.
* Have an [XML sitemap](http://www.sitemaps.org/), preferably in the default location `/sitemap.xml`.
* Use [`<link rel="canonical" ... />`](http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html) when you have multiple URLs that point to the same content, this issue can also be addressed from [Google Webmaster Tools](http://www.google.com/webmasters/).
* Use [Google Webmaster Tools](http://www.google.com/webmasters/) and [Bing Webmaster Tools](http://www.bing.com/toolbox/webmaster).
* Install [Google Analytics](http://www.google.com/analytics/) right at the start (or an open source analysis tool like [Piwik](http://piwik.org/)).
* Know how [robots.txt](http://en.wikipedia.org/wiki/Robots_exclusion_standard) and search engine spiders work.
* Redirect requests (using `301 Moved Permanently`) asking for `www.example.com` to `example.com` (or the other way round) to prevent splitting  the google ranking between both sites.
* Know that there can be badly-behaved spiders out there.
* If you have non-text content look into Google's sitemap extensions for video etc. There is some good information about this in [Tim Farley's answer](http://stackoverflow.com/questions/72394/what-should-a-developer-know-before-building-a-public-web-site#167608).


### Technology

 * Understand [HTTP](http://www.ietf.org/rfc/rfc2616.txt) and things like GET, POST, sessions, cookies, and what it means to be "stateless".
 * Write your [XHTML](http://www.w3.org/TR/xhtml1/)/[HTML](http://www.w3.org/TR/REC-html40/) and [CSS](http://www.w3.org/TR/CSS2/) according to the [W3C specifications](http://www.w3.org/TR/) and make sure they [validate](http://validator.w3.org/).  The goal here is to avoid browser quirks modes and as a bonus make it much easier to work with non-traditional browsers like screen readers and mobile devices.
 * Understand how JavaScript is processed in the browser.
 * Understand how JavaScript, style sheets, and other resources used by your page are loaded and consider their impact on *perceived* performance. It is now widely regarded as appropriate to [move scripts to the bottom](http://developer.yahoo.com/blogs/ydn/posts/2007/07/high_performanc_5/) of your pages with exceptions typically being things like analytics apps or HTML5 shims.
 * Understand how the JavaScript sandbox works, especially if you intend to use iframes.
 * Be aware that JavaScript can and will be disabled, and that AJAX is therefore an extension, not a baseline.  Even if most normal users leave it on now, remember that [NoScript](http://noscript.net/) is becoming more popular, mobile devices may not work as expected, and Google won't run most of your JavaScript when indexing the site.
 * Learn the [difference between 301 and 302 redirects](http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/) (this is also an SEO issue).
 * Learn as much as you possibly can about your deployment platform.
 * Consider using a [Reset Style Sheet](http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet) or [normalize.css](http://necolas.github.com/normalize.css/).
 * Consider JavaScript frameworks (such as [jQuery](http://jquery.com/), [MooTools](http://mootools.net/), [Prototype](http://www.prototypejs.org/), [Dojo](http://dojotoolkit.org) or [YUI 3](http://developer.yahoo.com/yui/3/)), which will hide a lot of the browser differences when using JavaScript for DOM manipulation.
 * Taking perceived performance and JS frameworks together, consider using a service such as the [Google Libraries API](http://developers.google.com/speed/libraries/devguide) to load frameworks so that a browser can use a copy of the framework it has already cached rather than downloading a duplicate copy from your site.
 * Don't reinvent the wheel. Before doing ANYTHING search for a component or example on how to do it. There is a 99% chance that someone has done it and released an OSS version of the code.
 * On the flipside of that, don't start with 20 libraries before you've even decided what your needs are. Particularly on the client-side web where it's almost always ultimately more important to keep things lightweight, fast, and flexible.


### Bug fixing

* Understand you'll spend 20% of your time coding and 80% of it maintaining, so code accordingly.
* Set up a good error reporting solution.
* Have a system for people to contact you with suggestions and criticisms.
* Document how the application works for future support staff and people performing maintenance.
* Make frequent backups! (And make sure those backups are functional) Have a restore strategy, not just a backup strategy.
* Use a version control system to store your files, such as [Subversion](http://subversion.apache.org/), [Mercurial](http://mercurial.selenic.com/) or [Git](http://git-scm.org).
* Don't forget to do your Acceptance Testing.  Frameworks like [Selenium](http://seleniumhq.org/) can help. Especially if you fully automate your testing, perhaps by using a Continuous Integration tool, such as [Jenkins](http://jenkins-ci.org/).
* Make sure you have sufficient logging in place using frameworks such as [log4j](http://logging.apache.org/log4j/), [log4net](http://logging.apache.org/log4net/) or [log4r](http://log4r.rubyforge.org/). If something goes wrong on your live site, you'll need a way of finding out what.
* When logging make sure you capture both handled exceptions, and unhandled exceptions. Report/analyse the log output, as it'll show you where the key issues are in your site.
