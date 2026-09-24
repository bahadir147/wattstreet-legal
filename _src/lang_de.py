L = {
"code": "de", "htmllang": "de", "name": "Deutsch",
"date": "25. September 2026",
"ui": {
    "home": "Start", "privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "delete": "Daten löschen",
    "menu": "Seiten", "language": "Sprache", "effective": "Gültig ab", "contact": "Kontakt",
    "summary": "Kurz gesagt", "toc": "Inhalt", "legal": "Rechtliches",
    "by": "Ein Mobile Game von Synverse",
    "tagline": "Datenschutzerklärung, Nutzungsbedingungen und Datenlöschung für Watt Street.",
    "landing": "Watt Street ist ein Idle-Tycoon-Spiel, in dem du elektrisches Licht in eine Stadt im Stil von 1882 bringst. Hier findest du die rechtlichen Dokumente des Spiels.",
},
"privacy": {
"title": "Datenschutzerklärung",
"blurb": "Welche Daten das Spiel nutzt, wozu, und welche Rechte du hast.",
"intro": """<p>Diese Datenschutzerklärung erklärt, wie <b>Synverse</b> („wir“) Informationen verarbeitet, wenn du <b>%GAME%</b> („das Spiel“, Paket <code>%PKG%</code>) auf Android oder iOS spielst. Das Spiel ist so gebaut, dass es mit möglichst wenigen Daten auskommt: Es gibt keine Registrierung, und wir fragen nie nach deinem Namen, deiner E-Mail-Adresse oder Telefonnummer.</p>""",
"summary": [
    "Kein Konto und kein Login nötig. Das Spiel erstellt über Unity Gaming Services eine anonyme, zufällige Spieler-ID (Player ID).",
    "Dein Stadtfortschritt wird auf deinem Gerät gespeichert und unter dieser Spieler-ID in Unity Cloud Save gesichert.",
    "Wir erheben weder Namen, E-Mail, Telefonnummer, Kontakte, Fotos, genauen Standort noch Kamera- oder Mikrofondaten.",
    "Werbung, sofern angeboten, besteht aus freiwilligen Belohnungsvideos von Google AdMob. Google kann Gerätekennungen für Werbung nutzen – wo gesetzlich erforderlich, nur mit deiner Einwilligung.",
    "Du kannst jederzeit die Löschung deiner Cloud-Daten verlangen: siehe <a href=\"%DELETE_LINK%\">Daten löschen</a>.",
],
"sections": [
("Verantwortlicher", """<p>Verantwortlicher im Sinne der DSGVO ist Synverse, der Publisher von %GAME%. Du erreichst uns unter %EMAIL%.</p>"""),
("Welche Informationen das Spiel verarbeitet", """<h3>a) Nur auf deinem Gerät gespeicherte Daten</h3>
<p>Das Spiel speichert deinen Spielstand (Stadtfortschritt, Gebäude, Spielwährung, Zeitstempel für Offline-Einnahmen) und deine Einstellungen (Musik, Soundeffekte, Vibration, Sprache, Tutorial-Fortschritt und Werbe-Wartezeiten) im privaten App-Speicher deines Geräts. Wir haben keinen Zugriff auf diese Daten. Die Vibration (Haptik) läuft lokal auf deinem Gerät und sendet nichts.</p>
<h3>b) Anonyme Spieler-ID (Unity Authentication)</h3>
<p>Wenn du online spielst, meldet sich das Spiel anonym bei Unity Authentication an. Unity vergibt eine zufällige <b>Spieler-ID</b> und Sitzungstoken. Die Spieler-ID ist nicht mit deinem Namen, deiner E-Mail oder Telefonnummer verknüpft. Unity-Dienste nutzen außerdem eine zufällige Installationskennung sowie technische Daten wie IP-Adresse, Gerätetyp, Betriebssystem und App-Version, um den Dienst bereitzustellen.</p>
<h3>c) Cloud-Sicherung (Unity Cloud Save)</h3>
<p>Eine Kopie deines Spielstands (die oben beschriebenen Fortschrittsdaten plus technische Versionskennungen) wird unter deiner Spieler-ID in Unity Cloud Save gespeichert, damit deine Stadt wiederhergestellt werden kann. Das Spiel synchronisiert diese Sicherung regelmäßig während des Spielens.</p>
<h3>d) Spielinhalte (Unity Remote Config)</h3>
<p>Das Spiel lädt seinen Aufgabenkatalog von Unity Remote Config. Diese Anfrage nutzt deine Spieler-ID und die technischen Daten, die zur Auslieferung nötig sind; dein Spielstand wird dabei nicht gesendet.</p>
<h3>e) Optionale Kontoverknüpfung (falls verfügbar)</h3>
<p>Bietet das Spiel an, deinen Fortschritt mit einem Unity-Konto zu verknüpfen, erfolgt die Anmeldung auf Unitys eigener Seite. Wir sehen oder speichern dein Passwort nie; Unity übermittelt dem Spiel nur eine Kontokennung, damit dein Spielstand auf einem anderen Gerät wiederhergestellt werden kann.</p>
<h3>f) Werbung (Google AdMob, falls/sobald verfügbar)</h3>
<p>Das Spiel kann <b>freiwillige Belohnungswerbung</b> anbieten: Eine Anzeige läuft nur, wenn du sie gegen eine Belohnung im Spiel aktiv startest. Es gibt keine Zwangswerbung. Die Anzeigen stammen von Google AdMob, das die Werbe-ID deines Geräts (Android-Werbe-ID / Apple IDFA), deine IP-Adresse, Geräte- und App-Informationen sowie Interaktionsdaten erheben und verarbeiten kann, um Anzeigen auszuliefern, zu messen, zu personalisieren und Betrug zu verhindern. Ab Android 13 deklariert das Spiel die Berechtigung <code>AD_ID</code>, damit AdMob die Werbe-ID lesen kann; du kannst sie in den Geräteeinstellungen zurücksetzen oder löschen.</p>
<p>Im Europäischen Wirtschaftsraum, im Vereinigten Königreich und in der Schweiz fragt das Spiel über Googles User Messaging Platform (UMP) nach deiner Einwilligung, bevor personalisierte Anzeigen gezeigt werden (§ 25 TDDDG, Art. 6 Abs. 1 lit. a DSGVO); lehnst du ab, kann Google weiterhin nicht personalisierte Anzeigen zeigen. Unter iOS wird die Werbe-ID nur genutzt, wenn du es in Apples App-Tracking-Transparenz-Abfrage erlaubst. Mehr dazu: <a href="%G_PARTNER%">Wie Google Daten von Websites und Apps verwendet, auf bzw. in denen Google-Dienste genutzt werden</a> und die <a href="%G_PRIV%">Datenschutzerklärung von Google</a>.</p>
<h3>g) In-App-Käufe (falls/sobald verfügbar)</h3>
<p>Bietet das Spiel Käufe an, werden Zahlungen vollständig von Google Play oder dem Apple App Store abgewickelt. Wir erhalten nie deine Karten- oder Bankdaten, sondern nur eine Kaufbestätigung (z. B. Produkt-ID und Bestell-/Transaktions-ID), um dir den Kauf bereitzustellen.</p>
<h3>h) Wenn du uns schreibst</h3>
<p>Wenn du uns eine E-Mail sendest, erhalten wir deine E-Mail-Adresse und den Inhalt deiner Nachricht und nutzen sie nur, um dir zu antworten.</p>
<h3>i) Was wir nicht erheben</h3>
<p>Wir erheben weder deinen Namen, deine E-Mail-Adresse (außer du schreibst uns), Telefonnummer, Kontakte, Fotos oder Dateien, genauen oder ungefähren Standort über die Standortdienste des Geräts noch Kamera- oder Mikrofondaten. Das Spiel hat keinen Chat und keine sozialen Funktionen. Wir nutzen weder den Dienst Unity Analytics noch Absturzberichts-Dienste. Die Unity-Engine selbst kann begrenzte technische Informationen (z. B. Gerätemodell, Betriebssystem und Engine-Version) an Unity senden, wie in der <a href="%U_PRIV%">Datenschutzerklärung von Unity</a> beschrieben.</p>"""),
("Zwecke und Rechtsgrundlagen", """<ul>
<li><b>Betrieb des Spiels und Sicherung deines Fortschritts</b> (lokaler Spielstand, Cloud-Sicherung, anonyme Anmeldung, Laden von Aufgaben): zur Erfüllung des von dir gewünschten Dienstes erforderlich (Art. 6 Abs. 1 lit. b DSGVO).</li>
<li><b>Sicherheit, Missbrauchsschutz und Stabilität</b> (z. B. Anfragelimits und technische Protokolle bei Unity): unsere berechtigten Interessen (Art. 6 Abs. 1 lit. f DSGVO).</li>
<li><b>Personalisierte Werbung</b>: deine Einwilligung, wo erforderlich (Art. 6 Abs. 1 lit. a DSGVO), jederzeit widerrufbar. Nicht personalisierte Werbung und Schutz vor Werbebetrug: berechtigte Interessen.</li>
<li><b>Beantwortung deiner Anfragen und Erfüllung gesetzlicher Pflichten</b>: Art. 6 Abs. 1 lit. c und f DSGVO.</li>
</ul>
<p>Wir nutzen deine Daten nicht für automatisierte Entscheidungen mit rechtlicher oder ähnlich erheblicher Wirkung.</p>"""),
("Empfänger", """<ul>
<li><b>Unity Technologies</b> (Authentication, Cloud Save, Remote Config) hostet Spieler-ID, Cloud-Sicherung und Spielinhalte als unser Auftragsverarbeiter. Siehe <a href="%U_PRIV%">Datenschutzerklärung von Unity</a>.</li>
<li><b>Google</b> (AdMob), falls Werbung angeboten wird, wie oben beschrieben. Für personalisierte Werbung ist Google eigenständig Verantwortlicher für die erhobenen Daten. Siehe <a href="%G_PRIV%">Datenschutzerklärung von Google</a>.</li>
<li><b>Google Play / Apple</b> für Downloads, Updates und etwaige Käufe, nach deren eigenen Datenschutzbestimmungen.</li>
<li><b>Behörden</b>, nur wenn gesetzlich vorgeschrieben.</li>
</ul>
<p>Wir verkaufen deine personenbezogenen Daten nicht gegen Geld. Nach einigen US-Bundesstaatsgesetzen (z. B. Kalifornien) kann das Zulassen personalisierter AdMob-Werbung als „Sharing“ für kontextübergreifende verhaltensbasierte Werbung gelten; du kannst wie in Abschnitt 7 beschrieben widersprechen.</p>"""),
("Internationale Übermittlungen", """<p>Unity und Google können Daten auf Servern außerhalb deines Landes verarbeiten, auch in den USA. Diese Übermittlungen stützen sich auf geeignete Garantien wie die Standardvertragsklauseln der Europäischen Kommission bzw. das EU-US Data Privacy Framework, soweit der Empfänger zertifiziert ist.</p>"""),
("Speicherdauer", """<ul>
<li><b>Gerätedaten</b>: bis du das Spiel löschst oder seinen Speicher leerst.</li>
<li><b>Cloud-Sicherung und Spieler-ID</b>: solange du das Spiel nutzt. Auf Anfrage (siehe <a href="%DELETE_LINK%">Daten löschen</a>) löschen wir sie innerhalb von 30 Tagen nach Prüfung der Anfrage.</li>
<li><b>Support-E-Mails</b>: bis zu 12 Monate nach Abschluss deiner Anfrage, sofern das Gesetz keine längere Frist verlangt.</li>
<li><b>Werbedaten</b>: werden von Google nach eigenen Richtlinien gespeichert.</li>
</ul>"""),
("Deine Wahlmöglichkeiten und Rechte", """<p>Du hast nach der DSGVO das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Widerspruch, Datenübertragbarkeit sowie auf jederzeitigen Widerruf einer Einwilligung mit Wirkung für die Zukunft. Einwohner Kaliforniens und anderer US-Bundesstaaten können Auskunft, Löschung und Berichtigung verlangen und dem „Verkauf“ oder „Sharing“ widersprechen. Nutzer in der Türkei haben die Rechte aus Art. 11 KVKK. Wir benachteiligen dich nicht, wenn du diese Rechte ausübst.</p>
<p><b>So gehst du vor:</b> Schreib an %EMAIL% und gib die Spieler-ID an, die im Spiel unter <i>Einstellungen › Konto &amp; Cloud</i> angezeigt wird. Da wir weder deinen Namen noch deine E-Mail kennen, finden wir deine Daten nur über die Spieler-ID. Wir antworten innerhalb eines Monats.</p>
<p><b>Werbung:</b> Ändere deine Werbeeinwilligung über die Datenschutzoptionen des Spiels (im EWR, Vereinigten Königreich und der Schweiz angezeigt), setze deine Werbe-ID in den Geräteeinstellungen zurück oder lösche sie, oder verwalte Anzeigen im <a href="%G_ADS%">Mein Werbecenter</a>. Unter iOS kannst du Tracking unter Einstellungen › Datenschutz &amp; Sicherheit › Tracking deaktivieren.</p>
<p>Du kannst dich außerdem bei einer Datenschutz-Aufsichtsbehörde beschweren (<a href="%EDPB%">Liste der Behörden</a>).</p>"""),
("Deine Daten löschen", """<p>Durch Deinstallation des Spiels werden alle auf deinem Gerät gespeicherten Daten entfernt. Um deine Cloud-Sicherung und anonyme Spieler-ID zu löschen, folge den Schritten unter <a href="%DELETE_LINK%">Daten löschen</a>.</p>"""),
("Kinder", """<p>%GAME% richtet sich an Spieler ab 13 Jahren und nicht an Kinder unter 13. Im Einklang mit dem US-amerikanischen Children's Online Privacy Protection Act (COPPA) erheben wir wissentlich keine personenbezogenen Daten von Kindern unter 13. Wenn du als Elternteil glaubst, dass dein Kind unter 13 das Spiel genutzt hat, schreib uns an %EMAIL%, und wir löschen die zugehörigen Daten. Wo das Gesetz ein höheres Einwilligungsalter vorsieht (in Deutschland 16 Jahre, Art. 8 DSGVO), sollten jüngere Spieler personalisierter Werbung nur mit Zustimmung der Eltern zustimmen.</p>"""),
("Sicherheit", """<p>Daten zwischen dem Spiel und den Diensten von Unity oder Google werden bei der Übertragung verschlüsselt (HTTPS/TLS). Daten auf deinem Gerät liegen im privaten App-Speicher, geschützt durch das Betriebssystem. Kein System ist vollkommen sicher, aber wir erheben wenig, damit es wenig zu schützen gibt.</p>"""),
("Änderungen dieser Erklärung", """<p>Wir können diese Erklärung anpassen, wenn sich das Spiel ändert (z. B. wenn Werbung oder Käufe hinzukommen). Wir aktualisieren dann das Datum oben und informieren dich bei wesentlichen Änderungen im Spiel.</p>"""),
("Kontakt", """<p>Synverse — %EMAIL%<br>Bitte schreib „%GAME%“ in den Betreff.</p>"""),
],
},
"terms": {
"title": "Nutzungsbedingungen",
"blurb": "Die kurzen Regeln zum Spielen.",
"intro": """<p>Diese Nutzungsbedingungen („Bedingungen“) sind eine Vereinbarung zwischen dir und <b>Synverse</b> über das Mobile Game <b>%GAME%</b>. Mit dem Herunterladen oder Spielen akzeptierst du diese Bedingungen und unsere <a href="%PRIVACY_LINK%">Datenschutzerklärung</a>. Wenn du nicht einverstanden bist, nutze das Spiel bitte nicht.</p>""",
"sections": [
("Wer spielen darf", """<p>Du musst mindestens 13 Jahre alt sein. Bist du nach dem Recht deines Wohnsitzes minderjährig, brauchst du die Erlaubnis eines Elternteils oder Erziehungsberechtigten.</p>"""),
("Deine Lizenz", """<p>Wir gewähren dir eine persönliche, nicht exklusive, nicht übertragbare und widerrufliche Lizenz, das Spiel auf deinen Geräten für nicht kommerzielle Zwecke herunterzuladen und zu spielen. Das Spiel, sein Code, Grafik, Musik, Texte und Marken gehören Synverse oder deren Lizenzgebern. Du darfst das Spiel nicht kopieren, verkaufen, vermieten, verändern, zurückentwickeln oder weiterverbreiten, soweit das Gesetz dies nicht ausdrücklich erlaubt.</p>"""),
("Spielgegenstände und Spielwährung", """<p>Spielgeld, Gegenstände, Boosts und Fortschritt haben keinen realen Wert, können nicht in echtes Geld getauscht werden und werden dir lizenziert, nicht verkauft. Wir können sie im Rahmen von Updates ausbalancieren, ändern oder entfernen.</p>"""),
("Käufe (falls/sobald verfügbar)", """<p>Bietet das Spiel Käufe an, erfolgen sie über Google Play oder den Apple App Store und unterliegen deren Bedingungen und Erstattungsrichtlinien. Deine gesetzlichen Verbraucherrechte bleiben unberührt.</p>"""),
("Werbung", """<p>Das Spiel kann freiwillige Belohnungswerbung anbieten. Werbeinhalte stammen von Dritten (Google AdMob); für Produkte oder Websites Dritter in Anzeigen sind wir nicht verantwortlich.</p>"""),
("Faire Nutzung", """<p>Nutze das Spiel nicht für rechtswidrige Zwecke, greife unsere Dienste oder die unserer Anbieter nicht an, überlaste sie nicht und störe andere Spieler nicht bei der Nutzung.</p>"""),
("Cloud-Speicherstand und Verfügbarkeit", """<p>Die Cloud-Sicherung ist ein Komfortangebot. Wir arbeiten an ihrer Zuverlässigkeit, können aber nicht garantieren, dass das Spiel oder seine Online-Dienste immer verfügbar und fehlerfrei sind oder dass nie Daten verloren gehen. Wir können das Spiel oder einzelne Funktionen aktualisieren, ändern oder einstellen.</p>"""),
("Haftung", """<p>Das Spiel wird „wie besehen“ und „wie verfügbar“ bereitgestellt. Soweit gesetzlich zulässig, haftet Synverse nicht für indirekte Schäden, Datenverlust oder den Verlust von Spielgegenständen. Die Haftung für Vorsatz, grobe Fahrlässigkeit und Verletzungen von Leben, Körper oder Gesundheit sowie deine zwingenden Verbraucherrechte bleiben unberührt.</p>"""),
("Beendigung", """<p>Du kannst das Spiel jederzeit durch Deinstallation beenden. Wir können deinen Zugang sperren oder beenden, wenn du schwerwiegend gegen diese Bedingungen verstößt.</p>"""),
("Apple-Geräte", """<p>Wenn du das Spiel aus dem Apple App Store geladen hast, gilt zusätzlich Apples <a href="%APPLE_EULA%">Standard-Endbenutzer-Lizenzvertrag</a>. Apple ist nicht für das Spiel oder dessen Support verantwortlich; Apple und seine Tochtergesellschaften sind Drittbegünstigte dieser Bedingungen.</p>"""),
("Anwendbares Recht und Änderungen", """<p>Diese Bedingungen unterliegen dem Recht der Republik Türkei. Als Verbraucher behältst du den Schutz der zwingenden Vorschriften deines Wohnsitzlandes und kannst dort Ansprüche geltend machen. Wir können diese Bedingungen aktualisieren; das Datum oben zeigt die aktuelle Fassung, und wer weiterspielt, akzeptiert die Aktualisierung.</p>"""),
("Kontakt", """<p>Synverse — %EMAIL%</p>"""),
],
},
"delete": {
"title": "Daten löschen",
"blurb": "So löschst du deine Watt-Street-Cloud-Daten und Spieler-ID.",
"intro": """<p>Diese Seite erklärt, wie du Daten von <b>%STORE%</b> von <b>Synverse</b> (Paket <code>%PKG%</code>) löschen lässt. Das Spiel hat keine Registrierung: Es nutzt eine anonyme Spieler-ID von Unity Gaming Services und eine Cloud-Sicherung deiner Stadt.</p>""",
"sections": [
("Löschung beantragen", """<ol>
<li>Öffne das Spiel und tippe auf <b>Einstellungen</b> (Zahnrad) › <b>Konto &amp; Cloud</b>. Kopiere deine <b>Spieler-ID</b>.</li>
<li>Schreib an %EMAIL% mit dem Betreff <b>„%GAME% – Datenlöschung“</b> und füge deine Spieler-ID ein.</li>
<li>Wir löschen deine Daten innerhalb von 30 Tagen und bestätigen es per E-Mail.</li>
</ol>
<p>Ohne Spieler-ID können wir deine Daten möglicherweise nicht finden, da wir weder deinen Namen noch deine E-Mail-Adresse kennen.</p>"""),
("Was gelöscht wird", """<ul>
<li>Dein Cloud-Spielstand (Stadtfortschritt) in Unity Cloud Save.</li>
<li>Deine anonyme Spieler-ID und ihr Anmeldedatensatz in Unity Authentication.</li>
</ul>
<p>Die Löschung ist endgültig: Dein Cloud-Fortschritt kann danach nicht wiederhergestellt werden.</p>"""),
("Was aufbewahrt werden kann", """<p>Wir bewahren deine E-Mail und Anfrage bis zu 12 Monate als Nachweis der Bearbeitung auf, sofern das Gesetz keine längere Frist verlangt. Technische Protokolle bei Unity werden nach Unitys eigenen Fristen gelöscht. Daten, die Google für Werbung erhebt, liegen in Googles Verantwortung.</p>"""),
("Daten auf deinem Gerät", """<p>Deinstalliere das Spiel oder leere seinen Speicher in den Geräteeinstellungen, um Spielstand und Einstellungen auf deinem Telefon zu entfernen. Deine Cloud-Sicherung wird dadurch nicht gelöscht; beantrage das wie oben beschrieben.</p>"""),
("Werbedaten", """<p>Zum Zurücksetzen oder Löschen deiner Werbe-ID nutze die Geräteeinstellungen (Android: Einstellungen › Datenschutz › Werbung; iOS: Einstellungen › Datenschutz &amp; Sicherheit › Tracking). Google-Werbedaten verwaltest du im <a href="%G_ADS%">Mein Werbecenter</a>.</p>"""),
],
},
}
