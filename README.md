# Webapp Checklist

Technical details that a programmer of a web application should consider before making the site public.

## Disclaimer

This question was originally asked by [Joel Coehoorn](http://programmers.stackexchange.com/users/8057/joel-coehoorn) on [Programmers-StackExchange](http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before) and has since been [answered](http://programmers.stackexchange.com/a/46760/54643) and [maintained](http://programmers.stackexchange.com/posts/46760/revisions) as community wiki.

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

### Interface and User Experience

Be aware that browsers implement standards inconsistently and make sure your site works reasonably well across all major browsers. At a minimum test against a recent Gecko engine (Firefox), a WebKit engine (Safari and some mobile browsers), Chrome, your supported IE browsers (take advantage of the Application Compatibility VPC Images), and Opera. Also consider how browsers render your site in different operating systems.
Consider how people might use the site other than from the major browsers: cell phones, screen readers and search engines, for example. — Some accessibility info: WAI and Section508, Mobile development: MobiForge.
Staging: How to deploy updates without affecting your users. Have one or more test or staging environments available to implement changes to architecture, code or sweeping content and ensure that they can be deployed in a controlled way without breaking anything. Have an automated way of then deploying approved changes to the live site. This is most effectively implemented in conjunction with the use of a version control system (CVS, Subversion, etc.) and an automated build mechanism (Ant, NAnt, etc.).
Don't display unfriendly errors directly to the user.
Don't put users' email addresses in plain text as they will get spammed to death.
Add the attribute rel="nofollow" to user-generated links to avoid spam.
Build well-considered limits into your site - This also belongs under Security.
Learn how to do progressive enhancement.
Redirect after a POST if that POST was successful, to prevent a refresh from submitting again.
Don't forget to take accessibility into account. It's always a good idea and in certain circumstances it's a legal requirement. WAI-ARIA and WCAG 2 are good resources in this area.
Don't make me think


### Security

It's a lot to digest but the OWASP development guide covers Web Site security from top to bottom.
Know about Injection especially SQL injection and how to prevent it.
Never trust user input, nor anything else that comes in the request (which includes cookies and hidden form field values!).
Hash passwords using salt and use different salts for your rows to prevent rainbow attacks. Use a slow hashing algorithm, such as bcrypt (time tested) or scrypt (even stronger, but newer) (1, 2), for storing passwords. (How To Safely Store A Password). The NIST also approves of PBKDF2 to hash passwords", and it's FIPS approved in .NET (more info here). Avoid using MD5 or SHA family directly.
Don't try to come up with your own fancy authentication system. It's such an easy thing to get wrong in subtle and untestable ways and you wouldn't even know it until after you're hacked.
Know the rules for processing credit cards. (See this question as well)
Use SSL/HTTPS for login and any pages where sensitive data is entered (like credit card info).
Prevent session hijacking.
Avoid cross site scripting (XSS).
Avoid cross site request forgeries (CSRF).
Avoid Clickjacking.
Keep your system(s) up to date with the latest patches.
Make sure your database connection information is secured.
Keep yourself informed about the latest attack techniques and vulnerabilities affecting your platform.
Read The Google Browser Security Handbook.
Read The Web Application Hacker's Handbook.
Consider The principle of least privilege. Try to run your app server as non-root. (tomcat example)


### Performance

Implement caching if necessary, understand and use HTTP caching properly as well as HTML5 Manifest.
Optimize images - don't use a 20 KB image for a repeating background.
Learn how to gzip/deflate content (deflate is better).
Combine/concatenate multiple stylesheets or multiple script files to reduce number of browser connections and improve gzip ability to compress duplications between files.
Take a look at the Yahoo Exceptional Performance site, lots of great guidelines, including improving front-end performance and their YSlow tool (requires Firefox, Safari, Chrome or Opera). Also, Google page speed (use with browser extension) is another tool for performance profiling, and it optimizes your images too.
Use CSS Image Sprites for small related images like toolbars (see the "minimize HTTP requests" point)
Busy web sites should consider splitting components across domains. Specifically...
Static content (i.e. images, CSS, JavaScript, and generally content that doesn't need access to cookies) should go in a separate domain that does not use cookies, because all cookies for a domain and its subdomains are sent with every request to the domain and its subdomains. One good option here is to use a Content Delivery Network (CDN), but consider the case where that CDN may fail by including alternative CDNs, or local copies that can be served instead.
Minimize the total number of HTTP requests required for a browser to render the page.
Utilize Google Closure Compiler for JavaScript and other minification tools.
Make sure there’s a favicon.ico file in the root of the site, i.e. /favicon.ico. Browsers will automatically request it, even if the icon isn’t mentioned in the HTML at all. If you don’t have a /favicon.ico, this will result in a lot of 404s, draining your server’s bandwidth.


### SEO (Search Engine Optimization)

Use "search engine friendly" URLs, i.e. use example.com/pages/45-article-title instead of example.com/index.php?page=45
When using # for dynamic content change the # to #! and then on the server $_REQUEST["_escaped_fragment_"] is what googlebot uses instead of #!. In other words, ./#!page=1 becomes ./?_escaped_fragments_=page=1. Also, for users that may be using FF.b4 or Chromium, history.pushState({"foo":"bar"}, "About", "./?page=1"); Is a great command. So even though the address bar has changed the page does not reload. This allows you to use ? instead of #! to keep dynamic content and also tell the server when you email the link that we are after this page, and the AJAX does not need to make another extra request.
Don't use links that say "click here". You're wasting an SEO opportunity and it makes things harder for people with screen readers.
Have an XML sitemap, preferably in the default location /sitemap.xml.
Use <link rel="canonical" ... /> when you have multiple URLs that point to the same content, this issue can also be addressed from Google Webmaster Tools.
Use Google Webmaster Tools and Bing Webmaster Tools.
Install Google Analytics right at the start (or an open source analysis tool like Piwik).
Know how robots.txt and search engine spiders work.
Redirect requests (using 301 Moved Permanently) asking for www.example.com to example.com (or the other way round) to prevent splitting the google ranking between both sites.
Know that there can be badly-behaved spiders out there.
If you have non-text content look into Google's sitemap extensions for video etc. There is some good information about this in Tim Farley's answer.


### Technology

Understand HTTP and things like GET, POST, sessions, cookies, and what it means to be "stateless".
Write your XHTML/HTML and CSS according to the W3C specifications and make sure they validate. The goal here is to avoid browser quirks modes and as a bonus make it much easier to work with non-traditional browsers like screen readers and mobile devices.
Understand how JavaScript is processed in the browser.
Understand how JavaScript, style sheets, and other resources used by your page are loaded and consider their impact on perceived performance. It is now widely regarded as appropriate to move scripts to the bottom of your pages with exceptions typically being things like analytics apps or HTML5 shims.
Understand how the JavaScript sandbox works, especially if you intend to use iframes.
Be aware that JavaScript can and will be disabled, and that AJAX is therefore an extension, not a baseline. Even if most normal users leave it on now, remember that NoScript is becoming more popular, mobile devices may not work as expected, and Google won't run most of your JavaScript when indexing the site.
Learn the difference between 301 and 302 redirects (this is also an SEO issue).
Learn as much as you possibly can about your deployment platform.
Consider using a Reset Style Sheet or normalize.css.
Consider JavaScript frameworks (such as jQuery, MooTools, Prototype, Dojo or YUI 3), which will hide a lot of the browser differences when using JavaScript for DOM manipulation.
Taking perceived performance and JS frameworks together, consider using a service such as the Google Libraries API to load frameworks so that a browser can use a copy of the framework it has already cached rather than downloading a duplicate copy from your site.
Don't reinvent the wheel. Before doing ANYTHING search for a component or example on how to do it. There is a 99% chance that someone has done it and released an OSS version of the code.
On the flipside of that, don't start with 20 libraries before you've even decided what your needs are. Particularly on the client-side web where it's almost always ultimately more important to keep things lightweight, fast, and flexible.


### Bug fixing

Understand you'll spend 20% of your time coding and 80% of it maintaining, so code accordingly.
Set up a good error reporting solution.
Have a system for people to contact you with suggestions and criticisms.
Document how the application works for future support staff and people performing maintenance.
Make frequent backups! (And make sure those backups are functional) Have a restore strategy, not just a backup strategy.
Use a version control system to store your files, such as Subversion, Mercurial or Git.
Don't forget to do your Acceptance Testing. Frameworks like Selenium can help. Especially if you fully automate your testing, perhaps by using a Continuous Integration tool, such as Jenkins.
Make sure you have sufficient logging in place using frameworks such as log4j, log4net or log4r. If something goes wrong on your live site, you'll need a way of finding out what.
When logging make sure you capture both handled exceptions, and unhandled exceptions. Report/analyse the log output, as it'll show you where the key issues are in your site.
Lots of stuff omitted not necessarily because they're not useful answers, but because they're either too detailed, out of scope, or go a bit too far for someone looking to get an overview of the things they should know. Please feel free to edit this as well, I probably missed some stuff or made some mistakes.
