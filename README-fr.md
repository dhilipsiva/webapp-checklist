# Webapp Liste de contrôle

Détails techniques qu'un programmeur d'une application web doivent considérer avant de faire le site public.

## Disclaimer

Ce était à l'origine une question posée sur [Programmers-StackExchange](http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before) par [Joel Coehoorn] (http://programmers.stackexchange.com/users/8057/joel-coehoorn) et a depuis été [répondu] (http://programmers.stackexchange.com/a/46760/54643) et [ maintenu] (http://programmers.stackexchange.com/posts/46760/revisions) que la communauté wiki.

Il ya trois raisons pour lesquelles je fais une mise en pension GitHub:

1. Édition collaborative est beaucoup plus puissant sur GitHub.
2. Les gens peuvent débourser cette pension et effectuer des personnalisations qui pourraient ne pas se appliquer à tout le monde.
3. Nous pouvons avoir des traductions de la réponse dans de nombreuses langues. Pas tout le monde est bon avec l'anglais.


## Question

Quelles sont les choses un programmeur mise en œuvre des détails techniques d'une application web devrait considérer avant de faire le site public? Si Jeff Atwood peut oublier HttpOnly biscuits, sitemaps, et cross-site demande faux tous dans le même site, ce qui est important pourrais-je être oubliais ainsi?

Je pense à ce sujet du point de vue d'un développeur web, de sorte que quelqu'un d'autre est de créer le design actuel et le contenu du site. Ainsi, alors que la convivialité et le contenu peut être plus important que la plate-forme, vous avez le programmeur peu à dire sur cela. Ce que vous ne avez pas besoin de se inquiéter, ce est que votre mise en œuvre de la plate-forme est stable, fonctionne bien, est sécurisé et répond à toutes les autres objectifs de l'entreprise (comme ne coûtent pas trop, prennent trop de temps à construire, et se classent ainsi avec Google comme supports contenu).

Pensez à cela du point de vue d'un développeur qui a fait un peu de travail pour les applications de type intranet dans un environnement assez grand, et est sur le point d'avoir son premier coup et de mettre sur un site potentiellement populaire pour toute la grande wide web mauvais monde.

Aussi, je suis à la recherche de quelque chose de plus spécifique que juste un "standards du Web" réponse vague. Je veux dire, HTML, JavaScript et CSS sur HTTP sont à peu près une donnée, surtout quand je l'ai déjà précisé que vous êtes un développeur web professionnel. Donc, allant au-delà, les normes? Dans quelles circonstances et pourquoi? Fournir un lien vers la spécification de la norme.


## Réponse

L'idée ici est que la plupart d'entre nous devrait savoir _already_ _most_ de ce qui est sur cette liste. Mais il pourrait bien être un ou deux éléments que vous ne avez pas vraiment penchés sur avant, ne comprenons pas pleinement, ou peut-être même jamais entendu parler.


### Interface et l'expérience utilisateur

* Soyez conscient que les navigateurs de mettre en œuvre les normes incohérente et assurez-vous que votre site fonctionne raisonnablement bien dans tous les principaux navigateurs. Lors d'une épreuve minimale contre une récente [Gecko] (http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29) moteur ([Firefox] (http://firefox.com/)), un moteur de WebKit ( [Safari] (http://www.apple.com/safari/) et certains navigateurs mobiles), [Chrome] (http://www.google.com/chrome), vos soutenus [navigateurs IE] (http: / /en.wikipedia.org/wiki/Internet_Explorer) (profiter de la [Application Compatibility VPC Images](http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&displaylang=en)), et [Opera] (http://www.opera.com/). Voir également la façon dont [navigateurs rendre votre site] (http://www.browsershots.org) dans les systèmes d'exploitation différents.
* Voyez comment les gens peuvent utiliser le site autre que des principaux navigateurs: les téléphones cellulaires, les lecteurs d'écran et les moteurs de recherche, par exemple. & Mdash; Quelques infos d'accessibilité: [WAI] (http://www.w3.org/WAI/) et [Section508] (http://www.section508.gov/), Développement mobile: [MobiForge] (http: // mobiforge .com /).
* Mise en scène: Comment déployer les mises à jour sans affecter vos utilisateurs. Avoir un ou plusieurs environnements de test ou de mise en scène pour mettre en œuvre des changements à l'architecture, code ou le contenu de balayage et se assurer qu'ils peuvent être déployés de manière contrôlée, sans rien casser. Avoir un moyen automatisé de déploiement puis modifications approuvées sur le site en direct. Ce est le plus efficacement mis en œuvre conjointement avec l'utilisation d'un système de contrôle de version (CVS, Subversion, etc.) et un mécanisme automatisé de construction (Ant, Nant, etc.).
* Ne pas afficher les erreurs hostiles directement à l'utilisateur.
* Ne mettez pas les adresses de messagerie des utilisateurs en texte clair car ils se spammé à mort.
* Ajouter l'attribut `rel =" nofollow "` aux liens générés par les utilisateurs [d'éviter spam] (http://en.wikipedia.org/wiki/Nofollow).
* [Construire bien considérés limites dans votre site] (http://www.codinghorror.com/blog/archives/001228.html) - Cette appartient aussi sous Sécurité.
* Apprenez à faire [amélioration progressive] (http://en.wikipedia.org/wiki/Progressive_enhancement).
* [Rediriger après un post] (http://en.wikipedia.org/wiki/Post/Redirect/Get) si ce poste a été un succès, pour empêcher une actualisation de soumettre à nouveau.
* Ne oubliez pas de prendre en compte l'accessibilité. Ce est toujours une bonne idée et dans certaines circonstances, ce est un [obligation légale] (http://www.section508.gov/). [WAI-ARIA] (http://www.w3.org/WAI/intro/aria) et [WCAG 2] (http://www.w3.org/TR/WCAG20/) sont de bonnes ressources dans ce domaine.
* [Ne me font penser] (http://www.sensible.com/dmmt.html)


### Question de sécurité

* Il ya beaucoup à digérer mais le [guide de développement OWASP] (http://www.owasp.org/index.php/Category:OWASP_Guide_Project) couvre Sécurité du site Web de haut en bas.
* Connaître injection en particulier [injection SQL] (http://en.wikipedia.org/wiki/SQL_injection) et comment le prévenir.
* Entrée Jamais la confiance des utilisateurs, ni rien d'autre qui vient dans la demande (qui comprend les biscuits et les valeurs cachées de champ de formulaire!).
* mots de passe de hachage en utilisant [sel] (http://security.stackexchange.com/q/21263/396) et utilisent différents sels pour vos lignes pour empêcher les attaques de l'arc. Utilisez un algorithme de hachage lente, comme bcrypt (testées avec le temps) ou scrypt (encore plus fort, mais plus récente) ([1] (http://www.tarsnap.com/scrypt.html), [2] (http: // it.slashdot.org/comments.pl?sid=1987632&cid=35149842)), pour stocker des mots de passe. ([Comment stocker en toute sécurité un mot de passe] (http://codahale.com/how-to-safely-store-a-password/)). Le [NIST approuve également PBKDF2 de hachage des mots de passe] (http://security.stackexchange.com/q/7689/396) ", et ce est [FIPS approuvés dans .NET] (http://security.stackexchange.com/ a / 2136/396) (plus d'info [ici] (http://security.stackexchange.com/questions/211/how-to-securely-hash-passwords)). * * Évitez directement en utilisant MD5 ou SHA famille.
* [Ne pas essayer de venir avec votre propre système d'authentification de fantaisie system](http://stackoverflow.com/questions/1581610/how-can-i-store-my-users-passwords-safely/1581919#1581919). Ce est une chose si facile de se tromper de manière subtile et invérifiables et vous ne saurait même pas jusqu'à ce que vous _after_ piraté.
* Connaître les règles [de cartes de crédit de traitement] (https://www.pcisecuritystandards.org/). ([Voir cette question well](http://stackoverflow.com/questions/51094/payment-processors-what-do-i-need-to-know-if-i-want-to-accept-credit-cards-on-m))
* Utilisation [SSL](http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt)/[HTTPS](http://en.wikipedia.org/wiki/Https) pour la connexion et toutes les pages où les données sensibles est entré (comme info sur les cartes de crédit).
* [Empêcher le détournement de session] (http://en.wikipedia.org/wiki/Session_hijacking#Prevention).
* Éviter [site scripting croix] (http://en.wikipedia.org/wiki/Cross-site_scripting) (XSS).
* Éviter [site demandent des croix faux] (http://en.wikipedia.org/wiki/Cross-site_request_forgery) (CSRF).
* Évitez [Clickjacking] (http://en.wikipedia.org/wiki/Clickjacking).
* Gardez votre système (s) à jour avec les derniers correctifs.
* Assurez-vous que vos informations de connexion à la base est fixé.
* Tenez-vous informé sur les dernières techniques d'attaque et les vulnérabilités qui affectent votre plate-forme.
* Lire [Le Manuel de sécurité du navigateur Google] (http://code.google.com/p/browsersec/wiki/Main).
* Lire [Manuel de The Hacker Web Application] (http://amzn.com/0470170778).
* Pensez [Le principe du moindre privilège] (https://en.wikipedia.org/wiki/Principle_of_least_privilege). Essayez de gérer votre serveur d'application [comme non-root](http://security.stackexchange.com/questions/47576/do-simple-linux-servers-really-need-a-non-root-user-for-security-reasons). ([Exemple tomcat] (http://tomcat.apache.org/tomcat-8.0-doc/security-howto.html#Non-Tomcat_settings))


### Performance

* Mettre en œuvre la mise en cache si nécessaire, comprendre et utiliser [la mise en cache HTTP] (http://www.mnot.net/cache_docs/) correctement ainsi que [HTML5 manifeste] (http://www.w3.org/TR/2011/ WD-html5-20110525 / offline.html).
* Optimiser images - ne pas utiliser une image de 20 Ko pour un fond de répétition.
* Apprenez à [gzip / dégonfler contenu] (http://developer.yahoo.com/performance/rules.html#gzip "gzipcontent") (<strike> [dégonfler est mieux] (http://stackoverflow.com/ Questions / 1574168 / gzip-vs-dégonflage-zlib-revisited) </ strike>).
* Combiné / concaténer plusieurs feuilles de style ou plusieurs fichiers de script pour réduire le nombre de connexions de navigateur et d'améliorer la capacité de gzip pour compresser les duplications entre les fichiers.
* Jetez un oeil sur le site [Yahoo performances exceptionnelles] (http://developer.yahoo.com/performance/), beaucoup de grandes lignes directrices, y compris l'amélioration des performances front-end et leur [YSlow] (http: // développeur. yahoo.com/yslow/) outil (nécessite Firefox, Safari, Chrome ou Opera). En outre, [Google vitesse de page] (https://developers.google.com/speed/docs/best-practices/rules_intro) (utiliser avec [extension de navigateur] (https://developers.google.com/speed/pagespeed/ insights_extensions)) est un autre outil de profilage des performances, et il optimise vos images aussi.
* Utilisez [CSS Sprites image] (http://alistapart.com/articles/sprites) pour les petites images connexes comme les barres d'outils (voir le point «minimiser les requêtes HTTP")
* Sites Web Busy devraient envisager [composants de séparation entre les domaines] (http://developer.yahoo.com/performance/rules.html#split). Plus précisément ...
* Contenu statique (ce est à dire des images, CSS, JavaScript, et généralement contenu qui n'a pas besoin d'accéder aux cookies) devraient aller dans un domaine distinct _ [qui ne utilise pas de cookies] (http://blog.stackoverflow.com/2009/ 08 / a-peu-vitesse-améliorations /) _, parce que tous les cookies pour un domaine et ses sous-domaines sont envoyés à chaque requête au domaine et ses sous-domaines. Une bonne option est d'utiliser un Content Delivery Network (CDN), mais considérer le cas où ce que le CDN peut échouer en incluant CDN alternatives, ou des copies locales qui peuvent être servis à la place.
* Réduire le nombre total de requêtes HTTP nécessaires à un navigateur pour afficher la page.
* Utiliser [Google Closure Compiler] (http://developers.google.com/closure/compiler/) pour JavaScript et [d'autres outils de minification] (http://developer.yahoo.com/yui/compressor/).
* Assurez-vous qu'il ya un fichier `favicon.ico` à la racine du site, ce est à dire` / favicon.ico`. [Navigateurs seront automatiquement demander] (http://mathiasbynens.be/notes/rel-shortcut-icon), même si l'icône ne est pas mentionné dans le code HTML du tout. Si vous ne avez pas de `/ favicon.ico`, cela se traduira par beaucoup de 404s, drainant la bande passante de votre serveur.


### SEO (Search Engine Optimization)

* Utilisez "moteur de recherche convivial" URL, soit utiliser `example.com / pages / 45-article-title` au lieu de ` example.com/index.php? Page = 45`
* Lorsque vous utilisez `#` pour le contenu dynamique changer le `#` à `#!`, Puis sur le serveur `$ _REQUEST [" _ _ escaped_fragment "]` est ce que Googlebot utilise au lieu de `#!`. En d'autres termes, `./#! Page = 1` devient` ./?_ escaped_fragments_ = page = 1`. En outre, pour les utilisateurs qui peuvent utiliser FF.b4 ou chrome, `history.pushState ({" foo ":" bar "}," A propos ","? Page = 1 ./ ");` est une grande commande. Ainsi, même si la barre d'adresse a changé la page ne se recharge pas. Cela vous permet d'utiliser `?` Au lieu de `#!` Pour maintenir le contenu dynamique et aussi de dire au serveur quand vous email le lien que nous sommes après cette page, et l'AJAX n'a ​​pas besoin de faire une autre demande supplémentaire.
* Ne pas utiliser les liens qui disent ["cliquez ici"] (http://ux.stackexchange.com/questions/12100/why-shouldnt-we-use-the-word-here-in-a-textlink). Vous perdez une occasion de SEO et il rend les choses plus difficiles pour les personnes avec les lecteurs d'écran.
* Vous avez déjà un [sitemap XML] (http://www.sitemaps.org/), de préférence dans l'emplacement par défaut `/ de sitemap.xml`.
* Utilisez [`<link rel =" canonical "... />`](http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html) lorsque vous avez plusieurs URL qui pointent vers le même contenu, cette question peut également être abordée dans [Google Webmaster Tools] (http://www.google.com/webmasters/).
* Utilisez [Google Webmaster Tools] (http://www.google.com/webmasters/) et [Bing Webmaster Tools] (http://www.bing.com/toolbox/webmaster).
* Installez [Google Analytics] (http://www.google.com/analytics/) dès le début (ou un outil d'analyse de la source ouverte comme [Piwik] (http://piwik.org/)).
* Savoir [robots.txt] (http://en.wikipedia.org/wiki/Robots_exclusion_standard) et les moteurs de recherche de travail.
* Rediriger les requêtes (en utilisant `301 Moved Permanently`) demandant` `www.example.com` à example.com` (ou l'inverse) pour éviter diviser le classement Google entre les deux sites.
* Sachez qu'il peut y avoir des araignées mal comportés là-bas.
* Si vous avez non-texte contenu coup d'oeil dans les extensions plan du site de Google pour la vidéo, etc. Il ya quelques bonnes informations à ce sujet [Tim Farley answer](http://stackoverflow.com/questions/72394/what-should-a-developer-know-before-building-a-public-web-site#167608).


### Technologie

* Comprendre [HTTP] (http://www.ietf.org/rfc/rfc2616.txt) et des choses comme GET, POST, sessions, les cookies, et ce que cela signifie d'être «apatride».
* Écrivez votre [XHTML] (http://www.w3.org/TR/xhtml1/) / [HTML] (http://www.w3.org/TR/REC-html40/) et [CSS] (http : //www.w3.org/TR/CSS2/) selon les spécifications du W3C [] (http://www.w3.org/TR/) et se assurer qu'ils [Valider] (http: //validator.w3 .org /). Le but ici est d'éviter navigateur bizarreries modes et en prime le rendre beaucoup plus facile de travailler avec les navigateurs non-traditionnels tels que les lecteurs d'écran et les périphériques mobiles.
* Comprendre comment JavaScript est traitée dans le navigateur.
* Comprendre comment JavaScript, feuilles de style, et d'autres ressources utilisées par votre page sont chargés et considèrent que leur impact sur la perception * * performance. Il est maintenant largement considéré comme approprié à [son de déplacement vers le bas] (http://developer.yahoo.com/blogs/ydn/posts/2007/07/high_performanc_5/) de vos pages avec des exceptions étant typiquement des choses comme analytics applications ou cales HTML5.
* Comprendre comment fonctionne le bac à sable JavaScript, surtout si vous avez l'intention d'utiliser les iframes.
* Soyez conscient que JavaScript peut et sera désactivée, et que AJAX est donc une extension, pas une référence. Même si la plupart des utilisateurs normaux laissent maintenant, rappelez-vous que [NoScript] (http://noscript.net/) est de plus en plus populaire, les appareils mobiles peut ne pas fonctionner comme prévu, et Google ne sera pas exécuter la plupart de votre JavaScript lors de l'indexation le site.
* Apprendre la [différence entre 301 et 302 redirections] (http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/) (ce est aussi un problème de référencement).
* Pour en savoir autant que vous pouvez sur votre plate-forme de déploiement.
* Pensez à utiliser un [Réinitialiser Style Sheet] (http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet) ou [normalize.css] (http: / /necolas.github.com/normalize.css/).
* Pensez frameworks JavaScript (comme [jQuery] (http://jquery.com/), [MooTools] (http://mootools.net/), [Prototype] (http://www.prototypejs.org/) , [Dojo] (http://dojotoolkit.org) ou [YUI 3] (http://developer.yahoo.com/yui/3/)), ce qui permet de masquer un grand nombre de différences de navigateur lorsque vous utilisez JavaScript pour DOM manipulation.
* Prendre performance perçue et les cadres JS ensemble, envisager d'utiliser un service tel que le [Google Bibliothèques API] (http://developers.google.com/speed/libraries/devguide) pour charger les cadres de sorte qu'un navigateur peut utiliser une copie de le cadre qu'elle a déjà mis en cache plutôt que de télécharger un duplicata de votre site.
* Ne pas réinventer la roue. Avant de faire la recherche de quelque chose pour un composant ou un exemple sur la façon de le faire. Il ya une chance de 99% que quelqu'un a fait et publié une version OSS du code.
* Sur le revers de cela, ne pas commencer par 20 bibliothèques avant même que vous avez décidé de ce que sont vos besoins. Particulièrement sur le web côté client où il est presque toujours finalement plus important de garder les choses léger, rapide et flexible.


### Correction

* Comprenez vous passerez 20% de votre codage de temps et 80% de celui-ci le maintien, donc le code en conséquence.
* Mettre en place une bonne solution de reporting d'erreur.
* Disposer d'un système pour les gens de vous contacter avec des suggestions et critiques.
* Documenter la façon dont l'application fonctionne pour le personnel et les gens qui font l'entretien futur soutien.
* Faites des sauvegardes fréquentes! (Et assurez-vous que ces sauvegardes sont fonctionnels) ont une stratégie de restauration, pas seulement une stratégie de sauvegarde.
* Utilisez un système de contrôle de version pour stocker vos fichiers, tels que [Subversion] (http://subversion.apache.org/), [Mercurial] (http://mercurial.selenic.com/) ou [Git] (http : //git-scm.org).
* Ne oubliez pas de faire vos tests d'acceptation. Cadres comme [sélénium] (http://seleniumhq.org/) peuvent aider. Surtout si vous automatiser entièrement vos tests, peut-être en utilisant un outil d'intégration continue, comme [Jenkins] (http://jenkins-ci.org/).
* Assurez-vous que vous avez suffisamment d'exploitation forestière en place en utilisant des cadres tels que [log4j] (http://logging.apache.org/log4j/), [log4net] (http://logging.apache.org/log4net/) ou [ log4r] (http://log4r.rubyforge.org/). Si quelque chose va mal sur votre site en direct, vous aurez besoin d'un moyen de savoir quoi.
* Lorsque vous vous connectez vous assurer que vous capturez des exceptions à la fois traitées, et les exceptions non gérées. Rapport / analyser la sortie du journal, que ça va vous montrer où sont les questions clés dans votre site.
