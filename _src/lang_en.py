L = {
"code": "en", "htmllang": "en", "name": "English",
"date": "September 25, 2026",
"ui": {
    "home": "Home", "privacy": "Privacy", "terms": "Terms", "delete": "Delete data",
    "menu": "Pages", "language": "Language", "effective": "Effective date", "contact": "Contact",
    "summary": "In short", "toc": "Contents", "legal": "Legal",
    "by": "A mobile game by Synverse",
    "tagline": "Privacy policy, terms of use and data deletion for Watt Street.",
    "landing": "Watt Street is an idle tycoon game about bringing electric light to an 1882-style city. This site holds the game's legal documents.",
},
"privacy": {
"title": "Privacy Policy",
"blurb": "What data the game uses, why, and your rights.",
"intro": """<p>This Privacy Policy explains how <b>Synverse</b> (“we”, “us”) handles information when you play <b>%GAME%</b> (“the game”, package <code>%PKG%</code>) on Android or iOS. We built the game to work with as little data as possible: there is no sign-up, and we never ask for your name, email address or phone number.</p>""",
"summary": [
    "No account or login is required. The game creates an anonymous, random Player ID through Unity Gaming Services.",
    "Your city progress is saved on your device and backed up to Unity Cloud Save under that Player ID.",
    "We do not collect your name, email, phone number, contacts, photos, precise location, camera or microphone.",
    "Ads, where offered, are optional rewarded videos from Google AdMob. Google may use device identifiers for ads, subject to your consent where the law requires it.",
    "You can ask us to delete your cloud data at any time: see <a href=\"%DELETE_LINK%\">Delete your data</a>.",
],
"sections": [
("Who is responsible", """<p>The data controller for the game is Synverse, the publisher of %GAME%. You can reach us at %EMAIL%. For users in Türkiye, Synverse acts as the data controller (<i>veri sorumlusu</i>) under Law No. 6698 on the Protection of Personal Data (KVKK).</p>"""),
("Information the game processes", """<h3>a) Data stored only on your device</h3>
<p>The game keeps your save file (city progress, buildings, in-game currency, timestamps used for offline earnings) and your settings (music, sound effects, vibration, language, tutorial progress, and ad cooldown counters) in the app's private storage on your device. We cannot access this data. Vibration (haptics) is handled locally by your device and sends nothing.</p>
<h3>b) Anonymous player ID (Unity Authentication)</h3>
<p>When you play online, the game signs in anonymously with Unity Authentication. Unity assigns a random <b>Player ID</b> and session tokens. The Player ID is not linked to your name, email or phone number. Unity services also use a random installation identifier and technical data such as your IP address, device type, operating system and app version to deliver the service.</p>
<h3>c) Cloud backup (Unity Cloud Save)</h3>
<p>A copy of your save (the same game progress data described above, plus technical revision identifiers) is stored in Unity Cloud Save under your Player ID, so the game can restore your city. The game syncs this backup periodically while you play.</p>
<h3>d) Game content (Unity Remote Config)</h3>
<p>The game downloads its quest catalog from Unity Remote Config. This request uses your Player ID and technical data needed to deliver the content; it does not send your save.</p>
<h3>e) Optional account linking (if available)</h3>
<p>If the game offers linking your progress to a Unity account, sign-in happens on Unity's own page. We never see or store your password; Unity only tells the game an account identifier so your save can be restored on another device.</p>
<h3>f) Ads (Google AdMob, if/when available)</h3>
<p>The game may offer <b>optional rewarded ads</b>: an ad only plays when you tap to watch one in exchange for an in-game reward. There are no forced ads. Ads are provided by Google AdMob, which may collect and process your device's advertising identifier (Android Advertising ID / Apple IDFA), IP address, device and app information, and ad interaction data to show, measure and personalize ads and to prevent fraud. On Android 13 and later the game declares the <code>AD_ID</code> permission so that AdMob can read the advertising ID; you can reset or delete it in your device settings.</p>
<p>In the European Economic Area, the United Kingdom and Switzerland, the game asks for your consent through Google's User Messaging Platform (UMP) before personalized ads are shown; if you decline, Google may still show non-personalized ads. On iOS, the advertising identifier is only used if you allow it in Apple's App Tracking Transparency prompt. Learn more: <a href="%G_PARTNER%">How Google uses information from sites or apps that use its services</a> and the <a href="%G_PRIV%">Google Privacy Policy</a>.</p>
<h3>g) In-app purchases</h3>
<p>The game offers optional in-app purchases (for example No Ads, a Starter Pack, permanent ×2 income and Patent packs). Payments are processed entirely by Google Play or the Apple App Store; we never receive your card or bank details. The game only receives the purchase token or receipt from the store (product ID, order/transaction ID and purchase date) to check the purchase on your device, deliver what you bought and restore it later. A record of your purchases (product and transaction IDs) is kept in your save and its cloud backup so it survives reinstalls. This is purchase history used only for app functionality.</p>
<h3>h) When you contact us</h3>
<p>If you email us, we receive your email address and whatever you include in your message, and use it only to answer you.</p>
<h3>i) What we do not collect</h3>
<p>We do not collect your name, email address (unless you write to us), phone number, contacts, photos or files, precise or approximate location through device location services, camera or microphone data. The game has no chat and no social features. We do not use the Unity Analytics service. If the game crashes or hits an error, a crash report (device model, operating system, app version and the technical error trace, with no personal data) is sent to Unity (Cloud Diagnostics) so we can fix bugs. The Unity engine itself may send limited technical information (for example device model, operating system and engine version) to Unity, as described in <a href="%U_PRIV%">Unity's privacy policy</a>.</p>"""),
("Why we use it and legal bases", """<ul>
<li><b>Running the game and keeping your progress</b> (local save, cloud backup, anonymous sign-in, quest downloads): necessary to provide the service you asked for (GDPR Art. 6(1)(b); KVKK Art. 5(2)(c)).</li>
<li><b>Security, abuse prevention and keeping the service stable</b> (for example request limits and technical logs kept by Unity): our legitimate interests (GDPR Art. 6(1)(f); KVKK Art. 5(2)(f)).</li>
<li><b>Personalized ads</b>: your consent where required (GDPR Art. 6(1)(a); KVKK Art. 5(1)). You can withdraw it at any time. Non-personalized ads and ad fraud prevention: legitimate interests.</li>
<li><b>Answering your requests and meeting legal obligations</b>: legal obligation and legitimate interests (GDPR Art. 6(1)(c) and (f); KVKK Art. 5(2)(ç) and (f)).</li>
</ul>
<p>We do not use your data for automated decisions that have legal or similarly significant effects on you.</p>"""),
("Who we share it with", """<ul>
<li><b>Unity Technologies</b> (Authentication, Cloud Save, Remote Config) hosts the player ID, cloud backup and game content for us as our service provider. See <a href="%U_PRIV%">Unity's privacy policy</a>.</li>
<li><b>Google</b> (AdMob), if ads are offered, as described above. For personalized ads, Google acts as an independent controller of the data it collects. See the <a href="%G_PRIV%">Google Privacy Policy</a>.</li>
<li><b>Google Play / Apple</b> for downloads, updates and any purchases, under their own privacy policies.</li>
<li><b>Authorities</b>, only if the law requires it.</li>
</ul>
<p>We do not sell your personal information for money. Under some US state laws (for example California), allowing AdMob to show personalized ads may count as “sharing” for cross-context behavioral advertising; you can opt out as described in section 7.</p>"""),
("International transfers", """<p>Unity and Google may process data on servers outside your country, including in the United States. These transfers rely on appropriate safeguards such as the European Commission's Standard Contractual Clauses and, for data from Türkiye, the transfer mechanisms of KVKK Article 9 (for example standard contracts).</p>"""),
("How long we keep it", """<ul>
<li><b>Device data</b>: until you delete the game or clear its storage.</li>
<li><b>Cloud backup and Player ID</b>: while you use the game. We delete them when you ask us to (see <a href="%DELETE_LINK%">Delete your data</a>), within 30 days of verifying the request.</li>
<li><b>Support emails</b>: up to 12 months after your request is resolved, unless the law requires longer.</li>
<li><b>Ad data</b>: retained by Google according to its own policies.</li>
</ul>"""),
("Your choices and rights", """<p>Depending on where you live, you have the right to access your data, correct it, delete it, restrict or object to its processing, receive it in a portable format, and withdraw consent at any time (GDPR / UK GDPR). Users in Türkiye have the rights listed in KVKK Article 11, including learning whether data is processed, requesting information, learning the purpose and recipients, requesting correction or deletion, and objecting to results arising from automated analysis. California and other US state residents may request to know, delete and correct personal information, and opt out of “sale” or “sharing”; we will not discriminate against you for using these rights.</p>
<p><b>How to use them:</b> email %EMAIL% and include the Player ID shown in the game under <i>Settings › Account &amp; cloud</i>. Because we do not know your name or email, the Player ID is how we find your data. We answer within 30 days (KVKK: within 30 days; GDPR: within one month).</p>
<p><b>Ads:</b> change your ad consent from the game's privacy options (shown in the EEA, UK and Switzerland), reset or delete your advertising ID in your device settings, or manage ads at <a href="%G_ADS%">My Ad Center</a>. On iOS, you can turn tracking off under Settings › Privacy &amp; Security › Tracking.</p>
<p>You can also complain to your data protection authority (EU/EEA: <a href="%EDPB%">list of authorities</a>; Türkiye: <a href="%KVKK%">Kişisel Verileri Koruma Kurumu</a>).</p>"""),
("Deleting your data", """<p>Uninstalling the game removes all data stored on your device. To delete your cloud backup and anonymous Player ID, follow the steps on <a href="%DELETE_LINK%">Delete your data</a>.</p>"""),
("Children", """<p>%GAME% is intended for players aged 13 and older and is not directed to children under 13. We do not knowingly collect personal information from children under 13, in line with the US Children's Online Privacy Protection Act (COPPA). If you are a parent or guardian and believe your child under 13 has used the game, contact us at %EMAIL% and we will delete the related data. Where local law sets a higher age for consent to data processing (up to 16 in some EU countries), players below that age should only agree to personalized ads with a parent's permission.</p>"""),
("Security", """<p>Data sent between the game and Unity or Google services is encrypted in transit (HTTPS/TLS). Data on your device is kept in the app's private storage, protected by your device's operating system. No system is perfectly secure, but we limit what we collect so there is little to protect in the first place.</p>"""),
("Changes to this policy", """<p>We may update this policy when the game changes (for example when ads or purchases are added). We will change the effective date above and, for important changes, let you know in the game.</p>"""),
("Contact", """<p>Synverse — %EMAIL%<br>Please write “%GAME%” in the subject line.</p>"""),
],
},
"terms": {
"title": "Terms of Use",
"blurb": "The short rules for playing the game.",
"intro": """<p>These Terms of Use (“Terms”) are an agreement between you and <b>Synverse</b> for the mobile game <b>%GAME%</b>. By downloading or playing the game you accept these Terms and our <a href="%PRIVACY_LINK%">Privacy Policy</a>. If you do not agree, please do not use the game.</p>""",
"sections": [
("Who can play", """<p>You must be at least 13 years old. If you are under the age of majority where you live, you must have a parent's or guardian's permission.</p>"""),
("Your license", """<p>We give you a personal, non-exclusive, non-transferable, revocable license to download and play the game on your devices for non-commercial purposes. The game, its code, art, music, texts and trademarks belong to Synverse or its licensors. You may not copy, sell, rent, modify, reverse-engineer or redistribute the game, except where the law expressly allows it.</p>"""),
("In-game items and currency", """<p>In-game money, items, boosts and progress have no real-world value, cannot be exchanged for real money, and are licensed to you, not sold. We may balance, change or remove them as part of updating the game.</p>"""),
("Purchases", """<p>The game offers optional in-app purchases. They are made through Google Play or the Apple App Store and are subject to their terms and refund policies. One-time items (No Ads, Starter Pack, ×2 income) can be restored with “Restore Purchases” in the in-game Shop; Patent packs are consumed when delivered. Your statutory consumer rights are not affected.</p>"""),
("Ads", """<p>The game may offer optional rewarded ads. Ad content is provided by third parties (Google AdMob), and we are not responsible for third-party products or websites shown in ads.</p>"""),
("Fair use", """<p>Do not use the game for unlawful purposes, attack or overload our services or those of our providers, or interfere with other players' use of the service.</p>"""),
("Cloud save and availability", """<p>Cloud backup is offered as a convenience. We work to keep it reliable, but we cannot guarantee that the game or its online services will always be available, error-free, or that data can never be lost. We may update, change or discontinue the game or any feature.</p>"""),
("Disclaimer and liability", """<p>The game is provided “as is” and “as available”. To the extent permitted by law, Synverse is not liable for indirect or consequential damages, loss of data or loss of in-game items. Nothing in these Terms limits liability that cannot be limited by law, or your mandatory consumer rights.</p>"""),
("Ending these Terms", """<p>You can stop using the game at any time by uninstalling it. We may suspend or end your access if you seriously breach these Terms.</p>"""),
("Apple devices", """<p>If you downloaded the game from the Apple App Store, Apple's <a href="%APPLE_EULA%">Standard End User License Agreement</a> also applies. Apple is not responsible for the game or its support, and Apple and its subsidiaries are third-party beneficiaries of these Terms.</p>"""),
("Law and changes", """<p>These Terms are governed by the laws of the Republic of Türkiye. If you are a consumer, you also keep the protection of the mandatory laws of your country of residence and may bring claims there. We may update these Terms; the effective date above shows the latest version, and continued play means you accept the update.</p>"""),
("Contact", """<p>Synverse — %EMAIL%</p>"""),
],
},
"delete": {
"title": "Delete your data",
"blurb": "How to delete your Watt Street cloud data and Player ID.",
"intro": """<p>This page explains how to delete data for <b>%STORE%</b> by <b>Synverse</b> (package <code>%PKG%</code>). The game has no sign-up: it uses an anonymous Player ID from Unity Gaming Services and a cloud backup of your city.</p>""",
"sections": [
("Request deletion", """<ol>
<li>Open the game and tap <b>Settings</b> (gear icon) › <b>Account &amp; cloud</b>. Copy your <b>Player ID</b>.</li>
<li>Email %EMAIL% with the subject <b>“%GAME% – data deletion”</b> and include your Player ID.</li>
<li>We delete your data within 30 days and confirm by email.</li>
</ol>
<p>If you cannot provide a Player ID, we may be unable to find your data, because we do not know your name or email address.</p>"""),
("What is deleted", """<ul>
<li>Your cloud save (city progress) stored in Unity Cloud Save.</li>
<li>Your anonymous Player ID and its sign-in record in Unity Authentication.</li>
</ul>
<p>Deletion is permanent: your cloud progress cannot be restored afterwards.</p>"""),
("What may be kept", """<p>We keep your email and request for up to 12 months as a record that we handled it, unless the law requires longer. Technical logs held by Unity are deleted on Unity's own schedule. Data Google collects for ads is controlled by Google.</p>"""),
("Data on your device", """<p>Uninstall the game, or clear its storage in your device settings, to remove the save and settings stored on your phone. This does not delete your cloud backup; request that as described above.</p>"""),
("Ad data", """<p>To reset or delete your advertising ID, use your device settings (Android: Settings › Privacy › Ads; iOS: Settings › Privacy &amp; Security › Tracking). You can manage Google ad data at <a href="%G_ADS%">My Ad Center</a>.</p>"""),
],
},
}
